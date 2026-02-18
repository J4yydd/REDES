
#### Descripción

¿Puedes descifrar la contraseña para obtener la bandera?Descargue el verificador de contraseñas [aquí](https://artifacts.picoctf.net/c/18/level3.py) y también necesitará la [bandera](https://artifacts.picoctf.net/c/18/level3.flag.txt.enc) cifrada y el [hash](https://artifacts.picoctf.net/c/18/level3.hash.bin) en el mismo directorio.Hay 7 contraseñas posibles, de las cuales una es correcta. Puedes encontrarlas examinando el script del verificador de contraseñas.
```
jayyd@MacBook-Pro-de-Victor xs % python3 levell.py

Please enter correct password for flag: 2295

Welcome back... your flag, user:

picoCTF{m45h_fl1ng1ng_6f98a49f}

jayyd@MacBook-Pro-de-Victor xs %
```
nota = se utuilizo el metodo de fuerza bruta, decifrando la contraaseña usando ptimero cat para analizar el codigo.
