Hemos detectado que este extraño mensaje circula por los servidores y creemos que tenemos un método de descifrado que funciona.Descarga el mensaje [aquí](https://artifacts.picoctf.net/c/129/message.txt) .Toma cada número módulo 37 y asígnalo al siguiente conjunto de caracteres: del 0 al 25 es el alfabeto (mayúsculas), del 26 al 35 son los dígitos decimales y el 36 es un guion bajo.Envuelva su mensaje descifrado en el formato de bandera picoCTF (es decir, `picoCTF{decrypted_message}`)


### solucion 
nuevo_valor = numero % 37
se hace en si con el indice del alfabeto con cada valor, igual se hace en py

