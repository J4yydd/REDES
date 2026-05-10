### descripcion
## Sleuthkit Apprentice

ForensicsMedium200 pts19,533 solves

by LT 'syreal' Jones

Download this disk image and find the flag.

Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/136/disk.flag.img.gz)


### solucion 
primeramente se descomprime el archivo

```
jayyd@MacBook-Pro-de-Victor lskdj % fls -r -o 360448 disk.flag.img | grep -i flag

++ r/r * 2082(realloc): flag.txt

++ r/r 2371: flag.uni.txt

jayyd@MacBook-Pro-de-Victor lskdj % icat -o 360448 disk.flag.img 2371

picoCTF{by73_5urf3r_3497ae6b}

jayyd@MacBook-Pro-de-Victor lskdj %
```