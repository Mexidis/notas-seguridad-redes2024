## Objetivo

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.
## Datos de Acceso al Nivel

```
username: bandit22
psw: tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

## Solución 1
```bash
C:\Users\pac61>ssh bandit22@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit22@bandit.labs.overthewire.org's password:

bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$
bandit22@bandit:~$ myname=bandit23
bandit22@bandit:~$ mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
bandit22@bandit:~$ echo $mytarget
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
bandit22@bandit:~$


```

# Información obtenida
```
pwd level 23: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```
## Notas Adicionales
- cron job en linux es una herramienta que permite programar y ejecutar tareas específicas dentro de nuestro sistema operativo linux de forma automática.
- /etc/cron.d - ahí ponemos los cronjobs, o dicho de otra forma, los archivos que quiero se ejecuten cada vez que arranca la computadora.
# Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)
## Referencias
- [¿Qué es cron?](https://opensource.com/article/21/7/cron-linux#:~:text=SA%20Seth%20Kenlon-,The%20cron%20system%20is%20a%20method%20to%20automatically%20run%20commands,user%20to%20automate%20their%20computer.)