class Puzzle:
    def __init__(self):
        self.goalMatrix = [3][3]  #correct answer matrix
        self.myMatrix = [3][3] #filled in a later method
        for r in range(0,3):
            for c in range(0,3):
                goalMatrix[r][c] = r*3+c+1
        self.myNum = 0
    
    def possibleMoves(): #finds the possible numbers that can switch with
                         #the blank space/line and puts them in an array
        possNumberMoves = []
        pos = findNumber(9)
        if(pos == 0):
            possNumberMoves.append(myMatrix[0][1])
            possNumberMoves.append(myMatrix[1][0])
        elif(pos == 1):
            possNumberMoves.append(myMatrix[0][0])
            possNumberMoves.append(myMatrix[0][2])
            possNumberMoves.append(myMatrix[1][1])
        elif(pos == 2):
            possNumberMoves.append(myMatrix[0][1])
            possNumberMoves.append(myMatrix[1][2])
        elif(pos == 3):
            possNumberMoves.append(myMatrix[0][0])
            possNumberMoves.append(myMatrix[1][1])
            possNumberMoves.append(myMatrix[2][0])
        elif(pos == 4):
            possNumberMoves.append(myMatrix[0][1])
            possNumberMoves.append(myMatrix[1][0])
            possNumberMoves.append(myMatrix[1][2])
            possNumberMoves.append(myMatrix[2][1])
        elif(pos == 5):
            possNumberMoves.append(myMatrix[0][2])
            possNumberMoves.append(myMatrix[1][1])
            possNumberMoves.append(myMatrix[2][2])
        elif(pos == 6):
            possNumberMoves.append(myMatrix[1][0])
            possNumberMoves.append(myMatrix[2][1])
        elif(pos == 7):
            possNumberMoves.append(myMatrix[1][1])
            possNumberMoves.append(myMatrix[2][0])
            possNumberMoves.append(myMatrix[2][2])
        elif(pos == 8):
            possNumberMoves.append(myMatrix[1][2])
            possNumberMoves.append(myMatrix[2][1])
            
    def findNumber(num):  #returns 0-8 position of the requested number
         for r in range(0,3):
            for c in range(0,3):
                if myMatrix[r][c] == num:
                    return r*3+c
    def createMatrix(num): #takes in a nine digit number like 123456789 to create goal state
        self.myNum = num
        stringVersion = str(num)
        for r in range(0,3):
            for c in range(0,3):
                myMatrix[r][c] = stringVersion[r*3+c]
    def createNumFromMoves(self,arrA[],num):  #finds all possible 2-4 new nums from the number tobe able to create a child of num
    def createTree():
        t = new Tree()
        t.addRoot(num)
        found = False
        while(found == False):
            t.addChild(
    def main(num):
        createMatrix(num)

                
class Node:
    def __init__(self, val):
        self.ll = None
        self.lr = None
        self.rl = None
        self.rr = None
        self.mypos = None # is node the ll, lr, rl, or rr of parent  root if root
        self.parent = None #reference to parent
        # 2-4 possible states after one move depending on placement of space/9
        # fills in order ll -> lr -> rl -> rr
        self.v = val  #sequence of 1-9 in order
                      #123
                      #456
                      #789  is 123456789

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addRoot(self, val):
        if(self.root == None):
            self.root = Node(val)
            self.root.ll = Node(None)
    def addChild(self, val, node):
            if(node.ll == None):
                node.ll = Node(val)
            elif(node.lr == None):
                node.lr = Node(val)
            elif(node.rl == None):
                node.rl = Node(val)
            else:
                node.rr = Node(val)
#   def find(self, val):
#     if(self.root != None):
#         return self._find(val, self.root)
#    else:
#       return None
#
#   def _find(self, val, node):
#      if(val == node.v):
#         return node
#    elif(val < node.v and node.l != None):
#       self._find(val, node.l)
#    elif(val > node.v and node.r != None):
#       self._find(val, node.r)

#    def deleteTree(self):
#        self.root = None
#
#    def printTree(self):
#        if(self.root != None):
#            self._printTree(self.root)
#
#    def _printTree(self, node):
#        if(node != None):
#            self._printTree(node.l)
#            print str(node.v) + ' '
#            self._printTree(node.r)
    def equals(node1, node2):
        if(node1.val == node2.val):
            return True
        else:
            return False
    
