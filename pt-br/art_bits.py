# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:20:56 2021

@author: aslam
"""
import numpy,os

class bit(object):#tratamento do desenho
    def __init__(self,matriz,linha,coluna): 
        self.matriz = matriz
        self.linha = linha
        self.coluna = coluna
        self.desenho_Uni = []
        self.desenho_Lin = []
        self.espaco = ''
        self.esqueleto = ''
        self.key = {'manual':'print(self.__str__())',
                    'lin':'self.lin()','matriz':'print(self.matriz)',
                    'linha':'print(self.linha)','coluna':'print(self.coluna)',
                    'H':'print(self.espaco)','uni':'self.uni()',
                    'clear':'self.limpo()','esqueleto':'print(self.esqueleto)',
                    'visual':'print(self.espaco)','uni -r':'self.uni(0)',
                    'salvar':'self.salvar()'
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
                
                self.matriz[linha][coluna] = n

                #salva os comandos
                self.desenho_Uni.append(f'U{str(linha)}.{str(coluna)}_')
                
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

            #salvar comandos -----------------------
            self.desenho_Lin.append(f'{pontoN}.{str(pontoL)}.{str(pontoC)}_')
            
            pontoN = pontoN.split()
            pontoN[1]=int(pontoN[1])
            
            if pontoN[0] == 'L':#modelo por linha
                if pontoN[1] > pontoL:
                    for i in range(pontoL,(pontoN[1]+1)): self.matriz[i][pontoC] = n
                    
                else:
                    for i in range(pontoN[1],(pontoL+1)): self.matriz[i][pontoC] = n
            
            elif pontoN[0] == 'C':#modelo por coluna
                if pontoN[1] > pontoC:
                    for i in range(pontoC,(pontoN[1]+1)): self.matriz[pontoL][i] = n
                                   
                else:
                    for i in range(pontoN[1],(pontoC + 1)): self.matriz[pontoL][i] = n
            self.campo()

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
    def salvar(self):#para salvar---------------------------------------
            with open('teste.dll','w') as o: 
                o.write(f'@{self.linha}.{self.coluna}-{Lin}-{Uni}')      
      
while True:
    #tamanho do campo
    #try:
    comando = input('deseja matriz já salva ou nova')

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
        with open(f'{comando}.dll') as o:
            dados = o.read()
            
        dados = dados.split('@')
        dados = dados.split('_')

        #base matriz
        matrizU = dados.split('-')
        matriz = matrizU[0].split('.')

        #base desenho

        matriz = numpy.zeros(shape=(matriz[0],matriz[1]))#cria a matriz
        matriz = matriz.astype(int)

        #organifar os dados
        for i in range(len(matrizU):
            #desenho Uni-----------------------------------
            if 'U' in matrizU[i]:
                numero = matrizU[i].replace('U','')
                numero = numero.split(',')

                #desenho
                matriz[int(numero[0])][int(numero[1])] = 1

            #desenho Lin-----------------------------------    
            elif 'L' or 'C' in matrizU[i]:
                base = matrizU[i].split('.')
                pontN = base[0]
                pontoL = int(base[1])
                pontoC = int(base[2])


                if pontoN[0] == 'L':#modelo por linha
                    if int(pontoN[2]) > pontoL:
                        for i in range(pontoL,(int(pontoN[2])+1)): matriz[i][pontoC] = 1
                        
                    else:
                        for i in range(int(pontoN[2]),(pontoL+1)): matriz[i][pontoC] = 1
                
                elif pontoN[0] == 'C':#modelo por coluna
                    if int(pontoN[2]) > pontoC:
                        for i in range(pontoC,(int(pontoN[2])+1)): matriz[pontoL][i] = 1
                                       
                    else:
                        for i in range(int(pontoN[2]),(pontoC+1)): matriz[pontoL][i] = 1

    else:break

    art = bit(matriz,matriz[0],matriz[1])
    art.campo()
    art.comandos()

    else: print('comando invalido')       
    #except:
        #break