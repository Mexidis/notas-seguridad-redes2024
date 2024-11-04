## Description

How about we take you on an adventure on exploring certificate signing requestsTake a look at this CSR file [here](https://artifacts.picoctf.net/c/423/readmycert.csr).
#### Hints
- Download the certificate signing request and try to read it.
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/read_my_cert]
└─$ cat readmycert.csr 
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF81N2Y1
ODgzMn0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBANZde4bKP/88bBY0RM2b+EyGoxWqWsADa7QIPRZM4jTAxPTC39Ld
6iDZwfA6Cu33KvkZbu1JpAFk/6O/lY+iwSCcZnBTp1p+Skn/BpIwW7KBEjnczulA
c/u4GYQgpU5Pxxd/gvOHLNtWHw8FjcHAV78Y23cwwfO1Gfae5eYrxHMa/nCiQmjC
9GwRsj2+cPmWiyFs1ntLREBGUKWBIHGoTR+ZMXv9aBeasIUlzWap/4ZsSOqoqzAL
3geZ9TfWd/pHtYgqA1jV60ogmWD2LKMU9F4s+5dJveO/5kV7kkpk+7VX3xlE1t/S
0/ThtcNU51WdfmFREr2hCUJgicQHbkkwq00CAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAHihiiyg
z69vMceQR0gOoTZS1RQKafdyX64IxwEuHdV8I0To+3VQp+3yp2yHNAjLxLEIam6f
4dlTZlWSSttHSjp1WjoabpQrSp7ANgTuLFwBsQkbXY72wm0LVrdSi1tuKTnl82vM
mXccuWLUXy71wmzKR+Wekf5JXX9AwFAEVedyAW5EP+bNOP/hQr1kiOCWge3pmGUq
9fVYITJs6gZ6aiDwx4O2jdJuP3CG1QRrKer89mgw5GkgvcVn38s7BF24kRddcBK1
RGSntFXy1CDUd55IhSoADxrZoXT5+5+GokM85JKTkwS9L/VGe2ZQuym+NyIkbfBm
I+FejxNz7x4Fmzg=
-----END CERTIFICATE REQUEST-----
                                                                        
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/read_my_cert]
└─$ vi readmycert.csr 
                                                                              
┌──(kali㉿kali)-[~/…/categorias/crypto/parte_03/read_my_cert]
└─$ base64 -d readmycert.csr
0��0��0<1&0$U
             picoCTF{read_mycert_57f58832}10U)
�0�     *�H��                                   ctfPlayer0�"0
��]{��?�<l4D�L���Z�k=L�4�������� ���:
��*�n�I�d������� �fpS�Z~JI��0[��9���@s��� �NO����,�V���W�▒�w0�������+�s▒�p�Bh��l�=�p���!l�{KD@FP�� q�M�1{�h���%�f���lH0
                                               ���7�w�G��*X��J �`�,��^,��I����E{100U%W�D��������T�U�~aQ��       B`��nI0�M�&0$   *�H��
             0
+0      *�H��
�x��,�ϯo1ǐGH�6R�
i�r_�.�|#D��uP����l��jn���SfU�J�GJ:uZ:▒n�+J��6�,\�
```

![[Pasted image 20241103051236.png]]
## Bandera
```css
flag: picoCTF{read_mycert_57f58832}
```
## Notas Adicionales
Para poder hacerlo desde terminal bastó con quitar el encabezado de `BEGIN CERTIFICATE REQUEST` y  `END CERTIFICATE` para luego mandar a desencriptar con `base64` y finalmente obtener la bandera.
## Referencias
-  [crs-decoder](https://www.sslshopper.com/csr-decoder.html)