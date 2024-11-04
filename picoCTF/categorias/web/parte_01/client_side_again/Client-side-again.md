## Description

Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/6353/` ([link](https://jupiter.challenges.picoctf.org/problem/6353/)) or http://jupiter.challenges.picoctf.org:6353
#### hints
- What is obfuscation?
## Solución
Definición de "Obfuscation":
	La ofuscación se refiere a encubrir el significado de una comunicación haciéndola más confusa y complicada de interpretar.

Primero inspeccionamos el código y nos topamos con esa función de ``js`` por lo que vemos más a fondo de qué se trata. Está "_Ofuscado_" y tenemos que hacerlo más "nice" con [niceJS](http://jsnice.org/). Por lo tanto usamos la página que se anexa en la figura 2. Luego copiamos el arreglo de cadenas que viene en la línea dos y la pegamos en la consola de inspeccionar el código. Finalmente en la figura 3 observamos que se dedujo la bandera por las posiciones del arreglo de cadenas, haciendo combinaciones entre ellas y tenemos la bandera. 
![[Pasted image 20240918210208.png]]
Figura 1.

![[Pasted image 20240918210157.png]]
Figura 2.

![[Pasted image 20240918211113.png]]
Figura 3.
## Bandera
```css
flag: picoCTF{not_this_again_50a029}
```
## Notas Adicionales
# comandos utilizados

## Referencias
