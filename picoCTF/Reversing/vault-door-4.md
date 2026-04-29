### descripcion
Esta bóveda utiliza codificación ASCII para la contraseña.El código fuente de esta bóveda se encuentra aquí: [VaultDoor4.java](https://challenge-files.picoctf.net/c_fickle_tempest/3af806b1d880a4a7cecd00831a8bcc913cf57c68cb7f5cfb8597f710c5d771e1/VaultDoor4.java)


### solucion

Básicamente, el código es como una cerradura que compara lo q escribes con una contraseña que ya tienen guardada en si  pero como no deja de leerla asi nomas , la ocultaron usando puros números. El truco es que esos números están mezclados como diferentesasí que para sacar la flag solo hay que traducir cada grupito de números a letras normales y juntarlos todos para armar la frase completa que abre el vault
