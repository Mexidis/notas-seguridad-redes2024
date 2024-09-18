## Description
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`.
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/plumbing]
└─$ nc jupiter.challenges.picoctf.org 14291 | grep picoCTF
picoCTF{digital_plumb3r_ea8bfec7}


```
## Bandera
```shell
flag: picoCTF{digital_plumb3r_ea8bfec7}
```
## Notas Adicionales
En este proceso, se utilizó el comando `nc` (netcat) para conectarse al servidor remoto `jupiter.challenges.picoctf.org` en el puerto `14291`. Luego, la salida de esa conexión fue canalizada a través del comando `grep` para buscar y filtrar líneas que contienen la palabra `picoCTF`. Como resultado, se encontró y se mostró la bandera picoCTF: `picoCTF{digital_plumb3r_ea8bfec7}`. Este enfoque es útil para extraer rápidamente información relevante de un flujo de datos utilizando herramientas de la línea de comandos.

# comandos utilizados
-  
## Referencias
- 