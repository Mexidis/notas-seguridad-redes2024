## Description

[keygenme-trial.py](https://mercury.picoctf.net/static/5a4198cd84f87c8a597cbd903d92fbf4/keygenme-trial.py)
#### Hints
-  (None)
## Solución

Se hará una solución a partir del código dado:
![[Pasted image 20241122214413.png]]

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_04_reversing_02/keygenme_py]
└─$ python3 solve.py  
picoCTF{1n_7h3_|<3y_of_01582419}
                                                                                                                                                                         
┌──(kali㉿kali)-[~/…/parciales/parcial_03/parte_04_reversing_02/keygenme_py]
└─$ python3 keygenme-trial.py 

===============================================
Welcome to the Arcane Calculator, ANDERSON!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy. 
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, ANDERSON (a/b/c/d)? c

Enter your license key: picoCTF{1n_7h3_|<3y_of_01582419}

Full version written to 'keygenme.py'.

Exiting trial version...

===================================================

Welcome to the Arcane Calculator, tron!

===================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) Estimate Astral Slingshot Approach Vector
(c) Exit Arcane Calculator
What would you like to do, tron (a/b/c)? 

```

### Solve.py
```python
import hashlib

username_trial = b"ANDERSON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

hash = hashlib.sha256(username_trial).hexdigest()

key_part_dynamic1_trial += hash[4]
key_part_dynamic1_trial += hash[5]
key_part_dynamic1_trial += hash[3]
key_part_dynamic1_trial += hash[6]
key_part_dynamic1_trial += hash[2]
key_part_dynamic1_trial += hash[7]
key_part_dynamic1_trial += hash[1]
key_part_dynamic1_trial += hash[8]

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

print(key_full_template_trial)
```

## Bandera
```css
flag: picoCTF{1n_7h3_|<3y_of_01582419}
```
## Notas Adicionales

## Referencias
- 