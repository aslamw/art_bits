# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:20:56 2021

@author: Marcos W
"""
from array import array
from time import sleep
from os import system

class ArtBit:#tratamento do desenho

    def __init__(self,linha=50,coluna=50): 
        
        self.linha = linha
        self.coluna = coluna
        
        self.matriz = [array('i', [0] * self.coluna) for _ in range(self.linha)]
        
        self.espaco = ''
        self.esqueleto = ''
        self.historico = {}
            
    def uni(self,linha, coluna, estado=1, save_history=True):
            
        self.matriz[linha][coluna] = estado
        
        if save_history:
            self.historico[len(self.historico)] = [linha[:] for linha in self.matriz]#saveframe
            
    def lin(self,ponto_f ,linha, coluna, estado=1, save_history=True):
       
        #define a linha do meio-----------------------
        
        pontoN = ponto_f.split()
        pontoN[1]=int(pontoN[1])
        
        if pontoN[0] == 'L':#modelo por linha
            
            if pontoN[1] > linha:
                
                for i in range(linha,(pontoN[1]+1)):
                    
                    self.matriz[i][coluna] = estado
                
            else:
            
                for i in range(pontoN[1],(pontoN+1)):
                    self.matriz[i][coluna] = estado
           
        
        elif pontoN[0] == 'C':#modelo por coluna
            
            if pontoN[1] > coluna:
                
                for i in range(coluna,(pontoN[1]+1)):
                    self.matriz[linha][i] = estado
                               
            else:
                
                for i in range(pontoN[1],(coluna + 1)):
                    
                    self.matriz[linha][i] = estado
        
        if save_history:
            self.historico[len(self.historico)] = [linha[:] for linha in self.matriz]#saveframe

    def campo(self,dot='@'):
        #cria o espaço no campo-------------------------
        self.espaco = ''#limpesa de campo
        self.esqueleto = ''
        for i in range(self.linha):
            
            self.espaco += '\n'
            self.esqueleto += '\n' + f'{i} : '
            for o in range(self.coluna):
                if self.matriz[i][o] == 0:self.espaco += '  '        
                
                else: self.espaco += f' {dot}'
                self.esqueleto += str(o) + ' |'
        print(self.espaco)
        
    def ver(self, matriz=False, dot='@'):
        #cria o espaço no campo-------------------------
        espaco = ''#limpesa de campo
        if not matriz: 
            matriz = self.matriz
        for i in range(len(matriz)):
            
            espaco += '\n'
            for o in range(len(matriz[i])):
                if matriz[i][o] == 0:espaco += '  '        
                
                else: espaco += f' {dot}'
        print(espaco)

        
    def salvar(self,file):#para salvar---------------------------------------
        
        posicao = ''
        for i in range(self.linha):
            for o in range(self.coluna):
                if self.matriz[i][o] == 1:  posicao += f'{i}/{o},'
    
        with open(f'{file}.dll','w') as o:
            o.write(f'{50,50}\n{posicao}')
            
    
    def open_date(self,file, save_history=True):
    
        with open(f'{file}.dll', 'r') as data_file:         
            dados = data_file.read()
    
        #divisão dos dados
        dados = dados.split('\n')
        matriz = dados[0].split(',')
        
        
        #dados = dados[1].split('.')


        	#base desenho
            
        self.coluna = int(matriz[0])
        self.linha = int(matriz[1])

        self.matriz = [array('i', [0] * int(matriz[0])) for _ in range(int(matriz[1]))]
        
        dados = dados[1].split(',')
        
        for i in range(len(dados)-1):
            parte = dados[i].split('/')
            
            self.matriz[int(parte[0])][int(parte[1])] = 1
        
        self.historico = {}#reseta o historico
        
        if save_history: 
            self.historico[len(self.historico)] = [linha[:] for linha in self.matriz]#saveframe
        
    def open_by_frame(self,file, save_history=True):
    
        with open(f'{file}.dll', 'r') as data_file:         
            dados = data_file.read()
    
        #divisão dos dados
        dados = dados.split('\n')
        matriz = dados[0].split(',')
        
        
        #dados = dados[1].split('.')


        	#base desenho
            
        self.coluna = int(matriz[0])
        self.linha = int(matriz[1])

        self.matriz = [array('i', [0] * int(matriz[0])) for _ in range(int(matriz[1]))]
        
        
        
        for i in range(1,len(dados)):
            dados2 = dados[i].split(',')
            #print(dados2)
            
            matriz_campo = [array('i', [0] * self.coluna) for _ in range(self.linha)]
            
            for item in dados2:
                parte = item.split('/')
                print(parte)
                if '' not in parte:
                    
                    print(parte)
                    matriz_campo[int(parte[0])][int(parte[1])] = 1

            if save_history:
                self.historico[len(self.historico)] = [linha[:] for linha in matriz_campo]#saveframe
                
        self.matriz= [linha[:] for linha in self.historico[len(self.historico)-1]]
        
        
    def add_image(self, file, save_history=True):
    
        with open(f'{file}', 'r') as data_file:         
            dados = data_file.read()
    
        #divisão dos dados
        dados = dados.split('\n')

        	#base desenho
        
        dados = dados[len(dados)-1].split(',')
        
        for i in range(len(dados)-1):
            parte = dados[i].split('/')
            
            self.matriz[int(parte[0])][int(parte[1])] = 1
          
        if save_history:
            self.historico[len(self.historico)] = [linha[:] for linha in self.matriz]#saveframe
    
    def add_history(self):
    
        self.historico[len(self.historico)] = [linha[:] for linha in self.matriz]#saveframe
        
        
    def save_frame(self,file):
    
        
        with open(f'{file}.dll','w') as o:
            o.write(f'{self.linha},{self.coluna}')
    
        posicao = ''
        
        for index in range(len(self.historico)):
            for linha in range(self.linha):
                for coluna in range(self.coluna):
                    if self.historico[index][linha][coluna] == 1:  posicao += f'{linha}/{coluna},'
                    
    
            with open(f'{file}.dll','a') as o:
                o.write('\n' + posicao)
            posicao = ''#limpar posição
        
    def move(self, linha_inicial, linha_final, coluna_inicial, coluna_final, direcao, distancia, dot=1):
        print('ok')
        index = 0
        while index < distancia:
            for linha in range(linha_inicial,linha_final+1):
                for coluna in range(coluna_inicial,coluna_final+1):
                    
                    if self.matriz[linha][coluna] == dot:
                        print('start match')
                        match direcao:
                            case 'U':
                                self.matriz[linha][coluna] = 0
                                print('adjusted move')
                                if linha != 0:
                                    print('move')
                                    self.matriz[linha-1][coluna] = dot
                            case 'R':
                                self.matriz[linha][coluna] = 0
                                print('adjusted move')
                                if linha != 0:
                                    print('move')
                                    self.matriz[linha][coluna+1] = dot
                            case 'L':
                                self.matriz[linha][coluna] = 0
                                print('adjusted move')
                                if linha != 0:
                                    print('move')
                                    self.matriz[linha][coluna-1] = dot
                            case 'D':
                                self.matriz[linha][coluna] = 0
                                print('adjusted move')
                                if linha != 0:
                                    print('move')
                                    self.matriz[linha+1][coluna] = dot
            index += 1
                            
                        
                            
        
    def movie(self):
    
        for index in range(len(self.historico)):
               
            system('cls')
            self.ver(self.historico[index])
            sleep(0.1)
             
        
    def open_frame(self, frame):
        
        keys_frames = list(self.historico.keys())
        
        if frame in keys_frames:
            self.matriz = self.historico[frame]
        else: raise ValueError('frame não existe')
        
    def see_frame(self, frame="all"):
    
        if frame == 'all':
            for index in range(len(self.historico)):
                
                print(f'frame {index}')
                self.ver(self.historico[index])
        else: 
              
            print(f'frame {frame}')
            self.ver(self.historico[frame])
            
   
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
    desenho = ArtBit(10,10)
    
    while True:
    
        comando = input('digite o comando desejado _> ')
        
        match comando:
            
            case 'open':
                desenho.open_by_frame('exemplo1')
        
            case 'uni':
                linha = int(input('digite a linha: '))
                coluna = int(input('digite a coluna: '))
                estado = int(input('digite a digite 1 ou mais para desenhar 0 para apagar: '))
                
                desenho.uni(linha,coluna,estado)
             
            case 'linha':
                linha = int(input('digite a linha: '))
                coluna = int(input('digite a coluna: '))
                final = input('digite a posição final da linha ou coluna EX.: "C 11": ')
                estado = int(input('digite a digite 1 ou mais para desenhar 0 para apagar: '))
               
            case 'salvar':
            
                desenho.save_frame('teste')
                
            case 'ver frame':
            
                desenho.see_frame()
            case 'ver':
                desenho.ver()
                
            case 'abrir frame':
            
                desenho.open_by_frame('exemplo1')
                
            case 'his':
                
                print(desenho.historico)
              
            case 'filme':
            
                desenho.movie()
            
            case 'move':
                desenho.move(0,5,0,5,'D',2)