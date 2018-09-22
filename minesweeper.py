#!/bin/python3

#Creates and returns a 2d list
def get_2d_list(width, height):
    list = [[Tile(False) for _ in range(width)] for _ in range(height)]
    return list

class Tile(object):

    #This is the initializer for the Tile class
    def __init__(self, is_bomb):
        self.is_bomb = is_bomb

def main():
    nl = get_2d_list(3,3)
    for i in range(len(nl)):
        for j in range(len(nl)):
            print(nl[i][j].is_bomb)

main()




