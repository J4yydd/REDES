### Descripcion
Description
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to fickle-tempest.picoctf.net 58255.
### Solucion
SOlo se accede al servidor del puerto  que te otorga el problema, de ahi no solo se pone el link, debes de hacer un grep para que no te lance tanto dato, una vez eso te da la bandera 


```
negrity@serverjayyd:~$ nc fickle-tempest.picoctf.net 58255 | grep picoCTF
picoCTF{digital_plumb3r_d3246b6B}

```