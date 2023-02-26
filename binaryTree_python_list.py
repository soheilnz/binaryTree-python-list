class binaryT:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUseIndex = 0
        self.maxSize = size

    def insert(self, value):
        if self.lastUseIndex + 1 == self.maxSize:
            return "bT is full."
        else:
            self.customList[self.lastUseIndex + 1] = value
            self.lastUseIndex += 1
            return "the value inserted."

    def search(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "not found"

    def preOrderT(self, index):
        if index > self.lastUseIndex:
            return
        print(self.customList[index])
        self.preOrderT(index * 2)
        self.preOrderT(index * 2 + 1)

    def inOrder(self, index):
        if index > self.lastUseIndex:
            return
        self.inOrder(index * 2)
        print(self.customList[index])
        self.inOrder(index * 2 + 1)

    def postOrder(self, index):
        if index > self.lastUseIndex:
            return
        self.postOrder(index * 2)
        self.postOrder(index * 2 + 1)
        print(self.customList[index])

    def levelOrder(self, index):
        for i in range(index, self.lastUseIndex + 1):
            print(self.customList[i])

    def delete(self, value):
        if self.lastUseIndex == 0:
            return " no Bt"
        for i in range(1, self.lastUseIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUseIndex]
                self.customList[self.lastUseIndex] = None
                self.lastUseIndex -= 1
                return "finish!"

    def deleteHole(self):
        self.customList = None
        return " success"


newBT = binaryT(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))
newBT.insert("Tea")
newBT.insert("Coffee")
print(newBT.search("Hot"))
# newBT.preOrderT(1)
# newBT.inOrder(1)
# newBT.postOrder(1)
# newBT.levelOrder(1)
# print(newBT.delete("Hot"))
# newBT.levelOrder(1)
