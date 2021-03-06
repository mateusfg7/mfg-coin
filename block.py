import hashlib
import time
import binascii


# classe pra gerar um bloco
class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce


# classe principal da blockchain
class Blockchain:
    def __init__(self, genesisBlock):
        # armazenamento de blocos da blockchain, onde os blocos ficam armazenados
        self.__chain = []
        self.__chain.append(genesisBlock)
        self.DIFFICULTY_AJUSTMENT = 10
        self.BLOCK_INTERVAL = 120

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

    def hashMatchesDifficulty(self, hash, difficulty):
        hashBinary = binascii.unhexlify(hash)
        requiredPrefix = '0' * int(difficulty)
        return hashBinary.startswith(requiredPrefix)

    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = self.calculateHash(
                index, previousHash, timestamp, data, difficulty, nonce)
            if self.hashMatchesDifficulty(hash, difficulty):
                block = Block(index, previousHash, timestamp,
                              data, difficulty, nonce)
                return block
            nonce += 1

    def getDifficulty(self):
        latestBlock = self.getLatestBlock()
        if latestBlock.index % self.DIFFICULTY_AJUSTMENT == 0 and latestBlock.index != 0:
            return self.getAjustedDifficulty()
        return latestBlock.difficulty

    def getAjustedDifficulty(self):
        latestBlock = self.getLatestBlock()
        previousAjustmentBlock = self.blockchain[len(
            self.blockchain) - self.DIFFICULTY_AJUSTMENT]
        timeExpected = self.BLOCK_INTERVAL * self.DIFFICULTY_AJUSTMENT
        timeTake = latestBlock.timestamp - prevAjustmentBlock.timestamp
        if timeTake < timeExpected * 2:
            return preAjustmentBlock.difficulty + 1
        elif timeTake > timeExpected * 2:
            return prevAdjustmentBlock.difficulty - 1
        return prevAjustmentBlock.difficulty


def calculateHash(index: int, previousHash: str, timestamp: int, data: str, difficulty: int, nonce: int) -> str:
    return hashlib.sha256((str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).encode('utf-8')).hexdigest()


timestamp = int(round(time.time() * 1000))
genesisBlock = Block(0, "", timestamp, 'Genesis Block',
                     calculateHash(0, "", timestamp, 'Genesis Block'))
