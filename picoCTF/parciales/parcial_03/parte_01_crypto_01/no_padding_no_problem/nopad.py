from pwn import *
r = remote("mercury.picoctf.net", 30048)
print(r.recvuntil("n:"))
n=int(r.recvline())
print(n)
print(r.recvuntil("e:"))
e=int(r.recvline())
print(e)
print(r.recvuntil("ciphertext:"))
c=int(r.recvline())
print(c)
print(r.recvuntil("to decrypt:"))
r.sendline(str(pow(2,e,n)*c))
print(r.recvuntil("you go:"))
p2=int(r.recvline())
print(p2)
print(p2//2)
st="{:x}".format(p2//2)
print(binascii.unhexlify(st))