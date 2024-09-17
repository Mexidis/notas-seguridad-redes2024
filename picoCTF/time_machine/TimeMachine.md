## Description

What was I last working on? I remember writing a note to help me remember... You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/163/challenge.zip)
## Solución
```shell
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ ls
message.txt
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat message.txt
This is what I was working on, but I'd need to look at my commit history to know why...                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git log             
commit e65fedb3a72a16c577f4b17023b63997134b307d (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:29 2024 +0000

    picoCTF{t1m3m@ch1n3_88c35e3b}
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$
```
## Bandera
```shell
flag: picoCTF{t1m3m@ch1n3_88c35e3b}
```
## Notas Adicionales
Únicamente se tuvo que revisar el historial de commits para revisar si había algún comentario que pudiera ayudarnos, en este caso el comentario del único commit fue la bandera.

# comandos utilizados
-  `git log` muestra el historial de commits en el repositorio de Git. Por defecto, presenta una lista de los commits realizados, ordenados desde el más reciente al más antiguo. Aquí está lo que generalmente incluye `git log`:

	- **Hash del commit**: Un identificador único para cada commit.
	- **Autor**: El nombre y correo electrónico del autor del commit.
	- **Fecha**: La fecha y hora en que se realizó el commit.
	- **Mensaje de commit**: La descripción del commit proporcionada por el autor.

## Referencias
- 