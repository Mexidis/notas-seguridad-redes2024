## Description

Connect to this PostgreSQL server and find the flag!`psql -h saturn.picoctf.net -p 54173 -U postgres pico`Password is `postgres`
#### Hints
- What does a SQL database contain?
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_01_web_01/sql_direct]
└─$ psql -h saturn.picoctf.net -p 54173 -U postgres pico
Password for user postgres: 
psql (16.4 (Debian 16.4-1), server 15.2 (Debian 15.2-1.pgdg110+1))
Type "help" for help.

pico=# \dt
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

pico=# 

```

## Bandera
```css
flag: picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}
```
## Notas Adicionales
Bastó con buscar la sintaxis de *Postgre SQL* para mostrar las tablas y hacer consultas.
## Referencias
- [PostgreSQL interactive terminal](https://neon.tech/postgresql/postgresql-administration/postgresql-show-tables)