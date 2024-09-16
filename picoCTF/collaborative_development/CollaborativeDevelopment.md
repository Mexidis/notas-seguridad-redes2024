## Description

My team has been working very hard on new features for our flag printing program! I wonder how they'll work together? You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/179/challenge.zip)
## Solución
```shell
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git branch -a    
  feature/part-1
  feature/part-2
  feature/part-3
* main
                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ ls           
flag.py
                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat flag.py
print("Printing the flag...")
                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git checkout feature/part-1
Switched to branch 'feature/part-1'
                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat flag.py
print("Printing the flag...")

print("picoCTF{t3@mw0rk_", end='')      
                                                                        
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git checkout feature/part-2
Switched to branch 'feature/part-2'
                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat flag.py                
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ git checkout feature/part-3
Switched to branch 'feature/part-3'
                                                                             
┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ cat flag.py                
print("Printing the flag...")

print("w0rk_798f9981}")

┌──(kali㉿kali)-[~/pruebas-seguridad/drop-in]
└─$ 


```
## Bandera
```shell
flag: picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_798f9981}
```
## Notas Adicionales
Primero descomprimimos el archivo zip y vemos que tiene un repositorio de git, revisamos su contenido, y vemos que no tiene aparece nada relevante, pero si revisamos las ramas existentes y vemos el contenido de cada una de ellas damos con la respuesta 
# comandos utilizados
- `git branch -a` muestra **todas las ramas** del repositorio Git, tanto locales como remotas.
- `git checkout` se utiliza principalmente para cambiar entre ramas en un repositorio Git. También tiene otros usos, pero su propósito principal es cambiar a una rama específica o a un commit.
- `cat` en Unix/Linux es una herramienta que se utiliza para:
	1. **Mostrar el contenido de archivos** en la terminal.
	2. **Concatenar archivos** (mostrar múltiples archivos uno tras otro).
	3. **Crear archivos de texto**.

## Referencias
- 
