## Description

Now you DON’T see me.This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
#### Hints
- How can you be sure of the redaction?
## Solución

![[Pasted image 20241107182238.png]]

![[Pasted image 20241107182345.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/redaction_gone_wrong]
└─$ file Financial_Report_for_ABC_Labs.pdf
Financial_Report_for_ABC_Labs.pdf: PDF document, version 1.7, 1 page(s)
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/redaction_gone_wrong]
└─$ nano flag.txt          
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/redaction_gone_wrong]
└─$ cat flag.txt                      
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.

Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.

```

## Bandera
```css
flag: picoCTF{C4n_Y0u_S33_m3_fully}
```
## Notas Adicionales
Bastó con copiar lo del ``pdf`` a un ``documento de texto`` y así obtener la flag.

## Referencias
- 