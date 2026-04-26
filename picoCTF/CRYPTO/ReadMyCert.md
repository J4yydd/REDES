### descripcion
¿Qué tal si te llevamos a una aventura para explorar las solicitudes de firma de certificados?Echa un vistazo a este archivo CSR [aquí](https://artifacts.picoctf.net/c/421/readmycert.csr) .




### solucion 
solo se ve el contenido competo con = openssl req -in readmycert.csr -noout -text
y luego se busca drecto la flag = openssl req -in readmycert.csr -noout -text | grep pico




