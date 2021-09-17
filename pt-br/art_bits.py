# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:20:56 2021

@author: aslam
"""
import numpy,os

class bit(object):#tratamento do desenho
    def __init__(self,matrix,linha,coluna): 
        self.matrix = matrix
        self.linha = linha
        self.coluna = coluna
        self.espaco = ''
        self.key = {'manual':'print(self.__str__())'}#comandos
        
    def desenho(self):
        #fazer os desenhos--------------------------------
        os.system('cls')
        os.system('color 2')
        print('modele o futuro')
        
        while 1:
            escolha = input('_> ')#terminal 
            if escolha in self.key: eval(f'{self.key[escolha]}')#tratamento de comandos
            
            elif escolha == 'x': break#fim do loop
            
            elif escolha == 'visual': print(self.espaco)
                
            elif escolha == 'lixo': os.system('cls')
            
            else:print('esse camando não é valido')
            
    def espelho(self):
        #define a linha do meio--------
        meio = input('digite a coluna que quer o espelhamento')
        if meio == 'n':
            
            if self.coluna % 2 == 0: meio = (self.coluna / 2)+1
            
            elif self.coluna % 2 == 1: meio = int(self.coluna / 2)+1
        #base de linhas
        try:
            pass
            
        except:
            print('você não digitou um número')
            
        
    def campo(self):
        #cria o espaço no campo-------------------------
        for i in range(0,len(self.matrix)):
            
            self.espaco += '\n'
            for o in range(0,len(self.matrix[i])):
                if self.matrix[i][o] == 0:self.espaco += ' '        
            
                else: self.espaco += ' @'        
        print(self.espaco)#apresentação
        self.desenho()
        
    def __str__(self):#manual 
        return 'foobarr é bom'
        
        
while True:
    #tamanho do campo
    matrizL = int(input('digite linhas --limite 50--: '))
    if matrizL == 00:break#-----fim-------------------
    
    matrizC = int(input('digite colunas --limite 20--: '))
    
    #ajuste de limite
    if matrizL > 50:matrizL = 50
    if matrizC > 20: matrizC = 20
    
    matrix = numpy.ones(shape=(matrizL,matrizC))#cria a matrix
    matrix = matrix.astype(int)
    
    art = bit(matrix,matrizL,matrizC).campo()