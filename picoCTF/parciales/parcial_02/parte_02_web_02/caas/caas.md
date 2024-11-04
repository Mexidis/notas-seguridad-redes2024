## Description

Now presenting [cowsay as a service](https://caas.mars.picoctf.net/)

| Challenge Endpoints |                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------- |
| Download index.js   | [index.js](https://artifacts.picoctf.net/picoMini+by+redpwn/Web+Exploitation/caas/index.js) |
#### Hints
-  (None)
## Solución

![[Pasted image 20241103233642.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_02_web_02/caas]
└─$ wget https://artifacts.picoctf.net/picoMini+by+redpwn/Web+Exploitation/caas/index.js
--2024-11-04 00:40:02--  https://artifacts.picoctf.net/picoMini+by+redpwn/Web+Exploitation/caas/index.js
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.100, 3.161.55.61, 3.161.55.64, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.100|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 424 [binary/octet-stream]
Saving to: ‘index.js’

index.js               100%[=========================>]     424  --.-KB/s    in 0s      

2024-11-04 00:40:03 (268 MB/s) - ‘index.js’ saved [424/424]

                                                                                         
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_02_web_02/caas]
└─$ cat index.js 
const express = require('express');
const app = express();
const { exec } = require('child_process');

app.use(express.static('public'));

app.get('/cowsay/:message', (req, res) => {
  exec(`/usr/games/cowsay ${req.params.message}`, {timeout: 5000}, (error, stdout) => {
    if (error) return res.status(500).end();
    res.type('txt').send(stdout).end();
  });
});

app.listen(3000, () => {
  console.log('listening');
});

```

![[Pasted image 20241103234542.png]]
![[Pasted image 20241103234121.png]]
![[Pasted image 20241103234134.png]]
![[Pasted image 20241103234341.png]]
![[Pasted image 20241103234435.png]]
```html
 _________
< {toron} >
 ---------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
```

## Bandera
```css
flag: picoCTF{moooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0o}
```
## Notas Adicionales

## Referencias
- 