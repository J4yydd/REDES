#### Descripción

¿Se pueden invocar indicadores de ayuda para una herramienta o un binario? Este programa contiene información muy útil...[cálido](https://challenge-files.picoctf.net/c_wily_courier/70013ed41d4cfe2bb48628471dac6fc12238b5dbe164301ae3b4e35277b1e80b/warm)

Solucion 
```
jayyd@MacBook-Pro-de-Victor aa % strings warm | grep pico

Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}

jayyd@MacBook-Pro-de-Victor aa %
```
	este literalmente se soluciona igual que el pasado, se utiliza strings, y usas pico, te da la bandera.