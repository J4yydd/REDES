
### descripcion 
## Operation Orchid

ForensicsMedium400 pts10,869 solves

by LT 'syreal' Jones

Download this disk image and find the flag.

Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

- [Download compressed disk image](https://artifacts.picoctf.net/c/213/disk.flag.img.gz)
### solucion 
```
jayyd@MacBook-Pro-de-Victor lskdj % openssl aes256 -d -in flag.txt.enc -out flag.txt -k PASSWORD

cat flag.txt

*** WARNING : deprecated key derivation used.

Using -iter or -pbkdf2 would be better.

bad decrypt

001FAF0302000000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:providers/implementations/ciphers/ciphercommon_block.c:107:

$?????w'?`?1?٭T?设??N?+?':??P**%**                                                  jayyd@MacBook-Pro-de-Victor lskdj % openssl aes256 -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567

cat flag.txt

*** WARNING : deprecated key derivation used.

Using -iter or -pbkdf2 would be better.

bad decrypt

001FAF0302000000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:providers/implementations/ciphers/ciphercommon_block.c:107:

picoCTF{h4un71ng_p457_5113beab}**%**                                                jayyd@MacBook-Pro-de-Victor lskdj %
```