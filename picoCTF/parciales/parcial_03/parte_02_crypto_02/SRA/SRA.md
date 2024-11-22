## Description

I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...Connect to the program on our server: `nc saturn.picoctf.net 50372`Download the program: [chal.py](https://artifacts.picoctf.net/c/297/chal.py)
#### Hints
- (None)
## Solución

Haciendo unas breves modificaciones al código que nos proporcionan.
```python
from pwn import *
import primefac
from itertools import combinations
from Crypto.Util.number import long_to_bytes

def sub_lists(l):
    comb = []
    for i in range(1,len(l)+1):
        comb += [list(j) for j in combinations(l, i)]
    return comb

def divisors(phi):
    print("Give me the divisors of ", phi-1)
    return(eval(input()))

r = remote('nc saturn.picoctf.net', 50372)
r.recvuntil("anger =")
ciphertext = int(r.recvline())
r.recvuntil("envy =")
d = int(r.recvline())
print("cipher=", ciphertext)
print("d=",d)
print(r.recvuntil("vainglory?"))
r.recvline()
factors=divisors(d*65537)
combos = sub_lists(factors)
primes = set()
for l in combos:
    product = 1
    for k in l:
        product = product * k
    if product.bit_length() == 128 and primefac.isprime(product+1):
        primes.add(product+1)
print(primes)
primelist = list(primes)
for p in primelist:
    for q in primelist:
        n = p*q
        plain = pow(ciphertext,d,n)
        try:
            plaintext = long_to_bytes(plain)
            print(plaintext.decode())
            r.sendline(plaintext.decode())
            print(r.recvline())
            print(r.recvline())
            print(r.recvline())
        except:
            continue
```

```shell
Mexidis-picoctf@webshell:~/picoCTF/sra$ python3 solve.py 
[+] Opening connection to saturn.picoctf.net on port 56935: Done
/home/Mexidis-picoctf/picoCTF/sra/solve.py:17: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("anger =")
/home/Mexidis-picoctf/picoCTF/sra/solve.py:19: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("envy =")
cipher= 17219400649571041919662308241244509572502363482957939359011739180886354682789
d= 7041969161555784603174050300214214983457843907673303603596612735138810213573
/home/Mexidis-picoctf/picoCTF/sra/solve.py:23: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("vainglory?"))
b'vainglory?'
Give me the divisors of  461509532940881455538217734525139007370876716177185298268911208822792204966933700
[2, 2, 3, 3, 3, 5, 5, 7, 7, 11, 19, 73, 3967, 428693, 925823, 2614359612359819, 20458581099053479, 2715027868783753446718259]
{225078752573580492316676853836043318469, 202951020407284451983048426057859074909, 190114373450651243259933449013091225351, 286635704044555119274838993035448353067, 258281645379443661118989299606905513951, 294080526012336152387458214401736096863, 213578233026330463848648909505925048701, 267345932738487411261325649456123724421, 276342090807388437732416902808220700651, 232127356278206287695230198358905388547, 193488752212376212693283611192388115877}
VU8Q8erPVytaXmDy
/home/Mexidis-picoctf/picoCTF/sra/solve.py:43: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendline(plaintext.decode())
b'> VU8Q8erPVytaXmDy\r\n'
b'Conquered!\r\n'
b'picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}\r\n'
VU8Q8erPVytaXmDy
[*] Closed connection to saturn.picoctf.net port 56935
Mexidis-picoctf@webshell:~/picoCTF/sra$ 
```

![[Pasted image 20241121234513.png]]
## Bandera
```css
flag: picoCTF{7h053_51n5_4r3_n0_m0r3_38268294}
```
## Notas Adicionales
Para poder resolver este reto se utilizó el webshell de la página de picoCTF para poder utilizar las librerías de python que no funcionan en kali linux.

## Referencias
- [Obtener-factores](https://www.dcode.fr/prime-factors-decomposition)