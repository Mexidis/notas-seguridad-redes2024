## Objetivo

Unzip this archive and find the flag.

## Solución
```shell
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip big-zip-files.zip -d /home/kali/mrrobot/notas-seguridad-redes2024/picoCTF/bigzip 
Archive:  big-zip-files.zip
			   
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF]
└─$ mkdir bigzip 
                                                                                                                       
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF]
└─$ grep -r "picoCTF{" bigzip 
^C
                                                                                                                       
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF]
└─$ grep -r "picoCTF{" bigzip
bigzip/big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
                                                                                                                       
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF]
└─$ 

```

## Notas Adicionales
Primero se tuvo que descomprimir el archivo zip en un directorio y posteriormente buscar la flag en el directorio y subdirectorios.

# comandos utilizados
- _unzip -d_ -> **`-d`** es una opción de `unzip` que se usa para **especificar el directorio de destino** donde deseas extraer los archivos.
- Sin esta opción, los archivos se descomprimirán en el directorio actual donde ejecutas el comando.
```shell
unzip archivo.zip -d /ruta/al/directorio		
```
- _grep -r_ -> **`-r`** es una opción de `grep` que habilita la **búsqueda recursiva**. Esto significa que `grep` buscará en **todos los archivos y subdirectorios** dentro del directorio especificado.
- Sin esta opción, `grep` solo buscaría en los archivos del directorio actual, sin descender en subdirectorios.
```shell
grep -r "picoCTF{" /ruta/al/directorio
```

## Referencias
- 
