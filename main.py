import transmitter
import channel
import receiver
import  os
import sys
from bitstring import ConstBitStream
from bitstring import ReadError


# Rozmiar przesyłanych pakietów
size = 200
5
# Ścieżka do pliku z przesyłanym sygnałem

# Ścieżka do pliku z testami
fileTest = 'output-files/test.txt'

# Ilość pomiarów
n = 5

# Prawdopodobieństwo wystąpienia błędu
error_rate = {0.005, 0.025, 0.050, 0.100, 0.150}


# Porównywanie input i output
def compare(input_message, output_message):
    counter = 0

    for i in input_message:
        if input_message[i] == output_message[i]:
            counter = counter + 1

    return str(counter) + "/" + str(len(input_message))


# ARQ stop and wait
def main():
    # Stworzenie nadajnika, odbiornika, kanału
    trns = transmitter.Transmitter(size)
    rcvr = receiver.Receiver()
    chnl = channel.Channel(trns, rcvr)

    if len(sys.argv) < 2:
        fileIn = 'input-files/input.txt'
    else:
        fileIn = sys.argv[1]


    file = open(fileTest, "a")
    inputFileStream = ConstBitStream(filename=fileIn)
    inputTab = []
    while(True):
            try:
                value = inputFileStream.read(1).uint
                inputTab.append(value)
            except ReadError:  # Spodziewa się końca pliku
                break
    


    print("Rozpoczęcie testowania:")

    for i in error_rate:
        chnl.set_error_rate(i)

        for i in range(1, n + 1):
            trns.connectToInputFile(fileIn)  # Wczytanie pliku .txt do nadajnika
            trns.beginTransmission()  # Rozpoczęcie transmisji

            file.write(str(i) + "/" + str(n) + " [Sent:" + str(trns.sent) + "] [Accepted: " + str(rcvr.accepted) +
                       "] [Error rate: " + str(chnl.error_Rate) + "] [Correct bits: " + str(rcvr.compare(inputTab))
                       + "/" + str(len(rcvr.finalTab)) + "]\n")

            print(i, "/", n, " [Sent:", trns.sent, "] [Accepted: ", rcvr.accepted, "] [Error rate: ",
                  chnl.error_Rate, "] [Correct bits: ", rcvr.compare(inputTab), "/", len(rcvr.finalTab), "]")

            rcvr.saveToFile()  # zapisanie wynikow do pliku txt

            trns.clear()
            rcvr.clear()

        print("\n")
        file.write("\n")

    file.close()

    print("Zakończenie testowania.")


# Start ARQ
if __name__ == "__main__":
    main()
