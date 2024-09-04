## Objetivo

A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

**NOTE:** Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.
## Datos de Acceso al Nivel

```
username: bandit24
psw: gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
```

## Solución
```bash
C:\Users\pac61>ssh bandit24@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit24@bandit.labs.overthewire.org's password:

bandit24@bandit:~$ for i in {0000..9999}; do echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i ; done | nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
Wrong! Please enter the correct current password and pincode. Try again.
^C
bandit24@bandit:~$ for i in {0000..9999}; do echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i ; done | nc localhost 30002 | grep
 -v Wrong
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```

# Información obtenida
```
pwd level 25: iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```
## Notas Adicionales
- grep -v mensaje / filtra todas las líneas que no contengan el mensaje
-  
# Commands you may need to solve this level
cron, crontab, crontab(5) (use “man 5 crontab” to access this)
## Referencias
- [¿Qué es cron?](https://opensource.com/article/21/7/cron-linux#:~:text=SA%20Seth%20Kenlon-,The%20cron%20system%20is%20a%20method%20to%20automatically%20run%20commands,user%20to%20automate%20their%20computer.)