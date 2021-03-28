#02.a) Use uma imagem em escala de cinza e faça um código para a correção gama desta imagem para os valores de gama 0.25, 0.5, 1, 2, 3. 
from PIL import Image

img = Image.open('imagens/escalacinza.jpg')

matrix = img.load()
gammacinza = 1/2 #(0,5)
gammacinza = 2/8 #(0,25)
gammacinza = 1
gammacinza = 2
gammacinza = 3

for i in range(img.size[0]):
    for j in range(img.size[1]):
      r = int((matrix[i, j][0]/255) ** gammacinza * 255)
      g = int((matrix[i, j][1]/255) ** gammacinza * 255)
      b = int((matrix[i, j][2]/255) ** gammacinza * 255)
      matrix[i, j] = (r, g, b)

      

img.save('imagens/gammacinza3pt0escalacinza.jpg')