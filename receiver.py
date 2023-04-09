bit_oven = True  # Bit parzystości


class Receiver:

    # Konstruktor klasy
    def __init__(self):
        self.channel = None
        self.tabOfBits = []

    # Dodawanie kanału do odbiornika
    def addChannel(self, chnl):
        self.channel = chnl

    # Odbieranie ciągu bitów z kanału
    def receive(self, bitsStream):
        self.tabOfBits = bitsStream
        if self.checkBits(): # Sprawdzanie parzystości bitów
            return True
        return False

    # Sprawdzanie parzystości ciągu bitów
    def checkBits(self):
        one = 0

        for i in range(len(self.tabOfBits) - 1):
            if self.tabOfBits[i] == 1:
                one = one + 1

        if one % 2 == 0:  # Jeśli ilość '1' w ciągu jest parzysta to zwraca True
            return True

        return False
