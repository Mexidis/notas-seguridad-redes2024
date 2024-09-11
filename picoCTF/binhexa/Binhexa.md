## Objetivo

How well can you perfom basic binary operations?

Start searching for the flag here `nc titan.picoctf.net 59560`
## Solución
```shell
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF/binhexa]
└─$ nc titan.picoctf.net 59560

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 10100000
Binary Number 2: 00011000


Question 1/6:
Operation 1: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 0
Correct!

Question 2/6:
Operation 2: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 1011 1000

Incorrect input. Provide the right input
Enter the binary result: 10111000         
Correct!

Question 3/6:
Operation 3: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 111100000000
Correct!

Question 4/6:
Operation 4: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 1000100000000000
Incorrect. Try again
Enter the binary result: 1100
Correct!

Question 5/6:
Operation 5: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10111000
Correct!

Question 6/6:
Operation 6: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 101000000
Correct!

Enter the results of the last operation in hexadecimal: 140

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF/binhexa]
└─$ 


```


## Bandera
```shell
flag: picoCTF{g00d_gu355_6dcfb67c}
```
## Notas Adicionales
Nos conectamos con ssh a la dirección que viene en la descripción del problema y de ahí tendremos que adivinar introduciendo números, nos aseguran que son 1000 números y nuestra bandera se encuentra a partir de realizar una búsqueda binaria, esto es que debemos dar la mitad de 1000, y a partir de ahí nos dirá si es más grande o más chico, debemos reducir el número por mitad, siguiendo ese algoritmo no deberíamos de usar más de 10 intentos, porque así lo dicta.
# comandos utilizados
- _unzip -d_ -> **`-d`** es una opción de `unzip` que se usa para **especificar el directorio de destino** donde deseas extraer los archivos.
- Sin esta opción, los archivos se descomprimirán en el directorio actual donde ejecutas el comando.
```shell
unzip archivo.zip -d /ruta/al/directorio		
```

## Referencias
- 