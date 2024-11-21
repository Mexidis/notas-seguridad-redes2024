## Description

Not all ancient ciphers were so bad... The flag is not in standard format. `nc mercury.picoctf.net 19860` [playfair.py](https://mercury.picoctf.net/static/3f082e143dd5b4ffe1a0aaaf317872b8/playfair.py)
#### Hints
- (None)
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_02_crypto_02/play_nice]
└─$  nc mercury.picoctf.net 19860
Here is the alphabet: lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9
Here is the encrypted message: 1x5hqlod8x7oa88h0de1b5r6xja5sd
What is the plaintext message? nothing

┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_02_crypto_02/play_nice]
└─$  nc mercury.picoctf.net 19860
Here is the alphabet: lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9
Here is the encrypted message: 1x5hqlod8x7oa88h0de1b5r6xja5sd
What is the plaintext message?                                                                                                             
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_02_crypto_02/play_nice]
└─$  nc mercury.picoctf.net 19860
Here is the alphabet: lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9
Here is the encrypted message: 1x5hqlod8x7oa88h0de1b5r6xja5sd
What is the plaintext message?                                                                                                             
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_02_crypto_02/play_nice]
└─$ python decryp.py 1x5hqlod8x7oa88h0de1b5r6xja5sd
lhxm62i5lwoi0rljor647xq9wh7wie
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_02_crypto_02/play_nice]
└─$ nc mercury.picoctf.net 19860                                                                 
Here is the alphabet: lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9
Here is the encrypted message: 1x5hqlod8x7oa88h0de1b5r6xja5sd
What is the plaintext message? lhxm62i5lwoi0rljor647xq9wh7wie
Congratulations! Here's the flag: f391b621282ef5063ab2de93ab9e4bff

```

Utilizando:
```python
#!/usr/bin/python3 -u
import signal
import sys

SQUARE_SIZE = 6


def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def encrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]]
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def encrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s
	else:
		plain = s + "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"[0]
	for i in range(0, len(plain), 2):
		result += encrypt_pair(plain[i:i + 2], matrix)
	return result

def decrypt_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    if p1[0] == p2[0]:  # Misma fila
        return matrix[p1[0]][(p1[1] - 1) % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1) % SQUARE_SIZE]
    elif p1[1] == p2[1]:  # Misma columna
        return matrix[(p1[0] - 1) % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1) % SQUARE_SIZE][p2[1]]
    else:  # Rectángulo
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def decrypt_string(s, matrix):
	result = ""
	for i in range(0, len(s), 2):
		result += decrypt_pair(s[i:i + 2], matrix)
    
	return result

alphabet = "lsi28c14ot0vbf7nagh3mpjuxy5kwz6edqr9"
m = generate_square(alphabet)
msg = sys.argv[1]

decrypted = decrypt_string(msg, m)
print(decrypted)

# https://en.wikipedia.org/wiki/Playfair_cipher

```
## Bandera
```css
flag: f391b621282ef5063ab2de93ab9e4bff
```
## Notas Adicionales

## Referencias
- 