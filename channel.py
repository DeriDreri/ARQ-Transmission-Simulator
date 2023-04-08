import bitstring

# Prawdopodobieństwo wystąpienia błędu
error_Rate = 0, 5

# Początkowy stan generatora (ziarno)
seed = 42


class Channel:

    # Konstruktor definiuje nadajnik i odbiornik
    def __init__(self, transmitter, receiver):
        self.transmitter = transmitter
        self.receiver = receiver

    # Generator liczb pseudolosowych
    def random(seed, a=1103515245, c=12345, m=2 ** 31 - 1):
        while True:
            seed = (a * seed + c) % m
            yield seed / m  #Normalizacja do przedziału [0,1)

    generator = random(seed)
