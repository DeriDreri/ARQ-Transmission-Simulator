from bitstring import ConstBitStream


class Receiver:

    # Konstruktor klasy
    def __init__(self):
        self.channel = None
        self.tabOfBits = []
        self.finalTab = []

    # Dodawanie kanału do odbiornika
    def addChannel(self, channel):
        self.channel = channel

    # Odbieranie ciągu bitów z kanału
    def receive(self, bitsStream):
        self.tabOfBits = bitsStream
        if self.checkBits():  # Sprawdzanie parzystości bitów
            #self.tabOfBits.append(bitsStream)
            for i in range (0,len(self.tabOfBits)-1):       # wpisuje zawartosc pakietu to jednej duzej listy na podstawie ktorej odtworzy sie wiadomosc
                self.finalTab.append(self.tabOfBits[i])
            #self.saveToFile()
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

    # wpisywanie do pliku
    def saveToFile(self):
        self.file = open("results.txt", "wb")               # tworzy pusty plik tekstowy do wynikow
        finalBitStream = ConstBitStream(self.finalTab)
        finalBitStream.tofile(self.file)                    # zapis typu ConstBitStream do pliku
        print(self.finalTab)                                # tymczasowa funkcja printujaca tablice
        self.file.close()
