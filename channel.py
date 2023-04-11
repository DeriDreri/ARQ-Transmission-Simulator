import time

# Prawdopodobieństwo wystąpienia błędu
error_Rate = 0.001  # 25%


class Channel:

    # Konstruktor definiuje nadajnik i odbiornik
    def __init__(self, transmitter, receiver):
        self.transmitter = transmitter
        self.receiver = receiver
        transmitter.connectToChannel(self)
        receiver.addChannel(self)

    # Generator liczb pseudolosowych

    @staticmethod
    def random():
        seed = int(round(time.time() * 1000))
        a = 1103515245
        c = 12345
        m = 2 ** 31
        seed = (a * seed + c) % m
        time.sleep(0.1)
        return seed / m

    # Odbieranie ciągu bitów z nadajnika, wysyłanie go do odbiornika
    def receive(self, bitsStream):
        print("=========================\n")
        print("\nCiąg bitów jest w kanale:")
        print(bitsStream)

        bitsStream = self.addNoise(bitsStream)  # Nakładanie zakłóceń na ciąg bitów
        print("\nNałożono zakłócenia na ciąg bitów:")
        print(bitsStream)
        print("=========================\n")

        return self.receiver.receive(bitsStream)  # Wysyłanie ciągu bitów do odbiornika i odbieranie potwierdzenia

    # Nakładanie zakłóceń
    def addNoise(self, bits):
        for bit in bits:
            if self.random() < error_Rate:
                bit = not bit
        return bits