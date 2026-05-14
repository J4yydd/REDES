### descripcion 

¿Qué devuelve asm3(0xb58568e8,0xc63ab2a1,0xf9d33ef4)? Envíe la bandera como un valor hexadecimal (que comience con '0x'). NOTA: Su respuesta a esta pregunta NO estará en el formato de bandera habitual. [Fuente](https://challenge-files.picoctf.net/c_fickle_tempest/b3fee52f11c2963c3f6008623c66d7c0906ab439f927132ac7fbc1d53f83c4ee/test.S)

### solucion 
python3 -c "var2 = 0x21; var1 = 0x6; \
while var1 <= 0x2d12: var2 += 0x1; var1 += 0x9f; \
print(hex(var2))"



solo ejecutas ese comando en python, para que te pueda dar la flag a base de lo que esta dentero del archivo ensambler.
