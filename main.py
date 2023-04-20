import transmitter
import channel
import receiver

# Rozmiar przesyłanych pakietów
size = 200

# Ścieżka do pliku z przesyłanym sygnałem
fileIn = 'input-files/input.txt'

# Ścieżka do pliku z testami
fileTest = 'output-files/test.txt'

# Ilość pomiarów
n = 5


# ARQ stop and wait
def main():
    # Stworzenie nadajnika, odbiornika, kanału
    trns = transmitter.Transmitter(size)
    rcvr = receiver.Receiver()
    chnl = channel.Channel(trns, rcvr)

    file = open(fileTest, "a")
    file.write("L.p |  Sent  |  Accepted  |  Bit comparsion: input/output  |\n")

    print("Rozpoczęcie testowania:")

    for i in range(1, n + 1):
        trns.connectToInputFile(fileIn)  # Wczytanie pliku .txt do nadajnika
        trns.beginTransmission()  # Rozpoczęcie transmisji

        file.write(
            str(i) + "  |  " + str(trns.sent) + "  |  " + str(rcvr.accepted) + "  |  " + str(rcvr.compare(trns.tabOfBits)) + "\n")

        print(i, "/", n, " [Sent:", trns.sent, "] [Accepted: ", rcvr.accepted, "] [Bit comparsion: ",
              rcvr.compare(trns.tabOfBits), "]")

        # rcvr.saveToFile()  # zapisanie wynikow do pliku txt

        trns.clear()
        rcvr.clear()

    file.close()

    print("Zakończenie testowania.")


# Start ARQ
if __name__ == "__main__":
    main()
