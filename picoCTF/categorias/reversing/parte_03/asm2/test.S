Stack
00000


[    ] <- esp
[    ] ebp - 0xc
[0x8b ] ebp - 0x8 - local2
[0x2f] ebp - 0x4 - local1
[ebp ] <- ebp 
[ret ] ebp + 0x4
[0xb ] ebp + 0x4
[0x2e] ebp + 0xc
fffff

Registers
[0xb] eax

asm2(0xb,0x2e):
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp

	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x509 <asm2+28>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	sub    DWORD PTR [ebp-0x8],0xffffff80
....	<+28>:	cmp    DWORD PTR [ebp-0x8],0x63f3
	<+35>:	jle    0x501 <asm2+20>
	<+37>:	mov    eax,DWORD PTR [ebp-0x4]

	<+40>:	leave  
	<+41>:	ret    

