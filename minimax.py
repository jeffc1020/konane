from konane import *

class MinimaxPlayer(Konane, Player):
    def __init__(self, size, depthLimit): 
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        self.side = side
        self.name = "MinimaxPlayer"
    def getMove(self, board):
        
        moves = self.generateMoves(board, self.side)
        # nextboard??
        n = len(moves)
        if n == 0:
            return []
        else:
            for i in moves:
                return
    def getMoveHelper(self, board, depth):
        return
    
    def eval(self, board):
        self.countSymbol(board, self.side)
        # easy eval function: counting number of your spaces on the board. you want to keep your pieces,
        # much like checkers and chess.
        #complete this – this will be your evaluation function. High should be good for max.
        
game = Konane(8)
game.playNGames(1, SimplePlayer(8), RandomPlayer(8), 1)