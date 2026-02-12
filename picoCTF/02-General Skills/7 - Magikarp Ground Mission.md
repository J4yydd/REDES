#### Descripción

¿Sabes cómo navegar entre directorios y leer archivos en el shell? Inicia el contenedor, `ssh`accede a él y, `ls`una vez conectado, comienza.Inicie sesión a través `ssh`de como `ctf-player`con la contraseña, `8c606eb1`en el host `wily-courier.picoctf.net`y el puerto `61281`.



Primero nos conectamos al servidor que se nos pide 
```
jayyd@MacBook-Pro-de-Victor Ularradallaku % ssh ctf-player@wily-courier.picoctf.net -p 61281

  

ctf-player@pico-chall$ ls

1of3.flag.txt  instructions-to-2of3.txt

ctf-player@pico-chall$ pwd

/home/ctf-player/drop-in

ctf-player@pico-chall$ ls -la

total 8

drwxr-xr-x 1 ctf-player ctf-player 59 Sep 12 16:20 .

drwxr-xr-x 1 ctf-player ctf-player 20 Feb 12 04:54 ..

-rw-r--r-- 1 ctf-player ctf-player 14 Aug 14 18:35 1of3.flag.txt

-rw-r--r-- 1 ctf-player ctf-player 56 Aug 14 18:35 instructions-to-2of3.txt

ctf-player@pico-chall$ cat instructions-to-2of3.txt

Next, go to the root of all things, more succinctly `/`

ctf-player@pico-chall$ cd /

ctf-player@pico-chall$ pwd

/

ctf-player@pico-chall$ /

-bash: /: Is a directory

ctf-player@pico-chall$ cd /

ctf-player@pico-chall$ cat 2of3.flag.txt

0ut_0f_//4t3r_

ctf-player@pico-chall$ ls /home

ctf-player

ctf-player@pico-chall$ find / -name "3of3.flag.txt" 2>/dev/null

/home/ctf-player/3of3.flag.txt

ctf-player@pico-chall$ cat /home/ctf-player/3of3.flag.txt

0b24fc4f}ctf-player@pico-chall

Nota: 
Se exploró el sistema en la terminal usando comandos básicos de Linux para buscar archivos relacionados con la flag. Se descubrió que la flag estaba dividida en tres partes en distintos archivos (1of3, 2of3 y 3of3). Se utilizó el comando cat para leer cada archivo y obtener los fragmentos. Finalmente, se unieron las tres partes en el orden correcto para reconstruir la flag completa.

solo se fue explorando en la terminal en ser puesto que se otorga, usando solo los comandos de exploracion que se relacionan con la flag, entonces una vez visto que estaba dividida, solo se usa el comando cat para ver cada archivo y formar las piezas
