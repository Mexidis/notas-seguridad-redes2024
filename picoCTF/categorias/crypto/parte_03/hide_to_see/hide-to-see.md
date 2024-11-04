## Description

How about some hide and seek heh?Look at this image [here](https://artifacts.picoctf.net/c/241/atbash.jpg).
#### Hints
- Download the image and try to extract it.
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/hide_to_see]
└─$ ls
 atbash.jpg      'Pasted image 20241103041957.png'
 encrypted.txt   'Pasted image 20241103042000.png'
 hide-to-see.md
                                                                   
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/hide_to_see]
└─$ file atbash.jpg                                    
atbash.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 465x455, components 3
                                                                   
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/hide_to_see]
└─$ steghide extract -sf atbash.jpg
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                   
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/hide_to_see]
└─$ cat encrypted.txt              
krxlXGU{zgyzhs_xizxp_7142uwv9}
                                                                   
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/hide_to_see]
└─$ 
```

![[Pasted image 20241103042000.png]]
## Bandera
```css
flag: picoCTF{atbash_crack_7142fde9}
```
## Notas Adicionales

## Referencias
- [Cyberchefsito](https://gchq.github.io/CyberChef/#recipe=Atbash_Cipher()&input=a3J4bFhHVXt6Z3l6aHNfeGl6eHBfNzE0MnV3djl9)