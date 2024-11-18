## Description

Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with `nc mercury.picoctf.net 30048`.
#### Hints
- What can you do with a different pair of ciphertext and plaintext? What if it is not so different after all...
## Solución

Utilizando este pequeño script de python:
```python
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

```

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem]
└─$ python3 nopad.py
[+] Opening connection to mercury.picoctf.net on port 30048: Done
/home/kali/shared/notas-seguridad-redes2024/picoCTF/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem/nopad.py:3: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("n:"))
b'Welcome to the Padding Oracle Challenge\nThis oracle will take anything you give it and decrypt using RSA. It will not accept the ciphertext with the secret message... Good Luck!\n\n\nn:'
86135606002986707704737996769621184606881982226581164781014799499861766224060348598091914022951373194959496433305233631756624583831569360624943185594899421360275893925124573874109656209848347100519964620393268017201518909547839092757987952120467684272837216643279483388588755411938805952193157109012896606619
/home/kali/shared/notas-seguridad-redes2024/picoCTF/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem/nopad.py:6: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("e:"))
b'e:'
65537
/home/kali/shared/notas-seguridad-redes2024/picoCTF/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem/nopad.py:9: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("ciphertext:"))
b'ciphertext:'
77731426269646195460940203085335840984348948115613618231226732706833339339691202848897096167499563954850340799247736686041627309942949132587204527591697903025094316660180525362297063402713943351701847041865449325629500890878857194020688809850182667664612098339514400750797396457163106131841288558887551829668
/home/kali/shared/notas-seguridad-redes2024/picoCTF/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem/nopad.py:12: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("to decrypt:"))
b'\n\nGive me ciphertext to decrypt:'
/home/kali/shared/notas-seguridad-redes2024/picoCTF/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem/nopad.py:13: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendline(str(pow(2,e,n)*c))
/home/kali/shared/notas-seguridad-redes2024/picoCTF/parciales/parcial_03/parte_01_crypto_01/no_padding_no_problem/nopad.py:14: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("you go:"))
b' Here you go:'
580550060391700078946913236734911770139931497702556153513487440893406629034802718534645538074938502890769425795379846471930
290275030195850039473456618367455885069965748851278076756743720446703314517401359267322769037469251445384712897689923235965
b'picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_5052620}'
[*] Closed connection to mercury.picoctf.net port 30048

```

## Bandera
```css
flag: picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_5052620}
```
## Notas Adicionales

## Referencias
- 