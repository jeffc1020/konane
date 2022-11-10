from json.encoder import INFINITY
from konane import *

class MinimaxPlayer(Konane, Player):
    def __init__(self, size, depthLimit): 
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        self.side = side
        self.name = "MinimaxPlayer"
    def getMove(self, board): # finds the optimal next move
        #return self.getMoveHelper(board, 0)
        availableMoves = self.generateMoves(board, self.side)
        if (len(availableMoves) == 0):
            return []
        else:
            bestMoveValue = self.getMoveHelper(board, 0, self.side)
            for child in availableMoves:
                if (self.eval(self.nextBoard(board, self.side, child)) == bestMoveValue):
                    return child
        
    def getMoveHelper(self, board, depth, currentTurn):
        if (self.generateMoves(board, currentTurn)): movesAvailable = True
        else: movesAvailable = False
        if (depth >= self.limit or movesAvailable == False):
            return self.eval(board)
        if (currentTurn == self.side): # maximizing
            value = -1000000
            for child in self.generateMoves(board, currentTurn):
                theNextBoard = self.nextBoard(board, currentTurn, child)
                nextIteration = self.getMoveHelper(theNextBoard, depth + 1, self.opponent(currentTurn))
                value = max(value, nextIteration)
            return value
        else: # minimizing
            value = 1000000
            for child in self.generateMoves(board, currentTurn):
                theNextBoard = self.nextBoard(board, currentTurn, child)
                nextIteration = self.getMoveHelper(theNextBoard, depth + 1, self.opponent(currentTurn))
                value = min(value, nextIteration)
            return value
        
    def eval(self, board):
        return self.countSymbol(board, self.side) # should be good for now
        
game = Konane(8)
game.playNGames(1, MinimaxPlayer(8, 2), MinimaxPlayer(8, 2), 1)