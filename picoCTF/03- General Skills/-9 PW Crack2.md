### Descripcion 
¿Puedes descifrar la contraseña para obtener la bandera?Descargue el verificador de contraseñas [aquí](https://artifacts.picoctf.net/c/13/level2.py) y también necesitará la [bandera](https://artifacts.picoctf.net/c/13/level2.flag.txt.enc) cifrada en el mismo directorio.


```
jayyd@MacBook-Pro-de-Victor xs % nano level2.py

jayyd@MacBook-Pro-de-Victor xs % python3 level2.py

Please enter correct password for flag: de76

Welcome back... your flag, user:

picoCTF{tr45h_51ng1ng_489dea9a}

jayyd@MacBook-Pro-de-Victor xs %



Notas. = al momento de usar nano en el archivo, aparece el usuario en base hexadecimal, por lo tanto sollamente se convierte a lenguaje normal, y al correr el programa, se pone el user decifrado.