## Description

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java)
#### Hints
- Look up the charAt() method online.
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/reversing/vault_door_1]
└─$ cat flag2                                                    
                password.charAt(00) == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(04) == 'r' &&
               password.charAt(02) == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(03) == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(01) == '3' &&
               password.charAt(07) == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(05) == '4' &&
               password.charAt(09) == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(08) == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(06) == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e'
                                                                                                                               
┌──(kali㉿kali)-[~/mrrobot/reversing/vault_door_1]
└─$ cat flag2 | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"
d35cr4mbl3_tH3_cH4r4cT3r5_75092e                                                                                                                               
┌──(kali㉿kali)-[~/mrrobot/reversing/vault_door_1]
└─$ 


```

```java

import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
}

```

## Bandera
```css
: picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```
## Notas Adicionales
Copiamos la parte que contiene los ``passwords.charAt() == 'char' &&`` los pegamos en un archivo nuevo, le agregamos un $0$ a la izquierda a los que sólo tengan un dígito luego:

1. **`cat flag2`**: Muestra el contenido del archivo `flag2`.
    
2. **`sort`**: Ordena las líneas del contenido alfabéticamente. Si `flag2` tiene líneas con información en algún orden específico, esto cambiará el orden alfabéticamente.
    
3. **`awk '{print($3)}'`**: Usa `awk` para imprimir solo el tercer campo de cada línea (asumiendo que el texto en cada línea está separado por espacios). Esto filtra el contenido para mostrar solo el tercer elemento de cada línea.
    
4. **`tr -d "'"`**: Elimina todas las comillas simples (`'`) de la salida.
    
5. **`tr -d "\n"`**: Elimina los saltos de línea (`\n`), uniendo toda la salida en una sola línea sin espacios.
    

**Resultado**: Se obtiene una cadena continua (sin saltos de línea ni comillas simples) que contiene solo el tercer campo de cada línea ordenada de `flag2`.


## Referencias
- 