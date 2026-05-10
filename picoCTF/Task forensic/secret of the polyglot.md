### descripcion 
## Secret of the Polyglot

ForensicsEasy100 pts42,886 solves

by syreal

The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/98/flag2of2-final.pdf).


### descripcion 
```
jayyd@MacBook-Pro-de-Victor lskdj % strings ukn_reality.jpg | grep pico

jayyd@MacBook-Pro-de-Victor lskdj % ls

flag2of2-final.pdf

jayyd@MacBook-Pro-de-Victor lskdj % file flag2of2-final.pdf

flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced

jayyd@MacBook-Pro-de-Victor lskdj % open flag2of2-final.pdf

jayyd@MacBook-Pro-de-Victor lskdj % strings flag2of2-final.pdf | head

IHDR

iCCPICC profile

byY%>'

\W<~

C`$G

pHYs

tIME

tEXtComment

Created with GIMPW

{IDATh

jayyd@MacBook-Pro-de-Victor lskdj % cp flag2of2-final.pdf flag.png

open flag.png

jayyd@MacBook-Pro-de-Victor lskdj %
```