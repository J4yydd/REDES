
### descripcion
En el último desafío, dominaste los números octales (base 8), decimales (base 10) y hexadecimales (base 16), ¡pero esta puerta de la bóveda utiliza un cambio de base diferente, así como una codificación URL distinta!El código fuente de esta bóveda se encuentra aquí: [VaultDoor5.java](https://challenge-files.picoctf.net/c_fickle_tempest/f2e90d844f6e64092bc1a611c16d52a832e0f2cb856991bc9fa205bcd0cd31bd/VaultDoor5.java)


### solucion 

Se toma la cadena esperada y se le aplica primero una decodificación base64 para obtener un texto en formato  de la url se decodifican interpretándolos como caracteres  en hexadecimal y así se reconstruye la contraseña del pico
