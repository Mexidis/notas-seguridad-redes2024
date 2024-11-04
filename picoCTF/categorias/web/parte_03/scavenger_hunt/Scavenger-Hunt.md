## Description

There is some interesting information hidden around this site [http://mercury.picoctf.net:5080/](http://mercury.picoctf.net:5080/). Can you find it?

### Hints
- You should have enough hints to find the files, don't run a brute forcer.
## Solución
Hay que entrar a varios apartados de la página, a continuación se muestran capturas de pantalla de cómo se obtuvieron:
1. ![[Pasted image 20240926164816.png]]
2. ![[Pasted image 20240926164854.png]]
3. ![[Pasted image 20240926164934.png]]
4. ![[Pasted image 20240926165006.png]]
5. ![[Pasted image 20240926165020.png]]
6. ![[Pasted image 20240926165030.png]]

## Bandera
```css
flag: picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}
```
## Notas Adicionales
1. `robots.txt` es un archivo de texto que se coloca en la raíz de un sitio web para indicar a los rastreadores web (como los bots de motores de búsqueda) qué páginas o secciones del sitio deben o no deben ser rastreadas o indexadas. Es parte del **Protocolo de Exclusión de Robots** y ayuda a los administradores web a controlar la visibilidad de su contenido en los motores de búsqueda.
2. El archivo `.htaccess` es un archivo de configuración que utilizan los servidores web Apache para definir reglas y directivas de cómo debe comportarse el servidor web en determinadas situaciones. Estas reglas afectan a la carpeta en la que se coloca el archivo `.htaccess` y a todas las subcarpetas dentro de esa misma estructura.
3. El archivo `.DS_Store` (Desktop Services Store) es un archivo oculto creado automáticamente por macOS en las carpetas que se navegan a través del Finder. Su propósito es almacenar metadatos y configuraciones de visualización de la carpeta, como el orden en que se muestran los archivos, el tamaño de los iconos, la disposición de las ventanas y la selección de vistas (iconos, lista, columnas, etc.).

# comandos utilizados

## Referencias
