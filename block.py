import hashlib
import time


# classe pra gerar um bloco
class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hahs = hash


# classe principal da blockchain
class Blockchain:
    def __init__(self, genesisBlock):
        # armazenamento de blocos da blockchain, onde os blocos ficam armazenados
        self.__chain = []
        self.__chain.append(genesisBlock)

    # pegar o último bloco na blockchain
    def getLatestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    # criar um novo bloco
    def generateNextBlock(self, data):
        previousBlock = self.getLatestBlock()
        nextIndex = previousBlock.index + 1
        nxtTimestamp = int(round(time.time() * 1000))
        nextPreviousHash = previousBlock.hash
        newBlock = Block(nextIndex, nextPreviousHash, nxtTimestamp, data,
                         calculateHash(nextIndex, nextPreviousHash, timestamp, data))

        # adicionar um novo bloco na bllockchain se a validação for bem sucedida
        if validatingBlock(newBlock):
            self.__chain.append(newBlock)

    # validar um bloco
    def validatingBlock(self, newBlock) -> bool:
        previousBlock = self.getLatestBlock()
        if previousBlock.index + 1 != newBlock.index:
            return False
        elif previousBlock.hash != newBlock.previousHash:
            return False
        return True


def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(str(index) + previousHash + str(timestamp) + data).hexdigest()


timestamp = int(round(time.time() * 1000))
genesisBlock = Block(0, "", timestamp, 'Genesis Block',
                     calculateHash(0, "", timestamp, 'Genesis Block'))
