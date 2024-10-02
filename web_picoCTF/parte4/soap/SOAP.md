## Description

The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?[Web Portal](http://saturn.picoctf.net:63109/)
#### Hints
- XML external entity Injection
## Solución

![[Pasted image 20241001233709.png]]
![[Pasted image 20241001233756.png]]
![[Pasted image 20241001233824.png]]
![[Pasted image 20241001233904.png]]
![[Pasted image 20241001233923.png]]
![[Pasted image 20241001234027.png]]
![[Pasted image 20241001234110.png]]
![[Pasted image 20241001234139.png]]

## Bandera
```css
flag: picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}
```
## Notas Adicionales
Utilizando la herramienta de *BURPSUITE* abrimos un navegador, pegamos el link de la página, ponemos la herramienta en modo interceptar y damos click en "details" de alguno de los botones de la página, en la herramienta nos aparecerá información de la intercepción y vamos a hacer la inyección de xml, usando la sección que está encerrada de la página de portswingger, lo reemplazamos como lo indica la imagen junto con las demás partes en rojo. Damos click en "forward" y regresamos a la página para observar que encontramos la bandera. Si no llégase a resultar habrá que probar con cada botón.
# comandos utilizados

## Referencias
- [portswingger](https://portswigger.net/web-security/xxe)
