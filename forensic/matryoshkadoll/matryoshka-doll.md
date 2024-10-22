## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/2978e1270538613cd8181c7b0dabe9bd/dolls.jpg)
#### Hints
- Wait, you can hide files inside files? But how do you find them?
- Make sure to submit the flag as picoCTF{XXXXX}
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/forensic/matryoshkadoll]
└─$ ls                      
dolls.jpg  matryoshka-doll.md
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/matryoshkadoll]
└─$ unzip dolls.jpg 
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg     
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/matryoshkadoll]
└─$ cd base_images 
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/matryoshkadoll/base_images]
└─$ unzip 2_c.jpg                                                              
Archive:  2_c.jpg
warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/3_c.jpg     
                                                                                                                             
┌──(kali㉿kali)-[~/mrrobot/forensic/matryoshkadoll/base_images]
└─$ cd base_images 
                                                                                                                             
┌──(kali㉿kali)-[~/…/forensic/matryoshkadoll/base_images/base_images]
└─$ unzip 2_c.jpg
unzip:  cannot find or open 2_c.jpg, 2_c.jpg.zip or 2_c.jpg.ZIP.
                                                                                                                             
┌──(kali㉿kali)-[~/…/forensic/matryoshkadoll/base_images/base_images]
└─$ ls
3_c.jpg
                                                                                                                             
┌──(kali㉿kali)-[~/…/forensic/matryoshkadoll/base_images/base_images]
└─$ unzip 3_c.jpg 
Archive:  3_c.jpg
warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/4_c.jpg     
                                                                                                                             
┌──(kali㉿kali)-[~/…/forensic/matryoshkadoll/base_images/base_images]
└─$ cd base_images 
                                                                                                                             
┌──(kali㉿kali)-[~/…/matryoshkadoll/base_images/base_images/base_images]
└─$ unzip 4_c.jpg 
Archive:  4_c.jpg
warning [4_c.jpg]:  79578 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: flag.txt                
                                                                                                                             
┌──(kali㉿kali)-[~/…/matryoshkadoll/base_images/base_images/base_images]
└─$ ls
4_c.jpg  flag.txt
                                                                                                                             
┌──(kali㉿kali)-[~/…/matryoshkadoll/base_images/base_images/base_images]
└─$ cat flag.txt  
picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}                                                                                                                             
┌──(kali㉿kali)-[~/…/matryoshkadoll/base_images/base_images/base_images]
└─$
```

## Bandera
```css
flag: picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}
```
## Notas Adicionales


# comandos utilizados
- 

## Referencias
- 