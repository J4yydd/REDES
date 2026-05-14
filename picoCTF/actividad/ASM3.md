### descripcion
¿Qué devuelve asm3(0xb58568e8,0xc63ab2a1,0xf9d33ef4)? Envíe la bandera como un valor hexadecimal (que comience con '0x'). NOTA: Su respuesta a esta pregunta NO estará en el formato de bandera habitual. [Fuente](https://challenge-files.picoctf.net/c_fickle_tempest/b3fee52f11c2963c3f6008623c66d7c0906ab439f927132ac7fbc1d53f83c4ee/test.S)


### solucion 
```
#include <stdio.h>
#include <stdint.h>

// Definición de la función usando ensamblador en línea de 32 bits
uint32_t asm3(uint32_t arg1, uint32_t arg2, uint32_t arg3) {
    uint32_t result;
    __asm__ (
        "push %%ebp;"
        "mov %%esp, %%ebp;"
        "xor %%eax, %%eax;"
        "mov 0xb(%%ebp), %%ah;"
        "shl $0x10, %%ax;"
        "sub 0xd(%%ebp), %%al;"
        "add 0xc(%%ebp), %%ah;"
        "xor 0x10(%%ebp), %%ax;"
        "mov %%eax, %0;"      // Guarda el resultado final de eax
        "pop %%ebp;"
        : "=r" (result)       // Salida
        : "r" (arg1), "r" (arg2), "r" (arg3) // Entradas para armar la pila
        : "eax"               // Registro modificado
    );
    return result;
}

int main() {
    // Parámetros del desafío de picoCTF
    uint32_t res = asm3(0xb58568e8, 0xc63ab2a1, 0xf9d33ef4);
    // Mascarilla de 16 bits porque el retorno real se corta en 'ax'
    printf("Flag: 0x%x\n", res & 0xFFFF); 
    return 0;
}

```