## Description

Using a Secure Shell (SSH) is going to be pretty important. Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `60294` to get the flag? You'll also need the password `f3b61b38`. If asked, accept the fingerprint with `yes`. If your device doesn't have a shell, you can use: [https://webshell.picoctf.org](https://webshell.picoctf.org/) If you're not sure what a shell is, check out our Primer: [https://primer.picoctf.com/#_the_shell](https://primer.picoctf.com/#_the_shell)
## Solución
```shell
┌──(kali㉿kali)-[~]
└─$ ssh ctf-player@titan.picoctf.net -p 60294
The authenticity of host '[titan.picoctf.net]:60294 ([3.139.174.234]:60294)' can't be established.
ED25519 key fingerprint is SHA256:4S9EbTSSRZm32I+cdM5TyzthpQryv5kudRP9PIKT7XQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[titan.picoctf.net]:60294' (ED25519) to the list of known hosts.
ctf-player@titan.picoctf.net's password: 

Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_3e293eea}
Connection to titan.picoctf.net closed.
                                                                                               
┌──(kali㉿kali)-[~]
└─$ 


```
## Bandera
```shell
flag: picoCTF{s3cur3_c0nn3ct10n_3e293eea}
```
## Notas Adicionales
Conexión SSH: Intentó establecer una conexión segura al servidor remoto usando el protocolo SSH (Secure Shell).

Nombre de usuario: Usó `ctf-player` como el nombre de usuario para autenticarse en el servidor.

Dirección del servidor: Se conectó al servidor con el nombre de dominio titan.picoctf.net.

Puerto personalizado: Especificó el puerto 60294 en lugar del puerto SSH por defecto (22). Esto significa que el servidor SSH en titan.picoctf.net está escuchando en el puerto 60294 para aceptar conexiones.

En resumen, el comando intentó establecer una sesión `SSH` con el servidor `titan.picoctf.net` en el puerto 60294, autenticándose con el nombre de usuario `ctf-player`.
# comandos utilizados
- 

## Referencias
- 