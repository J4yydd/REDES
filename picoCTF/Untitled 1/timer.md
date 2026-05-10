### descriocion

## timer

Reverse EngineeringMedium100 pts8,763 solves

by Loic Shema

You will find the flag after analysing this apk

Download [here](https://artifacts.picoctf.net/c/449/timer.apk).
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}

### solucion 
solo lo que se hace es descomprimir el archivoAPK para poder ver todo lo que contenia internamente. Luego se buscaron cadenas de texto dentro de los archivos `.dex`, que son donde esta el codigo compilado de la app Android. Al encontrar coincidencias con `picoCTF`, se pudo localizar la flag dentro del archivo `classes3.dex`.
