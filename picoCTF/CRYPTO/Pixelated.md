### descripcion
Tengo estas dos imágenes, ¿puedes hacer una bandera con ellas?[scrambled1.png](https://challenge-files.picoctf.net/c_wily_courier/fd911d04c960ddc4effdf884e8cc954b91e1936eb4c1bdee81a39f7b16a5e465/scrambled1.png) [scrambled2.png](https://challenge-files.picoctf.net/c_wily_courier/fd911d04c960ddc4effdf884e8cc954b91e1936eb4c1bdee81a39f7b16a5e465/scrambled2.png)


### solucion 
from PIL import Image

img1 = Image.open("scrambled1.png")
img2 = Image.open("scrambled2.png")

resultado = Image.new("RGB", img1.size)

for x in range(img1.width):
    for y in range(img1.height):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))

        nuevo_pixel = tuple(pixel1[i] ^ pixel2[i] for i in range(3))
        resultado.putpixel((x, y), nuevo_pixel)

resultado.save("flag.png")

simplemente se usa el piloow en python, para que se pueda decifrar a partir de lo que se descarga en png.
