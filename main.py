import transmitter
import channel
import receiver
import  os
import sys
from bitstring import ConstBitStream
from bitstring import ReadError
import numpy
import time

# Rozmiar przesyłanych pakietów
size = 200
5
# Ścieżka do pliku z przesyłanym sygnałem

# Ścieżka do pliku z testami
fileTest = 'output-files/test.txt'
fileOut = 'output-files/output.txt'
# Ilość pomiarów
n = 1

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

    if len(sys.argv) < 2:
        fileIn = 'input-files/input.txt'
    else:
        fileIn = sys.argv[1]
        if len(sys.argv) > 2:
            fileOut = sys.argv[2]

    rcvr = receiver.Receiver(fileOut)
    chnl = channel.Channel(trns, rcvr)
    
    file = open('output-files/test.txt', "a")
    
    start = time.time()
    inputFileStream = ConstBitStream(filename=fileIn)
    inputTab = []
    while(True):
            try:
                value = inputFileStream.read('uint:1')
                inputTab.append(value)
            except ReadError:  # Spodziewa się końca pliku
                break
    inputTab = numpy.array(inputTab)
    end = time.time()
    print("Czas ładowania początkowej tablicy: ", end - start)
    print("Rozpoczęcie testowania:")

    for error in error_rate:
        chnl.set_error_rate(error)

        for i in range(1, n + 1):
            start = time.time()
            trns.connectToInputFile(fileIn)  # Wczytanie pliku .txt do nadajnika
            trns.beginTransmission()  # Rozpoczęcie transmisji

            compared = len(rcvr.finalTab) - rcvr.compare(inputTab)
            file.write(str(i) + "/" + str(n) + " [Sent:" + str(trns.sent) + "] [Accepted: " + str(rcvr.accepted) +
                       "] [Error rate: " + str(chnl.error_Rate) + "] [Correct bits: " + str(compared)
                       + "/" + str(len(rcvr.finalTab)) + "]\n")

            print(i, "/", n, " [Sent:", trns.sent, "] [Accepted: ", rcvr.accepted, "] [Error rate: ",
                  chnl.error_Rate, "] [Correct bits: ", str(compared), "/", len(rcvr.finalTab), "]")

            rcvr.saveToFile()  # zapisanie wynikow do pliku txt

            trns.clear()
            rcvr.clear()
            end = time.time()

            print("Czas całej transmisji: ", end - start)
        print("\n")
        file.write("\n")

    file.close()

    print("Zakończenie testowania.")


# Start ARQ
if __name__ == "__main__":
    main()
