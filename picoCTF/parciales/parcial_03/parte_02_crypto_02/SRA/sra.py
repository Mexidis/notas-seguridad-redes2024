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
        