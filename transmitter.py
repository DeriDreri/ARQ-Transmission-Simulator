from bitstring import ConstBitStream
from bitstring import ReadError


class Transmitter:

    # Konstruktor definiuje długość pakietów i nadmiarowość
    def __init__(self, packetLength):
        self.packetLength = packetLength
        self.tabOfBits = []

    # Łaczy z plikiem odczytywanym
    def connectToInputFile(self, filePath):
        self.filePath = filePath
        self.reachedEndOfFile = False
        self.bitsStream = ConstBitStream(filename=filePath)

    # Podłącza do kanału
    def connectToChannel(self, channel):
        self.transmissionChannel = channel
        print("Podłączono kanał")

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
        self.tabOfBits = []  # Czyści tablicę z poprzednich bitów
        for i in range(0, self.packetLength):
            try:
                value = self.bitsStream.read(1).uint
                self.tabOfBits.insert(i, value)
            except ReadError:  # Spodziewa się końca pliku
                self.reachedEndOfFile = True
                return

    # Funkcja wysyłająca bity
    def send(self, correctTransmission):
        while not self.reachedEndOfFile or not correctTransmission :

            if correctTransmission:
                self.loadBites()
                self.codePacket()

            if self.transmissionChannel.receive(self.tabOfBits):
                print("Informacja potwierdzona")
                print()
                correctTransmission = True
            else:
                print("Informacja niepotwierdzona")
                print()
                correctTransmission = False

    def beginTransmission(self):
        self.send(True)

    # Funkcja wzywana wewnętrznie aby zakodować bit parzystości
    def codePacket(self):
        EvenOnes = True
        for i in self.tabOfBits:
            if i == 1:
                EvenOnes = not EvenOnes

        if (EvenOnes):
            self.tabOfBits.insert(len(self.tabOfBits), 0)
        else:
            self.tabOfBits.insert(len(self.tabOfBits), 1)
