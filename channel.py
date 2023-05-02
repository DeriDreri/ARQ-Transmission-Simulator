import time
import numpy

class Channel:

    # Konstruktor definiuje nadajnik i odbiornik
    def __init__(self, transmitter, receiver):
        self.error_Rate = 0
        self.transmitter = transmitter
        self.receiver = receiver
        transmitter.connectToChannel(self)
        receiver.addChannel(self)

    # Generator liczb pseudolosowych

    @staticmethod
    def random():
        seed = int(round(time.time() * 1000000000000))
        a = 1103515245
        c = 12345
        m = 2 ** 31
        seed = (a * seed + c) % m
        time.sleep(0.000000001)
        return seed / m

    # Odbieranie ciągu bitów z nadajnika, wysyłanie go do odbiornika
    def receive(self, bitsStream):

        bitsStream = self.addNoise(bitsStream)  # Nakładanie zakłóceń na ciąg bitów

        return self.receiver.receive(bitsStream)  # Wysyłanie ciągu bitów do odbiornika i odbieranie potwierdzenia

    # Nakładanie zakłóceń
    def addNoise(self, bits):
        noisy_bits = []
        for bit in bits:
            if self.random() < self.error_Rate:
                noisy_bits.append(int(not bit))
            else:
                noisy_bits.append(bit)

        return noisy_bits

    # Ustawianie prawdopodobieństwa wystąpienia błędu
    def set_error_rate(self, error):
        self.error_Rate = error
