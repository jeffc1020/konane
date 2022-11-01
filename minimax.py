from konane import *

class MinimaxPlayer(Konane, Player):
    def __init__(self, size, depthLimit): 
        Konane.__init__(self, size)
        self.limit = depthLimit
    def initialize(self, side):
        self.side = side
        self.name = "MinimaxPlayer"
    def getMove(self, board): # finds the optimal next move
        return self.getMoveHelper(board, 0)
        # moves = self.generateMoves(board, self.side)
        # # nextboard??
        # n = len(moves)
        # if n == 0:
        #     return []
        # else:
        #     for i in moves:
        #         return
    def getMoveHelper(self, board, depth):
        if (depth % 2 == 0): # if we are at an even depth 
            currentTurn = self.side # it's our turn (rather than the opponent's)
            maximizing = True
            # I may have this backwards
        else: # else, we are at an odd depth
            currentTurn = self.opponent # it's the opponent's turn
            maximizing = False
        # figure out if this is a min or max turn and figure out the optimal move in generateMoves
        moveList = []
        if depth == self.depthLimit: # base case: we are at a leaf node
            return eval(board) # return the heuristic (eval function) of this leaf node
        for move in self.generateMoves(board, currentTurn): # loops through each next move for the current node
            tempTuple = (move, self.getMoveHelper(self.nextBoard(board, currentTurn, move), depth + 1))
            moveList.append(tempTuple)
        # actually choose the next move
        if maximizing:
            # choose the move with the max associated value
            max(moveList[0[1]]) # needs fixin
        else:
            # choose the move with the min associated value
            min(moveList[0[1]]) # needs fixin
    
    def eval(self, board):
        self.countSymbol(board, self.side) # should be good for now
game = Konane(8)
game.playNGames(1, SimplePlayer(8), RandomPlayer(8), 1)