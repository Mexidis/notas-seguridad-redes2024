## Description

Unzip this archive and find the file named 'uber-secret.txt'

- [Download zip file](https://artifacts.picoctf.net/c/500/files.zip)
## Solución
```shell
┌──(kali㉿kali)-[~/pruebas-seguridad/files]
└─$ ls
13771.txt.utf-8  14789.txt.utf-8  acceptable_books  adequate_books  satisfactory_books
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/files]
└─$ grep -r "picoCTF{"                                             
adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:picoCTF{f1nd_15_f457_ab443fd1}
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/files]
└─$ 

```
## Bandera
```shell
flag: picoCTF{f1nd_15_f457_ab443fd1}
```
## Notas Adicionales
Para resolver este reto bastó con descomprimir el archivo files.zip, e inmediatamente vemos que hay dos archivos de texto y dos directorios y subdirectorios con más archivos de texto, para ello utilizamos el comando ``grep -r "picoCTF{"`` en busca de la bandera
# comandos utilizados
- El comando `grep -r "cadena"` busca de manera recursiva la cadena de texto en las comillas dentro de todos los archivos en el directorio actual y sus subdirectorios. Aquí está el desglose:
- `grep` es una utilidad de línea de comandos que busca patrones en archivos de texto.
- `-r` o `--recursive` indica que la búsqueda debe ser recursiva, es decir, que se debe buscar en todos los subdirectorios también.

## Referencias
- 