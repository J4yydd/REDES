### solucion 

solo se debe de descomprimr lo que tiene de cntenido y posterioemente tener los unmeros que te da el archivo para al final ponerlos en la instancia 
```
jayyd@MacBook-Pro-de-Victor lskdj % mmls disk.img         

DOS Partition Table

Offset Sector: 0

Units are in 512-byte sectors

  

      Slot      Start        End          Length       Description

000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)

001:  -------   0000000000   0000002047   0000002048   Unallocated

002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)

jayyd@MacBook-Pro-de-Victor lskdj % nc saturn.picoctf.net 49694

What is the size of the Linux partition in the given disk image?

Length in sectors: 202752

202752

Great work!

picoCTF{mm15_f7w!}

jayyd@MacBook-Pro-de-Victor lskdj %
```