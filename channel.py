import bitstring

import transmitter

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

    # Generator liczb pseudolosowych
    def random(self, seed, a=1103515245, c=12345, m=2 ** 31 - 1):
        while True:
            seed = (a * seed + c) % m
            yield seed / m  # Normalizacja do przedziału [0,1)

    # Odbieranie ciągu bitów z nadajnika
    def receive(self, bitsStream):
        self.bits = bitsStream

    # Nakładanie zakłóceń
    def addNoise(self):
        noisy_bits = []
        for bit in self.bits:
            if next(self.random(seed)) < error_Rate:
                noisy_bits.append(int(not bit))
            else:
                noisy_bits.append(bit)

        return noisy_bits
