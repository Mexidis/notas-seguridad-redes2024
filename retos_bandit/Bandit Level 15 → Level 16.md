## Objetivo

The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL/TLS encryption.

**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**
## Datos de Acceso al Nivel

```
username: bandit15
psw: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```

## Solución 1
```bash
C:\Users\pac61>ssh bandit15@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit2@bandit.labs.overthewire.org's password:

bandit15@bandit:~$ nc localhost 30001
ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, s^Z
[1]+  Stopped                 nc localhost 30001
bandit15@bandit:~$ nc localhost 30001
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
bandit15@bandit:~$ nc -v localhost 30001
Connection to localhost (127.0.0.1) 30001 port [tcp/*] succeeded!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
bandit15@bandit:~$ ncat -v --ssl localhost 30001
Ncat: Version 7.94SVN ( https://nmap.org/ncat )
Ncat: Subject: CN=SnakeOil
Ncat: Issuer: CN=SnakeOil
Ncat: SHA-1 fingerprint: 323A F3B1 4FC7 1B0F F71A 1931 8FF3 62A1 49AC 735A
Ncat: Certificate verification failed (self-signed certificate).
Ncat: SSL connection to 127.0.0.1:30001.
Ncat: SHA-1 fingerprint: 323A F3B1 4FC7 1B0F F71A 1931 8FF3 62A1 49AC 735A
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```

## Solución 2
```bash
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: F3B75C6C9DC0F7081E0986F100C7A57A639F1B7E50CB76B25BEB1BA64B952198
    Session-ID-ctx:
    Resumption PSK: 3FBD1BE2483855206AD1EEEE9173F555F505813587ED515B3767632173E39E116C3F3A200485FB81547600D159E551BA
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e5 a2 21 b4 fc 2d 07 43-5e 62 0e 98 32 55 cb 8c   ..!..-.C^b..2U..
    0010 - 14 46 88 9e 37 04 c4 3a-b2 7c 9b 0f 79 b0 5c 01   .F..7..:.|..y.\.
    0020 - 00 a6 12 32 60 6d d0 b0-6d 9f 6b 72 0a 16 be 67   ...2`m..m.kr...g
    0030 - de 07 34 bd 7f c0 63 17-f9 6c 5c 45 b0 cd b7 d2   ..4...c..l\E....
    0040 - 73 64 1d 4b 4f 96 5c fd-ab 44 7d 67 1f 9b 3a ab   sd.KO.\..D}g..:.
    0050 - 26 d7 2b 2f 71 9d b1 c0-13 72 d6 3e 29 57 cd b2   &.+/q....r.>)W..
    0060 - 48 f3 3c 67 32 34 ad c8-96 9a 6e fc 0c 6a a0 89   H.<g24....n..j..
    0070 - e5 5d c9 4a b1 39 9c e2-fc eb ee fe 5b d6 47 3d   .].J.9......[.G=
    0080 - c2 da da aa 5a 49 52 14-f2 7d f0 97 8f ea f7 f4   ....ZIR..}......
    0090 - 03 b6 ad b0 60 00 75 e8-86 41 f9 f9 6e 81 a7 db   ....`.u..A..n...
    00a0 - c4 42 43 9b 7d 0e a0 04-ea d9 b1 5f 7f ad 5e 71   .BC.}......_..^q
    00b0 - c4 7f 81 b4 65 af 6d c0-a0 18 37 6f 2b 57 64 55   ....e.m...7o+WdU
    00c0 - 10 94 e4 89 8c 41 7a ef-8f aa 50 3a d2 14 da 1f   .....Az...P:....
    00d0 - f2 83 ad e3 9e c5 30 1c-29 09 3a 3d 23 3d 73 ab   ......0.).:=#=s.

    Start Time: 1725295239
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 3AD9629323608F00E49938DC056C191891280FA1017505BABE1CB6192A9C3DF6
    Session-ID-ctx:
    Resumption PSK: 1ED3449370D94D4BECA0DDE57D08787FDCDC0941F1FD2795DB7CE2144B9CEF53FFB20F38051C32845589D04E7BC75550
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e5 a2 21 b4 fc 2d 07 43-5e 62 0e 98 32 55 cb 8c   ..!..-.C^b..2U..
    0010 - 40 ee dc e1 d5 21 7b e6-f5 1a ff d6 2c ae 08 ba   @....!{.....,...
    0020 - f2 65 b1 b9 06 6d 90 de-33 f4 eb 6c 54 75 38 c2   .e...m..3..lTu8.
    0030 - 10 27 73 f4 21 03 a7 14-f3 b5 c5 b4 08 f3 23 c8   .'s.!.........#.
    0040 - d6 33 9f db 90 05 27 f1-cc 59 c5 76 66 26 8a c6   .3....'..Y.vf&..
    0050 - 95 81 b6 21 ed 97 60 f5-61 63 1d 9c 7f 37 bd bf   ...!..`.ac...7..
    0060 - bf ae 1e c8 ba 7a ee 2e-41 df 1f d7 88 61 51 c7   .....z..A....aQ.
    0070 - d2 ec 6e b8 36 6e c6 03-64 f7 34 ff df 3d 38 10   ..n.6n..d.4..=8.
    0080 - d7 7c ab 67 21 10 d7 34-02 57 27 27 5d 40 ea e3   .|.g!..4.W'']@..
    0090 - 9b 3b 9e 59 d4 5c db a9-9f b0 a7 3e d6 a9 a4 73   .;.Y.\.....>...s
    00a0 - ab c1 be bb af 79 7d bc-63 87 32 bf 17 55 f0 87   .....y}.c.2..U..
    00b0 - 9e 83 b8 86 88 de 37 50-48 a0 8a 64 4f db 20 b2   ......7PH..dO. .
    00c0 - e2 a5 18 a1 ef bc 51 2b-65 c3 b2 34 d7 66 f8 3b   ......Q+e..4.f.;
    00d0 - 5e f7 88 93 67 52 32 dc-9e 0b 0e 34 77 4c 47 a1   ^...gR2....4wLG.

    Start Time: 1725295239
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed
bandit15@bandit:~$
```
# Información obtenida
```
pwd level 16: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx   
```
## Notas Adicionales

ssl / tls  -es un protocolo de comunicación generalmente usados en sitios web (https)
ncat - es una herramienta similar a netcat pero con otras ventajas como conectar a purertos ssl
openssl - es un cliente ssl para linux
# Commands you may need to solve this level

ssh, telnet, nc, ncat, socat, openssl, s_client, nmap, netstat, ss

## Referencias
- [Secure Socket Layer/Transport Layer Security on Wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [OpenSSL Cookbook - Testing with OpenSSL](https://www.feistyduck.com/library/openssl-cookbook/online/testing-with-openssl/index.html)