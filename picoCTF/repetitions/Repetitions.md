## Description

Can you make sense of this file? Download the file [here](https://artifacts.picoctf.net/c/476/enc_flag).
## Solución
```shell
┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag 
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKVVZXMTRWMDVHV2toalJYUlhDazFyV25sVVZXaHpWakpHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ base64 -d enc_flag       
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JUVW14V05GWkhjRXRXCk1rWnlUVWhzVjJGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
                                                                               
┌──(kali㉿kali)-[~/Downloads]
└─$ base64 -d enc_flag | base64 -d                      
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BTUmxWNFZHcEtW
MkZyTUhsV2FteEVXbm93T1VOblBUMEsK
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ base64 -d enc_flag | base64 -d | base64 -d          
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
WGRrTWpWelRVUlNhMDB5VW1aTwpSRlV4VGpKV2FrMHlWamxEWnowOUNnPT0K
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ base64 -d enc_flag | base64 -d | base64 -d | base64 -d
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZO
RFUxTjJWak0yVjlDZz09Cg==
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNDU1N2VjM2V9Cg==
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}
                                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$

```
## Bandera
```shell
flag: picoCTF{picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}}
```
## Notas Adicionales
Se está aplicando la decodificación base64 cinco veces consecutivas al contenido de `enc_flag`. Aquí está lo que ocurre paso a paso:

1. `base64 -d enc_flag` decodifica el contenido del archivo `enc_flag` de base64 a su forma original.
2. La salida de esa primera decodificación se pasa a través del siguiente `base64 -d`, decodificándola nuevamente.
3. Este proceso se repite cinco veces, cada vez decodificando el contenido que resulta de la decodificación anterior.

Esto es útil si el contenido fue codificado en base64 varias veces de manera anidada. Cada aplicación de `base64 -d` revierte una capa de codificación base64.:
# comandos utilizados
- `base64 -d "nombre del archivo"` decodifica una cadena o archivo que ha sido codificado en base64, devolviendo su contenido original.

## Referencias
- 