## Description

Can you find the robots? `https://jupiter.challenges.picoctf.org/problem/60915/` ([link](https://jupiter.challenges.picoctf.org/problem/60915/)) or http://jupiter.challenges.picoctf.org:60915

#### hints
- What part of the website could tell you where the creator doesn't want you to look?

## Solución
![[Pasted image 20240918183949.png]]
- Agregamos ``robots.txt`` al final de la liga que nos proporcionan para tener acceso al archivo en cuestión. Obtenemos lo siguiente:
```txt
User-agent: *
Disallow: /8028f.html
```
- copiamos la parte después de la barra y lo pegamos ahora en vez de ``robots.txt`` en el link.
![[Pasted image 20240918184131.png]]
- Nos lleva a una página oculta con la bandera.

## Bandera
```css
flag: picoCTF{ca1cu1at1ng_Mach1n3s_8028f}
```
## Notas Adicionales
# comandos utilizados

## Referencias
-  [robots.txt](https://en.wikipedia.org/wiki/Robots.txt)