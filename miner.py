from block import Block
import random
import hashlib
import string
import time
class Miner:
    def __init__(self):
        self.block = Block()
        self.currentBlockID = 0
        self.prevHash = -1
        self.difficulty = 3

        self.listOfBlocks = self.findBlocks()
        counter = 0
        while counter < 100:
            # Will change the difficulty based on the time.
            # We want a new block every 15 seconds
            start_time = time.time()
            start = time.clock()
            self.mine()
            end_time = time.time()
            end = time.clock()
            print("--- %s seconds ---" % (end_time - start_time))

            # change the difficulty based on time used
            if (end - start) > 60:
                self.difficulty -= 1
                if self.difficulty == 0:
                    self.difficulty = 1
                print("Decreased the difficulty, it's now: " + str(self.difficulty))

            if (end - start) < 4:
                self.difficulty += 1
                if self.difficulty == 0:
                    self.difficulty = 1
                print("Increased the difficulty, it's now: " + str(self.difficulty))
            counter += 0
            print(self.currentBlockID)



    def findBlocks(self):
        # Read the file with all the blocks
        blockFile = open("blockList.txt", "r")
        blockFile.readline()
        blocklist = []
        for line in blockFile:
            items = line.split("|")
            blocklist.append((items[0].strip(), items[1].strip()))
            self.prevHash = items[1]
            self.currentBlockID += 1

        #print(blocklist)
        if len(blocklist) == 0:
            # No block exists, we need to create the genisisblock
            print("No block, create genisisblock")
            block = Block()
            self.prevHash = block.generateGenisisBlock()
            self.currentBlockID += 1

    def mine(self):
        #
        pass
        # Will need to create a block
        # Will need to add all transactions (generate a random lenght list with some random numbers)
        # Will need to take the Sah256 of the:
        # block ID, the prevHash and the transactionsIDs and lastly the nounce.

        # Gen transactions
        transactionList = random.sample(range(0, 10000), random.randrange(1, 101, 1))
        #print(randomTransactions)

        passedAsValidBlock = False
        nounce = ""
        genHash = ""
        while not passedAsValidBlock:

            # Generate random nounce
            nounce = self.randomword(random.randint(0, 100))
            # Take the hash
            genHash = self.generateHash(self.currentBlockID, self.prevHash, transactionList, nounce)
            #print(genHash)
            #print(self.validatehash(genHash))
            validHash = self.block.validatehash(genHash, self.difficulty)
            if validHash:
                passedAsValidBlock = True
                print("We found a valid combination")

        self.block.writeToChain(self.currentBlockID, self.prevHash, transactionList, nounce)

        # Set the prevHash and increase the block ID
        self.currentBlockID += 1
        print("Prev hash" + self.prevHash)
        self.prevHash = genHash

        time.sleep(5)




    def randomword(self, length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    def generateHash(self, blockID, prevHash, transactionList, nounce):
        #print(hashlib.algorithms_available)
        #print(hashlib.algorithms_guaranteed)
        hashableString = str(blockID) + str(prevHash) + str(transactionList) + nounce
        #print(hashableString)
        b = hashableString.encode('utf-8')
        hash_object = hashlib.sha256(b)
        hex_dig = hash_object.hexdigest()
        #print(hex_dig)
        return hex_dig

    def validatehash(self, theHash):
        # Convert theHash to binary input

        checkable = theHash[:self.difficulty]

        for x in checkable:
            if x == "0":
                pass
            else:
                return False
        # All the letters are 0 (zero), then return true

        return True

miner = Miner()
