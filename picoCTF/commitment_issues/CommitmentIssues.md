## Description

I accidentally wrote the flag down. Good thing I deleted it! You download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/138/challenge.zip)
## Solución
```shell
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ ls -la
total 16
drwxr-xr-x 3 kali kali 4096 Mar 11  2024 .
drwxrwxr-x 3 kali kali 4096 Sep 16 19:15 ..
drwxr-xr-x 8 kali kali 4096 Mar 11  2024 .git
-rw-r--r-- 1 kali kali   11 Mar 11  2024 message.txt
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat message.txt 
TOP SECRET
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git reflog                                           
42942c9 (HEAD -> master) HEAD@{0}: commit: remove sensitive info
b562f0b HEAD@{1}: commit (initial): create flag
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git checkout b562f0b                                 
Note: switching to 'b562f0b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at b562f0b create flag
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ ls    
message.txt
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat message.txt
picoCTF{s@n1t1z3_c785c319}
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ 
```
## Bandera
```shell
flag: picoCTF{s@n1t1z3_c785c319}
```
## Notas Adicionales
Primero descomprimimos el archivo zip y , revisamos su contenido, y vemos que no tiene aparece nada relevante, pero si revisamos los commits existentes y vemos el contenido de commit entonces encontramos la bandera. 
# comandos utilizados
- `git reflog` es una herramienta poderosa que te permite ver el **historial de referencias** de los cambios en tu repositorio. Git rastrea todos los movimientos de las referencias (como `HEAD`, ramas, `stash`, etc.), y el comando `reflog` te muestra todos los commits recientes, incluso aquellos que podrían no estar accesibles por las ramas normales.
- `git checkout <nombre del commit>` te permite moverte a un commit específico en tu historial de Git. Esto te coloca en un **estado "detached HEAD"**, lo que significa que te estás moviendo a ese commit en particular sin estar en ninguna rama.

## Referencias
- 