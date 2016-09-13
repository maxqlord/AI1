class MinHeap:
    
    def __init__(self, size):
        self.size = size
        self.mH = [size + 1]
        self.position = 0
        
    def createHeap(arrA):
        if len(arrA)>0:
            for x in range(0, len(arrA)):
                insert(arrA[i])
    def display():
        for i in range(1,len(mH)):
            print (" " + (mH[i]))
        print ("")
    def insert(x):
        if position == 0:
            mH[position+1] = x
            position = 2
        else:
            mH[position + 1] = x
            bubbleUp()
    def bubbleUp():
        pos = position - 1
        x = 1
        while pos > 0 & mH[pos/2] > mh[pos]:
            y = mH[pos]
            mH[pos] = mH[pos/2]
            mH[pos/2] = y
            pos = pos/2
    def extractMin():
        min = mH[1]
        mH[1]=mH[position-1]
        mH[position-1]=0
        position = position - 1
        sinkDown(1)
        return min
    def sinkDown(k):
        a = mH[k]
        smallest = k
        if 2*k < position & mH[smallest]>mH[2*k+1]:
            smallest = 2*k
        if 2*k+1 < position & mH[smallest]>mH[2*k+1]:
            smallest = 2*k+1
        if smallest != k:
            swap(k,smallest)
            sinkDown(k,smallest)
    def swap(a,b):
        temp = mH[a]
        mH[a] = mH[b]
        mH[b] = temp



    arrA = {3,2,1,7,8,4,10,16,12}
    print("Original Array : ")
    for x in range(0, len(arrA)):
        print(" " + arrA[x])
    m = minHeap(len(arrA))
    print("nMin-Heap : ")
    

        

