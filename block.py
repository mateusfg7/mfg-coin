import hashlib
import time


class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hahs = hash


def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(index + previousHash + timestamp + data).hexdigest()


genesisBlock = Block(0, "", int(round(time.time() * 1000)), 'Genesis Block',
                     calculateHash(0, "", int(round(time.time() * 1000)), 'Genesis Block'))
