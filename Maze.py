#lets start
import os
import math
from simpleai.search import astar, SearchProblem
class MazeSolver(SearchProblem):
    def __init__(self, src_board):
        #loading the maze board in memory
        if not os.path.exists(src_board):
            raise Exception(src_board + ' doesnt exist!')

        #board (adj matrix)
        self.board = []

        #open the file (source for board)
        f_handle = open(src_board, 'r')
        for x in f_handle:
            x = x.strip() #remove the leading/trailing spaces and newline
            self.board.append([y for y in x])
        f_handle.close()

        #Recording the positions of turtle and the egg
        self.initial_pos = None
        self.goal_pos = None

        for i in range (len(self.board)):
            for j in range (len(self.board[i])):
                if self.board[i][j] == 'x': #turtle
                    self.initial_pos = (i,j)
                if self.board[i][j] == 'o':  # egg
                    self.goal_pos = (i,j)

        if self.initial_pos is None:
            raise Exception('Turtle not found')

        if self.goal_pos is None:
            raise Exception('Egg not found')

        #Define the costs
        regular_cost = 1
        diagonal_cost = 1.7

        self.COSTS = {
            "UP": regular_cost,
            "DOWN" : regular_cost,
            "LEFT" : regular_cost,
            "RIGHT" : regular_cost,
            "UP LEFT" : diagonal_cost,
            "UP RIGHT": diagonal_cost,
            "DOWN LEFT": diagonal_cost,
            "DOWN RIGHT" : diagonal_cost
        }

        #initial the super class sub object
        SearchProblem.__init__(self,initial_state = self.initial_pos)
