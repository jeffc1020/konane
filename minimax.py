from konane import *

class MinimaxPlayer(Konane, Player):
    def __init__(self, size, depthLimit): 
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        self.side = side
        self.name = "MinimaxPlayer"
    def getMove(self, board):
        self.getMoveHelper(board, 0)
        moves = self.generateMoves(board, self.side)
        # nextboard??
        n = len(moves)
        if n == 0:
            return []
        else:
            for i in moves:
                return
    def getMoveHelper(self, board, depth):
        if (depth % 2 == 0):
            currentTurn = self.side
            maximizing = True
        else:
            currentTurn = self.opponent
            maximizing = False
        # figure out if this is a min or max turn and figure out the optimal move in generateMoves
        moveList = []
        
        if depth == self.depthLimit:
            return eval(board)
        for move in self.generateMoves(board, currentTurn):
            tempTuple = (move, self.getMoveHelper(self.nextBoard(board, currentTurn, move), depth + 1))
            moveList.append(tempTuple)
        if maximizing:
             max(moveList[0[1]])
        else:
            min(moveList[0[1]])
    
    def eval(self, board):
        self.countSymbol(board, self.side)
        #complete this – this will be your evaluation function. High should be good for max.
        
game = Konane(8)
game.playNGames(1, SimplePlayer(8), RandomPlayer(8), 1)