### descripcion
We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/edaf70675fae491d08043f5f626637436b05319785fa562e9274cdb4b09ec7ba/capture.pcap). Recover the flag.

### solucion 
Lo primero que hago es abrir WireShark para analizar el tráfico de paquetes. Segun la sugerencia busco en los streams una bandera. Comenzo a buscar uno por uno en los streams, hasta que el stream numero 6, encuentro la flag:

![[imágenes/banderaWireshark.png]]