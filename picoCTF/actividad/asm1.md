### descripcion 
¿Qué devuelve asm3(0xb58568e8,0xc63ab2a1,0xf9d33ef4)? Envíe la bandera como un valor hexadecimal (que comience con '0x'). NOTA: Su respuesta a esta pregunta NO estará en el formato de bandera habitual. [Fuente](https://challenge-files.picoctf.net/c_fickle_tempest/b3fee52f11c2963c3f6008623c66d7c0906ab439f927132ac7fbc1d53f83c4ee/test.S)


### solucion 
El argumento de entrada asignado a `[ebp+0x8]` es **`0x36e`**.

 `<+7>` **`cmp DWORD PTR [ebp+0x8],0x6c8`**: Compara `0x36e` con `0x6c8`.
 `<+14>` **`jg 0x11d6`**: Salta si es mayor. Como `0x36e` **no** es mayor que `0x6c8`, el programa **no salta** y continúa en la siguiente línea.
 `<+16>` **`cmp DWORD PTR [ebp+0x8],0x36e`**: Compara `0x36e` con `0x36e`.
 `<+23>` **`jne 0x11ce`**: Salta si NO son iguales. Como los valores **son exactamente iguales**, el programa **no salta** y avanza al siguiente bloque.
`<+25>` **`mov eax,DWORD PTR [ebp+0x8]`**: Copia el valor de entrada (`0x36e`) en el registro `eax`.
`<+28>` **`add eax,0x6`**: Suma de manera hexadecimal:

solo se inspecciona el archivo y se hace la operacion arala decodificacionen ensambling.





