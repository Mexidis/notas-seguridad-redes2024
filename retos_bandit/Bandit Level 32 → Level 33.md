## Objetivo

After all this `git` stuff, it’s time for another escape. Good luck!
## Datos de Acceso al Nivel

```
username: bandit32
psw: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K
```

## Solución
```c
C:\Users\pac61>ssh bandit32@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames
```


```shell
bandit32@bandit.labs.overthewire.org's password:

WELCOME TO THE UPPERCASE SHELL
>> $0
$ cat /etc/bandit_pass/bandit33
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```

# Información obtenida
```
pwd level 33: tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0
```
## Notas Adicionales
- Como todo lo que escribimos lo transforma en mayúsculas y por lo tanto no podemos ejecutar ningún comando, ya que no existe ningún comando en bash cuyo nombre sean todo mayúsculas. Sin embargo, podemos usar las variables como $0, la cual contiene el nombre del programa ejecutándose, en este caso bash. Por lo que podemos invocar la shell escribiendo $0 en la terminal.
# Commands you may need to solve this level
sh, man
## Referencias
- 