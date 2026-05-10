### descripcion 
ForensicsEasy100 pts44,950 solves

by Mubarak Mikail

How about some hide and seek?

Download this file [here](https://artifacts.picoctf.net/c_titan/131/unknown.zip).

### solucion 

```
jayyd@MacBook-Pro-de-Victor lskdj % unzip unknown.zip

Archive:  unknown.zip

  inflating: ukn_reality.jpg         

jayyd@MacBook-Pro-de-Victor lskdj % exiftool ukn_reality.jpg

ExifTool Version Number         : 13.55

File Name                       : ukn_reality.jpg

Directory                       : .

File Size                       : 2.3 MB

File Modification Date/Time     : 2024:03:11 18:05:57-06:00

File Access Date/Time           : 2024:03:11 18:05:57-06:00

File Inode Change Date/Time     : 2026:05:10 16:17:08-06:00

File Permissions                : -rw-r--r--

File Type                       : JPEG

File Type Extension             : jpg

MIME Type                       : image/jpeg

JFIF Version                    : 1.01

Resolution Unit                 : inches

X Resolution                    : 72

Y Resolution                    : 72

XMP Toolkit                     : Image::ExifTool 11.88

Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==

Image Width                     : 4308

Image Height                    : 2875

Encoding Process                : Baseline DCT, Huffman coding

Bits Per Sample                 : 8

Color Components                : 3

Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)

Image Size                      : 4308x2875

Megapixels                      : 12.4

jayyd@MacBook-Pro-de-Victor lskdj % strings ukn_reality.jpg | grep pico

jayyd@MacBook-Pro-de-Victor lskdj %
```