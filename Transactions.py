import hashlib
import time


class Transaction:
    def __init__(self):
        self.id = None
        self.inputs = None
        self.outputs = None


class Output:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount


class Input:
    def __init__(self):
        self.outputId = None
        self.outputIndex = None
        self.signature = None


def idTransaction(transaction):
    pass
