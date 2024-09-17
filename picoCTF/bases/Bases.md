## Description

What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.
## Solución
```shell
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ touch file.txt
                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ nano file.txt 
  GNU nano 8.1                                file.txt                                         
bDNhcm5fdGgzX3IwcDM1


                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ base64 -d file.txt            
l3arn_th3_r0p35                                                                                               
┌──(kali㉿kali)-[~/pruebas-seguridad]
└─$ 
```
## Bandera
```shell
flag: picoCTF{l3arn_th3_r0p35}
```
## Notas Adicionales
Este reto se resolvió guardando el texto que nos proporcionan en el reto y guardarlo en un archivo de texto, para después decodificarlo con ``base64`` y obtenemos la respuesta.
# comandos utilizados
- `base64 -d` se utiliza para **decodificar** datos que han sido codificados en formato base64. La opción `-d` o `--decode` le indica al comando `base64` que realice una decodificación, es decir, que convierta los datos base64 de vuelta a su formato original.
## Referencias
- 