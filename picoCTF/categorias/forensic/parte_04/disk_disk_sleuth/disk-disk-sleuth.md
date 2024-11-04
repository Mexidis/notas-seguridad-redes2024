## Description

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/a734f18939e0aaea9d27bc7a243a0ed0/dds1-alpine.flag.img.gz)
#### Hints
- Have you ever used `file` to determine what a file was?
- Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
- Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
- Using your own computer, you could use qemu to boot from this disk!
## Solución

```shell
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/disk_disk_sleuth]
└─$ ls
dds1-alpine.flag.img.gz  disk-disk-sleuth.md
                                                                                          
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/disk_disk_sleuth]
└─$ gzip -d dds*.gz             
                                                                                          
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/disk_disk_sleuth]
└─$ ls
dds1-alpine.flag.img  disk-disk-sleuth.md
                                                                                          
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/disk_disk_sleuth]
└─$ file *.img                  
dds1-alpine.flag.img: DOS/MBR boot sector; partition 1 : ID=0x83, active, start-CHS (0x0,32,33), end-CHS (0x10,81,1), startsector 2048, 260096 sectors
                                                                                          
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/disk_disk_sleuth]
└─$ strings *.img | grep picoCTF
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_a69a712c}
                                                                                          
┌──(kali㉿kali)-[~/…/categorias/forensic/parte_04/disk_disk_sleuth]
└─$ 
```

## Bandera
```css
flag: picoCTF{f0r3ns1c4t0r_n30phyt3_a69a712c}
```
## Notas Adicionales
Se descomprimió un archivo de imagen de disco (`dds1-alpine.flag.img.gz`), obteniendo el archivo `dds1-alpine.flag.img`. Luego, se identificó el tipo de archivo, confirmando que era una imagen de disco con un sector de arranque DOS/MBR. Posteriormente, se usó el comando `strings` junto con `grep` para buscar en la imagen alguna cadena que contuviera `picoCTF`, encontrando la flag.

## Referencias
- 