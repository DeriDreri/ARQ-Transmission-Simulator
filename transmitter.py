from bitstring import ConstBitStream

class Transmitter:

    def __init__(self, packetLength, extraBits):
        self.packetLength = packetLength
        self.extraBits = extraBits

    def connectToInputFile(self, filePath):
        self.filePath = filePath
        self.bitsStream = ConstBitStream(filename = filePath)
    

    def connectToChannel(self, channel):
        self.transmissionChannel = channel

    def printBites(self):
        tab = []
        for i in range (0, 7):
            value = self.bitsStream.read(1).uint
            tab.insert(i, value)
        print(tab)

def main():
    transmitter = Transmitter(10, 0)
    transmitter.connectToInputFile('input-files/input.txt')
    transmitter.printBites()

main()