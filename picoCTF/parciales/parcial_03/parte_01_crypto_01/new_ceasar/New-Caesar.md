## Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) `mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj` [new_caesar.py](https://mercury.picoctf.net/static/b82dc751249b75b2509315c59f8200c7/new_caesar.py)
#### Hints
- How does the cipher work if the alphabet isn't 26 letters?
- Even though the letters are split up, the same paradigms still apply
## Solución

```python
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
        enc = ""
        for c in plain:
                binary = "{0:08b}".format(ord(c))
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
        return enc

def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
        enc += shift(c, key[i % len(key)])
print(enc)

```

## Corrigiendo un poco el código:

```python
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(cipher):
	enc = ""
	for i in range(0,len(cipher),2):
		binary = "{0:04b}".format(ALPHABET.index(cipher[i]))+"{0:04b}".format(ALPHABET.index(cipher[i+1]))
		enc += chr(int(binary,2))	
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

encflag = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
#flag = "redacted"
#key = "redacted"
#assert all([k in ALPHABET for k in key])
#assert len(key) == 1

print(len(encflag))
for key in ALPHABET:
	dec = ""
	for c in encflag:
		dec += shift(c,key)
	b16 = b16_decode(dec)
	print(key, b16)

```


```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_01_crypto_01/new_ceasar]
└─$ python3 new_caesar.py
78
a ËÚµÚÛµÇÊÇËÇÌÌÊËÈÇÉ
b ÜëÆëì¦ÆØ©ÛØ¨Ü¨¯ØÝ« Ý­« ¯§­ ¯¯®¯­ÛÜÙ©Ø­Ú
c íü×üý·×éºìé¹í¹°éî¼±î¾¼±°¸¾±°°¿°¾ìíêºé¾ë
ÈèúËýúÊþÊÁúÿÍÂÿÏÍÂÁÉÏÂÁÁÀÁÏýþûËúÏü
e ùÙù
     Ü
      ÛÛÒ
         ÞÓÐÞÓÒÚÐÓÒÒÑÒÐ
                       Ü
                        Ð
f /
/ ê
íììãïäáïäãëáäããâãáíá
g !01ûþ -ý!ýô-"ðõ"òðõôüòõôôóôò !.þ-ò/
h 2A,AB
12?>0  ,>1>2>33
i CR=RS=OBOCODDBC@OA
j TcNcd.NP!SP T 'PU#(U%#('/%(''&'%STQ!P%R

*tal vez el siguiente texto sea la bandera*

k et_tu?_a2da1e18af49f649806988786deb2a6c


l v`@`rCurBvBIrwEJwGEJIAGJIIHIGuvsCrGt
m qQqTSSZV[XV[ZRX[ZZYZXTX
n §§¨beddkgliglkcilkkjkiei
o ©¸¸¹s¥v¨¥u©u|¥ªx}ªzx}|tz}||{|z¨©¦v¥z§
p ºÉ¤ÉÊ¤¶¹¶º¶»»¹º·¶¸
```

## Bandera
```css
flag: picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c}
```
## Notas Adicionales

## Referencias
- 