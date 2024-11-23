## Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.Debug [this](https://artifacts.picoctf.net/c/520/debugger0_b).
#### Hints
- You could calculate `eax` yourself, or you could set a breakpoint for after the calculcation and inspect `eax` to let the program do the heavy-lifting for you.
## Solución

![[Pasted image 20241122211331.png]]
![[Pasted image 20241122211430.png]]

## Bandera
```css
flag: picoCTF{307019}
```
## Notas Adicionales

## Referencias
- 