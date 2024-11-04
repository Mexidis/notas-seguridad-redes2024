## Description

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/15796/` ([link](https://jupiter.challenges.picoctf.org/problem/15796/)) or http://jupiter.challenges.picoctf.org:15796

#### hints
- Hmm it doesn't seem to check anyone's password, except for Joe's?
## Solución
Entramos a la página y nos logeamos con cualquier nombre y contraseña
![[Pasted image 20240918192503.png]]
Después nos aparecerá esto:
![[Pasted image 20240918192538.png]]
No hay bandera pero con la siguiente herramienta podremos cambiar algunas cookies:
![[Pasted image 20240918191111.png]]
[cookie editor](https://cookie-editor.com/) 

![[Pasted image 20240918192744.png]]
Abrimos la extensión, vamos a la sección de admin, cambiamos el valor de _False_ a _True_ y guardamos. Posteriormente recargamos la página y tendremos la bandera.
![[Pasted image 20240918192945.png]]
## Bandera
```css
flag: picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
```
## Notas Adicionales
# comandos utilizados

## Referencias
-  