from bitstring import ConstBitStream


class Receiver:

    # Konstruktor klasy
    def __init__(self):
        self.tabOfBits = []
        self.finalTab = []
        self.fileName = 'output-files/output.txt'

    # Dodawanie kanału do odbiornika
    def addChannel(self, channel):
        self.channel = channel

    # Odbieranie ciągu bitów z kanału
    def receive(self, bitsStream):
        self.tabOfBits = bitsStream
        if self.checkBits():  # Sprawdzanie parzystości bitów
        #    for i in range (0,len(self.tabOfBits)-1):       # wpisuje zawartosc pakietu to jednej duzej listy na podstawie ktorej odtworzy sie wiadomosc
        #        self.finalTab.append(self.tabOfBits[i])
            bitsStream.pop()
            self.finalTab = self.finalTab + bitsStream
            return True
        return False

    # Sprawdzanie parzystości ciągu bitów
    def checkBits(self):
        evenOnes = True

        for i in self.tabOfBits:
            if i == 1:
                evenOnes = not evenOnes

        return evenOnes

    def setNewOutput(self, fileName):
        self.fileName = fileName

    # wpisywanie do pliku
    def saveToFile(self):
        file = open(self.fileName, "wb")               # tworzy pusty plik tekstowy do wynikow
        finalBitStream = ConstBitStream(self.finalTab)
        finalBitStream.tofile(file)                    # zapis typu ConstBitStream do pliku
        self.finalTab = []                             # czyści tablicę po zapisie danych
        file.close()
