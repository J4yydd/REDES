### descripcion 
Qué tal si jugamos al escondite, jeje?Mira esta imagen [de aquí](https://artifacts.picoctf.net/c/236/atbash.jpg) .

---

### solucion 
from PIL import Image

img = Image.open("imagen.png")
bits = ""

for pixel in img.getdata():
    for valor in pixel[:3]:  # RGB
        bits += str(valor & 1)

# convertir bits a texto
texto = ""
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    texto += chr(int(byte, 2))

print(texto)


la forma en la que yo lo hice fue ir sacando la info a partir de los bits con este codigo, este problema ya lo habia solucionado hace tiempo en otra cuenta.
