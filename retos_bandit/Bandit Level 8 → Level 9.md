## Objetivo

The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.
## Datos de Acceso al Nivel

```
username: bandit8
psw: dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```

## Solución
```bash
C:\Users\pac61>ssh bandit8@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ wc data.txt
 1001  1001 33033 data.txt
bandit8@bandit:~$ cat data.txt | sort | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
bandit8@bandit:~$
```

# Información obtenida
```
pwd level 9: 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```
## Notas Adicionales

1. `cat data.txt`: Muestra el contenido del archivo `data.txt`.
2. `|`: El operador pipe (`|`) redirige la salida del comando anterior como entrada al siguiente comando.
3. `sort`: Ordena las líneas del archivo en orden alfabético o numérico.
4. `uniq -u`: El comando `uniq` se utiliza para eliminar líneas duplicadas, pero con la opción `-u`, solo muestra las líneas que aparecen una única vez.

En resumen, el comando completo `cat data.txt | sort | uniq -u` realiza las siguientes operaciones:

- Lee el archivo `data.txt`.
- Ordena las líneas del archivo.
- Muestra solo aquellas líneas que no están duplicadas, es decir, aquellas que aparecen exactamente una vez en el archivo ordenado.

Este comando es útil cuando quieres encontrar las líneas únicas en un archivo.

# Commands you may need to solve this level

[man](https://manpages.ubuntu.com/manpages/noble/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd

## Referencias
[Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php) 