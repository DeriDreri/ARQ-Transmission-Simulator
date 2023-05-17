from bitstring import ConstBitStream
from bitstring import ReadError
import numpy
import time


class Transmitter:

    # Konstruktor definiuje długość pakietów, nadmiarowość oraz liczbę wysłanych pakietów
    def __init__(self, packetLength):
        self.packetLength = packetLength
        self.tabOfBits = []
#        self.message = numpy.empty()
        self.sent = 0

    # Łaczy z plikiem odczytywanym
    def connectToInputFile(self, filePath):
        self.filePath = filePath
        self.reachedEndOfFile = False
        self.bitsStream = ConstBitStream(filename=filePath)

    # Podłącza do kanału
    def connectToChannel(self, channel):
        self.transmissionChannel = channel

    # Testowa funkcja do drukowania pakietów bitów
    def printBites(self):
        while (self.reachedEndOfFile == False):
            self.loadBites()
            if not self.tabOfBits:
                return
            self.codePacket()
            print(self.tabOfBits)

            # Ładuje nową porcję bitów do tablicy

    def loadBites(self):
        #start = time.time()
        self.tabOfBits = []  # Czyści tablicę z poprzednich bitów
        for i in range(0, self.packetLength):
            try:
                value = self.bitsStream.read('uint:1')
                self.tabOfBits.append(value)
            except ReadError:  # Spodziewa się końca pliku
                self.reachedEndOfFile = True
                return
        end = time.time()
        #print("Czas ładowania w nadajniku: ", end-start)

    # Funkcja wysyłająca bity
    def send(self, correctTransmission):
        
        while not self.reachedEndOfFile or not correctTransmission:
            #start = time.time()
            if correctTransmission:
                self.loadBites()
                self.codePacket()
            #end = time.time()
            #print("Czas w nadajniku: ", end - start )

            if self.transmissionChannel.receive(self.tabOfBits):
                correctTransmission = True
            else:
                correctTransmission = False

            self.sent = self.sent + 1


    def beginTransmission(self):
        self.send(True)

    # Funkcja wzywana wewnętrznie aby zakodować bit parzystości
    def codePacket(self):
        #start = time.time()
        self.tabOfBits = numpy.array(self.tabOfBits)
        onesAmount = numpy.count_nonzero(self.tabOfBits == 1)

        #for i in self.tabOfBits:
        #    if i == 1:
        #        EvenOnes = not EvenOnes

        if (onesAmount % 2 == 0):
            self.tabOfBits = numpy.append(self.tabOfBits, 0)
        else:
            self.tabOfBits = numpy.append(self.tabOfBits, 1)
        #end = time.time()
        #print("Czas kodowania w nadajniku: ", end - start)
      #  numpy.append(self.message, self.tabOfBits)

    # Zerowanie ilości wysłanych pakietów po zakończonej transmisji
    def clear(self):
        self.sent = 0
        self.tabOfBits = []
#        self.message = []
