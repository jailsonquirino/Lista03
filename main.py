#1) O que significa o negativo de uma imagem? Responda como comentário no início do seu código.
   # R: É as colres ao contrario da outra onde ouver preto fica branco, e o branco fica preto.  


#02) O que significa a correção gama de uma imagem? Responda como comentário no início do seu código. 
# R: Correção gamma altere as cores da imagens atraves dos pixel

from PIL import Image
#01.b) Faça um código para gerar o negativo de uma imagem em escala de cinza.
#1.a) Faça um código para gerar o negativo de uma imagem colorida. 
img = Image.open('imagens/goku.jpg')
print(img.size)
matrix = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
     r = 255 - matrix[i, j][0]
     g = 255 - matrix[i, j][1]
     b = 255 - matrix[i, j][2]
     matrix[i, j] = (r, g, b)
img.save('imagens/novogoku.jpg')         