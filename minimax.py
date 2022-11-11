from konane import *

class MinimaxPlayer(Konane, Player):
    def __init__(self, size, depthLimit): 
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        self.side = side
        self.name = "Minimax depth: " + str(self.limit)
    def getMove(self, board): # finds the optimal next move
        print("DepthLimit:", self.limit)
        availableMoves = self.generateMoves(board, self.side)
        if (len(availableMoves) == 0):
            return []
        else:
            bestMove = (-1000000, [0, 0, 0, 0])
            for child in availableMoves:
                theNextBoard = self.nextBoard(board, self.side, child)
                # print("Move:", child)
                # print("Eval:", self.eval(theNextBoard))
                # print("BestMoveValue:", bestMoveValue)
                evalResult = self.getMoveHelper(theNextBoard, 0, self.opponent(self.side))
                print("Eval:", evalResult)
                if (evalResult > bestMove[0]):
                    bestMove = (evalResult, child)
            return bestMove[1]
            
            # what we need to do: 
                # get the available moves
                # call getMoveHelper for each of the available moves
                # pick the move with the lowest eval
        
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
        return self.size ** 2 - self.countSymbol(board, self.opponent(self.side))

game = Konane(10)
game.playNGames(1, MinimaxPlayer(8, 1), MinimaxPlayer(8, 4), 1)