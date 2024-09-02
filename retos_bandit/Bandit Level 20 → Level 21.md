## Objetivo

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

**NOTE:** Try connecting to your own network daemon to see if it works as you think
## Datos de Acceso al Nivel

```
username: bandit20
psw: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
```

## Solución 1
```bash
C:\Users\pac61>ssh bandit20@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit20@bandit.labs.overthewire.org's password:

bandit20@bandit:~$ nc -lnvp 7769 <<< 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO &
[2] 3141922
bandit20@bandit:~$ Listening on 0.0.0.0 7769

bandit20@bandit:~$ ./suconnect 7769
Connection received on 127.0.0.1 60326
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
[2]+  Done                    nc -lnvp 7769 <<< 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
bandit20@bandit:~$

```

# Información obtenida
```
pwd level 21: EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```
## Notas Adicionales
- & si agregamos un símbolo de estos al final del comando, lo estamos enviando al segundo plano (background) 
- jobs - me muestra que comandos están en el segundo plano
- fg - saca un proceso o comando del segundo plano y lo trae al primer plano (foregorund)
# Commands you may need to solve this level
ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)
## Referencias
* 