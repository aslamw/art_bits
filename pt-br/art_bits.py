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
        self.key = {'manual':'print(self.__str__())',
                    'lin':'self.lin()','matrix':'print(self.matrix)',
                    'linha':'print(self.linha)','coluna':'print(self.coluna)',
                    'espaço':'print(self.espaco)','uni':'self.uni()',
                    'clear':'self.limpo()'
                    }#comandos
        
    def comandos(self):
        #fazer os desenhos--------------------------------
        print('modele o futuro')
        
        while 1:
            escolha = input('_> ')#terminal 
            if escolha in self.key: eval(f'{self.key[escolha]}')#tratamento de comandos
            
            elif escolha == 'x': break#fim do loop
            
            elif escolha == 'visual': print(self.campo())
            
            else:print('esse camando não é valido')
            
    def uni(self):
        try:
            while 1:
                linha = int(input('L_> '))
                coluna = int(input('C_> '))
                self.campo()
                
                self.matrix[linha][coluna] = 0 
        except:
            self.comandos()
            
    def lin(self):
        #define a linha do meio-----------------------
        while 1:
            pontoN = input('digite a linha ou coluna limite -EX.: L 3--')
            if pontoN == 'x':break
            
            pontoL = int(input('digite -linha-'))
            pontoC = int(input('digite -coluna-'))
            pontoN = pontoN.split()
            pontoN[1]=int(pontoN[1])
            
            if pontoN[0] == 'L':
                if pontoN[1] > pontoL:
                    for i in range(pontoL,pontoN[1]): self.matrix[i][pontoC] = 0
                                   
                else:
                    for i in range(pontoN[1],pontoL): self.matrix[i][pontoC] = 0        
            
            elif pontoN[0] == 'C':
                if pontoN[1] > pontoC:
                    for i in range(pontoC,pontoN[1]): self.matrix[pontoL][i] = 0
                                   
                else:
                    for i in range(pontoN[1],pontoC): self.matrix[pontoL][i] = 0

    def campo(self):
        #cria o espaço no campo-------------------------
        self.espaco = ''#limpesa de campo
        for i in range(self.linha):
            
            self.espaco += '\n'
            for o in range(self.coluna):
                if self.matrix[i][o] == 0:self.espaco += '  '        
            
                else: self.espaco += ' @'
        print(self.espaco)#apresentação

    def __str__(self):#manual---------------------------------
        return 'foobarr é bom'
    def limpo(self):
        return os.system('cls')
        
        
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
    
    art = bit(matrix,matrizL,matrizC)
    art.campo()
    art.comandos()