## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 7449`, but it doesn't speak English...
## Solución
```shell
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/nice_netcat]
└─$ nc mercury.picoctf.net 7449             
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
102 
50 
100 
55 
99 
97 
102 
97 
125 
10 
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/nice_netcat]
└─$ nc mercury.picoctf.net 7449 > output.txt              
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/nice_netcat]
└─$ cat output.txt | tr ' ' '\n' | awk '{printf "%c", $1}'

picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
                                                                                                               
┌──(kali㉿kali)-[~/shared/notas-seguridad-redes2024/picoCTF/nice_netcat]
└─$ 
```
## Bandera
```shell
flag: picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
```
## Notas Adicionales
 Para convertir los números a texto en Linux, primero se redirigió la salida del comando `nc` a un archivo con `nc mercury.picoctf.net 7449 > output.txt`. Luego, se procesó el archivo utilizando una serie de comandos para transformar los números ASCII en caracteres. Con `tr` y `awk`, se convirtió cada número en su carácter correspondiente y se  obtuvo el texto decodificado. El texto resultante se imprimió en la terminal.
# comandos utilizados
1. **`nc mercury.picoctf.net 7449 > output.txt`**:
    - **`nc`** (netcat) es una herramienta que permite realizar conexiones de red. En este caso, se conecta al servidor `mercury.picoctf.net` en el puerto `7449`.
    - **`>`** redirige la salida del comando a un archivo. Aquí, la salida del comando `nc` se guarda en `output.txt`.
      
1. **`cat output.txt`**:
    - Muestra el contenido del archivo `output.txt` en la terminal.
      
3. **`tr ' ' '\n'`**:
    - **`tr`** (translate) es una utilidad para traducir o reemplazar caracteres. En este caso, convierte los espacios en nuevas líneas (`\n`), lo que hace que cada número ASCII esté en una línea separada.
      
4. **`awk '{printf "%c", $1}'`**:
    - **`awk`** es un lenguaje de procesamiento de textos que se usa aquí para formatear la salida. El comando `printf "%c", $1` toma cada línea (que ahora contiene un número ASCII) y lo convierte en su carácter correspondiente usando la especificación de formato `%c`.

Estos comandos en conjunto permiten transformar una lista de números ASCII en texto legible.

## Referencias
	- 