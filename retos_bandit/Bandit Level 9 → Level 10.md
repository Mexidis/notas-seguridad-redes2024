## Objetivo

The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.
## Datos de Acceso al Nivel

```
username: bandit9
psw: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```

## Solución
```bash
C:\Users\pac61>ssh bandit9@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ file data.txt
data.txt: data
bandit9@bandit:~$ strings data.txt | grep ==
\a!;========== the
========== passwordf
========== isc
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
bandit9@bandit:~$
```

# Información obtenida
```
pwd level 10: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```
## Notas Adicionales

1. **`strings data.txt`**: El comando `strings` busca y muestra todas las cadenas de texto legibles (cadenas imprimibles) en un archivo binario o en cualquier archivo que contenga datos no legibles. En este caso, busca las cadenas legibles en el archivo `data.txt`.
2. **`|`**: El operador pipe (`|`) redirige la salida del comando `strings` como entrada al siguiente comando.
3. **`grep ==`**: El comando `grep` busca líneas que contengan un patrón específico en la entrada. En este caso, el patrón es `==`. Este comando buscará todas las líneas que contengan `==` en la salida proporcionada por el comando `strings`.

En resumen, el comando completo `strings data.txt | grep ==`:
- Busca todas las cadenas legibles dentro del archivo `data.txt`.
- Filtra y muestra solo las cadenas que contienen el patrón `==`.

Este comando podría ser útil para extraer información específica que contenga `==` de un archivo que podría estar en un formato no completamente legible.

# Commands you may need to solve this level

[man](https://manpages.ubuntu.com/manpages/noble/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Referencias
[Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php) 