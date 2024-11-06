## Description

Someone might have hidden the password in the trace file.Find the key to unlock [this file](https://artifacts.picoctf.net/c/496/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/496/dump.pcap) might be good to analyze.
#### Hints
- Download the pcap and look for the password or flag.
- Don't try to use a password cracking tool, there are easier ways here.
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ wget https://artifacts.picoctf.net/c/496/flag.zip        
--2024-11-06 01:23:29--  https://artifacts.picoctf.net/c/496/flag.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.64, 3.161.55.26, 3.161.55.61, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.64|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 231 [application/octet-stream]
Saving to: ‘flag.zip’

flag.zip               100%[===========================>]     231  --.-KB/s    in 0s      

2024-11-06 01:23:30 (113 MB/s) - ‘flag.zip’ saved [231/231]

                                                                                           
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ wget https://artifacts.picoctf.net/c/496/dump.pcap
--2024-11-06 01:23:38--  https://artifacts.picoctf.net/c/496/dump.pcap
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.100, 3.161.55.61, 3.161.55.26, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.100|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7413 (7.2K) [application/octet-stream]
Saving to: ‘dump.pcap’

dump.pcap              100%[===========================>]   7.24K  --.-KB/s    in 0.001s  

2024-11-06 01:23:39 (4.96 MB/s) - ‘dump.pcap’ saved [7413/7413]

                                                                                           
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ ls
dump.pcap  find-and-open.md  flag.zip
                                                                                           
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ wireshark dump.pcap &                             
[1] 44330
                                                                                           
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ unzip flag.zip                          
Archive:  flag.zip
[flag.zip] flag password:
```

![[Pasted image 20241106002717.png]]
![[Pasted image 20241106002739.png]]
![[Pasted image 20241106002800.png]]
Al inspeccionar los paquetes encontramos algunas referencias, que pudieran darnos la clave para descomprimir el ``.zip`` se observan cadenas que pudieran estar en ``base64``.
![[Pasted image 20241106003232.png]]
![[Pasted image 20241106004008.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ unzip flag.zip                          
Archive:  flag.zip
[flag.zip] flag password: picoCTF{R34DING_LOKd_
 extracting: flag                    
                                                                                           
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_03_forensic_01/find_and_open]
└─$ cat flag 
picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}

```
## Bandera
```css
flag: picoCTF{R34DING_LOKd_fil56_succ3ss_5ed3a878}
```
## Notas Adicionales

## Referencias
- 