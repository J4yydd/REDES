from pwn import remote
from sympy import factorint
from math import prod

HOST = "fickle-tempest.picoctf.net"
PORT = 60234

io = remote(HOST, PORT)

def enviar(valor):
    io.sendline(str(valor).encode())

while True:
    texto = io.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):", timeout=5).decode(errors="ignore")
    print(texto)

    if "p :" in texto and "q :" in texto and "PRODUCE THE FOLLOWING ####\nn" in texto:
        enviar("Y")
        p = int(texto.split("p :")[1].split()[0])
        q = int(texto.split("q :")[1].split()[0])
        io.recvuntil(b"n:")
        enviar(p * q)

    elif "p :" in texto and "n :" in texto and "PRODUCE THE FOLLOWING ####\nq" in texto:
        enviar("Y")
        p = int(texto.split("p :")[1].split()[0])
        n = int(texto.split("n :")[1].split()[0])
        io.recvuntil(b"q:")
        enviar(n // p)

    elif "e :" in texto and "n :" in texto and "PRODUCE THE FOLLOWING ####\nq\np" in texto:
        enviar("N")

    else:
        enviar("N")
