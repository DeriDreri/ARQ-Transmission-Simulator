import transmitter
import channel
import receiver

# Rozmiar przesyłanych pakietów
size = 200

# Ścieżka do pliku z przesyłanym sygnałem
fileIn = 'input-files/input.txt'

# Ilość pomiarów
n = 5


# ARQ stop and wait
def main():
    # Stworzenie nadajnika, odbiornika, kanału
    trns = transmitter.Transmitter(size)
    rcvr = receiver.Receiver()
    chnl = channel.Channel(trns, rcvr)
    sent_packages = []
    accepted_packages = []

    print("Rozpoczęcie testowania:")

    for i in range(1, n + 1):
        trns.connectToInputFile(fileIn)  # Wczytanie pliku .txt do nadajnika
        trns.beginTransmission()  # Rozpoczęcie transmisji

        sent_packages.append(trns.sent)
        accepted_packages.append(rcvr.accepted)
        print(i, "/", n, " [Sent:", trns.sent, "] [Accepted: ", rcvr.accepted, "] [Bit comparsion: ",
              rcvr.compare(trns.tabOfBits), "]")

        rcvr.saveToFile()  # zapisanie wynikow do pliku txt

        trns.clear()
        rcvr.clear()

    print("Zakończenie testowania.")


# Start ARQ
if __name__ == "__main__":
    main()
