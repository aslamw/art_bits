# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:20:56 2021

@author: aslam
"""
import numpy

class ArtBit:#tratamento do desenho

    def __init__(self,linha=50,coluna=50): 
        self.matriz = numpy.zeros(shape=(linha,coluna))#cria a matriz
        self.linha = linha
        self.coluna = coluna
        self.espaco = ''
        self.esqueleto = ''
            
    def uni(self,linha,coluna,estado=1):
            
        self.matriz[linha][coluna] = estado
            
    def lin(self,ponto_f:str ,linha:int, coluna:int, estado:int =1):
        """
            lin(teste)
        """
        #define a linha do meio-----------------------
        
        pontoN = ponto_f.split()
        pontoN[1]=int(pontoN[1])
        
        if pontoN[0] == 'L':#modelo por linha
            
            if pontoN[1] > linha:
                
                for i in range(linha,(pontoN[1]+1)):
                    
                    self.matriz[i][coluna] = estado
                
            else:
                for i in range(pontoN[1],(pontoL+1)):
                    self.matriz[i][coluna] = estado
        
        elif pontoN[0] == 'C':#modelo por coluna
            
            if pontoN[1] > coluna:
                
                for i in range(coluna,(pontoN[1]+1)):
                    self.matriz[linha][i] = estado
                               
            else:
                
                for i in range(pontoN[1],(coluna + 1)):
                    
                    self.matriz[linha][i] = estado

    def campo(self):
        #cria o espaço no campo-------------------------
        self.espaco = ''#limpesa de campo
        self.esqueleto = ''
        for i in range(self.linha):
            
            self.espaco += '\n'
            self.esqueleto += '\n' + f'{i} : '
            for o in range(self.coluna):
                if self.matriz[i][o] == 0:self.espaco += '  '        
                
                else: self.espaco += ' @'
                self.esqueleto += str(o) + ' |'
        print(self.espaco)

        
    def salvar(self):#para salvar---------------------------------------
        
        posicao = ''
        for i in range(self.linha):
            for o in range(self.coluna):
                if self.matriz[i][o] == 1:  posicao += f'{i}/{o},'
    
        nome = input('nome do arquivo: ')
        with open(f'{nome}.dll','w') as o: 
            o.write(f'{self.linha}.{self.coluna}-{posicao}')
            
    
    def open_date(self,file):
    
        with open(f'{file}', 'r') as data_file:         
            dados = data_file.read()
    
        #divisão dos dados
        dados = dados.split('-')
        dados1 = dados[0].split('.')


        	#base desenho
            
        self.coluna = int(dados1[1])
        self.linha = int(dados1[0])

        self.matriz = numpy.zeros(shape=(int(dados1[0]),int(dados1[1])))#cria a matriz
        
        dados2 = dados[1].split(',')
        
        for i in range(len(dados2)-1):
            parte = dados2[i].split('/')
            
            self.matriz[int(parte[0])][int(parte[1])] = 1
            
        
        
        
        
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

if __name__ == "__main__":
    pass
    """while True:
        #tamanho do campo
        #try:
        comando = input('deseja matriz já salvo ou nova_>')

        if comando == 'nova':
            matrizL = int(input('digite linhas da matriz --limite 50--: '))    
            matrizC = int(input('digite colunas da matriz --limite 20--: '))
        
            #ajuste de limite
            if matrizL > 50:matrizL = 50
            if matrizC > 20: matrizC = 20
            
            matriz = numpy.zeros(shape=(matrizL,matrizC))#cria a matriz
            matriz = matriz.astype(int)
            
            art = bit(matriz,matrizL,matrizC)
            art.campo()
            art.comandos()

    	elif comando == 'salvo':
            
            #tratamento dos dados salvos
            local = input('digite diretorio e o nome do arquivo desejado:>_ ')
            with open(f'{local}.dll') as o:
                
            	dados = o.read()
        
        	#divisão dos dados
        	dados = dados.split('-')
        	dados1 = dados[0].split('.')


        	#base desenho

        	matriz = numpy.zeros(shape=(int(dados1[0]),int(dados1[1])))#cria a matriz
        	matriz = matriz.astype(int)
        
        	dados2 = dados[1].split(',')
        	for i in range(len(dados2)-1):
            	    parte = dados2[i].split('/')
            
            	matriz[int(parte[0])][int(parte[1])] = 1
                
        
    	else: break 

    	art = bit(matriz,len(matriz),len(matriz[0]))
    	art.campo()
    	art.comandos()"""
