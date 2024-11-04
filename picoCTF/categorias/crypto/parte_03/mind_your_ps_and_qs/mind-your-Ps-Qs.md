## Description

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values)
#### Hints
- Bits are expensive, I used only a little bit over 100 to save money
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/mind_your_ps_and_qs]
└─$ cat values 
Decrypt my super sick RSA:
c: 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n: 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e: 65537

┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/mind_your_ps_and_qs]
└─$ cat ps_and_qs.py 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473
n = p*q
phi = (p-1)*(q-1)

e = 65537
d = modinv(e, phi)
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
plain = pow(c,d,n)
print(plain)
print(hex(plain))
print(bytearray.fromhex(hex(plain)[2:]).decode())

                                                                        
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/mind_your_ps_and_qs]
└─$ python3 ps_and_qs.py
13016382529449106065927291425342535437996222135352905256639555294957886055592061
0x7069636f4354467b736d6131315f4e5f6e305f67306f645f30303236343537307d
picoCTF{sma11_N_n0_g0od_00264570}


```

![[Pasted image 20241103044006.png]]


```txt
c - texto cifrado
m - mensaje texto plano
p - primo 1
q - primo 2
n - modulo
tn - totient n (euler)
e - exponente (llave pública) 2^16 + 1 = 65537
d - llave privada

n = p * q
tn = (p - 1)*(q - 1)
d = e mod inv tn / inverse(e, tn)

Encriptar     :  c = m^e mod n / pow(m, e, n)
Desencriptar  :  m = c^d mod n / pow(c, d, n)

c = m^e mod n
c = m^3
m = 3 raiz c
```


## Bandera
```css
flag: picoCTF{sma11_N_n0_g0od_00264570}
```
## Notas Adicionales
Para obtener `p` y `q` se tuvo que sacar de la página: [Integer factorization calculator](https://www.alpertron.com.ar/ECM.HTM) y a partir de ahí podemos calcular y desencriptar la bandera.

## Referencias
- [python-code](https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python)