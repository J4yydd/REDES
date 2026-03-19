### descripcion

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one?Image: [dolls.jpg](https://challenge-files.picoctf.net/c_wily_courier/feaddb84eaaa2f8d6b83bda9e7a9c46a86474361e095fea9ee3840873f3506b4/dolls.jpg)


```
$ binwalk dolls.jpg            

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378933, uncompressed size: 383920, name: base_images/2_c.jpg
651591        0x9F147         End of Zip archive, footer length: 22
```Descubrimos que tiene zip guardado dentro de la imagen, al hacerle unzip nos saca otra imagen, le volvemos a hacer unzip varias veces hasta que la ultima magen nos arroja la flag
