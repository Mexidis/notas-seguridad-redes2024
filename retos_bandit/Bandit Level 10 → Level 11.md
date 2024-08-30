## Objetivo

The password for the next level is stored in the file **data.txt**, which contains base64 encoded data.
## Datos de Acceso al Nivel

```
username: bandit10
psw: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

## Solución
```bash
C:\Users\pac61>ssh bandit10@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
bandit10@bandit:~$ echo "hola mundo"
hola mundo
bandit10@bandit:~$ echo "hola mundo" | base64
aG9sYSBtdW5kbwo=
bandit10@bandit:~$ echo -n aG9sYSBtdW5kbwo= | base64
YUc5c1lTQnRkVzVrYndvPQ==
bandit10@bandit:~$ echo -n aG9sYSBtdW5kbwo= | base64 -d
hola mundo
bandit10@bandit:~$ base64 -d data.txt
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
bandit10@bandit:~$
```

# Información obtenida
```
pwd level 11: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```
## Notas Adicionales

Los comandos utilizan echo para generar y manipular cadenas de texto, y base64 para codificar y decodificar cadenas utilizando el estándar Base64.

1. **`ls`**: Lista los archivos en el directorio actual. En este caso, muestra `data.txt`.
    
2. **`cat data.txt`**: Muestra el contenido del archivo `data.txt`, que es una cadena codificada en Base64.
    
3. **`echo "hola mundo"`**: Imprime "hola mundo" en la terminal.
    
4. **`echo "hola mundo" | base64`**: Codifica el texto "hola mundo" en Base64 y muestra la salida (`aG9sYSBtdW5kbwo=`).
    
5. **`echo -n aG9sYSBtdW5kbwo= | base64`**: Decodifica la cadena Base64 `aG9sYSBtdW5kbwo=`. La opción `-n` de `echo` se usa para evitar que añada un salto de línea al final, lo cual es importante para la decodificación precisa.
    
6. **`echo -n aG9sYSBtdW5kbwo= | base64 -d`**: Decodifica la cadena Base64 `aG9sYSBtdW5kbwo=` directamente y muestra "hola mundo".
    
7. **`base64 -d data.txt`**: Decodifica el contenido de `data.txt` desde Base64. El resultado es la contraseña para el siguiente nivel del desafío.
    
8. **`cat data.txt`**: Muestra nuevamente el contenido de `data.txt`, que es la cadena codificada en Base64.
    
9. **`cat data.txt | base64 -d`**: Pasa el contenido de `data.txt` a `base64 -d`, lo que decodifica la cadena Base64 y muestra la contraseña para el siguiente nivel: "The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr".

# Commands you may need to solve this level

[man](https://manpages.ubuntu.com/manpages/noble/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Referencias
[Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php) , [CyberChef](https://gchq.github.io/CyberChef/), 