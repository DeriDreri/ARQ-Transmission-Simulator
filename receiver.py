class Receiver:

    # Konstruktor klasy
    def __init__(self):
        self.channel = None
        self.tabOfBits = []
        self.file = open("wyniki.txt", "w")         #tworzy pusty plik tekstowy do wynikow
        self.file.close()

    # Dodawanie kanału do odbiornika
    def addChannel(self, channel):
        self.channel = channel

    # Odbieranie ciągu bitów z kanału
    def receive(self, bitsStream):
        self.tabOfBits = bitsStream
        if self.checkBits(): # Sprawdzanie parzystości bitów
            self.saveToFile()
            self.tabOfBits.append(bitsStream)
            return True
        return False

    # Sprawdzanie parzystości ciągu bitów
    def checkBits(self):
        one = 0

        for i in range(len(self.tabOfBits)):
            if self.tabOfBits[i] == 1:
                one = one + 1

        if one % 2 == 0:  # Jeśli ilość '1' w ciągu jest parzysta to zwraca True
            return True

        return False
    #wpisywanie do pliku
    def saveToFile(self):
        self.file = open("wyniki.txt", "a")
        for bit in self.tabOfBits[:-1]:         #nawias kwadratowy sprawia, ze wpisuje sie bez bitu parzystości
            self.file.write(str(bit))
            self.file.write(",")        #wpisuje przecinek po kazdej liczbie, trzeba ustalic czy z czy bez nich
        self.file.write("\n")
        self.file.close()
