# Prawdopodobieństwo wystąpienia błędu
error_Rate = 0.5

# Początkowy stan generatora (ziarno)
seed = 42


class Channel:

    # Konstruktor definiuje nadajnik i odbiornik
    def __init__(self, transmitter, receiver):
        self.bits = []
        self.transmitter = transmitter
        self.receiver = receiver
        receiver.addChannel(self)

    # Generator liczb pseudolosowych
    @staticmethod
    def random(seed, a=1103515245, c=12345, m=2 ** 31 - 1):
        while True:
            seed = (a * seed + c) % m
            yield seed / m  # Normalizacja do przedziału [0,1)

    # Odbieranie ciągu bitów z nadajnika, wysyłanie go do odbiornika
    def receive(self, bitsStream):
        self.bits = bitsStream  # Odbieranie ciągu bitów z nadajnika
        self.addNoise()  # Nakładanie zakłóceń na ciąg bitów
        return self.receiver.receive(self.bits)  # Wysyłanie ciągu bitów do odbiornika i odbieranie potwierdzenia

    # Nakładanie zakłóceń
    def addNoise(self):
        noisy_bits = []
        for bit in self.bits:
            if next(self.random(seed)) < error_Rate:
                noisy_bits.append(int(not bit))
            else:
                noisy_bits.append(bit)

        return noisy_bits
