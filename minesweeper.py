#!/bin/python3

#Here is where you'll define the Tile objects Madison
class Tile(object):

    #This is the initializer for the Tile class
    def __init__(self, is_bomb):
        self.is_bomb = is_bomb

#Creates and returns a 2d list
def get_2d_list(width, height):
    list = []
    for i in range(width):
        for j in range(height):	   
            list.append(Tile(True))
    return list

def main():
    nl = get_2d_list(3,3)
    for i in range(len(nl)):
        print(nl[i].is_bomb)

main()




