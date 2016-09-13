class minHeap:
    def __init__(self, size):
        self.size = size
        self.mH = []
        for x in range(size + 1):
            self.mH.append(0)
        self.position = 0
    def createHeap(self, arrA):
        if(len(arrA)>0):
            for x in range(0, len(arrA)):
                self.insert(arrA[x])
    def display(self):
        for i in range(1, self.size + 1):
            print (" " + (str(self.mH[i])))
        print ("")
    def insert(self,x):
        if(self.position == 0):
            self.mH[self.position + 1] = x
            self.position = 2
        else:
            self.mH[self.position] = x
            self.position += 1
            self.bubbleUp()
    def bubbleUp(self):
        pos = self.position - 1
        while pos > 0 and self.mH[pos//2] > self.mH[pos]:
            y = self.mH[pos]
            self.mH[pos] = self.mH[pos//2]
            self.mH[pos//2] = y
            pos = pos//2
    def extractMin(self):
        minNum = self.mH[1]
        self.mH[1]= self.mH[self.position-1]
        self.mH[self.position-1]=0
        self.position = self.position - 1
        self.sinkDown(1)
        return minNum
    def sinkDown(self,k):
        a = self.mH[k]
        smallest = k
        if(2*k < self.position and self.mH[smallest]> self.mH[2*k]):
            smallest = 2*k
        if(2*k+1 < self.position and self.mH[smallest]> self.mH[2*k+1]):
            smallest = 2*k+1
        if(smallest != k):
            self.swap(k,smallest)
            self.sinkDown(smallest)
    def swap(self,a,b):
        temp = self.mH[a]
        self.mH[a] = self.mH[b]
        self.mH[b] = temp
    def main():
        arrA = [3,2,1,7,8,4,10,16,12]
        print("Original Array : ")
        for x in range(0, len(arrA)):
            print(" " + str(arrA[x]))
        print("\nMin-Heap : ")
        m = minHeap(len(arrA))
        m.createHeap(arrA)
        m.display()
        print("Extract Min :")
        for i in range(0,len(arrA)):
            print(" " + str(m.extractMin()))
minHeap.main()
        

