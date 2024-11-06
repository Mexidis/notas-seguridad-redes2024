## Description

We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/31c9b832d036a10daeef52d8b4290ef0/rev_this). Can you reverse the flag.
#### Hints
- objdump and Gihdra are some tools that could assist with this
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ ls -la
total 25
drwxrwx--- 1 root vboxsf     0 Nov  6 12:18 .
drwxrwx--- 1 root vboxsf  4096 Nov  6 09:45 ..
-rwxrwx--- 1 root vboxsf 16856 Oct 26  2020 rev
-rwxrwx--- 1 root vboxsf    24 Oct 26  2020 rev_this
-rwxrwx--- 1 root vboxsf   447 Nov  6 09:53 reverse-cipher.md
                                                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ file rev 
rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=523d51973c11197605c76f84d4afb0fe9e59338c, not stripped
                                                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ file rev_this 
rev_this: ASCII text, with no line terminators
                                                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ ./rev           
No flag found, please make sure this is run on the server
zsh: segmentation fault  ./rev
                                                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ caat rev_this 
Command 'caat' not found, did you mean:
  command 'cat' from deb coreutils
  command 'acat' from deb atool
  command 'chat' from deb ppp
  command 'ccat' from deb ccrypt
Try: sudo apt install <deb name>
                                                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ cat rev_this 
picoCTF{w1{1wq85jc=2i0<}                                                           
```

```python
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ cat solve.py                                                   
rev = open('rev_this').read()
flag = ''

for i in range(8):
        flag += rev[i]
for j in range(8, 24):
        if j & 1 == 0:
                flag += chr(ord(rev[j]) - 5)
        else:
                flag += chr(ord(rev[j]) + 2)
flag += rev[23]
print(flag)

```

```shell
┌──(kali㉿kali)-[~/…/categorias/reversing/parte_04/reverse_cipher]
└─$ python3 solve.py                    
picoCTF{r3v3rs37ee84d27}
```

## Bandera
```css
flag: picoCTF{r3v3rs37ee84d27}
```
## Notas Adicionales

## Referencias
- 