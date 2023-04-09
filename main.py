import transmitter
import channel
import receiver

# Rozmiar przesyłanych pakietów
size = 5

# Ścieżka do pliku z przesyłanym sygnałem
filePath = 'input-files/input.txt'

# Stworzenie nadajnika, odbiornika, kanału
trns = transmitter.Transmitter(size)
rcvr = receiver.Receiver()
chnl = channel.Channel(trns, rcvr)


# ARQ stop and wait
def main():
    # Konfiguracja nadajnika
    tab = [0, 0, 0, 1, 1, 1]
    print("Nadawany ciąg bitów:")
    print(tab)

    if chnl.receive(tab):
        print("Informacja dostarczona!")
    else:
        print("NIE dostarczono")
    # Konfiguracja kanału


# Start ARQ
main()