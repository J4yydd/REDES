## Descripción

  

This website can be rendered only by picobrowser, go and catch the flag!

http://fickle-tempest.picoctf.net:50487

## Solución

  

- Usando la terminal para cambiar el agente

  

```

└─$ curl -s http://fickle-tempest.picoctf.net:50487/flag -H 'User-Agent: picobrowser' | grep pico

         <!-- <strong>Title</strong> --> picobrowser!

            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{p1c0_s3cr3t_ag3nt_fba5c48f}</code></p>

  

```

  

picoCTF{p1c0_s3cr3t_ag3nt_fba5c48f}