import time

# Prawdopodobieństwo wystąpienia błędu
error_Rate = 0.25  # 25%


class Channel:

    # Konstruktor definiuje nadajnik i odbiornik
    def __init__(self, transmitter, receiver):
        self.bits = []
        self.transmitter = transmitter
        self.receiver = receiver
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
        self.bits = bitsStream  # Odbieranie ciągu bitów z nadajnika
        print("\nCiąg bitów jest w kanale:")
        print(self.bits)

        self.bits = self.addNoise()  # Nakładanie zakłóceń na ciąg bitów
        print("\nNałożono zakłócenia na ciąg bitów:")
        print(self.bits)
        print("=========================\n")

        return self.receiver.receive(self.bits)  # Wysyłanie ciągu bitów do odbiornika i odbieranie potwierdzenia

    # Nakładanie zakłóceń
    def addNoise(self):
        noisy_bits = []
        for bit in self.bits:
            if self.random() < error_Rate:
                noisy_bits.append(int(not bit))
            else:
                noisy_bits.append(bit)

        return noisy_bits