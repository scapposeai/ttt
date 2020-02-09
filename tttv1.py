import random


#constants
X=1
OPEN=0
O=-1

X_WIN=100
O_WIN=-100
NO_WINNER=0

squares = [OPEN,OPEN,OPEN,OPEN,OPEN,OPEN,OPEN,OPEN,OPEN]
winlines = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

def evaluateBoard():
    for i in range(0,8):
        sum=0
        for j in range(0,3):
            sum = sum + squares[winlines[i][j]]
        #print("sum={}".format(sum))
        if sum == 3:
            return X_WIN
        if sum == -3:
            return O_WIN
    return NO_WINNER

def gameOver():
    eval = evaluateBoard()
    if eval==X_WIN or eval==O_WIN:
        return True
    for i in range(0,9):
        if squares[i]==OPEN:
            return False
    return True

def getXmove():
    #for i in range(0,9):
    #    if squares[i]==OPEN:
    #        return i
    score, move = getBestMove(X,9)
    #print("score-{}, move={}".format(score,move))
    return move

def makeXmove():
    takeSquare = getXmove()
    squares[takeSquare]=X

def getOmove():
    score, move = getBestMove(O,1)
    #print("score-{}, move={}".format(score,move))
    return move

def makeOmove():
    takeSquare = getOmove()
    squares[takeSquare]=O

def getPrintChar(c):
    if c==X:
        return "X"
    if c==O:
        return "O"
    return "."

def printBoard():
    print(" {} {} {}".format(getPrintChar(squares[0]),getPrintChar(squares[1]),getPrintChar(squares[2])))
    print(" {} {} {}".format(getPrintChar(squares[3]),getPrintChar(squares[4]),getPrintChar(squares[5])))
    print(" {} {} {}".format(getPrintChar(squares[6]),getPrintChar(squares[7]),getPrintChar(squares[8])))
    print("")
    
def playGame():
    squares = [0,0,0,0,0,0,0,0,0]
    while gameOver()==False:
        makeXmove()
        printBoard()
        if gameOver()==False:
            makeOmove()
            printBoard()

def getBestMove(player, depth):
    #print("calling getBestMove {} , {}".format(player,depth))
    bestMove=None
    if player == X:
        bestScore=-100000
    else:
        bestScore=100000

    for i in range(0,9):
        if squares[i]==OPEN:
            squares[i]=player
            if gameOver()==False and depth>0:
                score, move = getBestMove(player * (-1), depth-1)
                if player==X:
                    if score>bestScore:
                        bestScore=score+depth
                        bestMove=i
                        #print("setting best {} = {}".format(bestMove,bestScore))
                        
                if player==O:
                    if score<bestScore:
                        bestScore=score-depth
                        bestMove=i
                        #print("setting best {} = {}".format(bestMove,bestScore))
                        
            else:
                score = evaluateBoard()
                #print("move {} = {}".format(i,score))
                if player==X:
                    if score>bestScore:
                        bestScore=score+depth
                        bestMove=i
                if player==O:
                    if score<bestScore:
                        bestScore=score-depth
                        bestMove=i
            
            squares[i]=OPEN
    return bestScore, bestMove

#squares = [X,X,X,0,0,0,0,0,0]
#evaluateBoard()
#score, move = getBestMove(O,1)
#print("score={}, move={}".format(score,move))

printBoard()
playGame()



