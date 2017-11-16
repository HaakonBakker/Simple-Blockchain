import time
import hashlib

class Block:
    def __init__(self):
        self.difficulty = 4



    def generateGenisisBlock(self):
        # Will create a genisisblock.
        return self.writeToChain(0, "Hello! This is the genesis block! No prev. hash necessary ", [], "First Ever Block!")


    def validateBlock(self):
        """ Will return whether or not a block is valid """
        pass

    def validateChain(self):
        """ Will validate the blockchain to make sure it's correct """
        pass

    def validatehash(self, theHash, difficulty):
        """ Will return whether or not a block has a valid hash (according to the difficulty) """

        checkable = theHash[:difficulty]

        for x in checkable:
            if x == "0":
                pass
            else:
                return False
        # All the letters are 0 (zero), then return true
        time.sleep(5)
        return True

    def writeToChain(self, blockID, previousHash, transactionList, nounce):
        """ Will write the block to the blockchain """
        # Now we need to add the block to the ledger
        file = open("blockList.txt", "a")
        # Write to file the correct way
        file.write(str(blockID) + "|" + str(previousHash) + "|" + str(transactionList) + "|" + str(nounce) + "\n")

        file.close()

        hashableString = str(blockID) + str(previousHash) + str(transactionList) + nounce
        #print(hashableString)
        b = hashableString.encode('utf-8')
        hash_object = hashlib.sha256(b)
        hex_dig = hash_object.hexdigest()
        #print(hex_dig)
        return hex_dig
