## Objetivo

The password for the next level is stored in a file called **spaces in this filename** located in the home director
## Datos de Acceso al Nivel

```
username: bandit2
psw: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```

## Solución
```bash
C:\Users\pac61>ssh bandit2@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:


bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
bandit2@bandit:~$ cat "spaces in this filename"
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
bandit2@bandit:~$
```

# Información obtenida
```
pwd level 3: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```
## Notas Adicionales

Si el nombre del archivo contiene espacios en blanco podemos autocompletar con la tecla tabulador o bien entrecomillar el nombre del archivo tal cuál está con sus espacios en blanco.

# Commands you may need to solve this level

[ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)

## Referencias
- [Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)