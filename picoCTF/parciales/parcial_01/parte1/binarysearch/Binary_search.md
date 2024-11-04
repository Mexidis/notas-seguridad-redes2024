## Objetivo

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses. Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools! You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/17/challenge.zip)

`ssh -p 49818 ctf-player@atlas.picoctf.net` Using the password `f3b61b38`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

## Solución
```shell
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip challenge.zip -d ../mrrobot/notas-seguridad-redes2024/picoCTF/binarysearch 
Archive:  challenge.zip
   creating: ../mrrobot/notas-seguridad-redes2024/picoCTF/binarysearch/home/ctf-player/drop-in/
  inflating: ../mrrobot/notas-seguridad-redes2024/picoCTF/binarysearch/home/ctf-player/drop-in/guessing_game.sh  

┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF/binarysearch]
└─$ ssh -p 49818 ctf-player@atlas.picoctf.net
The authenticity of host '[atlas.picoctf.net]:49818 ([18.217.83.136]:49818)' can't be established.
ED25519 key fingerprint is SHA256:M8hXanE8l/Yzfs8iuxNsuFL4vCzCKEIlM/3hpO13tfQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[atlas.picoctf.net]:49818' (ED25519) to the list of known hosts.
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 375
Higher! Try again.
Enter your guess: 420
Higher! Try again.
Enter your guess: 480
Higher! Try again.
Enter your guess: 490
Higher! Try again.
Enter your guess: 495
Congratulations! You guessed the correct number: 495
Here's your flag: picoCTF{g00d_gu355_6dcfb67c}
Connection to atlas.picoctf.net closed.
                                                                                                                       
┌──(kali㉿kali)-[~/mrrobot/notas-seguridad-redes2024/picoCTF/binarysearch]
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