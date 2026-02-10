### Descripcion
Our flag printing service has started glitching!
Additional details will be available after launching your challenge instance.

### Solucion

lo que se hace es de nuevo poner el lonk que de da el problema, una vez puesto eso, te da la bandera en formato hex, por lo tanto entramos a python3, para que pueda decifrar la bandera
```
negrity@serverjayyd:~$  nc saturn.picoctf.net 62094 
'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
^C
negrity@serverjayyd:~$ python3
Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'
'picoCTF{gl17ch_m3_n07_a4392d2e}'
>>> 

``