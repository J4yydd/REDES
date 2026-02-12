#### Descripción

Para obtener el verdadero 1337, debes comprender diferentes codificaciones de datos, como hexadecimal o binaria. ¿Puedes obtener la bandera de este programa para demostrar que estás en camino de convertirte en 1337?Conéctese con nc fickle-tempest.picoctf.net 64741 .
### Solucion 
```
jayyd@MacBook-Pro-de-Victor ~ % nc fickle-tempest.picoctf.net 64741

Let us see how data is stored

computer

Please give the 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 as a word.

...

you have 45 seconds.....

  

Input:

computer

Please give me the  o143 o150 o141 o151 o162 as a word.

Input:

chair

Please give me the 6d6170 as a word.

Input:

map

You've beaten the challenge

Flag: picoCTF{learning_about_converting_values_563BAF26}

jayyd@MacBook-Pro-de-Victor ~ %
```
Notas 
se tenia que entrar a un servidor el cual se te pedia, para posteirrmente ir decifrando los codigos en hexa, binarios etc, tenias 45 seg, los pude ir decifrando gracias a Hexconverter.com

Referencias
https://gchg.gitgub.io/CyberChef/
