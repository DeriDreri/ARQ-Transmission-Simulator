import bitstring


class Channel:

    # Konstruktor definiuje nadajnik i odbiornik
    def __init__(self, transmitter, receiver):
        self.transmitter = transmitter
        self.receiver = receiver
