## Description

This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/50522/` ([link](https://jupiter.challenges.picoctf.org/problem/50522/)) or http://jupiter.challenges.picoctf.org:50522

#### hints
- You don't need to download a new web browser
## Solución
Para resolver este reto se tiene que hacer en un navegador _firefox_. Damos clic derecho, inspeccionar, nos pasamos al apartador de red, luego damos clic en flag y nos aparecerán esos encabezados, nos vamos al que está encerrado en rojo. Después damos clic en reenviar y buscamos el apartado de _User-Agent_ y cambiamos lo que tenga por "_picobrowser_". Finalmente damos clic en el apartado de respuesta y tendremos la bandera
![[Pasted image 20240918204759.png]]
![[Pasted image 20240918204940.png]]
![[Pasted image 20240918205200.png]]

## Bandera
```css
flag: picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}
```
## Notas Adicionales
# comandos utilizados

## Referencias
