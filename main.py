import transmitter
import channel
import receiver

# Rozmiar przesyłanych pakietów
size = 10

# Ścieżka do pliku z przesyłanym sygnałem
filePath = 'input-files/input.txt'

# Stworzenie nadajnika, odbiornika, kanału
trns = transmitter.Transmitter(size)
rcvr = receiver.Receiver()
chnl = channel.Channel(trns, rcvr)


# ARQ stop and wait
def main():
    trns.connectToInputFile('input-files/input.txt')  # Wczytanie pliku .txt do nadajnika
    trns.connectToChannel(chnl)  # Podłączenie nadajnika do kanału
    trns.beginTransmission()  # Rozpoczęcie transmisji
    rcvr.saveToFile()           # zapisanie wynikow do pliku txt

# Start ARQ
main()
