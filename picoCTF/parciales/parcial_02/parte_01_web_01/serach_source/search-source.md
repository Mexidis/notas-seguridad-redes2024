## Description

The developer of this website mistakenly left an important artifact in the website source, can you find it?The website is [here](http://saturn.picoctf.net:63939/)
#### Hints
- How could you mirror the website on your local machine so you could use more powerful tools for searching?
## Solución

![[Pasted image 20241103191805.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_01_web_01/serach_source]
└─$ wget -r -nH --cut-dirs=1 -P ./saturn_site http://saturn.picoctf.net:63939/
--2024-11-03 20:29:27--  http://saturn.picoctf.net:63939/
Resolving saturn.picoctf.net (saturn.picoctf.net)... 13.59.203.175
Connecting to saturn.picoctf.net (saturn.picoctf.net)|13.59.203.175|:63939... connected.
HTTP request sent, awaiting response... 200 OK
Length: 15920 (16K) [text/html]
Saving to: ‘./saturn_site/index.html’

index.html             100%[=========================>]  15.55K  --.-KB/s    in 0.09s   

2024-11-03 20:29:28 (172 KB/s) - ‘./saturn_site/index.html’ saved [15920/15920]

Loading robots.txt; please ignore errors.
--2024-11-03 20:29:28--  http://saturn.picoctf.net:63939/robots.txt
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 404 Not Found
2024-11-03 20:29:28 ERROR 404: Not Found.

--2024-11-03 20:29:28--  http://saturn.picoctf.net:63939/css/bootstrap.min.css
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 140421 (137K) [text/css]
Saving to: ‘./saturn_site/bootstrap.min.css’

bootstrap.min.css      100%[=========================>] 137.13K   711KB/s    in 0.2s    

2024-11-03 20:29:28 (711 KB/s) - ‘./saturn_site/bootstrap.min.css’ saved [140421/140421]

--2024-11-03 20:29:28--  http://saturn.picoctf.net:63939/css/owl.carousel.min.css
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 3351 (3.3K) [text/css]
Saving to: ‘./saturn_site/owl.carousel.min.css’

owl.carousel.min.css   100%[=========================>]   3.27K  --.-KB/s    in 0s      

2024-11-03 20:29:28 (105 MB/s) - ‘./saturn_site/owl.carousel.min.css’ saved [3351/3351]

--2024-11-03 20:29:28--  http://saturn.picoctf.net:63939/css/style.css
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 10449 (10K) [text/css]
Saving to: ‘./saturn_site/style.css’

style.css              100%[=========================>]  10.20K  --.-KB/s    in 0s      

2024-11-03 20:29:28 (283 MB/s) - ‘./saturn_site/style.css’ saved [10449/10449]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/css/responsive.css
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 8660 (8.5K) [text/css]
Saving to: ‘./saturn_site/responsive.css’

responsive.css         100%[=========================>]   8.46K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (234 MB/s) - ‘./saturn_site/responsive.css’ saved [8660/8660]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/loading.gif
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 35499 (35K) [image/gif]
Saving to: ‘./saturn_site/loading.gif’

loading.gif            100%[=========================>]  34.67K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (1.79 GB/s) - ‘./saturn_site/loading.gif’ saved [35499/35499]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/mail_icon.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 1717 (1.7K) [image/png]
Saving to: ‘./saturn_site/mail_icon.png’

mail_icon.png          100%[=========================>]   1.68K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (148 MB/s) - ‘./saturn_site/mail_icon.png’ saved [1717/1717]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/index.html
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 15920 (16K) [text/html]
Saving to: ‘./saturn_site/index.html’

index.html             100%[=========================>]  15.55K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (382 MB/s) - ‘./saturn_site/index.html’ saved [15920/15920]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/logo.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 5009 (4.9K) [image/png]
Saving to: ‘./saturn_site/logo.png’

logo.png               100%[=========================>]   4.89K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (214 MB/s) - ‘./saturn_site/logo.png’ saved [5009/5009]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/phone_icon.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 2277 (2.2K) [image/png]
Saving to: ‘./saturn_site/phone_icon.png’

phone_icon.png         100%[=========================>]   2.22K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (150 MB/s) - ‘./saturn_site/phone_icon.png’ saved [2277/2277]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/banner.jpg
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 62595 (61K) [image/jpeg]
Saving to: ‘./saturn_site/banner.jpg’

banner.jpg             100%[=========================>]  61.13K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (516 MB/s) - ‘./saturn_site/banner.jpg’ saved [62595/62595]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/1.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 23667 (23K) [image/png]
Saving to: ‘./saturn_site/1.png’

1.png                  100%[=========================>]  23.11K  --.-KB/s    in 0s      

2024-11-03 20:29:29 (576 MB/s) - ‘./saturn_site/1.png’ saved [23667/23667]

--2024-11-03 20:29:29--  http://saturn.picoctf.net:63939/images/2.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 23992 (23K) [image/png]
Saving to: ‘./saturn_site/2.png’

2.png                  100%[=========================>]  23.43K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (1.47 GB/s) - ‘./saturn_site/2.png’ saved [23992/23992]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/images/3.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 50839 (50K) [image/png]
Saving to: ‘./saturn_site/3.png’

3.png                  100%[=========================>]  49.65K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (1.15 GB/s) - ‘./saturn_site/3.png’ saved [50839/50839]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/jquery.min.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 87088 (85K) [application/javascript]
Saving to: ‘./saturn_site/jquery.min.js’

jquery.min.js          100%[=========================>]  85.05K  --.-KB/s    in 0.02s   

2024-11-03 20:29:30 (4.29 MB/s) - ‘./saturn_site/jquery.min.js’ saved [87088/87088]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/popper.min.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 19190 (19K) [application/javascript]
Saving to: ‘./saturn_site/popper.min.js’

popper.min.js          100%[=========================>]  18.74K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (1.54 GB/s) - ‘./saturn_site/popper.min.js’ saved [19190/19190]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/bootstrap.bundle.min.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 70808 (69K) [application/javascript]
Saving to: ‘./saturn_site/bootstrap.bundle.min.js’

bootstrap.bundle.min.j 100%[=========================>]  69.15K  --.-KB/s    in 0.005s  

2024-11-03 20:29:30 (13.7 MB/s) - ‘./saturn_site/bootstrap.bundle.min.js’ saved [70808/70808]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/owl.carousel.min.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 44342 (43K) [application/javascript]
Saving to: ‘./saturn_site/owl.carousel.min.js’

owl.carousel.min.js    100%[=========================>]  43.30K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (1.11 GB/s) - ‘./saturn_site/owl.carousel.min.js’ saved [44342/44342]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/custom.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 7781 (7.6K) [application/javascript]
Saving to: ‘./saturn_site/custom.js’

custom.js              100%[=========================>]   7.60K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (486 MB/s) - ‘./saturn_site/custom.js’ saved [7781/7781]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/jquery.mCustomScrollbar.concat.min.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 45479 (44K) [application/javascript]
Saving to: ‘./saturn_site/jquery.mCustomScrollbar.concat.min.js’

jquery.mCustomScrollba 100%[=========================>]  44.41K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (2.75 GB/s) - ‘./saturn_site/jquery.mCustomScrollbar.concat.min.js’ saved [45479/45479]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/js/jquery-3.0.0.min.js
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 200 OK
Length: 11324 (11K) [application/javascript]
Saving to: ‘./saturn_site/jquery-3.0.0.min.js’

jquery-3.0.0.min.js    100%[=========================>]  11.06K  --.-KB/s    in 0s      

2024-11-03 20:29:30 (966 MB/s) - ‘./saturn_site/jquery-3.0.0.min.js’ saved [11324/11324]

--2024-11-03 20:29:30--  http://saturn.picoctf.net:63939/css/owl.video.play.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 404 Not Found
2024-11-03 20:29:31 ERROR 404: Not Found.

--2024-11-03 20:29:31--  http://saturn.picoctf.net:63939/images/fevicon.png
Reusing existing connection to saturn.picoctf.net:63939.
HTTP request sent, awaiting response... 404 Not Found
2024-11-03 20:29:31 ERROR 404: Not Found.

FINISHED --2024-11-03 20:29:31--
Total wall clock time: 3.2s
Downloaded: 21 files, 670K in 0.3s (2.12 MB/s)
                                                                                         
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_01_web_01/serach_source]
└─$ ls
'Pasted image 20241103191805.png'   saturn_site   search-source.md
                                                                                         
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_01_web_01/serach_source]
└─$ grep -R pico saturn_site 
saturn_site/style.css:/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49} **/
```

## Bandera
```css
flag: picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49}
```
## Notas Adicionales

En este comando, se utilizó `wget` con las opciones `-r -nH --cut-dirs=1 -P ./saturn_site` para descargar recursivamente todo el contenido de la página `http://saturn.picoctf.net:63939/` y almacenarlo en el directorio local `saturn_site`, ignorando el directorio superior en la estructura de URLs para simplificar la organización. Después de descargar los archivos, el comando `grep -R pico saturn_site` se ejecutó para buscar cualquier mención de la palabra "pico" dentro de los archivos descargados, lo cual reveló la bandera `picoCTF{1nsp3ti0n_0f_w3bpag3s_ec95fa49}` en el archivo `style.css`.
## Referencias
- 