## Objetivo

There is a git repository at `ssh://bandit28-git@localhost/home/bandit28-git/repo` via the port `2220`. The password for the user `bandit28-git` is the same as for the user `bandit28`.

Clone the repository and find the password for the next level.
## Datos de Acceso al Nivel

```
username: bandit28
psw: Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN
```

## Solución
```bash
C:\Users\pac61>ssh bandit28@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit28@bandit.labs.overthewire.org's password:

bandit28@bandit:~$ mktemp -d
/tmp/tmp.6FuNhWBrUs
bandit28@bandit:~$ cd /tmp/tmp.6FuNhWBrUs
bandit28@bandit:/tmp/tmp.6FuNhWBrUs$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password:
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.6FuNhWBrUs$ ls
repo
bandit28@bandit:/tmp/tmp.6FuNhWBrUs$ cd repo/
bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```

# No se encontraba en ese commit

```bash

bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$ git log --oneline
8cbd1e0 (HEAD -> master, origin/master, origin/HEAD) fix info leak
73f5d04 add missing data
5f72655 initial commit of README.md

bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$ git checkout 73f5d04
Note: switching to '73f5d04'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 73f5d04 add missing data

bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

bandit28@bandit:/tmp/tmp.6FuNhWBrUs/repo$
```

# Información obtenida
```
pwd level 29: 4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7
```
## Notas Adicionales
- Se tuvo que ir a un commit diferente para ver si ahí estaba la contraseña que necesitabamos con el comando _git log --oneline_ para ver el historial de commits y con _git checkout [clave commit]_ cambiamos al otro commit y vemos todo el contenido de ese commit.
# Commands you may need to solve this level
git
## Referencias
- 