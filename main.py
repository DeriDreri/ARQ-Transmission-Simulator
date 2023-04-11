import transmitter
import channel
import receiver

# Rozmiar przesyłanych pakietów
size = 200

# Ścieżka do pliku z przesyłanym sygnałem
fileIn = 'input-files/input.txt'

# ARQ stop and wait
def main():
    # Stworzenie nadajnika, odbiornika, kanału
    trns = transmitter.Transmitter(size)
    rcvr = receiver.Receiver()
    chnl = channel.Channel(trns, rcvr)

    trns.connectToInputFile(fileIn)  # Wczytanie pliku .txt do nadajnika
    trns.beginTransmission()  # Rozpoczęcie transmisji
    rcvr.saveToFile()           # zapisanie wynikow do pliku txt

# Start ARQ
if __name__ == "__main__":
    main()
