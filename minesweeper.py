#!/bin/python3

class Board(object):
    
    #This is the initializer for the Board class
    def __init__(self, row, column, game_over)
        self.row = row
	self.column = column
	self.game_over = game_over
	
    #Creates and returns a 2d list
    def get_2d_list(row, column):
        list = [[Tile(False) for _ in range(width)] for _ in range(height)]
        return list

    def display():

    def click(row, column):

    def win():

class Tile(object):

    #This is the initializer for the Tile class
    def __init__(self, is_bomb):
        self.is_bomb = is_bomb

def main():
    nl = get_2d_list(3,3)
    for i in range(len(nl)):
        for j in range(len(nl)):
            print(nl[i][j].is_bomb)

main():
    board = Board(rows=10, columns=15)
    while not board.game_over:
	board.display()
	column = int(input('Enter column:'))
	row = int(input('Enter row:'))
	board.click(row, column)
    board.display()
    if board.win():
	print('You win!')
    else:
	print('You lose.')
