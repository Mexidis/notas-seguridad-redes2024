## Description

BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book!Here are the credentials to get you started:

- Username: "user"
- Password: "user"

Source code can be downloaded [here](https://artifacts.picoctf.net/c/480/bookshelf-pico.zip).Website can be accessed [here!](http://saturn.picoctf.net:59090/).
#### Hints
- Maybe try to find the JWT Signing Key ("secret key") in the source code? Maybe it's hardcoded somewhere? Or maybe try to crack it?
- The 'role' and 'userId' fields in the JWT can be of interest to you!
- The 'controllers', 'services' and 'security' java packages in the given source code might need your attention. We've provided a README.md file that contains some documentation.
- Upgrade your 'role' with the _new_ (cracked) JWT. And re-login for the new role to get reflected in browser's localStorage.
## Solución

![[Pasted image 20241104000319.png]]
![[Pasted image 20241104000335.png]]
![[Pasted image 20241104000413.png]]
![[Pasted image 20241104000431.png]]
![[Pasted image 20241104000542.png]]
![[Pasted image 20241104000731.png]]
![[Pasted image 20241104000836.png]]
![[Pasted image 20241104000915.png]]
![[Pasted image 20241104001131.png]]
Pegamos la nueva `key JWT` en el `value` de ``auth-token``
![[Pasted image 20241104001205.png]]
![[Pasted image 20241104001341.png]]
![[Pasted image 20241104001420.png]]
![[Pasted image 20241104001713.png]]
![[Pasted image 20241104001658.png]]
Cambiamos el `userId` a `2` y ahora pegamos la nueva key. Refresh a la página y despues:
![[Pasted image 20241104002033.png]]

## Bandera
```css
flag: picoCTF{w34k_jwt_n0t_g00d_7745dc02}
```
## Notas Adicionales

## Referencias
- 