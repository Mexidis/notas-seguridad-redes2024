## Description

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:45028/](http://mercury.picoctf.net:45028/)

### Hints
- Maybe you have more than 2 choices
- Check out tools like Burpsuite to modify your requests and look at the responses
## Solución
### Solución navegador
Entramos al link y aparece esto:
![[Pasted image 20240925102546.png]] 

Inspeccionamos el código fuente y en el apartado de RED:
![[Pasted image 20240925103026.png]]
```shell



```

![[Pasted image 20240925103236.png]]
![[Pasted image 20240925103257.png]]

### Solución Términal
``` shell
┌──(kali㉿kali)-[~]
└─$ curl -X HEAD http://mercury.picoctf.net:45028/index.php                                            
Warning: Setting custom HTTP method to HEAD with -X/--request may not work the way you want. Consider using -I/--head 
Warning: instead.

┌──(kali㉿kali)-[~]
└─$ curl -I  http://mercury.picoctf.net:45028/index.php
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_775f2530}
Content-type: text/html; charset=UTF-8

                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 

```

### Solución Burp
## Bandera
```css
flag: picoCTF{r3j3ct_th3_du4l1ty_775f2530}
```
## Notas Adicionales

# comandos utilizados

## Referencias
