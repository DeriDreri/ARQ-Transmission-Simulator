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
        seed = int(round(time.time() * 10000000000000))
        a = 1103515245
        c = 12345
        m = 2 ** 31
        seed = (a * seed + c) % m
        time.sleep(0.0000000001)
        return seed / m

    # Odbieranie ciągu bitów z nadajnika, wysyłanie go do odbiornika
    def receive(self, bitsStream):
        #start = time.time()

        bitsStream = self.addNoise(bitsStream)  # Nakładanie zakłóceń na ciąg bitów
        #end = time.time()
        #print("Time in channel: ", end - start)

        return self.receiver.receive(bitsStream)  # Wysyłanie ciągu bitów do odbiornika i odbieranie potwierdzenia

    # Nakładanie zakłóceń
    def addNoise(self, bits):
        noisy_bits = numpy.random.rand(len(bits))
        noisy_bits = numpy.array(noisy_bits)
        amount = numpy.count_nonzero(noisy_bits < self.error_Rate)
        inds = numpy.random.choice(bits, size=amount)
        if (inds.any()):
            for i in inds:
                bits[i] = not bits[i]
        return bits

    # Ustawianie prawdopodobieństwa wystąpienia błędu
    def set_error_rate(self, error):
        self.error_Rate = error
