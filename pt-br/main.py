# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:20:56 2021

@author: Marcos W
"""
from array import array
from time import sleep
from os import system


class ArtBit:
    def __init__(self, line: int = 50, column: int = 50) -> None:
        self.line: int = line
        self.column: int = column

        self.space: str = ""
        self.skeleton: str = ""
        self.dot: str = "@"

        self.history: dict = {}

        self.matrix: array = [array("i", [0] * self.column) for _ in range(self.line)]

    def __add_history(self) -> None:
        self.history[len(self.history)] = [line[:] for line in self.matrix]

    def draw_bit(self) -> array:
        space: str = ""
        skeleton: str = ""

        for line in range(self.line):
            space += "\n"
            skeleton += "\n" + f"{line} : "

            for column in range(self.column):
                if self.matrix[line][column] == 0:
                    space += "  "

                else:
                    space += f" {self.dot}"

                skeleton += str(column) + " |"

        return space, skeleton

    def uni(
        self, 
        line: int, 
        column: int, 
        state: int = 1, 
        save_history: bool = True
    ):
        self.matrix[line][column] = state

        if save_history:
            self.__add_history()
            self.space, self.skeleton = self.draw_bit()

    def lin(
        self,
        end_point: str,
        line: int,
        column: int,
        state: int = 1,
        save_history: bool = True,
    ):
        
        date = end_point.split()
        type_point, value_point = date[0],int(date[1])
        

        if type_point in ["C", "L"]:  # Line model
            if type_point == "L":
                
                if value_point > line:
                    for indexLine in range(value_point, line + 1):
                        self.matrix[indexLine][column] = state
                        
                else: return "size error"
                    

            else:  # column model
                if value_point > column:
                    for indexColumn in range(column, (value_point + 1)):
                        self.matrix[line][indexColumn] = state

                else: return "size error"

        if save_history:
            self.__add_history()
            self.space, self.skeleton = self.draw_bit()

    def box_move(self, direction, distance, dot=1, save_history=True):
        
        def traverse(lineDirectionX, lineDirectiony, lineOrder, columnDirectionX, columnDirectionY,  columnOrder):
            
            positions = []
            
            for line in range(lineDirectionX, lineDirectiony, lineOrder, ):
                for column in range( columnDirectionX, columnDirectionY, columnOrder):
                    
                    if self.matrix[line][column] == dot :
                        
                        positions.append([line,column])
            return positions
      
        match direction:
            
            case 'R':
                
                positionSide = traverse(0, self.line, 1, self.column-1, 0, -1)
                print(positionSide)
                for line,column in positionSide:
                    if column+distance < self.column:
                        if self.matrix[line][column + distance] == 0:
                            dot = self.matrix[line][column]
                            self.matrix[line][column + distance] = dot
                            self.matrix[line][column] = 0
                            
            case 'D':
                
                positionSide = traverse(0, self.line-1, 1, self.column-1, 0, -1)
                print(positionSide)
                for line,column in positionSide:
                    if column+distance < self.column:
                        if self.matrix[line][column + distance] == 0:
                            dot = self.matrix[line][column]
                            self.matrix[line][column + distance] = dot
                            self.matrix[line][column] = 0
        
        if save_history:
            self.__add_history()
            self.space, self.skeleton = self.draw_bit()                        
                                
            

if __name__ == "__main__":
    art = ArtBit(10, 10)

    art.uni(5, 5)
    art.lin("C 9", 2, 0)
    draw, _= art.draw_bit()
    print(draw)
    
    art.box_move('R',2)
    draw, _= art.draw_bit()
    print(draw)
