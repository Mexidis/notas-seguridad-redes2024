## Description

I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/c9593d1d2ac9d850da95bffe0ac3b6c6/scrambled2.png)
#### Hints
- [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
- Think of different ways you can "stack" images
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/pixelated]
└─$ ls
pixelated.md  scrambled1.png  scrambled2.png
                                                                        
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/pixelated]
└─$ touch exploit.py 
                                                                        
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/pixelated]
└─$ cat exploit.py   
from PIL import Image
img1 = Image.open("scrambled1.png")
pixels1 = img1.load()
img2 = Image.open("scrambled2.png")
pixels2 = img2.load()

flag = Image.new("RGB", img1.size)
flagpix = flag.load()
for row in range(img1.size[1]):
    for col in range(img1.size[0]):
        flagpix[col,row] = (
            (pixels1[col,row][0] + pixels2[col,row][0]) % 256,
            (pixels1[col,row][1] + pixels2[col,row][1]) % 256,
            (pixels1[col,row][2] + pixels2[col,row][2]) % 256
        )
flag.save("flag.png")
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/pixelated]
└─$ python3 exploit.py  
                                                                        
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/pixelated]
└─$ ls
exploit.py  flag.png  pixelated.md  scrambled1.png  scrambled2.png
                                                                        
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/pixelated]
└─$ open flag.png &  
[1] 39549
```
![[Pasted image 20241103050638.png]]

## Bandera
```css
flag: picoCTF{da8fcef8}
```
## Notas Adicionales

## Referencias
- 