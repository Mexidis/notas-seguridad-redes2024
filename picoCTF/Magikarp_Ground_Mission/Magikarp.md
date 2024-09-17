## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`

**ssh** ctf-player@venus.picoctf.net -p 49324
## Solución
```shell
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt 

picoCTF{xxsh_

ctf-player@pico-chall$ cat instructions-to-2of3.txt 
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  boot  etc   instructions-to-3of3.txt  lib64  mnt  proc  run   srv  tmp  var
bin            dev   home  lib                       media  opt  root  sbin  sys  usr
ctf-player@pico-chall$ cat 2of3.flag.txt 

0ut_0f_\/\/4t3r_

ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd
ctf-player@pico-chall$ ls
3of3.flag.txt  concatenado.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt 

3ca613a1}

ctf-player@pico-chall$ 

```
## Bandera
```shell
flag: picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}
```
## Notas Adicionales
Se estableció una conexión por ``ssh`` a otra máquina y se tuvo que navegar entre directorios y concatenar los archivos que tenían dentro para formar la bandera.
# comandos utilizados
- 

## Referencias
	- 