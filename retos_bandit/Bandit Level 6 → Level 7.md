## Objetivo

The password for the next level is stored **somewhere on the server** and has all of the following properties:

- owned by user bandit7
- owned by group bandit6
- 33 bytes in size
## Datos de Acceso al Nivel

```
username: bandit6
psw: HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

## Solución
```bash
C:\Users\pac61>ssh bandit6@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:

bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
bandit6@bandit:~$

```

# Información obtenida
```
pwd level 7: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```
## Notas Adicionales

El comando _ls -R_ lista archivos de forma recursiva, es decir todas los directorios internos y sus archivos internos y/o subdirectorios.
_find / -user bandit7 -group bandit6 - size 33c 2>/dev/null_
	  / indica a find que busque desde el directorio raíz.
	 -user - indica a qué usuario pertenece el archivo
	 -group - indica a qué grupo pertenece el archivo
	 -size - indica el tamaño del archivo
	 2>/dev/null - manda la salida de errror al dispositivo null, es decir, se oculta al usuario.
	

# Commands you may need to solve this level

[ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)

