from queue import *
def findAllNeighbors(string, array):
    arrA = []
    stringLetters = "abcdefghijklmnopqrstuvwxyz"
    stringLettersList = list(stringLetters)
    myString = string
    newString = ""
    newStringList = list(myString)
    myArray = array
    for x in range(0,6):
        for y in range(0,26):
            newStringList = list(myString)
            newStringList[x] = stringLettersList[y]
            newString = "".join(newStringList)
            if(newString != myString and newString in myArray):
                arrA.append(newString)
    return arrA
def inputFile(filename):
    array = []
    f = open(filename)
    for s in f:
        s = f.readline()
        s = s.strip()
        array.append(s)
    return array;

def BFS(start, goal, dictionary):
    discovered = []
    queue = Queue()
    n = Node(start, None)
    queue.put(n)
    pathFound = False

    
    while(not queue.empty()):
        node = queue.get()
        if(node.getString() == goal):
            found(node)
            pathFound = True
            break;
        elif(node.getString() not in discovered):
            discovered.append(node.getString())
            arrNeighbors = findAllNeighbors(node.getString(), dictionary)
            for x in range(0, len(arrNeighbors)):
                queue.put(Node(arrNeighbors[x], node))
    if(pathFound == False):
        print("No path found")
                
    



def found(n):
    arrPath = []
    nPtr = n
    while(nPtr != None):
        arrPath.insert(0, nPtr.getString())
        nPtr = nPtr.getParent()
    print(arrPath)

def main():
    startString = input("Enter start word: ")
    endString = input("Enter end word: ")
    if len(startString) != len(endString):
        print("Words must be the same length")
    elif len(startString) < 6 or len(startString) > 10:
        print("Words must be between 6 and 10 letters long")
    else:
        BFS(startString, endString, inputFile(str(len(startString)) + "letterwords.txt"))
    
    
class Node:
    def __init__(self, value, parentNode):
        self.string = value
        self.parent = parentNode
    def getString(self):
        return self.string
    def getParent(self):
        return self.parent
while(True):               
    main()
