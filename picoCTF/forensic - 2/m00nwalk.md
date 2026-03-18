### Solucion 

En este caso cuando descargamos el mensaje de la luna obtenemos un archivo `.wav`, esto nos quiere decir que es un archivo de audio. Por lo tanto tenemos que encontrar la bandera aquí. Lo que hago es analizar el espectrograma del audio, en busca de técnicas de esteganografía, usando la aplicación de audacity. Pero desafortunadamente no encontré nada escondido en el espectro. Ahora usando una herramienta para decodificar señales sstv, que son las que se usan para mandar mensajes a la tierra, entonces, hago uso de esta herramienta.

Después de la instalación, hago uso del siguiente comando:
```
```
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [##############################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
```
```

ya depues solo se abre la imagen y aparece como tal la bandera.
