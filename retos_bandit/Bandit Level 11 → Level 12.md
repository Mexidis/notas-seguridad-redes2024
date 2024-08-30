## Objetivo

The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.
## Datos de Acceso al Nivel

```
username: bandit11
psw: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

## Solución
```bash
C:\Users\pac61>ssh bandit11@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
bandit11@bandit:~$ cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
bandit11@bandit:~$
```

# Información obtenida
```
pwd level 12: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
## Notas Adicionales

Aquí se realizó una operación de decodificación utilizando el cifrado ROT13. Vamos a desglosarlo paso a paso:

1. **`cat data.txt`**: Este comando muestra el contenido del archivo `data.txt`. El contenido es:

    `Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4`
    
2. **`|`**: El operador pipe (`|`) redirige la salida del comando `cat data.txt` como entrada al siguiente comando.
    
3. **`tr [a-zA-Z] [n-za-mN-ZA-M]`**: El comando `tr` realiza una traducción de caracteres. En este caso, traduce las letras del alfabeto (`a-zA-Z`) utilizando el cifrado ROT13, que desplaza cada letra 13 posiciones en el alfabeto. Esto significa que:
    
    - `a` se convierte en `n`,
    - `b` se convierte en `o`,
    - y así sucesivamente. Las letras mayúsculas (`A-Z`) también se desplazan de manera similar.
    
    Al aplicar ROT13 al texto "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4", se obtiene:
    
    `The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`
    
	
En resumen, lo que se hizo fue decodificar un mensaje cifrado con ROT13. El contenido cifrado era "Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4", y al aplicar el cifrado ROT13, se obtuvo el mensaje decodificado: "The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4".

# Commands you may need to solve this level

[man](https://manpages.ubuntu.com/manpages/noble/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Referencias
[Rot13 on Wikipedia](https://en.wikipedia.org/wiki/ROT13)