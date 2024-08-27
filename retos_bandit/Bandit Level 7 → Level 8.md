## Objetivo

The password for the next level is stored in the file **data.txt** next to the word **millionth**
## Datos de Acceso al Nivel

```
username: bandit7
psw: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```

## Solución
```bash
C:\Users\pac61>ssh bandit7@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ wc data.txt
  98567  197133 4184396 data.txt
bandit7@bandit:~$ grep millionth data.txt
millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
bandit7@bandit:~$
```

# Información obtenida
```
pwd level 8: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```
## Notas Adicionales

El grep nos busca el contenido con ese nombre.
Usage: grep [OPTION]... PATTERNS [FILE]...
Search for PATTERNS in each FILE.

# Commands you may need to solve this level

[man](https://manpages.ubuntu.com/manpages/noble/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd