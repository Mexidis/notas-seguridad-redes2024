## Objetivo

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
## Datos de Acceso al Nivel

```
username: bandit19
psw: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
```

## Solución 1
```bash
C:\Users\pac61>ssh bandit19@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit19@bandit.labs.overthewire.org's password:
bandit19@bandit:~$ whoami
bandit19
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Jul 17 15:57 .
drwxr-xr-x 70 root     root      4096 Jul 17 15:58 ..
-rwsr-x---  1 bandit20 bandit19 14880 Jul 17 15:57 bandit20-do
-rw-r--r--  1 root     root       220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root     root      3771 Mar 31 08:41 .bashrc
-rw-r--r--  1 root     root       807 Mar 31 08:41 .profile
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do /etc/bandit_pass/bandit20
env: ‘/etc/bandit_pass/bandit20’: Permission denied
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
bandit19@bandit:~$


```

# Información obtenida
```
pwd level 20: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```
## Notas Adicionales
- setuid - es un bit que se puede modificar en un ejecutable para darle permisos a un usuario especifico
# Commands you may need to solve this level

## Referencias
- [setuid on Wikipedia](https://en.wikipedia.org/wiki/Setuid)