from bitstring import ConstBitStream
import numpy


class Receiver:

    # Konstruktor klasy
    def __init__(self):
        self.tabOfBits = numpy.empty(0)
        self.finalTab = numpy.empty(0)
        self.fileName = 'output-files/output.txt'
        self.accepted = 0

    # Dodawanie kanału do odbiornika
    def addChannel(self, channel):
        self.channel = channel

    # Odbieranie ciągu bitów z kanału
    def receive(self, bitsStream):
        self.tabOfBits = bitsStream
        if self.checkBits():  # Sprawdzanie parzystości bitów
            # for i in range (0,len(self.tabOfBits)-1):       # wpisuje zawartosc pakietu to jednej duzej listy na
            # podstawie ktorej odtworzy sie wiadomosc self.finalTab.append(self.tabOfBits[i])
            self.tabOfBits = numpy.delete(self.tabOfBits, -1)
            self.finalTab = numpy.append(self.finalTab, self.tabOfBits)
            self.accepted = self.accepted + 1
            return True
        return False

    # Sprawdzanie parzystości ciągu bitów
    def checkBits(self):
        #evenOnes = True

        onesCount = numpy.count_nonzero(self.tabOfBits == 1)

        #for i in self.tabOfBits:
        #    if i == 1:
        #        evenOnes = not evenOnes

        return (onesCount % 2 == 0)

    def setNewOutput(self, fileName):
        self.fileName = fileName

    # wpisywanie do pliku
    def saveToFile(self):
        file = open(self.fileName, "wb")  # tworzy pusty plik tekstowy do wynikow
        finalBitStream = ConstBitStream(self.finalTab)
        finalBitStream.tofile(file)  # zapis typu ConstBitStream do pliku
        self.finalTab = numpy.empty(0)  # czyści tablicę po zapisie danych
        file.close()


    # Porównywanie input z output
    def compare(self, input_message):
        counter = 0 # Zliczanie ilosci takich samych bitow

        numpy.add(self.finalTab, input_message)
        antiCounter = numpy.count_nonzero(self.finalTab == 1)
        #for i in range(0, len(self.finalTab)):
        #    if self.finalTab[i] == input_message[i]:
        #        counter = counter + 1

        return counter

    # Zerowanie ilości zaakceptowanych pakietów po zakończonej transmisji
    def clear(self):
        self.accepted = 0
        self.finalTab = []

