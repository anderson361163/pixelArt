'''
Created 03rd June

by: @Isinha in Ubuntu 18.04.4 LTS
'''

'''
Importando a biblioteca Pillow para suporte de imagens.

conda install pillow
--> caso não esteja instalada

[[ 255, 255, 255 ],
 [   0, 255, 255 ]] #as imagens se comportam como matrizes
'''

from PIL import Image #importando a imagem da biblioteca pillow

SIMBOLOS = " .,:;+!ox?*%#@" #símbolos que formarão a imagem
# SIMBOLOS = "░▒▓█" 

def redimensiona(imagem, nova_largura): #função para redimensionar a imagem e não fique muito grande
    largura, altura = imagem.size
    proporcao = altura/largura
    nova_altura = int(proporcao*nova_largura)

    return imagem.resize((nova_largura, nova_altura))

def pixels2ascii(imagem):
    '''
    cores = 0 .. 255, 0 - preto, 255 - branco
    [0..255]
    [0..13]

    0/x = 0
    255/x = len(SIMBOLOS) - 1
    x = 255/(len(SIMBOLOS) - 1)

    '''
    razao = int( 255/(len(SIMBOLOS)-1) )
    largura = imagem.size[0]
    
    pixels = list(imagem.getdata())
    arte   = ""

    for i, pixel in enumerate(pixels):
        if i%largura==0:
            arte = arte + "\n"
        simbolo = int(pixel/razao)
        arte = arte + SIMBOLOS[simbolo]*2

    return arte

def converteASCII(imagem, largura):
    imagem = redimensiona(imagem, largura)
    return pixels2ascii(imagem)

imagem = Image.open("C:\\Users\\Anderson\\Desktop\\python\\eu.png").convert("L")

print(converteASCII(imagem, 200))
