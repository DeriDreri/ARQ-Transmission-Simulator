from bitstring import ConstBitStream
import numpy
import time


class Receiver:

    # Konstruktor klasy
    def __init__(self, filename):
        self.tabOfBits = []
        self.finalTab = []
        self.fileName = filename
        self.accepted = 0

    # Dodawanie kanału do odbiornika
    def addChannel(self, channel):
        self.channel = channel

    # Odbieranie ciągu bitów z kanału
    def receive(self, bitsStream):
        start = time.time()
        self.tabOfBits = bitsStream
        if self.checkBits():  # Sprawdzanie parzystości bitów
            # for i in range (0,len(self.tabOfBits)-1):       # wpisuje zawartosc pakietu to jednej duzej listy na
            # podstawie ktorej odtworzy sie wiadomosc self.finalTab.append(self.tabOfBits[i])
            bitsStream = bitsStream.tolist()   
            bitsStream.pop()
            self.finalTab = self.finalTab + bitsStream
            self.accepted = self.accepted + 1
            end = time.time()
            #print("Czas w odbiorniku: ", end-start)
            return True
        end = time.time()
        #print("Czas w odbiorniku: ", end-start)
        return False

    # Sprawdzanie parzystości ciągu bitów
    def checkBits(self):
        start = time.time()
        #evenOnes = True

        onesCount = numpy.count_nonzero(self.tabOfBits == 1)

        #for i in self.tabOfBits:
        #    if i == 1:
        #        evenOnes = not evenOnes
        end = time.time()
        #print("Czas dekodowania: ", end - start)
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
        #start = time.time()
        checkFinal = numpy.array(self.finalTab)
        input_message = numpy.add(checkFinal, input_message)
        antiCounter = numpy.count_nonzero(input_message == 1)
        #end = time.time()
        #print("Czas porównywania: ", end - start)
        #for i in range(0, len(self.finalTab)):
        #    if self.finalTab[i] == input_message[i]:
        #        counter = counter + 1

        return antiCounter

    # Zerowanie ilości zaakceptowanych pakietów po zakończonej transmisji
    def clear(self):
        self.accepted = 0
        self.finalTab = []

