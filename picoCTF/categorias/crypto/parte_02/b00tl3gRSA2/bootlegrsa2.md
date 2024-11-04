## Description

In RSA d is a lot bigger than e, why don't we use d to encrypt instead of e? Connect with `nc jupiter.challenges.picoctf.org 57464`.
#### Hints
- What is $e$ generally?
## Solución

```shell


```


## Script de python
```python

```

## RSA notes
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
picoCTF{}
```
## Notas Adicionales


## Referencias
- 