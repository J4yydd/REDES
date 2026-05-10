

### solucion 
Se realizó ingeniería inversa básica sobre el archivo  Primero se identificó el tipo de archivo y después se usó `strings` para extraer las cadenas de texto almacenadas dentro del binario. Luego se filtró la salida buscando el formato típico de las flags, encontrando así la clave directamente sin ejecutar el programa y solo se usaba el ggrep para la bandera. 


