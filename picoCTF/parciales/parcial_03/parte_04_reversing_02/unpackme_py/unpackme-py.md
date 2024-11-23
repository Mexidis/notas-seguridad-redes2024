## Description

Can you get the flag?Reverse engineer this [Python program](https://artifacts.picoctf.net/c/49/unpackme.flag.py).
#### Hints
- (None)
## Solución

```shell
Mexidis-picoctf@webshell:~/picoCTF/unpackme_py$ ls
unpackme.flag.py
Mexidis-picoctf@webshell:~/picoCTF/unpackme_py$ nano solve.py
Mexidis-picoctf@webshell:~/picoCTF/unpackme_py$ python3 solve.py 

pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_cd82f94c}')
else:
  print('That password is incorrect.')


Mexidis-picoctf@webshell:~/picoCTF/unpackme_py$
```

### solve.py
```python
import base64
from cryptography.fernet import Fernet

# Payload cifrado
payload = b'gAAAAABkzWGSzE6VQNTzvRXOXekQeW4CY6NiRkzeImo9LuYBHAYw_hagTJLJL0c-kmNsjY33IUbU2IWlqxA3Fpp9S7RxNkiwMDZgLmRlI9-lGAEW-_i72RSDvylNR3QkpJW2JxubjLUC5VwoVgH62wxDuYu1rRD5KadwTADdABqsx2MkY6fKNTMCYY09Se6yjtRBftfTJUL-LKz2bwgXNd6O-WpbfXEMvCv3gNQ7sW4pgUnb-gDVZvrLNrug_1YFaIe3yKr0Awo0HIN3XMdZYpSE1c9P4G0sMQ=='

# Clave utilizada para cifrar/descifrar
key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())

# Inicializar Fernet con la clave
f = Fernet(key_base64)

# Descifrar el payload
plain = f.decrypt(payload)

# Mostrar el contenido descifrado
print(plain.decode())

```

## Bandera
```css
flag: picoCTF{175_chr157m45_cd82f94c}
```
## Notas Adicionales

## Referencias
- 