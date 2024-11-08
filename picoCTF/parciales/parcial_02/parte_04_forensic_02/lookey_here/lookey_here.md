## Description

Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.Download the data [here](https://artifacts.picoctf.net/c/125/anthem.flag.txt).
#### Hints
- Download the file and search for the flag based on the known prefix.
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/lookey_here]
└─$ cat anthem.flag.txt | grep picoCTF
      we think that the men of picoCTF{gr3p_15_@w3s0m3_58f5c024}
```

## Bandera
```css
flag: picoCTF{gr3p_15_@w3s0m3_58f5c024}
```
## Notas Adicionales

## Referencias
- 