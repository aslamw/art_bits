# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:20:56 2021

@author: aslam
"""
import numpy

class bit(object):
    def __init__(self,matrix): 
        self.matrix = matrix
        self.espaco = ''
        
    def campo(self):#cria o espaço no campo
        for i in range(0,len(self.matrix)):
            
            self.espaco += '\n'
            for o in range(0,len(self.matrix[i])):
                if self.matrix[i][o] == 0:self.espaco += ' '        
            
                else: self.espaco += ' @'
                
        print(self.espaco)
        
while True:
    #tamanho do campo
    matrizL = int(input('digite linhas --limite 50--: '))
    matrizC = int(input('digite colunas --limite 20--: '))
    
    #ajuste de limite
    if matrizL > 50:matrizL = 50
    if matrizC > 20: matrizC = 20
    
    matrix = numpy.ones(shape=(matrizL,matrizC))#cria a matrix
    matrix = matrix.astype(int)
    
    art = bit(matrix).campo()