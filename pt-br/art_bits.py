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
        self.esqueleto = ''
        self.key = {'manual':'print(self.__str__())',
                    'lin':'self.lin()','matriz':'print(self.matrix)',
                    'linha':'print(self.linha)','coluna':'print(self.coluna)',
                    'H':'print(self.espaco)','uni':'self.uni()',
                    'clear':'self.limpo()','esqueleto':'print(self.esqueleto)',
                    'visual':'print(self.espaco)','uni -r':'self.uni(0)'
                    }#comandos
        
    def comandos(self):
        #fazer os desenhos--------------------------------
        print('modele o futuro')
        
        while 1:
            escolha = input('_> ')#terminal 
            
            if escolha in self.key: eval(f'{self.key[escolha]}')#tratamento de comandos
            
            elif escolha == 'x': break#fim do loop
            
            else:print('esse camando não é valido')
            
    def uni(self,n=1):
        try:
            while 1:
                linha = int(input('Linha_> '))
                coluna = int(input('Coluna_> '))
                
                self.matrix[linha][coluna] = n
                
                self.campo()
        except:
            self.comandos()
            
    def lin(self,n=1):
        #define a linha do meio-----------------------
        while 1:
            pontoN = input('digite a linha L ou coluna C __-EX.: L 3--> ')
            if pontoN == 'x':break
            
            pontoL = int(input('digite -linha-> '))
            pontoC = int(input('digite -coluna-> '))
            
            pontoN = pontoN.split()
            pontoN[1]=int(pontoN[1])
            
            if pontoN[0] == 'L':#modelo por linha
                if pontoN[1] > pontoL:
                    for i in range(pontoL,pontoN[1]): self.matrix[i][pontoC] = n
                    
                else:
                    for i in range(pontoN[1],pontoL): self.matrix[i][pontoC] = n
            
            elif pontoN[0] == 'C':#modelo por coluna
                if pontoN[1] > pontoC:
                    for i in range(pontoC,pontoN[1]): self.matrix[pontoL][i] = n
                                   
                else:
                    for i in range(pontoN[1],pontoC): self.matrix[pontoL][i] = n
            self.campo()

    def campo(self):
        #cria o espaço no campo-------------------------
        self.espaco = ''#limpesa de campo
        self.esqueleto = ''
        for i in range(self.linha):
            
            self.espaco += '\n'
            self.esqueleto += '\n' + f'{i} : '
            for o in range(self.coluna):
                if self.matrix[i][o] == 0:self.espaco += '  '        
                
                else: self.espaco += ' @'
                self.esqueleto += str(o) + ' |'

    def __str__(self):#manual---------------------------------
        return f'''
                                ---------Comandos-------------
                                
                  x    __________sair
                  uni  _____________desenho por unidade
                  lin  _____________desenho por linha ou coluna
                  visual____________visualizar imagem
                  matriz____________apresenta a matriz
                  linha_____________mostra a quantidade de linhas na matriz
                  coluna____________mostra a quantidade de coluna na matriz
                  H    _____________mostra o desenho sem 
                  -r   ____________para remover, use <*uni -r *> ou <* lin -r*>
    
                  
                  
                               ---------modelo da matriz----------
                               
                  {self.esqueleto}
                  
                  Oque está a esquerda de * : * é contado como linha e
                  tudo a direita é coluna.
            ''' 
    def limpo(self):
        return os.system('cls')          
      
while True:
    #tamanho do campo
    try:
        matrizL = int(input('digite linhas da matriz --limite 50--: '))    
        matrizC = int(input('digite colunas da matriz --limite 20--: '))
    
        #ajuste de limite
        if matrizL > 50:matrizL = 50
        if matrizC > 20: matrizC = 20
        
        matrix = numpy.zeros(shape=(matrizL,matrizC))#cria a matrix
        matrix = matrix.astype(int)
        
        art = bit(matrix,matrizL,matrizC)
        art.campo()
        art.comandos()
    except:
        break