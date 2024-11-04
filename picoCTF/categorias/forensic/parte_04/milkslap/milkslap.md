## Description
[🥛](http://mercury.picoctf.net:48319/)

#### Hints
- Look at the problem category
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/milkslap]
└─$ RUBY_THREAD_VM_STACK_SIZE=500000000 zsteg concat_v.png 
imagedata           .. text: "\n\n\n\n\n\n\t\t"
b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
b1,bgr,lsb,xy       .. ^C/var/lib/gems/3.1.0/gems/iostruct-0.1.3/lib/iostruct.rb:159:in `inspect': SystemStackError
        from /var/lib/gems/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.1.0/gems/iostruct-0.1.3/lib/iostruct.rb:159:in `inspect'
        from /var/lib/gems/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.1.0/gems/iostruct-0.1.3/lib/iostruct.rb:159:in `inspect'
        from /var/lib/gems/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.1.0/gems/iostruct-0.1.3/lib/iostruct.rb:159:in `inspect'
        from /var/lib/gems/3.1.0/gems/zsteg-0.2.13/lib/zsteg/checker/wbstego.rb:41:in `to_s'
        from /var/lib/gems/3.1.0/gems/iostruct-0.1.3/lib/iostruct.rb:159:in `inspect'
         ... 4807703 levels...
        from /var/lib/gems/3.1.0/gems/zsteg-0.2.13/lib/zsteg.rb:26:in `run'
        from /var/lib/gems/3.1.0/gems/zsteg-0.2.13/bin/zsteg:8:in `<top (required)>'
        from /usr/local/bin/zsteg:25:in `load'
        from /usr/local/bin/zsteg:25:in `<main>'
                                                                                                                
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/milkslap]
└─$ 

```

## Bandera
```css
flag: picoCTF{imag3_m4n1pul4t10n_sl4p5}
```
## Notas Adicionales
Fue necesario acceder al link que nos dan en la descripción del reto y guardar la imagen directo de la página, como se muestra a continuación:
![[Pasted image 20241103011520.png]]
Así con ``wget`` podemos descargar la imagen directamente de ese link. 

Luego ocurrió un problema con la ejecución de `zsteg` porque la imagen es demasiado grande por lo tanto:
	Para ejecutar `zsteg` en el archivo `concat_v.png` sin que fallara, fue necesario aumentar el tamaño de la pila de Ruby usando la variable `RUBY_THREAD_VM_STACK_SIZE=500000000`. Esto se debió a que el análisis del archivo generaba una gran cantidad de llamadas recursivas dentro de la biblioteca `zpng`, utilizada por `zsteg`, lo que causaba un error de "stack level too deep". Al aumentar el tamaño de la pila, se le dio al programa suficiente espacio en la memoria para procesar el archivo sin alcanzar el límite de recursión, lo que permitió obtener los datos ocultos y encontrar la flag `picoCTF`

## Referencias
- [Error Ruby Stack](https://stackoverflow.com/questions/242617/how-to-increase-stack-size-for-a-ruby-app-recursive-app-getting-stack-level-to/27510458#27510458)