## Objetivo

The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.
## Datos de Acceso al Nivel

```
username: bandit18
psw: x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO
```

## Solución 1
```bash
C:\Users\pac61>ssh bandit18@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:

Byebye !
Connection to bandit.labs.overthewire.org closed.

C:\Users\pac61>ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
Permission denied, please try again.
bandit18@bandit.labs.overthewire.org's password:
id
uid=11018(bandit18) gid=11018(bandit18) groups=11018(bandit18)
ls
readme
cat readme
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

```

# Información obtenida
```
pwd level 19: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```
## Notas Adicionales
- ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash
	* ssh permite que al conectarte puedas ejecutar una serie de comandos(ej. /bin/bash)
# Commands you may need to solve this level

cat, grep, ls, diff
## Referencias
- [Port scanner on Wikipedia](https://en.wikipedia.org/wiki/Port_scanner)
- [nmap](https://www.freecodecamp.org/espanol/news/que-es-nmap-y-como-usarlo-un-tutorial-para-la-mejor-herramienta-de-escaneo-de-todos-los-tiempos/#:~:text=Nmap%20es%20la%20abreviatura%20de,y%20para%20detectar%20aplicaciones%20instaladas.)