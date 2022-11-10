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
        bestMoveValue = self.getMoveHelper(board, 0, self.side)
        availableMoves = self.generateMoves(board, self.side)
        if (len(availableMoves) == 0):
            return []
        else:
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
        
        """
        if depth == self.limit: # base case: we are at a leaf node
            return eval(board)# return the heuristic (eval function) of this leaf node
        if (depth % 2 == 0): # if we are at an even depth 
            currentTurn = self.side # it's our turn (rather than the opponent's)
            maximizing = True
            # I may have this backwards
        else: # else, we are at an odd depth
            currentTurn = self.opponent # it's the opponent's turn
            maximizing = False
        # figure out if this is a min or max turn and figure out the optimal move in generateMoves
        moveList = []
         # return the heuristic (eval function) of this leaf node
        for mov in self.generateMoves(board, currentTurn): # loops through each next move for the current node
            nextBoard = self.nextBoard(board, currentTurn, mov)
            nextMove = self.getMoveHelper(nextBoard, depth + 1)
            tempTuple = (mov, nextMove)
            moveList.append(tempTuple)
        # actually choose the next move
        if maximizing:
            # choose the move with the max associated value
            return max(value[1] for value in moveList)
            #return max(moveList[0[1]]) # needs fixin
        else:
            # choose the move with the min associated value
            return min(value[1] for value in moveList)
            #return min(moveList[0[1]]) # needs fixin
        """
    def eval(self, board):
        return self.countSymbol(board, self.side) # should be good for now
        
game = Konane(8)
game.playNGames(1, MinimaxPlayer(8, 1), MinimaxPlayer(8, 1), 1)