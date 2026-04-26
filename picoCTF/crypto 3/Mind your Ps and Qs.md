
### descripcion
En RSA, un valor pequeño de e puede ser problemático, pero ¿qué pasa con N ? ¿Puedes descifrarlo?[valores](https://challenge-files.picoctf.net/c_wily_courier/4540a62876bdb4e341c70e3300408ced0ae02e4d27bb41b747a80f42aef919ba/values)

### solucion
aqui soo se deben de ver los valores que te otorgan, posteriormente poer este codigo con sus respetivos  valores = 
c = 15341890103764929939105506004034128738090325640037083301857608662849501626260517
n = 948406957756830799684818171639547165784816468744946013083947881743680617123566349
e = 65537

p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477

phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

m = pow(c, d, n)

mensaje = m.to_bytes((m.bit_length() + 7) // 8, "big")

print(mensaje[::-1].decode())