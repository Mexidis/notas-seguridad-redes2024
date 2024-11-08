## Description

Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/0fe13a33318e756f71c35cb490e64c81/shark2.pcapng).
#### Hints
- Did you really find _the_ flag?
- Look for traffic that seems suspicious.
## Solución

```shell
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/wireshark_02]
└─$ tshark -nr shark2.pcapng -Y 'dns'                                                     
  791   7.931626 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x76aa A lDqoR16q.reddshrimpandherring.com
  792   7.943025      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x76aa No such name A lDqoR16q.reddshrimpandherring.com SOA a.gtld-servers.net
  793   7.947216 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcdd5 A lDqoR16q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  794   7.957680      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xcdd5 No such name A lDqoR16q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
  795   7.958549 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5d2d A lDqoR16q.reddshrimpandherring.com.windomain.local
  796   7.967998      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5d2d No such name A lDqoR16q.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
  797   7.968981 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc847 A 1Th0dQuT.reddshrimpandherring.com
  798   8.049550      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc847 No such name A 1Th0dQuT.reddshrimpandherring.com SOA a.gtld-servers.net
  799   8.050527 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x21a5 A 1Th0dQuT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  800   8.061483      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x21a5 No such name A 1Th0dQuT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
  801   8.062385 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc006 A 1Th0dQuT.reddshrimpandherring.com.windomain.local
  802   8.071914      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc006 No such name A 1Th0dQuT.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
  803   8.073001 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4249 A ysnuBebx.reddshrimpandherring.com
  804   8.142293      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4249 No such name A ysnuBebx.reddshrimpandherring.com SOA a.gtld-servers.net
  805   8.143556 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb326 A ysnuBebx.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  806   8.155877      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb326 No such name A ysnuBebx.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
  807   8.156879 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc91b A ysnuBebx.reddshrimpandherring.com.windomain.local
  808   8.166474      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc91b No such name A ysnuBebx.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
  809   8.167511 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6a22 A OKm0XI7q.reddshrimpandherring.com
  828   8.180638      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6a22 No such name A OKm0XI7q.reddshrimpandherring.com SOA a.gtld-servers.net
  829   8.181651 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb5aa A OKm0XI7q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
  857   8.192002      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xb5aa No such name A OKm0XI7q.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
  861   8.193159 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9e3d A OKm0XI7q.reddshrimpandherring.com.windomain.local
  892   8.202532      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9e3d No such name A OKm0XI7q.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
  893   8.203642 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xda95 A j/RVIHi2.reddshrimpandherring.com
  972   8.226558      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xda95 No such name A j/RVIHi2.reddshrimpandherring.com SOA a.gtld-servers.net
  985   8.227737 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9c1b A j/RVIHi2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1016   8.238033      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x9c1b No such name A j/RVIHi2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1017   8.238926 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa0ed A j/RVIHi2.reddshrimpandherring.com.windomain.local
 1054   8.248407      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa0ed No such name A j/RVIHi2.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1057   8.249253 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x483a A d+KVXhMV.reddshrimpandherring.com
 1095   8.260649      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x483a No such name A d+KVXhMV.reddshrimpandherring.com SOA a.gtld-servers.net
 1096   8.261573 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x49d8 A d+KVXhMV.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1130   8.272031      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x49d8 No such name A d+KVXhMV.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1137   8.272877 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x65df A d+KVXhMV.reddshrimpandherring.com.windomain.local
 1174   8.282335      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x65df No such name A d+KVXhMV.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1178   8.283337 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2a2a A ky0+eTqU.reddshrimpandherring.com
 1311   8.326523      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2a2a No such name A ky0+eTqU.reddshrimpandherring.com SOA a.gtld-servers.net
 1315   8.327573 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa842 A ky0+eTqU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1360   8.338869      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa842 No such name A ky0+eTqU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1365   8.339771 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x8c1a A ky0+eTqU.reddshrimpandherring.com.windomain.local
 1399   8.349983      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x8c1a No such name A ky0+eTqU.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1403   8.350972 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x35a3 A poybMrsl.reddshrimpandherring.com
 1440   8.362689      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x35a3 No such name A poybMrsl.reddshrimpandherring.com SOA a.gtld-servers.net
 1444   8.363480 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x31e5 A poybMrsl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1484   8.373987      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x31e5 No such name A poybMrsl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1491   8.374996 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb29a A poybMrsl.reddshrimpandherring.com.windomain.local
 1522   8.386470      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb29a No such name A poybMrsl.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1523   8.387406 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x5a3d A jK2eAyOi.reddshrimpandherring.com
 1524   8.429794      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x5a3d No such name A jK2eAyOi.reddshrimpandherring.com SOA a.gtld-servers.net
 1525   8.430761 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0197 A jK2eAyOi.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1526   8.449829      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x0197 No such name A jK2eAyOi.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1527   8.450895 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xab28 A jK2eAyOi.reddshrimpandherring.com.windomain.local
 1528   8.460565      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xab28 No such name A jK2eAyOi.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1529   8.461733 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0c17 A 48b4iU01.reddshrimpandherring.com
 1530   8.473406      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0c17 No such name A 48b4iU01.reddshrimpandherring.com SOA a.gtld-servers.net
 1531   8.474391 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xaeba A 48b4iU01.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1532   8.484679      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xaeba No such name A 48b4iU01.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1533   8.485660 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcd31 A 48b4iU01.reddshrimpandherring.com.windomain.local
 1534   8.495714      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcd31 No such name A 48b4iU01.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1535   8.496584 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6d73 A FvJnCBT8.reddshrimpandherring.com
 1536   8.509538      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6d73 No such name A FvJnCBT8.reddshrimpandherring.com SOA a.gtld-servers.net
 1537   8.510444 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf7db A FvJnCBT8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1538   8.520798      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xf7db No such name A FvJnCBT8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1539   8.521657 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x834f A FvJnCBT8.reddshrimpandherring.com.windomain.local
 1542   8.531187      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x834f No such name A FvJnCBT8.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1543   8.532222 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xcbc7 A km29WP3g.reddshrimpandherring.com
 1546   8.577711      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xcbc7 No such name A km29WP3g.reddshrimpandherring.com SOA a.gtld-servers.net
 1548   8.578968 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf136 A km29WP3g.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1553   8.589583      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xf136 No such name A km29WP3g.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1554   8.591066 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x582f A km29WP3g.reddshrimpandherring.com.windomain.local
 1555   8.600503      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x582f No such name A km29WP3g.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1556   8.601450 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6a81 A /3Dz6rCU.reddshrimpandherring.com
 1557   8.622628      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6a81 No such name A /3Dz6rCU.reddshrimpandherring.com SOA a.gtld-servers.net
 1558   8.623613 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9474 A /3Dz6rCU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1560   8.634261      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x9474 No such name A /3Dz6rCU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1561   8.635123 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb194 A /3Dz6rCU.reddshrimpandherring.com.windomain.local
 1562   8.646508      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb194 No such name A /3Dz6rCU.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1563   8.647563 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4484 A di8sCDPv.reddshrimpandherring.com
 1564   8.718587      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4484 No such name A di8sCDPv.reddshrimpandherring.com SOA a.gtld-servers.net
 1565   8.719963 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xac14 A di8sCDPv.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1566   8.730448      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xac14 No such name A di8sCDPv.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1567   8.731446 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9cc6 A di8sCDPv.reddshrimpandherring.com.windomain.local
 1568   8.741031      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9cc6 No such name A di8sCDPv.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1569   8.742041 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x06f8 A b38U91ep.reddshrimpandherring.com
 1570   8.812615      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x06f8 No such name A b38U91ep.reddshrimpandherring.com SOA a.gtld-servers.net
 1571   8.813625 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb736 A b38U91ep.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1572   8.824198      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb736 No such name A b38U91ep.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1573   8.825100 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb821 A b38U91ep.reddshrimpandherring.com.windomain.local
 1574   8.834559      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb821 No such name A b38U91ep.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1575   8.835440 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe44d A 2DA0w7Jt.reddshrimpandherring.com
 1576   8.879722      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe44d No such name A 2DA0w7Jt.reddshrimpandherring.com SOA a.gtld-servers.net
 1577   8.880742 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1d6d A 2DA0w7Jt.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1578   8.893268      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x1d6d No such name A 2DA0w7Jt.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1579   8.894085 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5ce2 A 2DA0w7Jt.reddshrimpandherring.com.windomain.local
 1580   8.903629      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5ce2 No such name A 2DA0w7Jt.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1581   8.904459 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x5eb2 A FZYl6dCA.reddshrimpandherring.com
 1582   8.951344      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x5eb2 No such name A FZYl6dCA.reddshrimpandherring.com SOA a.gtld-servers.net
 1583   8.952363 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3cc2 A FZYl6dCA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1584   8.962736      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3cc2 No such name A FZYl6dCA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1585   8.963629 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5a40 A FZYl6dCA.reddshrimpandherring.com.windomain.local
 1586   8.973163      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5a40 No such name A FZYl6dCA.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1587   8.974037 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb094 A BoORWyDu.reddshrimpandherring.com
 1588   9.018320      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb094 No such name A BoORWyDu.reddshrimpandherring.com SOA a.gtld-servers.net
 1589   9.019377 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7cea A BoORWyDu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1590   9.029749      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x7cea No such name A BoORWyDu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1591   9.030864 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x708e A BoORWyDu.reddshrimpandherring.com.windomain.local
 1592   9.040484      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x708e No such name A BoORWyDu.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1593   9.041453 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x03f1 A MVsbj1/d.reddshrimpandherring.com
 1594   9.055728      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x03f1 No such name A MVsbj1/d.reddshrimpandherring.com SOA a.gtld-servers.net
 1595   9.056766 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe705 A MVsbj1/d.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1596   9.067026      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xe705 No such name A MVsbj1/d.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1597   9.067845 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x81a0 A MVsbj1/d.reddshrimpandherring.com.windomain.local
 1598   9.077327      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x81a0 No such name A MVsbj1/d.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1599   9.078735 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd2d4 A UWrgyXWr.reddshrimpandherring.com
 1600   9.147148      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd2d4 No such name A UWrgyXWr.reddshrimpandherring.com SOA a.gtld-servers.net
 1601   9.148170 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb9a4 A UWrgyXWr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1602   9.167300      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb9a4 No such name A UWrgyXWr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1603   9.168302 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3f44 A UWrgyXWr.reddshrimpandherring.com.windomain.local
 1604   9.177625      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3f44 No such name A UWrgyXWr.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1605   9.178628 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xccfe A 9NzCwWxd.reddshrimpandherring.com
 1606   9.199964      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xccfe No such name A 9NzCwWxd.reddshrimpandherring.com SOA a.gtld-servers.net
 1607   9.200981 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6c9a A 9NzCwWxd.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1609   9.211496      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x6c9a No such name A 9NzCwWxd.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1611   9.212564 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x458f A 9NzCwWxd.reddshrimpandherring.com.windomain.local
 1612   9.222010      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x458f No such name A 9NzCwWxd.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1613   9.222994 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x233e A m/TqO+IW.reddshrimpandherring.com
 1614   9.236640      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x233e No such name A m/TqO+IW.reddshrimpandherring.com SOA a.gtld-servers.net
 1615   9.237818 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd8a7 A m/TqO+IW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1616   9.250219      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xd8a7 No such name A m/TqO+IW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1617   9.251250 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x215f A m/TqO+IW.reddshrimpandherring.com.windomain.local
 1618   9.260659      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x215f No such name A m/TqO+IW.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1622   9.261930 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x7487 A o2ZJtOyF.reddshrimpandherring.com
 1627   9.306399      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x7487 No such name A o2ZJtOyF.reddshrimpandherring.com SOA a.gtld-servers.net
 1628   9.307387 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf18f A o2ZJtOyF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1630   9.319919      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xf18f No such name A o2ZJtOyF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1631   9.320742 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcd93 A o2ZJtOyF.reddshrimpandherring.com.windomain.local
 1632   9.330068      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcd93 No such name A o2ZJtOyF.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1633   9.334169 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0xdf26 A cGljb0NU.reddshrimpandherring.com
 1634   9.388061  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0xdf26 No such name A cGljb0NU.reddshrimpandherring.com SOA a.gtld-servers.net
 1635   9.389117 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xa12d A cGljb0NU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1636   9.439381  18.217.1.57 → 192.168.38.104 DNS 205 Standard query response 0xa12d No such name A cGljb0NU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1637   9.440363 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local
 1638   9.490669  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x1dd2 No such name A cGljb0NU.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1639   9.491830 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8872 A um0kpvjf.reddshrimpandherring.com
 1640   9.506471      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8872 No such name A um0kpvjf.reddshrimpandherring.com SOA a.gtld-servers.net
 1641   9.507474 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0d00 A um0kpvjf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1642   9.517878      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0d00 No such name A um0kpvjf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1643   9.518810 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2b5f A um0kpvjf.reddshrimpandherring.com.windomain.local
 1644   9.528297      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2b5f No such name A um0kpvjf.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1645   9.529155 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa098 A Sox37h19.reddshrimpandherring.com
 1646   9.540788      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa098 No such name A Sox37h19.reddshrimpandherring.com SOA a.gtld-servers.net
 1647   9.541580 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8e79 A Sox37h19.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1648   9.553916      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8e79 No such name A Sox37h19.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1649   9.554655 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7ece A Sox37h19.reddshrimpandherring.com.windomain.local
 1650   9.564195      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7ece No such name A Sox37h19.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1651   9.565033 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc4ac A Z5hJZHyn.reddshrimpandherring.com
 1652   9.576027      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc4ac No such name A Z5hJZHyn.reddshrimpandherring.com SOA a.gtld-servers.net
 1653   9.576922 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xbf63 A Z5hJZHyn.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1654   9.587388      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xbf63 No such name A Z5hJZHyn.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1655   9.588158 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5a1e A Z5hJZHyn.reddshrimpandherring.com.windomain.local
 1656   9.599696      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5a1e No such name A Z5hJZHyn.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1657   9.600522 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xacc9 A nlF4PBzk.reddshrimpandherring.com
 1658   9.611312      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xacc9 No such name A nlF4PBzk.reddshrimpandherring.com SOA a.gtld-servers.net
 1659   9.612086 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8008 A nlF4PBzk.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1660   9.624407      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x8008 No such name A nlF4PBzk.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1661   9.625615 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x247e A nlF4PBzk.reddshrimpandherring.com.windomain.local
 1662   9.636963      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x247e No such name A nlF4PBzk.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1663   9.637994 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe2e4 A h+CXa09t.reddshrimpandherring.com
 1664   9.649804      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe2e4 No such name A h+CXa09t.reddshrimpandherring.com SOA a.gtld-servers.net
 1665   9.650605 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8cd3 A h+CXa09t.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1666   9.663091      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x8cd3 No such name A h+CXa09t.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1667   9.664091 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb69f A h+CXa09t.reddshrimpandherring.com.windomain.local
 1668   9.673465      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb69f No such name A h+CXa09t.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1669   9.674366 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd80a A tbK/uIWB.reddshrimpandherring.com
 1670   9.685543      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd80a No such name A tbK/uIWB.reddshrimpandherring.com SOA a.gtld-servers.net
 1671   9.686424 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7508 A tbK/uIWB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1672   9.696831      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x7508 No such name A tbK/uIWB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1673   9.697698 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3377 A tbK/uIWB.reddshrimpandherring.com.windomain.local
 1674   9.707291      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3377 No such name A tbK/uIWB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1675   9.708194 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3d13 A 2a3XH03l.reddshrimpandherring.com
 1678   9.752970      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3d13 No such name A 2a3XH03l.reddshrimpandherring.com SOA a.gtld-servers.net
 1679   9.753978 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xbfdd A 2a3XH03l.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1680   9.766418      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xbfdd No such name A 2a3XH03l.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1681   9.768033 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x17e7 A 2a3XH03l.reddshrimpandherring.com.windomain.local
 1682   9.779425      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x17e7 No such name A 2a3XH03l.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1683   9.780547 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa010 A J0AWOs3w.reddshrimpandherring.com
 1691   9.824205      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa010 No such name A J0AWOs3w.reddshrimpandherring.com SOA a.gtld-servers.net
 1692   9.825319 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x29a4 A J0AWOs3w.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1693   9.835775      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x29a4 No such name A J0AWOs3w.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1694   9.836681 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcb2a A J0AWOs3w.reddshrimpandherring.com.windomain.local
 1696   9.848146      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcb2a No such name A J0AWOs3w.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1697   9.849197 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd2b1 A FIAowc1g.reddshrimpandherring.com
 1698   9.918876      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd2b1 No such name A FIAowc1g.reddshrimpandherring.com SOA a.gtld-servers.net
 1699   9.919916 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3ea2 A FIAowc1g.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1700   9.930187      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3ea2 No such name A FIAowc1g.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1701   9.931050 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9f28 A FIAowc1g.reddshrimpandherring.com.windomain.local
 1702   9.940362      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9f28 No such name A FIAowc1g.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1703   9.941181 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0036 A drwIRfot.reddshrimpandherring.com
 1704   9.952358      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0036 No such name A drwIRfot.reddshrimpandherring.com SOA a.gtld-servers.net
 1705   9.953338 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb145 A drwIRfot.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1706   9.963722      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xb145 No such name A drwIRfot.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1707   9.964508 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xe270 A drwIRfot.reddshrimpandherring.com.windomain.local
 1708   9.976018      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xe270 No such name A drwIRfot.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1709   9.976955 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb3c4 A ZjLL+DYc.reddshrimpandherring.com
 1710   9.998665      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb3c4 No such name A ZjLL+DYc.reddshrimpandherring.com SOA a.gtld-servers.net
 1711   9.999684 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xde6d A ZjLL+DYc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1712  10.010099      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xde6d No such name A ZjLL+DYc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1713  10.010855 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xfe50 A ZjLL+DYc.reddshrimpandherring.com.windomain.local
 1714  10.020496      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xfe50 No such name A ZjLL+DYc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1715  10.021392 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc8cd A kXD4OIb9.reddshrimpandherring.com
 1730  10.067262      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc8cd No such name A kXD4OIb9.reddshrimpandherring.com SOA a.gtld-servers.net
 1732  10.068179 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa9da A kXD4OIb9.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1735  10.078624      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa9da No such name A kXD4OIb9.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1736  10.079599 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6ac8 A kXD4OIb9.reddshrimpandherring.com.windomain.local
 1737  10.089191      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6ac8 No such name A kXD4OIb9.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1738  10.090264 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc679 A h81LA4Xw.reddshrimpandherring.com
 1743  10.134677      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc679 No such name A h81LA4Xw.reddshrimpandherring.com SOA a.gtld-servers.net
 1744  10.135694 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3c8e A h81LA4Xw.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1745  10.148815      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3c8e No such name A h81LA4Xw.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1746  10.149836 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xfdf5 A h81LA4Xw.reddshrimpandherring.com.windomain.local
 1748  10.159335      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xfdf5 No such name A h81LA4Xw.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1749  10.160315 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x37b7 A nT95IG26.reddshrimpandherring.com
 1750  10.205148      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x37b7 No such name A nT95IG26.reddshrimpandherring.com SOA a.gtld-servers.net
 1751  10.206166 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x88c1 A nT95IG26.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1752  10.218379      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x88c1 No such name A nT95IG26.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1753  10.219301 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1050 A nT95IG26.reddshrimpandherring.com.windomain.local
 1754  10.228580      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1050 No such name A nT95IG26.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1755  10.229414 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xfd89 A BySoFVNP.reddshrimpandherring.com
 1756  10.240990      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xfd89 No such name A BySoFVNP.reddshrimpandherring.com SOA a.gtld-servers.net
 1759  10.243179 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x58ae A BySoFVNP.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1760  10.253858      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x58ae No such name A BySoFVNP.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1761  10.254761 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc143 A BySoFVNP.reddshrimpandherring.com.windomain.local
 1762  10.264118      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc143 No such name A BySoFVNP.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1763  10.264976 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4c4f A kqOgISqa.reddshrimpandherring.com
 1764  10.289434      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4c4f No such name A kqOgISqa.reddshrimpandherring.com SOA a.gtld-servers.net
 1765  10.290452 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf814 A kqOgISqa.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1773  10.301006      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xf814 No such name A kqOgISqa.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1774  10.302544 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1b25 A kqOgISqa.reddshrimpandherring.com.windomain.local
 1775  10.312105      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1b25 No such name A kqOgISqa.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1776  10.313420 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa0cf A YuvBSCsM.reddshrimpandherring.com
 1777  10.325242      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa0cf No such name A YuvBSCsM.reddshrimpandherring.com SOA a.gtld-servers.net
 1778  10.326175 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1c9d A YuvBSCsM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1779  10.338668      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x1c9d No such name A YuvBSCsM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1780  10.339640 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xe865 A YuvBSCsM.reddshrimpandherring.com.windomain.local
 1782  10.348972      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xe865 No such name A YuvBSCsM.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1783  10.349854 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd466 A bq7AocPI.reddshrimpandherring.com
 1784  10.361123      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd466 No such name A bq7AocPI.reddshrimpandherring.com SOA a.gtld-servers.net
 1785  10.362188 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa7e7 A bq7AocPI.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1786  10.374714      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa7e7 No such name A bq7AocPI.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1787  10.375664 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0882 A bq7AocPI.reddshrimpandherring.com.windomain.local
 1788  10.387025      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0882 No such name A bq7AocPI.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1789  10.388031 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xbe8b A JSAAt3gF.reddshrimpandherring.com
 1790  10.399283      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xbe8b No such name A JSAAt3gF.reddshrimpandherring.com SOA a.gtld-servers.net
 1791  10.400187 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xfc9e A JSAAt3gF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1792  10.410605      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xfc9e No such name A JSAAt3gF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1793  10.411391 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x08b6 A JSAAt3gF.reddshrimpandherring.com.windomain.local
 1794  10.420785      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x08b6 No such name A JSAAt3gF.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1795  10.421706 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xf676 A x5HUgibz.reddshrimpandherring.com
 1796  10.432953      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xf676 No such name A x5HUgibz.reddshrimpandherring.com SOA a.gtld-servers.net
 1797  10.433732 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x820b A x5HUgibz.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1798  10.444229      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x820b No such name A x5HUgibz.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1799  10.445019 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcf90 A x5HUgibz.reddshrimpandherring.com.windomain.local
 1800  10.456439      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcf90 No such name A x5HUgibz.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1801  10.457318 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb1f6 A OsGF7kWB.reddshrimpandherring.com
 1802  10.503341      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb1f6 No such name A OsGF7kWB.reddshrimpandherring.com SOA a.gtld-servers.net
 1803  10.504367 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3152 A OsGF7kWB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1804  10.515098      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3152 No such name A OsGF7kWB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1805  10.515844 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb674 A OsGF7kWB.reddshrimpandherring.com.windomain.local
 1806  10.525247      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb674 No such name A OsGF7kWB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1807  10.526131 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6acc A K99ppjF/.reddshrimpandherring.com
 1808  10.569565      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6acc No such name A K99ppjF/.reddshrimpandherring.com SOA a.gtld-servers.net
 1809  10.570599 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcc29 A K99ppjF/.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1810  10.581065      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xcc29 No such name A K99ppjF/.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1811  10.581866 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xac5c A K99ppjF/.reddshrimpandherring.com.windomain.local
 1812  10.591216      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xac5c No such name A K99ppjF/.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1813  10.592635 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xfe4b A jTyNCNhU.reddshrimpandherring.com
 1814  10.606683      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xfe4b No such name A jTyNCNhU.reddshrimpandherring.com SOA a.gtld-servers.net
 1815  10.607597 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4c01 A jTyNCNhU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1816  10.617774      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x4c01 No such name A jTyNCNhU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1817  10.618599 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2614 A jTyNCNhU.reddshrimpandherring.com.windomain.local
 1818  10.627977      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2614 No such name A jTyNCNhU.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1819  10.629075 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x791f A cWVizacs.reddshrimpandherring.com
 1869  10.702212      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x791f No such name A cWVizacs.reddshrimpandherring.com SOA a.gtld-servers.net
 1873  10.703358 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xdbf6 A cWVizacs.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1889  10.713809      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xdbf6 No such name A cWVizacs.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1890  10.714661 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5fa4 A cWVizacs.reddshrimpandherring.com.windomain.local
 1891  10.726204      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5fa4 No such name A cWVizacs.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1892  10.727196 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xbef2 A K4DhGAWE.reddshrimpandherring.com
 1895  10.751606      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xbef2 No such name A K4DhGAWE.reddshrimpandherring.com SOA a.gtld-servers.net
 1896  10.752590 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf79e A K4DhGAWE.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1897  10.764965      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xf79e No such name A K4DhGAWE.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1898  10.766162 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5426 A K4DhGAWE.reddshrimpandherring.com.windomain.local
 1899  10.775699      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5426 No such name A K4DhGAWE.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1900  10.776686 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xcc97 A uAY+tVE7.reddshrimpandherring.com
 1908  10.819939      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xcc97 No such name A uAY+tVE7.reddshrimpandherring.com SOA a.gtld-servers.net
 1909  10.820954 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x33c0 A uAY+tVE7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1910  10.831627      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x33c0 No such name A uAY+tVE7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1911  10.832692 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6a18 A uAY+tVE7.reddshrimpandherring.com.windomain.local
 1913  10.842251      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6a18 No such name A uAY+tVE7.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1914  10.843198 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6370 A 60aidRgy.reddshrimpandherring.com
 1915  10.854894      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6370 No such name A 60aidRgy.reddshrimpandherring.com SOA a.gtld-servers.net
 1916  10.855892 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb619 A 60aidRgy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1917  10.874448      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb619 No such name A 60aidRgy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1918  10.875432 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x311d A 60aidRgy.reddshrimpandherring.com.windomain.local
 1919  10.884885      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x311d No such name A 60aidRgy.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1920  10.885817 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe02d A nBt3Mokk.reddshrimpandherring.com
 1921  10.896649      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe02d No such name A nBt3Mokk.reddshrimpandherring.com SOA a.gtld-servers.net
 1922  10.897678 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0c38 A nBt3Mokk.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1923  10.908316      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0c38 No such name A nBt3Mokk.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1924  10.909344 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0803 A nBt3Mokk.reddshrimpandherring.com.windomain.local
 1925  10.921129      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0803 No such name A nBt3Mokk.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1926  10.922258 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x7b04 A 30d1RFWu.reddshrimpandherring.com
 1927  10.990830      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x7b04 No such name A 30d1RFWu.reddshrimpandherring.com SOA a.gtld-servers.net
 1928  10.991855 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5540 A 30d1RFWu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1929  11.002106      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x5540 No such name A 30d1RFWu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1930  11.003022 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x30a0 A 30d1RFWu.reddshrimpandherring.com.windomain.local
 1931  11.016704      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x30a0 No such name A 30d1RFWu.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1932  11.017761 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc695 A +9eXNk0X.reddshrimpandherring.com
 1933  11.062494      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc695 No such name A +9eXNk0X.reddshrimpandherring.com SOA a.gtld-servers.net
 1934  11.063498 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0621 A +9eXNk0X.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1935  11.074084      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0621 No such name A +9eXNk0X.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1936  11.075110 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd02b A +9eXNk0X.reddshrimpandherring.com.windomain.local
 1937  11.084667      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd02b No such name A +9eXNk0X.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1938  11.085850 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x23db A TI2DYRO/.reddshrimpandherring.com
 1939  11.127447      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x23db No such name A TI2DYRO/.reddshrimpandherring.com SOA a.gtld-servers.net
 1940  11.128568 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x880e A TI2DYRO/.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1941  11.138871      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x880e No such name A TI2DYRO/.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1942  11.139895 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd32c A TI2DYRO/.reddshrimpandherring.com.windomain.local
 1943  11.149376      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd32c No such name A TI2DYRO/.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1944  11.150344 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4731 A 9MjYzoLj.reddshrimpandherring.com
 1945  11.161179      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4731 No such name A 9MjYzoLj.reddshrimpandherring.com SOA a.gtld-servers.net
 1946  11.162207 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb684 A 9MjYzoLj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1947  11.174603      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb684 No such name A 9MjYzoLj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1948  11.175383 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x262f A 9MjYzoLj.reddshrimpandherring.com.windomain.local
 1949  11.186935      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x262f No such name A 9MjYzoLj.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1950  11.187990 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4435 A Z+BtbAta.reddshrimpandherring.com
 1953  11.265768      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4435 No such name A Z+BtbAta.reddshrimpandherring.com SOA a.gtld-servers.net
 1954  11.267496 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7f56 A Z+BtbAta.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1955  11.278046      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7f56 No such name A Z+BtbAta.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1956  11.279015 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf956 A Z+BtbAta.reddshrimpandherring.com.windomain.local
 1959  11.288401      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf956 No such name A Z+BtbAta.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1961  11.289386 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd8b3 A YkmRh2nr.reddshrimpandherring.com
 1966  11.310419      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd8b3 No such name A YkmRh2nr.reddshrimpandherring.com SOA a.gtld-servers.net
 1967  11.311600 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2841 A YkmRh2nr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1968  11.322064      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2841 No such name A YkmRh2nr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1969  11.322997 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x58b9 A YkmRh2nr.reddshrimpandherring.com.windomain.local
 1970  11.332353      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x58b9 No such name A YkmRh2nr.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1971  11.333536 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x487b A OTPSYXkE.reddshrimpandherring.com
 1973  11.345043      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x487b No such name A OTPSYXkE.reddshrimpandherring.com SOA a.gtld-servers.net
 1974  11.346047 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xca7c A OTPSYXkE.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1981  11.364785      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xca7c No such name A OTPSYXkE.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1982  11.365858 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x919c A OTPSYXkE.reddshrimpandherring.com.windomain.local
 1983  11.375265      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x919c No such name A OTPSYXkE.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1984  11.376300 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x44c8 A uXvd48AT.reddshrimpandherring.com
 1985  11.400733      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x44c8 No such name A uXvd48AT.reddshrimpandherring.com SOA a.gtld-servers.net
 1986  11.401745 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x11f2 A uXvd48AT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1987  11.420656      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x11f2 No such name A uXvd48AT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1988  11.421635 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb60e A uXvd48AT.reddshrimpandherring.com.windomain.local
 1989  11.431497      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb60e No such name A uXvd48AT.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1990  11.432498 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9c4d A /PNsKWtj.reddshrimpandherring.com
 1991  11.444101      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9c4d No such name A /PNsKWtj.reddshrimpandherring.com SOA a.gtld-servers.net
 1992  11.445068 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x272c A /PNsKWtj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1993  11.455466      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x272c No such name A /PNsKWtj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 1994  11.456355 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xbe0a A /PNsKWtj.reddshrimpandherring.com.windomain.local
 1995  11.465831      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xbe0a No such name A /PNsKWtj.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 1996  11.466780 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa857 A tFSfHl/9.reddshrimpandherring.com
 1997  11.511134      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa857 No such name A tFSfHl/9.reddshrimpandherring.com SOA a.gtld-servers.net
 1998  11.512145 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x63a7 A tFSfHl/9.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1999  11.522765      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x63a7 No such name A tFSfHl/9.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2000  11.523771 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd664 A tFSfHl/9.reddshrimpandherring.com.windomain.local
 2001  11.533501      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd664 No such name A tFSfHl/9.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2002  11.534498 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x62cb A 5HyMGCS6.reddshrimpandherring.com
 2003  11.578726      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x62cb No such name A 5HyMGCS6.reddshrimpandherring.com SOA a.gtld-servers.net
 2004  11.580735 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x03f6 A 5HyMGCS6.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2005  11.591242      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x03f6 No such name A 5HyMGCS6.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2006  11.592270 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x64ce A 5HyMGCS6.reddshrimpandherring.com.windomain.local
 2007  11.601708      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x64ce No such name A 5HyMGCS6.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2008  11.602640 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x40f8 A 1FjuRiR8.reddshrimpandherring.com
 2009  11.643451      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x40f8 No such name A 1FjuRiR8.reddshrimpandherring.com SOA a.gtld-servers.net
 2010  11.644393 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1ea7 A 1FjuRiR8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2011  11.655258      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x1ea7 No such name A 1FjuRiR8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2012  11.656124 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4a07 A 1FjuRiR8.reddshrimpandherring.com.windomain.local
 2013  11.665752      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4a07 No such name A 1FjuRiR8.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2014  11.666647 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x523f A jVZNhQOT.reddshrimpandherring.com
 2017  11.708002      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x523f No such name A jVZNhQOT.reddshrimpandherring.com SOA a.gtld-servers.net
 2018  11.709123 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa459 A jVZNhQOT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2019  11.719377      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa459 No such name A jVZNhQOT.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2020  11.720356 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4ee0 A jVZNhQOT.reddshrimpandherring.com.windomain.local
 2021  11.730023      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4ee0 No such name A jVZNhQOT.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2022  11.730929 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x7beb A ZtxW+iuv.reddshrimpandherring.com
 2030  11.775329      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x7beb No such name A ZtxW+iuv.reddshrimpandherring.com SOA a.gtld-servers.net
 2031  11.776329 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3d3a A ZtxW+iuv.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2032  11.787119      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x3d3a No such name A ZtxW+iuv.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2033  11.788019 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xdff5 A ZtxW+iuv.reddshrimpandherring.com.windomain.local
 2035  11.801432      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xdff5 No such name A ZtxW+iuv.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2036  11.802726 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9b29 A UWyNwFJZ.reddshrimpandherring.com
 2037  11.846077      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9b29 No such name A UWyNwFJZ.reddshrimpandherring.com SOA a.gtld-servers.net
 2038  11.847114 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1d0c A UWyNwFJZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2039  11.857364      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x1d0c No such name A UWyNwFJZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2040  11.858206 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x958f A UWyNwFJZ.reddshrimpandherring.com.windomain.local
 2041  11.869653      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x958f No such name A UWyNwFJZ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2042  11.870534 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x3a30 A RntkbnNf.reddshrimpandherring.com
 2043  11.921106  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x3a30 No such name A RntkbnNf.reddshrimpandherring.com SOA a.gtld-servers.net
 2044  11.922284 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xec57 A RntkbnNf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2045  11.971614  18.217.1.57 → 192.168.38.104 DNS 203 Standard query response 0xec57 No such name A RntkbnNf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2046  11.972605 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local
 2047  12.021881  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0xabb9 No such name A RntkbnNf.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2048  12.022971 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xcc58 A MBJKiAFX.reddshrimpandherring.com
 2049  12.033860      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xcc58 No such name A MBJKiAFX.reddshrimpandherring.com SOA a.gtld-servers.net
 2050  12.034685 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xdc92 A MBJKiAFX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2051  12.046873      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xdc92 No such name A MBJKiAFX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2052  12.047687 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0f9b A MBJKiAFX.reddshrimpandherring.com.windomain.local
 2053  12.057067      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0f9b No such name A MBJKiAFX.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2054  12.057925 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xef9b A ZLRLdSKq.reddshrimpandherring.com
 2055  12.100136      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xef9b No such name A ZLRLdSKq.reddshrimpandherring.com SOA a.gtld-servers.net
 2058  12.104124 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xef14 A ZLRLdSKq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2059  12.128945      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xef14 No such name A ZLRLdSKq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2060  12.129996 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa19e A ZLRLdSKq.reddshrimpandherring.com.windomain.local
 2061  12.139591      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa19e No such name A ZLRLdSKq.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2062  12.140777 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa047 A ++FVriJb.reddshrimpandherring.com
 2071  12.212527      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa047 No such name A ++FVriJb.reddshrimpandherring.com SOA a.gtld-servers.net
 2072  12.213553 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xca8b A ++FVriJb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2073  12.224048      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xca8b No such name A ++FVriJb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2074  12.224888 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0d68 A ++FVriJb.reddshrimpandherring.com.windomain.local
 2075  12.234288      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0d68 No such name A ++FVriJb.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2076  12.235205 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xfcfc A S8mxGlhF.reddshrimpandherring.com
 2077  12.277691      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xfcfc No such name A S8mxGlhF.reddshrimpandherring.com SOA a.gtld-servers.net
 2078  12.278703 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb3ea A S8mxGlhF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2079  12.291212      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb3ea No such name A S8mxGlhF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2080  12.292118 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd0f7 A S8mxGlhF.reddshrimpandherring.com.windomain.local
 2081  12.301735      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd0f7 No such name A S8mxGlhF.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2082  12.302648 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x5741 A 7cNUr26D.reddshrimpandherring.com
 2083  12.314249      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x5741 No such name A 7cNUr26D.reddshrimpandherring.com SOA a.gtld-servers.net
 2084  12.315334 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x98e6 A 7cNUr26D.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2085  12.326077      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x98e6 No such name A 7cNUr26D.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2086  12.327047 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3fef A 7cNUr26D.reddshrimpandherring.com.windomain.local
 2087  12.336513      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3fef No such name A 7cNUr26D.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2088  12.337530 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3720 A mC90A9B0.reddshrimpandherring.com
 2089  12.349286      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3720 No such name A mC90A9B0.reddshrimpandherring.com SOA a.gtld-servers.net
 2090  12.350245 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5a19 A mC90A9B0.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2091  12.361238      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x5a19 No such name A mC90A9B0.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2092  12.362080 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc4e7 A mC90A9B0.reddshrimpandherring.com.windomain.local
 2093  12.371668      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc4e7 No such name A mC90A9B0.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2094  12.372554 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x5731 A a3P9pD4z.reddshrimpandherring.com
 2095  12.413993      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x5731 No such name A a3P9pD4z.reddshrimpandherring.com SOA a.gtld-servers.net
 2096  12.415007 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe4c0 A a3P9pD4z.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2142  12.433251      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xe4c0 No such name A a3P9pD4z.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2146  12.434132 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3135 A a3P9pD4z.reddshrimpandherring.com.windomain.local
 2153  12.443682      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3135 No such name A a3P9pD4z.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2154  12.444693 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6a8b A mq6ivImu.reddshrimpandherring.com
 2163  12.486314      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6a8b No such name A mq6ivImu.reddshrimpandherring.com SOA a.gtld-servers.net
 2164  12.487383 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5843 A mq6ivImu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2165  12.497939      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x5843 No such name A mq6ivImu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2166  12.498738 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7dd5 A mq6ivImu.reddshrimpandherring.com.windomain.local
 2167  12.508244      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7dd5 No such name A mq6ivImu.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2168  12.509375 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xf772 A ZSdLCe14.reddshrimpandherring.com
 2169  12.520748      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xf772 No such name A ZSdLCe14.reddshrimpandherring.com SOA a.gtld-servers.net
 2170  12.521648 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x13ef A ZSdLCe14.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2172  12.532318      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x13ef No such name A ZSdLCe14.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2178  12.533661 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3d7b A ZSdLCe14.reddshrimpandherring.com.windomain.local
 2180  12.543173      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3d7b No such name A ZSdLCe14.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2181  12.544775 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc495 A fIGPcLax.reddshrimpandherring.com
 2182  12.558630      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc495 No such name A fIGPcLax.reddshrimpandherring.com SOA a.gtld-servers.net
 2183  12.559588 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x81ee A fIGPcLax.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2184  12.572040      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x81ee No such name A fIGPcLax.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2185  12.572870 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x17d5 A fIGPcLax.reddshrimpandherring.com.windomain.local
 2186  12.582673      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x17d5 No such name A fIGPcLax.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2188  12.583711 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8f9a A 32eplH1b.reddshrimpandherring.com
 2189  12.595273      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8f9a No such name A 32eplH1b.reddshrimpandherring.com SOA a.gtld-servers.net
 2190  12.596110 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa7f7 A 32eplH1b.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2191  12.606288      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa7f7 No such name A 32eplH1b.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2192  12.607224 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xeef0 A 32eplH1b.reddshrimpandherring.com.windomain.local
 2193  12.616666      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xeef0 No such name A 32eplH1b.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2194  12.617601 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xca1d A K7ZFuDrG.reddshrimpandherring.com
 2195  12.629439      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xca1d No such name A K7ZFuDrG.reddshrimpandherring.com SOA a.gtld-servers.net
 2196  12.630396 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa7e6 A K7ZFuDrG.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2197  12.648633      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa7e6 No such name A K7ZFuDrG.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2198  12.649635 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3fcf A K7ZFuDrG.reddshrimpandherring.com.windomain.local
 2199  12.659179      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3fcf No such name A K7ZFuDrG.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2200  12.659987 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc1dd A du8XDVin.reddshrimpandherring.com
 2201  12.728061      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc1dd No such name A du8XDVin.reddshrimpandherring.com SOA a.gtld-servers.net
 2202  12.729083 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1b74 A du8XDVin.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2203  12.756037      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x1b74 No such name A du8XDVin.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2204  12.757023 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf089 A du8XDVin.reddshrimpandherring.com.windomain.local
 2205  12.768353      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf089 No such name A du8XDVin.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2206  12.769409 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x075a A Kj9GKCI/.reddshrimpandherring.com
 2207  12.780710      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x075a No such name A Kj9GKCI/.reddshrimpandherring.com SOA a.gtld-servers.net
 2208  12.781683 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xea04 A Kj9GKCI/.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2209  12.792142      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xea04 No such name A Kj9GKCI/.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2210  12.792933 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xdab6 A Kj9GKCI/.reddshrimpandherring.com.windomain.local
 2211  12.802466      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xdab6 No such name A Kj9GKCI/.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2212  12.803288 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x653a A bxl/NUmd.reddshrimpandherring.com
 2213  12.814698      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x653a No such name A bxl/NUmd.reddshrimpandherring.com SOA a.gtld-servers.net
 2214  12.815518 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb247 A bxl/NUmd.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2215  12.836226      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xb247 No such name A bxl/NUmd.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2216  12.837026 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x552a A bxl/NUmd.reddshrimpandherring.com.windomain.local
 2217  12.846570      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x552a No such name A bxl/NUmd.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2218  12.847457 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x02a8 A 5lZkiKa3.reddshrimpandherring.com
 2219  12.858547      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x02a8 No such name A 5lZkiKa3.reddshrimpandherring.com SOA a.gtld-servers.net
 2220  12.859359 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8ee6 A 5lZkiKa3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2221  12.869916      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8ee6 No such name A 5lZkiKa3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2222  12.871111 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0d0f A 5lZkiKa3.reddshrimpandherring.com.windomain.local
 2225  12.882562      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0d0f No such name A 5lZkiKa3.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2226  12.883462 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8cce A tPwzBtD8.reddshrimpandherring.com
 2227  12.894825      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8cce No such name A tPwzBtD8.reddshrimpandherring.com SOA a.gtld-servers.net
 2228  12.895718 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa26c A tPwzBtD8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2229  12.906349      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xa26c No such name A tPwzBtD8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2230  12.907157 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x756e A tPwzBtD8.reddshrimpandherring.com.windomain.local
 2231  12.916715      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x756e No such name A tPwzBtD8.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2232  12.917853 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9adc A dt0idpyB.reddshrimpandherring.com
 2240  12.962992      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9adc No such name A dt0idpyB.reddshrimpandherring.com SOA a.gtld-servers.net
 2241  12.964096 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0ff6 A dt0idpyB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2242  12.982466      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x0ff6 No such name A dt0idpyB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2243  12.983452 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf694 A dt0idpyB.reddshrimpandherring.com.windomain.local
 2244  12.992887      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf694 No such name A dt0idpyB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2245  12.993849 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x1589 A GY3VancC.reddshrimpandherring.com
 2247  13.015299      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x1589 No such name A GY3VancC.reddshrimpandherring.com SOA a.gtld-servers.net
 2248  13.016430 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x87b8 A GY3VancC.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2249  13.027276      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x87b8 No such name A GY3VancC.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2250  13.028073 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4d5b A GY3VancC.reddshrimpandherring.com.windomain.local
 2251  13.037356      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4d5b No such name A GY3VancC.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2252  13.038572 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x57e6 A pFnvUGtZ.reddshrimpandherring.com
 2253  13.108215      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x57e6 No such name A pFnvUGtZ.reddshrimpandherring.com SOA a.gtld-servers.net
 2254  13.109412 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8ab0 A pFnvUGtZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2255  13.119908      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8ab0 No such name A pFnvUGtZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2256  13.120896 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc764 A pFnvUGtZ.reddshrimpandherring.com.windomain.local
 2257  13.130438      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc764 No such name A pFnvUGtZ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2258  13.131416 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4adc A ttY3YINW.reddshrimpandherring.com
 2259  13.142525      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4adc No such name A ttY3YINW.reddshrimpandherring.com SOA a.gtld-servers.net
 2260  13.143618 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5e02 A ttY3YINW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2261  13.154240      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x5e02 No such name A ttY3YINW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2262  13.155153 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb901 A ttY3YINW.reddshrimpandherring.com.windomain.local
 2263  13.164580      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb901 No such name A ttY3YINW.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2264  13.165475 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xdcf8 A gie24mjc.reddshrimpandherring.com
 2265  13.186989      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xdcf8 No such name A gie24mjc.reddshrimpandherring.com SOA a.gtld-servers.net
 2266  13.188032 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x88ea A gie24mjc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2267  13.200369      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x88ea No such name A gie24mjc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2268  13.201239 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3ae9 A gie24mjc.reddshrimpandherring.com.windomain.local
 2269  13.212520      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3ae9 No such name A gie24mjc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2270  13.213412 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3e65 A NEQMIULq.reddshrimpandherring.com
 2271  13.234025      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3e65 No such name A NEQMIULq.reddshrimpandherring.com SOA a.gtld-servers.net
 2272  13.235013 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcf93 A NEQMIULq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2273  13.245503      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xcf93 No such name A NEQMIULq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2274  13.246285 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1f64 A NEQMIULq.reddshrimpandherring.com.windomain.local
 2275  13.257815      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1f64 No such name A NEQMIULq.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2276  13.258971 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4336 A 2fHPxt2H.reddshrimpandherring.com
 2277  13.269809      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4336 No such name A 2fHPxt2H.reddshrimpandherring.com SOA a.gtld-servers.net
 2278  13.270829 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd2fc A 2fHPxt2H.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2281  13.281354      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xd2fc No such name A 2fHPxt2H.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2282  13.282456 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x844a A 2fHPxt2H.reddshrimpandherring.com.windomain.local
 2283  13.293875      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x844a No such name A 2fHPxt2H.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2284  13.294798 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x1f6c A +hFPfydr.reddshrimpandherring.com
 2292  13.339425      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x1f6c No such name A +hFPfydr.reddshrimpandherring.com SOA a.gtld-servers.net
 2293  13.340470 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9483 A +hFPfydr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2295  13.350966      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x9483 No such name A +hFPfydr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2296  13.352145 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc5e9 A +hFPfydr.reddshrimpandherring.com.windomain.local
 2297  13.363684      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc5e9 No such name A +hFPfydr.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2298  13.364914 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x377f A CormfRcj.reddshrimpandherring.com
 2299  13.376253      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x377f No such name A CormfRcj.reddshrimpandherring.com SOA a.gtld-servers.net
 2300  13.377150 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x49e3 A CormfRcj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2303  13.387353      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x49e3 No such name A CormfRcj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2304  13.388223 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc00a A CormfRcj.reddshrimpandherring.com.windomain.local
 2305  13.398023      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc00a No such name A CormfRcj.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2306  13.398899 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb0b1 A OdUL5++a.reddshrimpandherring.com
 2307  13.440951      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb0b1 No such name A OdUL5++a.reddshrimpandherring.com SOA a.gtld-servers.net
 2308  13.442055 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8227 A OdUL5++a.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2309  13.452446      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8227 No such name A OdUL5++a.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2310  13.453335 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf0d1 A OdUL5++a.reddshrimpandherring.com.windomain.local
 2311  13.464836      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf0d1 No such name A OdUL5++a.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2312  13.465734 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xcd9d A 44ujVBuF.reddshrimpandherring.com
 2313  13.508731      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xcd9d No such name A 44ujVBuF.reddshrimpandherring.com SOA a.gtld-servers.net
 2314  13.509734 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6f29 A 44ujVBuF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2315  13.520262      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x6f29 No such name A 44ujVBuF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2316  13.521277 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5258 A 44ujVBuF.reddshrimpandherring.com.windomain.local
 2317  13.530793      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5258 No such name A 44ujVBuF.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2318  13.531862 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x1aad A bM+BQ8dN.reddshrimpandherring.com
 2319  13.542881      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x1aad No such name A bM+BQ8dN.reddshrimpandherring.com SOA a.gtld-servers.net
 2320  13.543705 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2d45 A bM+BQ8dN.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2321  13.554120      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2d45 No such name A bM+BQ8dN.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2322  13.554911 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x308b A bM+BQ8dN.reddshrimpandherring.com.windomain.local
 2323  13.564517      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x308b No such name A bM+BQ8dN.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2324  13.565473 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2734 A 8XyIkzP+.reddshrimpandherring.com
 2325  13.609468      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2734 No such name A 8XyIkzP+.reddshrimpandherring.com SOA a.gtld-servers.net
 2326  13.610500 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2ec7 A 8XyIkzP+.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2327  13.624396      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2ec7 No such name A 8XyIkzP+.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2328  13.625329 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x8806 A 8XyIkzP+.reddshrimpandherring.com.windomain.local
 2329  13.634833      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x8806 No such name A 8XyIkzP+.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2330  13.636843 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3f69 A ruXuMxNJ.reddshrimpandherring.com
 2333  13.648084      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3f69 No such name A ruXuMxNJ.reddshrimpandherring.com SOA a.gtld-servers.net
 2334  13.649013 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x73ff A ruXuMxNJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2335  13.659317      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x73ff No such name A ruXuMxNJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2336  13.660312 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x164a A ruXuMxNJ.reddshrimpandherring.com.windomain.local
 2337  13.669657      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x164a No such name A ruXuMxNJ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2338  13.670746 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd836 A MjIGXIqy.reddshrimpandherring.com
 2339  13.684108      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd836 No such name A MjIGXIqy.reddshrimpandherring.com SOA a.gtld-servers.net
 2340  13.685109 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xec7d A MjIGXIqy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2348  13.696243      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xec7d No such name A MjIGXIqy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2349  13.697696 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1a76 A MjIGXIqy.reddshrimpandherring.com.windomain.local
 2350  13.707223      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1a76 No such name A MjIGXIqy.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2351  13.709340 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x50f6 A 05lusaWy.reddshrimpandherring.com
 2353  13.753754      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x50f6 No such name A 05lusaWy.reddshrimpandherring.com SOA a.gtld-servers.net
 2354  13.754840 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1c32 A 05lusaWy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2355  13.765691      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x1c32 No such name A 05lusaWy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2356  13.766917 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x255c A 05lusaWy.reddshrimpandherring.com.windomain.local
 2357  13.776306      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x255c No such name A 05lusaWy.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2358  13.777244 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x42a1 A IXbbtV+m.reddshrimpandherring.com
 2359  13.822126      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x42a1 No such name A IXbbtV+m.reddshrimpandherring.com SOA a.gtld-servers.net
 2360  13.823169 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe7cf A IXbbtV+m.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2361  13.835457      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xe7cf No such name A IXbbtV+m.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2362  13.836335 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9065 A IXbbtV+m.reddshrimpandherring.com.windomain.local
 2363  13.845905      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9065 No such name A IXbbtV+m.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2364  13.846767 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0a4d A 6tNHEBtX.reddshrimpandherring.com
 2365  13.890659      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0a4d No such name A 6tNHEBtX.reddshrimpandherring.com SOA a.gtld-servers.net
 2366  13.891855 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xfaec A 6tNHEBtX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2367  13.902326      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xfaec No such name A 6tNHEBtX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2368  13.903271 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5cd7 A 6tNHEBtX.reddshrimpandherring.com.windomain.local
 2369  13.914550      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5cd7 No such name A 6tNHEBtX.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2370  13.915582 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x66f7 A LzIOPkPb.reddshrimpandherring.com
 2371  13.937394      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x66f7 No such name A LzIOPkPb.reddshrimpandherring.com SOA a.gtld-servers.net
 2372  13.938451 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x269f A LzIOPkPb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2373  13.949038      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x269f No such name A LzIOPkPb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2374  13.950020 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x8576 A LzIOPkPb.reddshrimpandherring.com.windomain.local
 2375  13.959562      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x8576 No such name A LzIOPkPb.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2376  13.960458 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe998 A gxp8M51b.reddshrimpandherring.com
 2379  14.028094      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe998 No such name A gxp8M51b.reddshrimpandherring.com SOA a.gtld-servers.net
 2380  14.029124 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x54c5 A gxp8M51b.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2381  14.039530      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x54c5 No such name A gxp8M51b.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2382  14.041982 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9212 A gxp8M51b.reddshrimpandherring.com.windomain.local
 2383  14.052081      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9212 No such name A gxp8M51b.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2384  14.053088 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x70d3 A +nB4/jzJ.reddshrimpandherring.com
 2391  14.064345      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x70d3 No such name A +nB4/jzJ.reddshrimpandherring.com SOA a.gtld-servers.net
 2392  14.065411 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xbd6b A +nB4/jzJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2394  14.076600      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xbd6b No such name A +nB4/jzJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2395  14.077717 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7a8e A +nB4/jzJ.reddshrimpandherring.com.windomain.local
 2396  14.087321      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7a8e No such name A +nB4/jzJ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2397  14.088413 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x462d A uXhVF4ys.reddshrimpandherring.com
 2398  14.099198      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x462d No such name A uXhVF4ys.reddshrimpandherring.com SOA a.gtld-servers.net
 2399  14.100211 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3fd1 A uXhVF4ys.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2400  14.110706      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3fd1 No such name A uXhVF4ys.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2401  14.113393 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9336 A uXhVF4ys.reddshrimpandherring.com.windomain.local
 2403  14.122744      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9336 No such name A uXhVF4ys.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2404  14.123842 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x68e1 A GJlKZrN+.reddshrimpandherring.com
 2405  14.192140      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x68e1 No such name A GJlKZrN+.reddshrimpandherring.com SOA a.gtld-servers.net
 2406  14.193241 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7087 A GJlKZrN+.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2407  14.211699      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7087 No such name A GJlKZrN+.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2408  14.212713 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x67e9 A GJlKZrN+.reddshrimpandherring.com.windomain.local
 2409  14.222388      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x67e9 No such name A GJlKZrN+.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2410  14.223877 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa67e A 282DOxFJ.reddshrimpandherring.com
 2411  14.244708      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa67e No such name A 282DOxFJ.reddshrimpandherring.com SOA a.gtld-servers.net
 2412  14.245727 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5f42 A 282DOxFJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2413  14.258153      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x5f42 No such name A 282DOxFJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2414  14.259080 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3b4c A 282DOxFJ.reddshrimpandherring.com.windomain.local
 2415  14.268682      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3b4c No such name A 282DOxFJ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2416  14.269918 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x1378 A zpt1YuKN.reddshrimpandherring.com
 2417  14.314265      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x1378 No such name A zpt1YuKN.reddshrimpandherring.com SOA a.gtld-servers.net
 2418  14.315290 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5009 A zpt1YuKN.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2419  14.327898      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x5009 No such name A zpt1YuKN.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2420  14.328716 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xce0c A zpt1YuKN.reddshrimpandherring.com.windomain.local
 2421  14.338251      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xce0c No such name A zpt1YuKN.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2422  14.339136 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x73bf A NRsUAHXx.reddshrimpandherring.com
 2425  14.383889      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x73bf No such name A NRsUAHXx.reddshrimpandherring.com SOA a.gtld-servers.net
 2426  14.384959 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x72ed A NRsUAHXx.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2427  14.397452      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x72ed No such name A NRsUAHXx.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2428  14.398424 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xfdaf A NRsUAHXx.reddshrimpandherring.com.windomain.local
 2432  14.407790      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xfdaf No such name A NRsUAHXx.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2436  14.408745 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8171 A oDIrXLVR.reddshrimpandherring.com
 2439  14.477854      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8171 No such name A oDIrXLVR.reddshrimpandherring.com SOA a.gtld-servers.net
 2440  14.478924 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2367 A oDIrXLVR.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2441  14.491349      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x2367 No such name A oDIrXLVR.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2442  14.492508 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb782 A oDIrXLVR.reddshrimpandherring.com.windomain.local
 2443  14.502069      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb782 No such name A oDIrXLVR.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2444  14.503146 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x531d A M3hmMWxf.reddshrimpandherring.com
 2445  14.553435  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x531d No such name A M3hmMWxf.reddshrimpandherring.com SOA a.gtld-servers.net
 2446  14.554475 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0x3bd6 A M3hmMWxf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2447  14.604708  18.217.1.57 → 192.168.38.104 DNS 203 Standard query response 0x3bd6 No such name A M3hmMWxf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2448  14.605726 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local
 2671  14.657185  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x9e21 No such name A M3hmMWxf.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2672  14.658202 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xfd9e A Mk5HboDA.reddshrimpandherring.com
 2796  14.670078      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xfd9e No such name A Mk5HboDA.reddshrimpandherring.com SOA a.gtld-servers.net
 2798  14.670861 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2fda A Mk5HboDA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2842  14.681370      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2fda No such name A Mk5HboDA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2843  14.682230 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3790 A Mk5HboDA.reddshrimpandherring.com.windomain.local
 2853  14.693639      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3790 No such name A Mk5HboDA.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2854  14.694663 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0af7 A JX5nT3mx.reddshrimpandherring.com
 2855  14.708117      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0af7 No such name A JX5nT3mx.reddshrimpandherring.com SOA a.gtld-servers.net
 2856  14.709127 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb1be A JX5nT3mx.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2857  14.721452      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb1be No such name A JX5nT3mx.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2858  14.722383 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd087 A JX5nT3mx.reddshrimpandherring.com.windomain.local
 2859  14.733913      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd087 No such name A JX5nT3mx.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2860  14.734902 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x17e9 A Q9yUm/uO.reddshrimpandherring.com
 2867  14.746796      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x17e9 No such name A Q9yUm/uO.reddshrimpandherring.com SOA a.gtld-servers.net
 2868  14.750959 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x597c A Q9yUm/uO.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2870  14.771323      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x597c No such name A Q9yUm/uO.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2871  14.772895 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xe559 A Q9yUm/uO.reddshrimpandherring.com.windomain.local
 2872  14.782415      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xe559 No such name A Q9yUm/uO.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2873  14.783475 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb72a A GBsIaOVw.reddshrimpandherring.com
 2875  14.826323      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb72a No such name A GBsIaOVw.reddshrimpandherring.com SOA a.gtld-servers.net
 2876  14.827382 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9b59 A GBsIaOVw.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2877  14.837703      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x9b59 No such name A GBsIaOVw.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2878  14.838792 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2673 A GBsIaOVw.reddshrimpandherring.com.windomain.local
 2879  14.850243      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2673 No such name A GBsIaOVw.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2880  14.851410 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xdbf8 A udbwL8HA.reddshrimpandherring.com
 2881  14.872778      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xdbf8 No such name A udbwL8HA.reddshrimpandherring.com SOA a.gtld-servers.net
 2882  14.873833 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1e52 A udbwL8HA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2883  14.884009      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x1e52 No such name A udbwL8HA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2884  14.884906 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf8bd A udbwL8HA.reddshrimpandherring.com.windomain.local
 2885  14.894557      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf8bd No such name A udbwL8HA.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2886  14.895534 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6966 A UtR5YJk0.reddshrimpandherring.com
 2887  14.908683      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6966 No such name A UtR5YJk0.reddshrimpandherring.com SOA a.gtld-servers.net
 2888  14.909629 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9dbc A UtR5YJk0.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2889  14.920635      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x9dbc No such name A UtR5YJk0.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2890  14.921518 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x247f A UtR5YJk0.reddshrimpandherring.com.windomain.local
 2891  14.931100      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x247f No such name A UtR5YJk0.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2892  14.931969 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x70d2 A hTid4evh.reddshrimpandherring.com
 2893  14.944898      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x70d2 No such name A hTid4evh.reddshrimpandherring.com SOA a.gtld-servers.net
 2894  14.945893 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8e3b A hTid4evh.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2895  14.956013      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8e3b No such name A hTid4evh.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2896  14.956822 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x213c A hTid4evh.reddshrimpandherring.com.windomain.local
 2897  14.966220      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x213c No such name A hTid4evh.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2898  14.967126 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2872 A ky4GGyGX.reddshrimpandherring.com
 2899  15.010155      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2872 No such name A ky4GGyGX.reddshrimpandherring.com SOA a.gtld-servers.net
 2900  15.011162 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc256 A ky4GGyGX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2901  15.021932      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc256 No such name A ky4GGyGX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2902  15.023223 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4f42 A ky4GGyGX.reddshrimpandherring.com.windomain.local
 2905  15.032567      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4f42 No such name A ky4GGyGX.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2906  15.033562 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0c11 A XJbKd2Gc.reddshrimpandherring.com
 2909  15.077227      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0c11 No such name A XJbKd2Gc.reddshrimpandherring.com SOA a.gtld-servers.net
 2910  15.078436 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x653b A XJbKd2Gc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2916  15.096953      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x653b No such name A XJbKd2Gc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2917  15.098515 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc841 A XJbKd2Gc.reddshrimpandherring.com.windomain.local
 2918  15.108105      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc841 No such name A XJbKd2Gc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2919  15.109169 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x164c A yHINlfmQ.reddshrimpandherring.com
 2920  15.120423      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x164c No such name A yHINlfmQ.reddshrimpandherring.com SOA a.gtld-servers.net
 2921  15.121449 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa88b A yHINlfmQ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2922  15.131944      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xa88b No such name A yHINlfmQ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2924  15.132848 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x8885 A yHINlfmQ.reddshrimpandherring.com.windomain.local
 2925  15.142971      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x8885 No such name A yHINlfmQ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2926  15.143911 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa80b A TerVtBw4.reddshrimpandherring.com
 2927  15.157929      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa80b No such name A TerVtBw4.reddshrimpandherring.com SOA a.gtld-servers.net
 2928  15.158927 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x062e A TerVtBw4.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2929  15.169566      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x062e No such name A TerVtBw4.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2930  15.170552 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5e37 A TerVtBw4.reddshrimpandherring.com.windomain.local
 2931  15.180390      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5e37 No such name A TerVtBw4.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2932  15.181388 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc778 A rgiQTZeg.reddshrimpandherring.com
 2933  15.202138      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc778 No such name A rgiQTZeg.reddshrimpandherring.com SOA a.gtld-servers.net
 2934  15.203311 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4330 A rgiQTZeg.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2935  15.213733      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x4330 No such name A rgiQTZeg.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2936  15.214694 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0e09 A rgiQTZeg.reddshrimpandherring.com.windomain.local
 2937  15.224051      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0e09 No such name A rgiQTZeg.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2938  15.225081 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0d31 A mqqZKNFc.reddshrimpandherring.com
 2939  15.238664      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0d31 No such name A mqqZKNFc.reddshrimpandherring.com SOA a.gtld-servers.net
 2940  15.239688 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0f65 A mqqZKNFc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2941  15.250423      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x0f65 No such name A mqqZKNFc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2942  15.251299 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xba98 A mqqZKNFc.reddshrimpandherring.com.windomain.local
 2943  15.260805      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xba98 No such name A mqqZKNFc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2944  15.261977 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x77b2 A hurTYxbn.reddshrimpandherring.com
 2945  15.285573      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x77b2 No such name A hurTYxbn.reddshrimpandherring.com SOA a.gtld-servers.net
 2946  15.286613 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9553 A hurTYxbn.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2949  15.307441      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x9553 No such name A hurTYxbn.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2950  15.308397 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xee84 A hurTYxbn.reddshrimpandherring.com.windomain.local
 2951  15.317929      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xee84 No such name A hurTYxbn.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2952  15.318998 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x42d2 A M2yc0p/K.reddshrimpandherring.com
 2953  15.332451      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x42d2 No such name A M2yc0p/K.reddshrimpandherring.com SOA a.gtld-servers.net
 2954  15.333539 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6837 A M2yc0p/K.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2955  15.344117      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x6837 No such name A M2yc0p/K.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2956  15.345151 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xef0a A M2yc0p/K.reddshrimpandherring.com.windomain.local
 2960  15.354688      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xef0a No such name A M2yc0p/K.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2964  15.355837 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x99d4 A k9hfHtFr.reddshrimpandherring.com
 2965  15.366541      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x99d4 No such name A k9hfHtFr.reddshrimpandherring.com SOA a.gtld-servers.net
 2966  15.367737 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x44f0 A k9hfHtFr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2968  15.378065      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x44f0 No such name A k9hfHtFr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2969  15.379955 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2ba7 A k9hfHtFr.reddshrimpandherring.com.windomain.local
 2970  15.389290      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2ba7 No such name A k9hfHtFr.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2971  15.393243 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x960f A 3gEtiL6U.reddshrimpandherring.com
 2973  15.436860      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x960f No such name A 3gEtiL6U.reddshrimpandherring.com SOA a.gtld-servers.net
 2974  15.437892 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3268 A 3gEtiL6U.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2975  15.448283      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3268 No such name A 3gEtiL6U.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2976  15.449483 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0e80 A 3gEtiL6U.reddshrimpandherring.com.windomain.local
 2977  15.459099      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0e80 No such name A 3gEtiL6U.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2980  15.460648 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x10a7 A J+3dTlY7.reddshrimpandherring.com
 2981  15.481419      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x10a7 No such name A J+3dTlY7.reddshrimpandherring.com SOA a.gtld-servers.net
 2982  15.482424 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xaffe A J+3dTlY7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2983  15.495119      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xaffe No such name A J+3dTlY7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2984  15.496065 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcd9d A J+3dTlY7.reddshrimpandherring.com.windomain.local
 2985  15.507404      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcd9d No such name A J+3dTlY7.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2986  15.508446 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xcf9b A WBYd1saM.reddshrimpandherring.com
 2994  15.529943      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xcf9b No such name A WBYd1saM.reddshrimpandherring.com SOA a.gtld-servers.net
 2995  15.531223 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0633 A WBYd1saM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2996  15.541711      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0633 No such name A WBYd1saM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 2997  15.542672 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4fa1 A WBYd1saM.reddshrimpandherring.com.windomain.local
 2998  15.554131      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4fa1 No such name A WBYd1saM.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2999  15.555311 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4e64 A UykMEuPb.reddshrimpandherring.com
 3001  15.566096      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4e64 No such name A UykMEuPb.reddshrimpandherring.com SOA a.gtld-servers.net
 3002  15.567046 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xbda5 A UykMEuPb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3003  15.579430      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xbda5 No such name A UykMEuPb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3004  15.580408 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6c98 A UykMEuPb.reddshrimpandherring.com.windomain.local
 3005  15.589863      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6c98 No such name A UykMEuPb.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3006  15.590810 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x04af A usspm1e3.reddshrimpandherring.com
 3009  15.633687      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x04af No such name A usspm1e3.reddshrimpandherring.com SOA a.gtld-servers.net
 3010  15.634687 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x380d A usspm1e3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3011  15.645239      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x380d No such name A usspm1e3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3012  15.646200 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4a86 A usspm1e3.reddshrimpandherring.com.windomain.local
 3013  15.655588      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4a86 No such name A usspm1e3.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3014  15.656615 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb620 A n6LAUOHr.reddshrimpandherring.com
 3015  15.668039      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb620 No such name A n6LAUOHr.reddshrimpandherring.com SOA a.gtld-servers.net
 3016  15.668972 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xec41 A n6LAUOHr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3023  15.679703      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xec41 No such name A n6LAUOHr.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3024  15.681111 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa04b A n6LAUOHr.reddshrimpandherring.com.windomain.local
 3026  15.694763      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa04b No such name A n6LAUOHr.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3027  15.695890 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x880a A a7fKrq7b.reddshrimpandherring.com
 3031  15.737630      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x880a No such name A a7fKrq7b.reddshrimpandherring.com SOA a.gtld-servers.net
 3032  15.739543 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf520 A a7fKrq7b.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3033  15.750179      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xf520 No such name A a7fKrq7b.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3034  15.751180 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x33b3 A a7fKrq7b.reddshrimpandherring.com.windomain.local
 3035  15.762702      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x33b3 No such name A a7fKrq7b.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3036  15.763745 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9b5d A NLWqvffb.reddshrimpandherring.com
 3040  15.775492      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9b5d No such name A NLWqvffb.reddshrimpandherring.com SOA a.gtld-servers.net
 3044  15.776706 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xdc55 A NLWqvffb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3046  15.787715      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xdc55 No such name A NLWqvffb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3047  15.788680 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xccc1 A NLWqvffb.reddshrimpandherring.com.windomain.local
 3048  15.798163      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xccc1 No such name A NLWqvffb.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3049  15.802099 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6846 A jA7cwYZS.reddshrimpandherring.com
 3050  15.815855      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6846 No such name A jA7cwYZS.reddshrimpandherring.com SOA a.gtld-servers.net
 3051  15.816884 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8a7f A jA7cwYZS.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3053  15.835527      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x8a7f No such name A jA7cwYZS.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3054  15.836595 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x41f1 A jA7cwYZS.reddshrimpandherring.com.windomain.local
 3055  15.846061      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x41f1 No such name A jA7cwYZS.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3056  15.847105 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9b09 A YQoNqdqR.reddshrimpandherring.com
 3057  15.857967      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9b09 No such name A YQoNqdqR.reddshrimpandherring.com SOA a.gtld-servers.net
 3058  15.858910 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2bcc A YQoNqdqR.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3059  15.871340      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2bcc No such name A YQoNqdqR.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3060  15.872381 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x693e A YQoNqdqR.reddshrimpandherring.com.windomain.local
 3061  15.881876      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x693e No such name A YQoNqdqR.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3062  15.882859 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2219 A bEJJWqvq.reddshrimpandherring.com
 3063  15.926520      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2219 No such name A bEJJWqvq.reddshrimpandherring.com SOA a.gtld-servers.net
 3064  15.927570 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcd61 A bEJJWqvq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3065  15.938181      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xcd61 No such name A bEJJWqvq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3066  15.939152 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1b93 A bEJJWqvq.reddshrimpandherring.com.windomain.local
 3067  15.948569      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1b93 No such name A bEJJWqvq.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3068  15.950588 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x735a A rIrbCl8t.reddshrimpandherring.com
 3071  15.996228      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x735a No such name A rIrbCl8t.reddshrimpandherring.com SOA a.gtld-servers.net
 3072  15.997288 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0d36 A rIrbCl8t.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3080  16.007650      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x0d36 No such name A rIrbCl8t.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3081  16.009764 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1551 A rIrbCl8t.reddshrimpandherring.com.windomain.local
 3082  16.023104      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1551 No such name A rIrbCl8t.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3083  16.024396 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x85cb A 2VPCMWzB.reddshrimpandherring.com
 3084  16.045574      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x85cb No such name A 2VPCMWzB.reddshrimpandherring.com SOA a.gtld-servers.net
 3085  16.046793 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe42f A 2VPCMWzB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3087  16.057283      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xe42f No such name A 2VPCMWzB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3088  16.058230 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf61f A 2VPCMWzB.reddshrimpandherring.com.windomain.local
 3089  16.067891      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf61f No such name A 2VPCMWzB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3090  16.068900 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb95c A vH/vJiy2.reddshrimpandherring.com
 3091  16.080105      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb95c No such name A vH/vJiy2.reddshrimpandherring.com SOA a.gtld-servers.net
 3092  16.081166 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa923 A vH/vJiy2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3093  16.091625      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xa923 No such name A vH/vJiy2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3094  16.092662 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb9a3 A vH/vJiy2.reddshrimpandherring.com.windomain.local
 3095  16.102202      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb9a3 No such name A vH/vJiy2.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3096  16.103384 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd0cb A e8bxxZ92.reddshrimpandherring.com
 3099  16.125166      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd0cb No such name A e8bxxZ92.reddshrimpandherring.com SOA a.gtld-servers.net
 3100  16.126172 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3018 A e8bxxZ92.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3101  16.136451      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3018 No such name A e8bxxZ92.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3102  16.137434 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7e01 A e8bxxZ92.reddshrimpandherring.com.windomain.local
 3103  16.148847      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7e01 No such name A e8bxxZ92.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3104  16.149906 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x05a3 A Sk7RnT+D.reddshrimpandherring.com
 3112  16.219010      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x05a3 No such name A Sk7RnT+D.reddshrimpandherring.com SOA a.gtld-servers.net
 3113  16.220198 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x97d4 A Sk7RnT+D.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3115  16.230582      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x97d4 No such name A Sk7RnT+D.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3116  16.231680 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc88c A Sk7RnT+D.reddshrimpandherring.com.windomain.local
 3117  16.241164      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc88c No such name A Sk7RnT+D.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3118  16.242084 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xfeb0 A CeBXXXFy.reddshrimpandherring.com
 3121  16.286578      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xfeb0 No such name A CeBXXXFy.reddshrimpandherring.com SOA a.gtld-servers.net
 3122  16.287935 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf1d3 A CeBXXXFy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3123  16.298640      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xf1d3 No such name A CeBXXXFy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3124  16.299555 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x31a7 A CeBXXXFy.reddshrimpandherring.com.windomain.local
 3125  16.308971      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x31a7 No such name A CeBXXXFy.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3126  16.309899 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3263 A 2Gu7zRXL.reddshrimpandherring.com
 3134  16.381807      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3263 No such name A 2Gu7zRXL.reddshrimpandherring.com SOA a.gtld-servers.net
 3135  16.382829 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6535 A 2Gu7zRXL.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3137  16.393465      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x6535 No such name A 2Gu7zRXL.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3138  16.394329 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0339 A 2Gu7zRXL.reddshrimpandherring.com.windomain.local
 3139  16.403885      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0339 No such name A 2Gu7zRXL.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3140  16.404809 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x99dd A ZnR3X2Rl.reddshrimpandherring.com
 3143  16.455193  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x99dd No such name A ZnR3X2Rl.reddshrimpandherring.com SOA a.gtld-servers.net
 3144  16.456229 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0x028b A ZnR3X2Rl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3152  16.505490  18.217.1.57 → 192.168.38.104 DNS 203 Standard query response 0x028b No such name A ZnR3X2Rl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3153  16.506492 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local
 3155  16.557035  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x2ee1 No such name A ZnR3X2Rl.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3156  16.558132 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9d9d A vQ6gMW/g.reddshrimpandherring.com
 3159  16.600383      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9d9d No such name A vQ6gMW/g.reddshrimpandherring.com SOA a.gtld-servers.net
 3160  16.601432 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xeecc A vQ6gMW/g.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3161  16.611797      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xeecc No such name A vQ6gMW/g.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3162  16.614241 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xaec7 A vQ6gMW/g.reddshrimpandherring.com.windomain.local
 3165  16.623692      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xaec7 No such name A vQ6gMW/g.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3167  16.624933 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb4d5 A q18YMnNi.reddshrimpandherring.com
 3171  16.638055      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb4d5 No such name A q18YMnNi.reddshrimpandherring.com SOA a.gtld-servers.net
 3172  16.646235 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5608 A q18YMnNi.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3174  16.658623      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x5608 No such name A q18YMnNi.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3175  16.659599 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xac87 A q18YMnNi.reddshrimpandherring.com.windomain.local
 3176  16.669121      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xac87 No such name A q18YMnNi.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3177  16.670061 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x65f4 A N9teS0Ov.reddshrimpandherring.com
 3178  16.681565      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x65f4 No such name A N9teS0Ov.reddshrimpandherring.com SOA a.gtld-servers.net
 3179  16.682723 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6b5c A N9teS0Ov.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3180  16.693003      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x6b5c No such name A N9teS0Ov.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3181  16.693822 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5cf0 A N9teS0Ov.reddshrimpandherring.com.windomain.local
 3183  16.703254      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5cf0 No such name A N9teS0Ov.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3184  16.704227 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x629a A FbzJBzzB.reddshrimpandherring.com
 3194  16.778173      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x629a No such name A FbzJBzzB.reddshrimpandherring.com SOA a.gtld-servers.net
 3195  16.780086 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc9c6 A FbzJBzzB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3196  16.790417      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc9c6 No such name A FbzJBzzB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3197  16.791286 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x57d2 A FbzJBzzB.reddshrimpandherring.com.windomain.local
 3198  16.800597      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x57d2 No such name A FbzJBzzB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3199  16.801740 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3bad A SmDzvZ71.reddshrimpandherring.com
 3201  16.812957      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3bad No such name A SmDzvZ71.reddshrimpandherring.com SOA a.gtld-servers.net
 3202  16.813955 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa9ef A SmDzvZ71.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3203  16.824202      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xa9ef No such name A SmDzvZ71.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3204  16.825093 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x13fa A SmDzvZ71.reddshrimpandherring.com.windomain.local
 3205  16.836507      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x13fa No such name A SmDzvZ71.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3206  16.837633 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x48e0 A PFD94NTp.reddshrimpandherring.com
 3209  16.905728      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x48e0 No such name A PFD94NTp.reddshrimpandherring.com SOA a.gtld-servers.net
 3210  16.906736 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcce6 A PFD94NTp.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3211  16.916999      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xcce6 No such name A PFD94NTp.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3214  16.917788 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x05d2 A PFD94NTp.reddshrimpandherring.com.windomain.local
 3220  16.927304      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x05d2 No such name A PFD94NTp.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3221  16.928391 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x82b6 A /ye5yTrK.reddshrimpandherring.com
 3222  16.970396      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x82b6 No such name A /ye5yTrK.reddshrimpandherring.com SOA a.gtld-servers.net
 3223  16.971436 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0054 A /ye5yTrK.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3225  16.984732      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0054 No such name A /ye5yTrK.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3226  16.985816 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb476 A /ye5yTrK.reddshrimpandherring.com.windomain.local
 3227  16.995149      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb476 No such name A /ye5yTrK.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3228  16.996463 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x53ad A EwV0JaDu.reddshrimpandherring.com
 3229  17.007835      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x53ad No such name A EwV0JaDu.reddshrimpandherring.com SOA a.gtld-servers.net
 3230  17.008822 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xabd9 A EwV0JaDu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3231  17.019607      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xabd9 No such name A EwV0JaDu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3232  17.020618 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xce07 A EwV0JaDu.reddshrimpandherring.com.windomain.local
 3235  17.031338      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xce07 No such name A EwV0JaDu.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3236  17.032503 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x032f A N5SEeqoS.reddshrimpandherring.com
 3244  17.103277      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x032f No such name A N5SEeqoS.reddshrimpandherring.com SOA a.gtld-servers.net
 3245  17.104314 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6779 A N5SEeqoS.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3246  17.114844      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x6779 No such name A N5SEeqoS.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3247  17.115851 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2c30 A N5SEeqoS.reddshrimpandherring.com.windomain.local
 3248  17.125293      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2c30 No such name A N5SEeqoS.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3249  17.126370 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb240 A aKMnpRkB.reddshrimpandherring.com
 3251  17.137507      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb240 No such name A aKMnpRkB.reddshrimpandherring.com SOA a.gtld-servers.net
 3252  17.138513 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9f69 A aKMnpRkB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3253  17.148819      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x9f69 No such name A aKMnpRkB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3254  17.149715 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xfbce A aKMnpRkB.reddshrimpandherring.com.windomain.local
 3255  17.159292      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xfbce No such name A aKMnpRkB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3256  17.160497 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xec44 A ttR69hjV.reddshrimpandherring.com
 3259  17.201309      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xec44 No such name A ttR69hjV.reddshrimpandherring.com SOA a.gtld-servers.net
 3260  17.202396 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd122 A ttR69hjV.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3261  17.212833      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xd122 No such name A ttR69hjV.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3262  17.213761 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9e10 A ttR69hjV.reddshrimpandherring.com.windomain.local
 3266  17.223199      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9e10 No such name A ttR69hjV.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3270  17.224390 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x87aa A fvMGQY0s.reddshrimpandherring.com
 3272  17.267757      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x87aa No such name A fvMGQY0s.reddshrimpandherring.com SOA a.gtld-servers.net
 3273  17.268851 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7b29 A fvMGQY0s.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3275  17.279224      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7b29 No such name A fvMGQY0s.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3276  17.280037 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x707f A fvMGQY0s.reddshrimpandherring.com.windomain.local
 3277  17.289373      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x707f No such name A fvMGQY0s.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3278  17.290524 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8fd9 A tTTnvTin.reddshrimpandherring.com
 3279  17.305261      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8fd9 No such name A tTTnvTin.reddshrimpandherring.com SOA a.gtld-servers.net
 3280  17.306546 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc7b2 A tTTnvTin.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3283  17.316967      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc7b2 No such name A tTTnvTin.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3284  17.318070 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf9b0 A tTTnvTin.reddshrimpandherring.com.windomain.local
 3285  17.329481      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf9b0 No such name A tTTnvTin.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3286  17.330617 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x1835 A SO4JxvAC.reddshrimpandherring.com
 3294  17.374323      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x1835 No such name A SO4JxvAC.reddshrimpandherring.com SOA a.gtld-servers.net
 3295  17.375375 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7f84 A SO4JxvAC.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3296  17.386372      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7f84 No such name A SO4JxvAC.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3297  17.387284 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2d08 A SO4JxvAC.reddshrimpandherring.com.windomain.local
 3298  17.398839      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2d08 No such name A SO4JxvAC.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3299  17.399906 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xcb3e A rAlDx9m7.reddshrimpandherring.com
 3300  17.413514      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xcb3e No such name A rAlDx9m7.reddshrimpandherring.com SOA a.gtld-servers.net
 3302  17.414589 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x16bd A rAlDx9m7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3303  17.424858      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x16bd No such name A rAlDx9m7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3304  17.425828 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x58a2 A rAlDx9m7.reddshrimpandherring.com.windomain.local
 3305  17.435353      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x58a2 No such name A rAlDx9m7.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3306  17.436457 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc7ee A fMHx7/PX.reddshrimpandherring.com
 3307  17.447719      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc7ee No such name A fMHx7/PX.reddshrimpandherring.com SOA a.gtld-servers.net
 3308  17.448699 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0472 A fMHx7/PX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3309  17.467466      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0472 No such name A fMHx7/PX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3310  17.468424 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4cf4 A fMHx7/PX.reddshrimpandherring.com.windomain.local
 3311  17.479662      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4cf4 No such name A fMHx7/PX.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3312  17.480908 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xeeed A yF3zkFuG.reddshrimpandherring.com
 3314  17.502402      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xeeed No such name A yF3zkFuG.reddshrimpandherring.com SOA a.gtld-servers.net
 3315  17.503356 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe845 A yF3zkFuG.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3316  17.521998      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xe845 No such name A yF3zkFuG.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3317  17.522964 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xfd6b A yF3zkFuG.reddshrimpandherring.com.windomain.local
 3321  17.534792      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xfd6b No such name A yF3zkFuG.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3322  17.535917 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2462 A UFq4pqcs.reddshrimpandherring.com
 3325  17.581963      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2462 No such name A UFq4pqcs.reddshrimpandherring.com SOA a.gtld-servers.net
 3327  17.583112 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9f81 A UFq4pqcs.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3331  17.593402      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x9f81 No such name A UFq4pqcs.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3332  17.594446 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcdcf A UFq4pqcs.reddshrimpandherring.com.windomain.local
 3333  17.604201      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcdcf No such name A UFq4pqcs.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3334  17.606039 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd790 A qmHFH7Ox.reddshrimpandherring.com
 3339  17.675878      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd790 No such name A qmHFH7Ox.reddshrimpandherring.com SOA a.gtld-servers.net
 3340  17.676909 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4cdf A qmHFH7Ox.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3347  17.697894      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x4cdf No such name A qmHFH7Ox.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3348  17.698971 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7370 A qmHFH7Ox.reddshrimpandherring.com.windomain.local
 3349  17.710447      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7370 No such name A qmHFH7Ox.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3350  17.712641 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb0cd A aHARNwGW.reddshrimpandherring.com
 3352  17.733918      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb0cd No such name A aHARNwGW.reddshrimpandherring.com SOA a.gtld-servers.net
 3353  17.737311 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x78ea A aHARNwGW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3354  17.747942      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x78ea No such name A aHARNwGW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3355  17.748942 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5f71 A aHARNwGW.reddshrimpandherring.com.windomain.local
 3356  17.758679      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5f71 No such name A aHARNwGW.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3357  17.759746 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x861e A a817nStX.reddshrimpandherring.com
 3361  17.802823      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x861e No such name A a817nStX.reddshrimpandherring.com SOA a.gtld-servers.net
 3362  17.803840 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9204 A a817nStX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3363  17.814553      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x9204 No such name A a817nStX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3364  17.815446 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xef22 A a817nStX.reddshrimpandherring.com.windomain.local
 3365  17.824961      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xef22 No such name A a817nStX.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3366  17.826441 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2969 A g9olPnyg.reddshrimpandherring.com
 3374  17.868760      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2969 No such name A g9olPnyg.reddshrimpandherring.com SOA a.gtld-servers.net
 3375  17.869811 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xbc7c A g9olPnyg.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3376  17.890501      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xbc7c No such name A g9olPnyg.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3377  17.891677 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5fd2 A g9olPnyg.reddshrimpandherring.com.windomain.local
 3378  17.902950      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5fd2 No such name A g9olPnyg.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3379  17.904090 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xbaa4 A PeOZIsZ8.reddshrimpandherring.com
 3381  17.915561      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xbaa4 No such name A PeOZIsZ8.reddshrimpandherring.com SOA a.gtld-servers.net
 3382  17.916438 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4fe8 A PeOZIsZ8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3384  17.927190      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x4fe8 No such name A PeOZIsZ8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3385  17.928233 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x41d4 A PeOZIsZ8.reddshrimpandherring.com.windomain.local
 3386  17.937724      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x41d4 No such name A PeOZIsZ8.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3387  17.938666 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x17d3 A pDt02i0L.reddshrimpandherring.com
 3391  17.979550      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x17d3 No such name A pDt02i0L.reddshrimpandherring.com SOA a.gtld-servers.net
 3392  17.980558 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd575 A pDt02i0L.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3393  17.991036      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xd575 No such name A pDt02i0L.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3395  17.992187 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa738 A pDt02i0L.reddshrimpandherring.com.windomain.local
 3399  18.001794      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa738 No such name A pDt02i0L.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3400  18.002876 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3728 A JnZqfeEB.reddshrimpandherring.com
 3402  18.044280      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3728 No such name A JnZqfeEB.reddshrimpandherring.com SOA a.gtld-servers.net
 3403  18.045309 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x256b A JnZqfeEB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3404  18.056107      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x256b No such name A JnZqfeEB.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3405  18.057133 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6f23 A JnZqfeEB.reddshrimpandherring.com.windomain.local
 3406  18.066553      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6f23 No such name A JnZqfeEB.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3407  18.067612 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8ef5 A LC5AR00m.reddshrimpandherring.com
 3411  18.146153      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8ef5 No such name A LC5AR00m.reddshrimpandherring.com SOA a.gtld-servers.net
 3412  18.147344 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xbd20 A LC5AR00m.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3415  18.159741      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xbd20 No such name A LC5AR00m.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3416  18.160854 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xe504 A LC5AR00m.reddshrimpandherring.com.windomain.local
 3421  18.170203      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xe504 No such name A LC5AR00m.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3422  18.171277 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa0ce A 5ga9YWjo.reddshrimpandherring.com
 3424  18.216409      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa0ce No such name A 5ga9YWjo.reddshrimpandherring.com SOA a.gtld-servers.net
 3425  18.217506 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb64c A 5ga9YWjo.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3426  18.228202      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb64c No such name A 5ga9YWjo.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3427  18.229171 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa294 A 5ga9YWjo.reddshrimpandherring.com.windomain.local
 3428  18.238523      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa294 No such name A 5ga9YWjo.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3429  18.239530 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x16f6 A YWRiZWVm.reddshrimpandherring.com
 3433  18.288746  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x16f6 No such name A YWRiZWVm.reddshrimpandherring.com SOA a.gtld-servers.net
 3434  18.289828 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xe7cb A YWRiZWVm.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3441  18.339039  18.217.1.57 → 192.168.38.104 DNS 205 Standard query response 0xe7cb No such name A YWRiZWVm.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3442  18.340155 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local
 3445  18.391844  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x2a4b No such name A YWRiZWVm.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3446  18.392915 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0c77 A T1Fqpwju.reddshrimpandherring.com
 3448  18.434762      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0c77 No such name A T1Fqpwju.reddshrimpandherring.com SOA a.gtld-servers.net
 3449  18.435791 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3b9d A T1Fqpwju.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3451  18.446300      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x3b9d No such name A T1Fqpwju.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3452  18.447294 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x60d8 A T1Fqpwju.reddshrimpandherring.com.windomain.local
 3453  18.456682      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x60d8 No such name A T1Fqpwju.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3454  18.457751 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa945 A qpvqibHM.reddshrimpandherring.com
 3455  18.469390      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa945 No such name A qpvqibHM.reddshrimpandherring.com SOA a.gtld-servers.net
 3456  18.470511 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xafff A qpvqibHM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3459  18.480935      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xafff No such name A qpvqibHM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3460  18.481827 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6b1e A qpvqibHM.reddshrimpandherring.com.windomain.local
 3461  18.491220      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6b1e No such name A qpvqibHM.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3462  18.492230 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x1d17 A jm+OqSx7.reddshrimpandherring.com
 3468  18.514701      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x1d17 No such name A jm+OqSx7.reddshrimpandherring.com SOA a.gtld-servers.net
 3469  18.515950 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcebd A jm+OqSx7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3470  18.526290      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xcebd No such name A jm+OqSx7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3471  18.527259 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd662 A jm+OqSx7.reddshrimpandherring.com.windomain.local
 3472  18.536520      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd662 No such name A jm+OqSx7.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3473  18.537539 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8a91 A V0XjJNSR.reddshrimpandherring.com
 3477  18.580639      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8a91 No such name A V0XjJNSR.reddshrimpandherring.com SOA a.gtld-servers.net
 3478  18.581756 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa89f A V0XjJNSR.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3479  18.592071      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa89f No such name A V0XjJNSR.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3480  18.592921 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3cba A V0XjJNSR.reddshrimpandherring.com.windomain.local
 3481  18.602317      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3cba No such name A V0XjJNSR.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3482  18.603353 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x68cf A hRnW+JSQ.reddshrimpandherring.com
 3486  18.614343      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x68cf No such name A hRnW+JSQ.reddshrimpandherring.com SOA a.gtld-servers.net
 3487  18.615333 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc518 A hRnW+JSQ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3491  18.625921      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc518 No such name A hRnW+JSQ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3492  18.626919 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd991 A hRnW+JSQ.reddshrimpandherring.com.windomain.local
 3494  18.640182      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd991 No such name A hRnW+JSQ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3495  18.643437 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc43b A 5gvgR+3U.reddshrimpandherring.com
 3496  18.655585      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc43b No such name A 5gvgR+3U.reddshrimpandherring.com SOA a.gtld-servers.net
 3497  18.656688 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc677 A 5gvgR+3U.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3504  18.675243      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc677 No such name A 5gvgR+3U.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3505  18.676200 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x333c A 5gvgR+3U.reddshrimpandherring.com.windomain.local
 3507  18.685628      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x333c No such name A 5gvgR+3U.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3508  18.686697 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xf2ca A vdGM6BgJ.reddshrimpandherring.com
 3539  18.761905      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xf2ca No such name A vdGM6BgJ.reddshrimpandherring.com SOA a.gtld-servers.net
 3543  18.763438 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcf46 A vdGM6BgJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3554  18.773901      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xcf46 No such name A vdGM6BgJ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3555  18.775351 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x1bc7 A vdGM6BgJ.reddshrimpandherring.com.windomain.local
 3556  18.784915      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x1bc7 No such name A vdGM6BgJ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3557  18.786074 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xce83 A 8SHMsy3c.reddshrimpandherring.com
 3564  18.863243      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xce83 No such name A 8SHMsy3c.reddshrimpandherring.com SOA a.gtld-servers.net
 3565  18.864257 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x58ee A 8SHMsy3c.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3567  18.874695      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x58ee No such name A 8SHMsy3c.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3569  18.875717 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xce9a A 8SHMsy3c.reddshrimpandherring.com.windomain.local
 3570  18.887283      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xce9a No such name A 8SHMsy3c.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3571  18.888158 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xdedc A LKMt6CLM.reddshrimpandherring.com
 3572  18.901027      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xdedc No such name A LKMt6CLM.reddshrimpandherring.com SOA a.gtld-servers.net
 3573  18.901966 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd87f A LKMt6CLM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3574  18.912721      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xd87f No such name A LKMt6CLM.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3575  18.913558 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc288 A LKMt6CLM.reddshrimpandherring.com.windomain.local
 3576  18.923145      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc288 No such name A LKMt6CLM.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3577  18.924014 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xec07 A EYysecBH.reddshrimpandherring.com
 3585  18.935355      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xec07 No such name A EYysecBH.reddshrimpandherring.com SOA a.gtld-servers.net
 3586  18.936375 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2caf A EYysecBH.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3587  18.946712      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2caf No such name A EYysecBH.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3588  18.948154 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x896c A EYysecBH.reddshrimpandherring.com.windomain.local
 3589  18.957631      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x896c No such name A EYysecBH.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3590  18.958743 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xbff0 A tpesAYtj.reddshrimpandherring.com
 3591  18.972454      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xbff0 No such name A tpesAYtj.reddshrimpandherring.com SOA a.gtld-servers.net
 3592  18.973441 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xdf50 A tpesAYtj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3594  18.983842      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xdf50 No such name A tpesAYtj.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3595  18.985064 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4495 A tpesAYtj.reddshrimpandherring.com.windomain.local
 3596  18.994714      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4495 No such name A tpesAYtj.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3597  18.995593 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa10b A Q1L7fBbd.reddshrimpandherring.com
 3598  19.016608      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa10b No such name A Q1L7fBbd.reddshrimpandherring.com SOA a.gtld-servers.net
 3599  19.017789 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x82c0 A Q1L7fBbd.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3600  19.028310      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x82c0 No such name A Q1L7fBbd.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3601  19.029168 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xbf0c A Q1L7fBbd.reddshrimpandherring.com.windomain.local
 3602  19.040660      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xbf0c No such name A Q1L7fBbd.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3603  19.042984 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9b71 A ODQ0m9DK.reddshrimpandherring.com
 3606  19.066713      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9b71 No such name A ODQ0m9DK.reddshrimpandherring.com SOA a.gtld-servers.net
 3607  19.067752 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8e6a A ODQ0m9DK.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3608  19.078358      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8e6a No such name A ODQ0m9DK.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3609  19.079903 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9bad A ODQ0m9DK.reddshrimpandherring.com.windomain.local
 3610  19.091154      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9bad No such name A ODQ0m9DK.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3611  19.092254 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd87d A iX+Zn2Gq.reddshrimpandherring.com
 3619  19.105037      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd87d No such name A iX+Zn2Gq.reddshrimpandherring.com SOA a.gtld-servers.net
 3620  19.106366 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe0c8 A iX+Zn2Gq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3621  19.126607      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xe0c8 No such name A iX+Zn2Gq.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3622  19.127660 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0f91 A iX+Zn2Gq.reddshrimpandherring.com.windomain.local
 3623  19.137471      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0f91 No such name A iX+Zn2Gq.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3624  19.138463 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb8ec A JUKUkUYn.reddshrimpandherring.com
 3626  19.180893      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb8ec No such name A JUKUkUYn.reddshrimpandherring.com SOA a.gtld-servers.net
 3627  19.182048 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x521c A JUKUkUYn.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3628  19.192471      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x521c No such name A JUKUkUYn.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3629  19.193406 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc59a A JUKUkUYn.reddshrimpandherring.com.windomain.local
 3630  19.203262      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc59a No such name A JUKUkUYn.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3632  19.204949 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x750f A eWUnpoWH.reddshrimpandherring.com
 3634  19.216170      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x750f No such name A eWUnpoWH.reddshrimpandherring.com SOA a.gtld-servers.net
 3635  19.217182 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x564f A eWUnpoWH.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3636  19.227800      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x564f No such name A eWUnpoWH.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3637  19.228739 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x586b A eWUnpoWH.reddshrimpandherring.com.windomain.local
 3638  19.238212      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x586b No such name A eWUnpoWH.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3639  19.239387 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9138 A Zf688UTz.reddshrimpandherring.com
 3647  19.306800      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9138 No such name A Zf688UTz.reddshrimpandherring.com SOA a.gtld-servers.net
 3648  19.307813 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4f24 A Zf688UTz.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3650  19.318329      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x4f24 No such name A Zf688UTz.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3651  19.319281 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd160 A Zf688UTz.reddshrimpandherring.com.windomain.local
 3652  19.328551      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd160 No such name A Zf688UTz.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3653  19.330064 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xad23 A uFH0VpwO.reddshrimpandherring.com
 3654  19.341342      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xad23 No such name A uFH0VpwO.reddshrimpandherring.com SOA a.gtld-servers.net
 3655  19.342355 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x06ad A uFH0VpwO.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3658  19.352757      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x06ad No such name A uFH0VpwO.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3659  19.353623 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xcaba A uFH0VpwO.reddshrimpandherring.com.windomain.local
 3660  19.365160      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xcaba No such name A uFH0VpwO.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3661  19.366267 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2aa6 A bJS/rrk1.reddshrimpandherring.com
 3669  19.407651      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2aa6 No such name A bJS/rrk1.reddshrimpandherring.com SOA a.gtld-servers.net
 3670  19.409022 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9fbe A bJS/rrk1.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3671  19.419353      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x9fbe No such name A bJS/rrk1.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3672  19.420773 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc7ee A bJS/rrk1.reddshrimpandherring.com.windomain.local
 3673  19.430210      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc7ee No such name A bJS/rrk1.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3676  19.431314 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa25a A YQuKySPc.reddshrimpandherring.com
 3738  19.500428      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa25a No such name A YQuKySPc.reddshrimpandherring.com SOA a.gtld-servers.net
 3741  19.501495 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2b89 A YQuKySPc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3752  19.511836      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2b89 No such name A YQuKySPc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3753  19.512674 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x9ca4 A YQuKySPc.reddshrimpandherring.com.windomain.local
 3766  19.524134      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x9ca4 No such name A YQuKySPc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3767  19.525129 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xdda1 A Vo/M+HTl.reddshrimpandherring.com
 3795  19.546564      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xdda1 No such name A Vo/M+HTl.reddshrimpandherring.com SOA a.gtld-servers.net
 3799  19.547811 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xe724 A Vo/M+HTl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3801  19.558241      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xe724 No such name A Vo/M+HTl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3802  19.559766 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0d56 A Vo/M+HTl.reddshrimpandherring.com.windomain.local
 3803  19.569441      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0d56 No such name A Vo/M+HTl.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3804  19.570560 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb1b5 A 7BBZdhts.reddshrimpandherring.com
 3811  19.582210      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb1b5 No such name A 7BBZdhts.reddshrimpandherring.com SOA a.gtld-servers.net
 3812  19.586577 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x3f6d A 7BBZdhts.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3822  19.596895      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x3f6d No such name A 7BBZdhts.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3826  19.597906 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5111 A 7BBZdhts.reddshrimpandherring.com.windomain.local
 3834  19.609335      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5111 No such name A 7BBZdhts.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3835  19.610710 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x166c A iN4OTru2.reddshrimpandherring.com
 3836  19.677930      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x166c No such name A iN4OTru2.reddshrimpandherring.com SOA a.gtld-servers.net
 3837  19.679356 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0458 A iN4OTru2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3840  19.689672      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0458 No such name A iN4OTru2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3841  19.690680 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x18be A iN4OTru2.reddshrimpandherring.com.windomain.local
 3842  19.700050      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x18be No such name A iN4OTru2.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3843  19.700936 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe6be A GoUf559H.reddshrimpandherring.com
 3844  19.712708      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe6be No such name A GoUf559H.reddshrimpandherring.com SOA a.gtld-servers.net
 3845  19.713778 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa719 A GoUf559H.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3846  19.726324      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xa719 No such name A GoUf559H.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3847  19.727298 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x54fb A GoUf559H.reddshrimpandherring.com.windomain.local
 3855  19.736744      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x54fb No such name A GoUf559H.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3856  19.738159 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb1c3 A zEBnIu8y.reddshrimpandherring.com
 3857  19.749356      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb1c3 No such name A zEBnIu8y.reddshrimpandherring.com SOA a.gtld-servers.net
 3858  19.750823 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd73b A zEBnIu8y.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3859  19.761232      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xd73b No such name A zEBnIu8y.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3860  19.762107 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x801f A zEBnIu8y.reddshrimpandherring.com.windomain.local
 3861  19.771695      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x801f No such name A zEBnIu8y.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3862  19.772634 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x39df A 5ShcZekS.reddshrimpandherring.com
 3863  19.784317      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x39df No such name A 5ShcZekS.reddshrimpandherring.com SOA a.gtld-servers.net
 3864  19.785276 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x878d A 5ShcZekS.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3866  19.805508      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x878d No such name A 5ShcZekS.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3867  19.806481 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2431 A 5ShcZekS.reddshrimpandherring.com.windomain.local
 3868  19.815972      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2431 No such name A 5ShcZekS.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3869  19.817146 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8a63 A M6XVMW0N.reddshrimpandherring.com
 3870  19.830926      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8a63 No such name A M6XVMW0N.reddshrimpandherring.com SOA a.gtld-servers.net
 3873  19.833167 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x648b A M6XVMW0N.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3874  19.843731      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x648b No such name A M6XVMW0N.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3875  19.844656 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x375c A M6XVMW0N.reddshrimpandherring.com.windomain.local
 3876  19.854357      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x375c No such name A M6XVMW0N.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3877  19.855147 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8c99 A DqAPj5pX.reddshrimpandherring.com
 3878  19.875715      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8c99 No such name A DqAPj5pX.reddshrimpandherring.com SOA a.gtld-servers.net
 3879  19.876737 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7dd1 A DqAPj5pX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3887  19.887005      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x7dd1 No such name A DqAPj5pX.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3888  19.888562 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7c47 A DqAPj5pX.reddshrimpandherring.com.windomain.local
 3889  19.897988      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7c47 No such name A DqAPj5pX.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3890  19.899034 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x911f A 6iKi0zDD.reddshrimpandherring.com
 3891  19.920544      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x911f No such name A 6iKi0zDD.reddshrimpandherring.com SOA a.gtld-servers.net
 3892  19.921743 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7bd6 A 6iKi0zDD.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3893  19.932180      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x7bd6 No such name A 6iKi0zDD.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3894  19.933228 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xe1de A 6iKi0zDD.reddshrimpandherring.com.windomain.local
 3896  19.944543      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xe1de No such name A 6iKi0zDD.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3897  19.945554 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xeff8 A x5KkdeHb.reddshrimpandherring.com
 3898  19.990806      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xeff8 No such name A x5KkdeHb.reddshrimpandherring.com SOA a.gtld-servers.net
 3899  19.991834 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8f11 A x5KkdeHb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3902  20.002590      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8f11 No such name A x5KkdeHb.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3903  20.003441 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2aeb A x5KkdeHb.reddshrimpandherring.com.windomain.local
 3904  20.014811      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2aeb No such name A x5KkdeHb.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3905  20.015753 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xfea1 A 9z6F1Kjc.reddshrimpandherring.com
 3913  20.057784      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xfea1 No such name A 9z6F1Kjc.reddshrimpandherring.com SOA a.gtld-servers.net
 3914  20.059025 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xabb2 A 9z6F1Kjc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3915  20.071363      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xabb2 No such name A 9z6F1Kjc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3916  20.072581 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6222 A 9z6F1Kjc.reddshrimpandherring.com.windomain.local
 3917  20.081910      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6222 No such name A 9z6F1Kjc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3918  20.083040 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x30c2 A NoqVsSW2.reddshrimpandherring.com
 3931  20.125912      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x30c2 No such name A NoqVsSW2.reddshrimpandherring.com SOA a.gtld-servers.net
 3932  20.126871 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1d57 A NoqVsSW2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3933  20.139416      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x1d57 No such name A NoqVsSW2.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3934  20.140691 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa77e A NoqVsSW2.reddshrimpandherring.com.windomain.local
 3937  20.152326      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa77e No such name A NoqVsSW2.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3938  20.153343 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa0b6 A NLjPcplu.reddshrimpandherring.com
 3942  20.168778      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa0b6 No such name A NLjPcplu.reddshrimpandherring.com SOA a.gtld-servers.net
 3944  20.169704 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x088f A NLjPcplu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3945  20.180069      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x088f No such name A NLjPcplu.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3946  20.181082 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x99a6 A NLjPcplu.reddshrimpandherring.com.windomain.local
 3947  20.192448      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x99a6 No such name A NLjPcplu.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3948  20.195343 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9b27 A v/Wnu7vs.reddshrimpandherring.com
 3956  20.206379      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9b27 No such name A v/Wnu7vs.reddshrimpandherring.com SOA a.gtld-servers.net
 3957  20.207884 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x11cd A v/Wnu7vs.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3959  20.220337      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x11cd No such name A v/Wnu7vs.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3960  20.221237 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x70c2 A v/Wnu7vs.reddshrimpandherring.com.windomain.local
 3961  20.230541      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x70c2 No such name A v/Wnu7vs.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3962  20.231724 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb5a6 A QZ7XVpoz.reddshrimpandherring.com
 3963  20.243205      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb5a6 No such name A QZ7XVpoz.reddshrimpandherring.com SOA a.gtld-servers.net
 3964  20.244185 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd5a9 A QZ7XVpoz.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3965  20.254564      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xd5a9 No such name A QZ7XVpoz.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3966  20.255534 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf6f9 A QZ7XVpoz.reddshrimpandherring.com.windomain.local
 3968  20.265041      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf6f9 No such name A QZ7XVpoz.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3969  20.266171 192.168.38.104 → 18.217.1.57  DNS 89 Standard query 0xbe68 A fQ==.reddshrimpandherring.com
 3972  20.316608  18.217.1.57 → 192.168.38.104 DNS 162 Standard query response 0xbe68 No such name A fQ==.reddshrimpandherring.com SOA a.gtld-servers.net
 3973  20.317649 192.168.38.104 → 18.217.1.57  DNS 127 Standard query 0xbaee A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3981  20.368147  18.217.1.57 → 192.168.38.104 DNS 199 Standard query response 0xbaee No such name A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3982  20.369626 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local
 3984  20.420054  18.217.1.57 → 192.168.38.104 DNS 180 Standard query response 0x4068 No such name A fQ==.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3985  20.421206 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2935 A vT6zzM2J.reddshrimpandherring.com
 3986  20.432334      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2935 No such name A vT6zzM2J.reddshrimpandherring.com SOA a.gtld-servers.net
 3987  20.433321 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4db0 A vT6zzM2J.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3988  20.443563      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x4db0 No such name A vT6zzM2J.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3989  20.444367 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5ab1 A vT6zzM2J.reddshrimpandherring.com.windomain.local
 3990  20.453748      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5ab1 No such name A vT6zzM2J.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3991  20.454930 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xb935 A yXzo0cCL.reddshrimpandherring.com
 3992  20.466236      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xb935 No such name A yXzo0cCL.reddshrimpandherring.com SOA a.gtld-servers.net
 3993  20.467324 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7e77 A yXzo0cCL.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3996  20.477759      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7e77 No such name A yXzo0cCL.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3997  20.478674 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4558 A yXzo0cCL.reddshrimpandherring.com.windomain.local
 3998  20.488154      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4558 No such name A yXzo0cCL.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3999  20.489039 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x3b06 A a+xLgs3W.reddshrimpandherring.com
 4000  20.500213      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x3b06 No such name A a+xLgs3W.reddshrimpandherring.com SOA a.gtld-servers.net
 4001  20.501053 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2985 A a+xLgs3W.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4002  20.511390      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2985 No such name A a+xLgs3W.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4003  20.512199 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd055 A a+xLgs3W.reddshrimpandherring.com.windomain.local
 4006  20.521549      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd055 No such name A a+xLgs3W.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4008  20.522530 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe294 A Yju2a1Nt.reddshrimpandherring.com
 4013  20.533316      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe294 No such name A Yju2a1Nt.reddshrimpandherring.com SOA a.gtld-servers.net
 4014  20.534572 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2721 A Yju2a1Nt.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4015  20.553439      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x2721 No such name A Yju2a1Nt.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4016  20.554506 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4d39 A Yju2a1Nt.reddshrimpandherring.com.windomain.local
 4017  20.563977      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4d39 No such name A Yju2a1Nt.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4018  20.564958 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xd418 A wLVUgWou.reddshrimpandherring.com
 4020  20.634526      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xd418 No such name A wLVUgWou.reddshrimpandherring.com SOA a.gtld-servers.net
 4021  20.635780 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x26f5 A wLVUgWou.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4024  20.646198      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x26f5 No such name A wLVUgWou.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4025  20.647066 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x24f9 A wLVUgWou.reddshrimpandherring.com.windomain.local
 4026  20.656482      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x24f9 No such name A wLVUgWou.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4027  20.657381 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x6945 A lvqrjuAa.reddshrimpandherring.com
 4028  20.679154      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x6945 No such name A lvqrjuAa.reddshrimpandherring.com SOA a.gtld-servers.net
 4029  20.680249 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2549 A lvqrjuAa.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4033  20.690976      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2549 No such name A lvqrjuAa.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4037  20.691827 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc59c A lvqrjuAa.reddshrimpandherring.com.windomain.local
 4039  20.701204      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc59c No such name A lvqrjuAa.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4040  20.702494 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x33c9 A j5t1Lfdo.reddshrimpandherring.com
 4041  20.713073      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x33c9 No such name A j5t1Lfdo.reddshrimpandherring.com SOA a.gtld-servers.net
 4042  20.714346 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xa38d A j5t1Lfdo.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4043  20.735356      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xa38d No such name A j5t1Lfdo.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4044  20.737000 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2145 A j5t1Lfdo.reddshrimpandherring.com.windomain.local
 4046  20.746481      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2145 No such name A j5t1Lfdo.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4047  20.747466 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2dba A s1VHzRn6.reddshrimpandherring.com
 4048  20.792013      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2dba No such name A s1VHzRn6.reddshrimpandherring.com SOA a.gtld-servers.net
 4049  20.793019 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0f22 A s1VHzRn6.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4050  20.803524      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x0f22 No such name A s1VHzRn6.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4052  20.804817 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xad35 A s1VHzRn6.reddshrimpandherring.com.windomain.local
 4054  20.814209      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xad35 No such name A s1VHzRn6.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4055  20.815076 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x78d7 A jM9GaAzF.reddshrimpandherring.com
 4056  20.826263      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x78d7 No such name A jM9GaAzF.reddshrimpandherring.com SOA a.gtld-servers.net
 4057  20.827034 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x80e1 A jM9GaAzF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4058  20.841550      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x80e1 No such name A jM9GaAzF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4059  20.842410 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x920b A jM9GaAzF.reddshrimpandherring.com.windomain.local
 4060  20.853674      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x920b No such name A jM9GaAzF.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4061  20.854589 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x5c48 A ecb6fGRc.reddshrimpandherring.com
 4069  20.896012      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x5c48 No such name A ecb6fGRc.reddshrimpandherring.com SOA a.gtld-servers.net
 4070  20.897245 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4bc1 A ecb6fGRc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4072  20.910360      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x4bc1 No such name A ecb6fGRc.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4073  20.911276 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xdb41 A ecb6fGRc.reddshrimpandherring.com.windomain.local
 4074  20.922608      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xdb41 No such name A ecb6fGRc.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4075  20.923488 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe2ca A N+6v2HTZ.reddshrimpandherring.com
 4078  20.966543      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe2ca No such name A N+6v2HTZ.reddshrimpandherring.com SOA a.gtld-servers.net
 4079  20.967546 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2647 A N+6v2HTZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4080  20.978095      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2647 No such name A N+6v2HTZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4081  20.978866 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xd054 A N+6v2HTZ.reddshrimpandherring.com.windomain.local
 4082  20.990279      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xd054 No such name A N+6v2HTZ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4083  20.991235 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x5b58 A +sorXMfa.reddshrimpandherring.com
 4084  21.003001      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x5b58 No such name A +sorXMfa.reddshrimpandherring.com SOA a.gtld-servers.net
 4085  21.004070 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x8e39 A +sorXMfa.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4092  21.014464      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x8e39 No such name A +sorXMfa.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4093  21.016751 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3b4e A +sorXMfa.reddshrimpandherring.com.windomain.local
 4094  21.026128      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3b4e No such name A +sorXMfa.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4095  21.029559 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xa10f A 5FALrYGV.reddshrimpandherring.com
 4097  21.042826      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xa10f No such name A 5FALrYGV.reddshrimpandherring.com SOA a.gtld-servers.net
 4098  21.043810 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xcd14 A 5FALrYGV.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4099  21.054234      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xcd14 No such name A 5FALrYGV.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4100  21.055201 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xc628 A 5FALrYGV.reddshrimpandherring.com.windomain.local
 4101  21.064656      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xc628 No such name A 5FALrYGV.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4102  21.065961 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xaf59 A eu71Cs0V.reddshrimpandherring.com
 4106  21.137843      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xaf59 No such name A eu71Cs0V.reddshrimpandherring.com SOA a.gtld-servers.net
 4107  21.138845 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xed2c A eu71Cs0V.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4108  21.149322      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xed2c No such name A eu71Cs0V.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4109  21.150170 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x5f1a A eu71Cs0V.reddshrimpandherring.com.windomain.local
 4112  21.159486      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x5f1a No such name A eu71Cs0V.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4113  21.160704 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x28c7 A dxr+G/kl.reddshrimpandherring.com
 4119  21.171643      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x28c7 No such name A dxr+G/kl.reddshrimpandherring.com SOA a.gtld-servers.net
 4120  21.172874 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x798a A dxr+G/kl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4121  21.183061      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x798a No such name A dxr+G/kl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4122  21.184382 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xa30a A dxr+G/kl.reddshrimpandherring.com.windomain.local
 4123  21.194131      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xa30a No such name A dxr+G/kl.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4124  21.195241 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xef10 A 0gHMI0EI.reddshrimpandherring.com
 4126  21.237469      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xef10 No such name A 0gHMI0EI.reddshrimpandherring.com SOA a.gtld-servers.net
 4127  21.238472 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x53b9 A 0gHMI0EI.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4128  21.248657      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x53b9 No such name A 0gHMI0EI.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4129  21.249696 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0c1e A 0gHMI0EI.reddshrimpandherring.com.windomain.local
 4130  21.259171      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0c1e No such name A 0gHMI0EI.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4131  21.260251 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x40d4 A 4n+wg52s.reddshrimpandherring.com
 4134  21.301785      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x40d4 No such name A 4n+wg52s.reddshrimpandherring.com SOA a.gtld-servers.net
 4135  21.302757 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc342 A 4n+wg52s.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4136  21.313273      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc342 No such name A 4n+wg52s.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4137  21.314001 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x087b A 4n+wg52s.reddshrimpandherring.com.windomain.local
 4138  21.323432      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x087b No such name A 4n+wg52s.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4139  21.324360 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x8c15 A 9bgMWa5Z.reddshrimpandherring.com
 4148  21.393798      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x8c15 No such name A 9bgMWa5Z.reddshrimpandherring.com SOA a.gtld-servers.net
 4149  21.394800 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x9a8e A 9bgMWa5Z.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4150  21.405260      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x9a8e No such name A 9bgMWa5Z.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4151  21.406117 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x831e A 9bgMWa5Z.reddshrimpandherring.com.windomain.local
 4152  21.417748      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x831e No such name A 9bgMWa5Z.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4153  21.418797 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x551d A bh2L8TFp.reddshrimpandherring.com
 4154  21.431696      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x551d No such name A bh2L8TFp.reddshrimpandherring.com SOA a.gtld-servers.net
 4155  21.432618 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xdacb A bh2L8TFp.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4156  21.451239      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xdacb No such name A bh2L8TFp.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4157  21.452614 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x3772 A bh2L8TFp.reddshrimpandherring.com.windomain.local
 4160  21.463426      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x3772 No such name A bh2L8TFp.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4161  21.464457 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4fc4 A 6YyOean+.reddshrimpandherring.com
 4168  21.508338      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4fc4 No such name A 6YyOean+.reddshrimpandherring.com SOA a.gtld-servers.net
 4169  21.510494 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xb307 A 6YyOean+.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4171  21.521009      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xb307 No such name A 6YyOean+.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4172  21.521987 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2dc9 A 6YyOean+.reddshrimpandherring.com.windomain.local
 4173  21.533339      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2dc9 No such name A 6YyOean+.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4174  21.534402 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2203 A Ften8lLo.reddshrimpandherring.com
 4175  21.546062      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2203 No such name A Ften8lLo.reddshrimpandherring.com SOA a.gtld-servers.net
 4176  21.547167 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x6ffa A Ften8lLo.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4177  21.557597      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x6ffa No such name A Ften8lLo.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4178  21.558476 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xadc8 A Ften8lLo.reddshrimpandherring.com.windomain.local
 4180  21.567771      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xadc8 No such name A Ften8lLo.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4181  21.568832 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x4f9c A 2CscKL+3.reddshrimpandherring.com
 4182  21.590010      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x4f9c No such name A 2CscKL+3.reddshrimpandherring.com SOA a.gtld-servers.net
 4183  21.591029 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x44d9 A 2CscKL+3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4184  21.609666      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x44d9 No such name A 2CscKL+3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4185  21.610717 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x97be A 2CscKL+3.reddshrimpandherring.com.windomain.local
 4186  21.620354      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x97be No such name A 2CscKL+3.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4187  21.622785 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0f08 A L/5yYuuf.reddshrimpandherring.com
 4190  21.633731      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0f08 No such name A L/5yYuuf.reddshrimpandherring.com SOA a.gtld-servers.net
 4191  21.634713 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x5982 A L/5yYuuf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4192  21.645208      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x5982 No such name A L/5yYuuf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4193  21.646171 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x407a A L/5yYuuf.reddshrimpandherring.com.windomain.local
 4194  21.655561      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x407a No such name A L/5yYuuf.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4195  21.656416 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0472 A H5RvSugA.reddshrimpandherring.com
 4196  21.667742      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0472 No such name A H5RvSugA.reddshrimpandherring.com SOA a.gtld-servers.net
 4197  21.668776 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xf145 A H5RvSugA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4205  21.679182      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xf145 No such name A H5RvSugA.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4206  21.680141 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xeb59 A H5RvSugA.reddshrimpandherring.com.windomain.local
 4207  21.693729      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xeb59 No such name A H5RvSugA.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4208  21.699927 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9fab A YdfbP1UZ.reddshrimpandherring.com
 4209  21.711531      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9fab No such name A YdfbP1UZ.reddshrimpandherring.com SOA a.gtld-servers.net
 4210  21.712528 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x27c2 A YdfbP1UZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4211  21.723079      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x27c2 No such name A YdfbP1UZ.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4212  21.724023 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xdb51 A YdfbP1UZ.reddshrimpandherring.com.windomain.local
 4214  21.736398      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xdb51 No such name A YdfbP1UZ.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4215  21.737852 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe3bf A I4U/5r2f.reddshrimpandherring.com
 4216  21.751329      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe3bf No such name A I4U/5r2f.reddshrimpandherring.com SOA a.gtld-servers.net
 4217  21.752355 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x850f A I4U/5r2f.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4218  21.764976      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x850f No such name A I4U/5r2f.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4219  21.765969 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x84f6 A I4U/5r2f.reddshrimpandherring.com.windomain.local
 4220  21.777519      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x84f6 No such name A I4U/5r2f.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4221  21.778556 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x7536 A 1X/s/2vy.reddshrimpandherring.com
 4222  21.792169      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x7536 No such name A 1X/s/2vy.reddshrimpandherring.com SOA a.gtld-servers.net
 4223  21.793191 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x2c6e A 1X/s/2vy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4225  21.803375      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x2c6e No such name A 1X/s/2vy.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4226  21.804512 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x0f2b A 1X/s/2vy.reddshrimpandherring.com.windomain.local
 4228  21.813871      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x0f2b No such name A 1X/s/2vy.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4229  21.814825 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x03ec A O+PFxqfF.reddshrimpandherring.com
 4230  21.837197      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x03ec No such name A O+PFxqfF.reddshrimpandherring.com SOA a.gtld-servers.net
 4231  21.838240 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4fff A O+PFxqfF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4232  21.848801      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x4fff No such name A O+PFxqfF.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4233  21.849729 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x2ae4 A O+PFxqfF.reddshrimpandherring.com.windomain.local
 4241  21.859060      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x2ae4 No such name A O+PFxqfF.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4242  21.861585 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x2a34 A Ju4eCL8V.reddshrimpandherring.com
 4243  21.873217      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x2a34 No such name A Ju4eCL8V.reddshrimpandherring.com SOA a.gtld-servers.net
 4244  21.874654 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x01cc A Ju4eCL8V.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4245  21.884896      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x01cc No such name A Ju4eCL8V.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4246  21.885749 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xe3be A Ju4eCL8V.reddshrimpandherring.com.windomain.local
 4247  21.897060      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xe3be No such name A Ju4eCL8V.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4248  21.898212 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xeaeb A JBfOkBIE.reddshrimpandherring.com
 4250  21.940445      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xeaeb No such name A JBfOkBIE.reddshrimpandherring.com SOA a.gtld-servers.net
 4251  21.941470 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x10af A JBfOkBIE.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4252  21.952018      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x10af No such name A JBfOkBIE.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4253  21.953274 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x53ab A JBfOkBIE.reddshrimpandherring.com.windomain.local
 4254  21.964728      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x53ab No such name A JBfOkBIE.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4255  21.965761 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x9b8c A 0bLbK94Z.reddshrimpandherring.com
 4258  22.008732      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x9b8c No such name A 0bLbK94Z.reddshrimpandherring.com SOA a.gtld-servers.net
 4259  22.009745 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7f95 A 0bLbK94Z.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4260  22.022382      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7f95 No such name A 0bLbK94Z.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4261  22.023268 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x80e1 A 0bLbK94Z.reddshrimpandherring.com.windomain.local
 4269  22.032490      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x80e1 No such name A 0bLbK94Z.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4270  22.033811 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x0815 A tEWQ8ZAi.reddshrimpandherring.com
 4271  22.045435      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x0815 No such name A tEWQ8ZAi.reddshrimpandherring.com SOA a.gtld-servers.net
 4272  22.046641 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x4b04 A tEWQ8ZAi.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4273  22.058947      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x4b04 No such name A tEWQ8ZAi.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4274  22.059926 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6482 A tEWQ8ZAi.reddshrimpandherring.com.windomain.local
 4275  22.071211      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6482 No such name A tEWQ8ZAi.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4276  22.072175 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xbe9c A JBQmApX7.reddshrimpandherring.com
 4278  22.086008      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xbe9c No such name A JBQmApX7.reddshrimpandherring.com SOA a.gtld-servers.net
 4279  22.087257 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xfa02 A JBQmApX7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4280  22.097756      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0xfa02 No such name A JBQmApX7.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4281  22.098725 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x345a A JBQmApX7.reddshrimpandherring.com.windomain.local
 4282  22.108296      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x345a No such name A JBQmApX7.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4283  22.109248 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x37d0 A GQ3caS/1.reddshrimpandherring.com
 4284  22.130669      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x37d0 No such name A GQ3caS/1.reddshrimpandherring.com SOA a.gtld-servers.net
 4285  22.131677 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x425f A GQ3caS/1.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4286  22.144105      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x425f No such name A GQ3caS/1.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4288  22.146990 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xf364 A GQ3caS/1.reddshrimpandherring.com.windomain.local
 4290  22.156308      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xf364 No such name A GQ3caS/1.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4291  22.157152 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xc6da A Yz2l3aBW.reddshrimpandherring.com
 4299  22.201187      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xc6da No such name A Yz2l3aBW.reddshrimpandherring.com SOA a.gtld-servers.net
 4300  22.202932 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x7bb7 A Yz2l3aBW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4301  22.213446      8.8.8.8 → 192.168.38.104 DNS 203 Standard query response 0x7bb7 No such name A Yz2l3aBW.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4302  22.217023 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x6c33 A Yz2l3aBW.reddshrimpandherring.com.windomain.local
 4303  22.226343      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x6c33 No such name A Yz2l3aBW.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4304  22.227270 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xe15b A xA3F0VZ8.reddshrimpandherring.com
 4306  22.271432      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xe15b No such name A xA3F0VZ8.reddshrimpandherring.com SOA a.gtld-servers.net
 4307  22.272517 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x0c85 A xA3F0VZ8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4308  22.283255      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x0c85 No such name A xA3F0VZ8.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4309  22.284358 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x7cf1 A xA3F0VZ8.reddshrimpandherring.com.windomain.local
 4310  22.295950      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x7cf1 No such name A xA3F0VZ8.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4311  22.297130 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xea1f A l7hTDJh3.reddshrimpandherring.com
 4314  22.339802      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xea1f No such name A l7hTDJh3.reddshrimpandherring.com SOA a.gtld-servers.net
 4315  22.340927 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xd794 A l7hTDJh3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4316  22.351823      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xd794 No such name A l7hTDJh3.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4317  22.352825 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xb38d A l7hTDJh3.reddshrimpandherring.com.windomain.local
 4318  22.362315      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xb38d No such name A l7hTDJh3.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4319  22.363188 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0x906e A BN9PyNZN.reddshrimpandherring.com
 4327  22.405430      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0x906e No such name A BN9PyNZN.reddshrimpandherring.com SOA a.gtld-servers.net
 4328  22.406439 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0x1e58 A BN9PyNZN.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4330  22.425663      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0x1e58 No such name A BN9PyNZN.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4334  22.426618 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0xac78 A BN9PyNZN.reddshrimpandherring.com.windomain.local
 4354  22.436037      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0xac78 No such name A BN9PyNZN.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4355  22.437065 192.168.38.104 → 8.8.8.8      DNS 93 Standard query 0xace9 A M9QZU6eP.reddshrimpandherring.com
 4356  22.450908      8.8.8.8 → 192.168.38.104 DNS 166 Standard query response 0xace9 No such name A M9QZU6eP.reddshrimpandherring.com SOA a.gtld-servers.net
 4357  22.451860 192.168.38.104 → 8.8.8.8      DNS 131 Standard query 0xc6e9 A M9QZU6eP.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4358  22.462196      8.8.8.8 → 192.168.38.104 DNS 205 Standard query response 0xc6e9 No such name A M9QZU6eP.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 4359  22.463138 192.168.38.104 → 8.8.8.8      DNS 109 Standard query 0x4ad9 A M9QZU6eP.reddshrimpandherring.com.windomain.local
 4360  22.474665      8.8.8.8 → 192.168.38.104 DNS 184 Standard query response 0x4ad9 No such name A M9QZU6eP.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4361  22.481648 192.168.38.104 → 18.217.1.57  DNS 89 Standard query 0xa740 A fQ==.reddshrimpandherring.com
 4364  22.532034  18.217.1.57 → 192.168.38.104 DNS 162 Standard query response 0xa740 No such name A fQ==.reddshrimpandherring.com SOA a.gtld-servers.net
 4365  22.533184 192.168.38.104 → 18.217.1.57  DNS 127 Standard query 0x683a A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4373  22.582748  18.217.1.57 → 192.168.38.104 DNS 199 Standard query response 0x683a No such name A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4374  22.583745 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local
 4376  22.633047  18.217.1.57 → 192.168.38.104 DNS 180 Standard query response 0x7418 No such name A fQ==.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/wireshark_02]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8'                                 
 1633   9.334169 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0xdf26 A cGljb0NU.reddshrimpandherring.com
 1634   9.388061  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0xdf26 No such name A cGljb0NU.reddshrimpandherring.com SOA a.gtld-servers.net
 1635   9.389117 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xa12d A cGljb0NU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1636   9.439381  18.217.1.57 → 192.168.38.104 DNS 205 Standard query response 0xa12d No such name A cGljb0NU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 1637   9.440363 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local
 1638   9.490669  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x1dd2 No such name A cGljb0NU.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2042  11.870534 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x3a30 A RntkbnNf.reddshrimpandherring.com
 2043  11.921106  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x3a30 No such name A RntkbnNf.reddshrimpandherring.com SOA a.gtld-servers.net
 2044  11.922284 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xec57 A RntkbnNf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2045  11.971614  18.217.1.57 → 192.168.38.104 DNS 203 Standard query response 0xec57 No such name A RntkbnNf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2046  11.972605 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local
 2047  12.021881  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0xabb9 No such name A RntkbnNf.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 2444  14.503146 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x531d A M3hmMWxf.reddshrimpandherring.com
 2445  14.553435  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x531d No such name A M3hmMWxf.reddshrimpandherring.com SOA a.gtld-servers.net
 2446  14.554475 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0x3bd6 A M3hmMWxf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2447  14.604708  18.217.1.57 → 192.168.38.104 DNS 203 Standard query response 0x3bd6 No such name A M3hmMWxf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 2448  14.605726 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local
 2671  14.657185  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x9e21 No such name A M3hmMWxf.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3140  16.404809 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x99dd A ZnR3X2Rl.reddshrimpandherring.com
 3143  16.455193  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x99dd No such name A ZnR3X2Rl.reddshrimpandherring.com SOA a.gtld-servers.net
 3144  16.456229 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0x028b A ZnR3X2Rl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3152  16.505490  18.217.1.57 → 192.168.38.104 DNS 203 Standard query response 0x028b No such name A ZnR3X2Rl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3153  16.506492 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local
 3155  16.557035  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x2ee1 No such name A ZnR3X2Rl.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3429  18.239530 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x16f6 A YWRiZWVm.reddshrimpandherring.com
 3433  18.288746  18.217.1.57 → 192.168.38.104 DNS 166 Standard query response 0x16f6 No such name A YWRiZWVm.reddshrimpandherring.com SOA a.gtld-servers.net
 3434  18.289828 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xe7cb A YWRiZWVm.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3441  18.339039  18.217.1.57 → 192.168.38.104 DNS 205 Standard query response 0xe7cb No such name A YWRiZWVm.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA dns-external-master.amazon.com
 3442  18.340155 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local
 3445  18.391844  18.217.1.57 → 192.168.38.104 DNS 184 Standard query response 0x2a4b No such name A YWRiZWVm.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 3969  20.266171 192.168.38.104 → 18.217.1.57  DNS 89 Standard query 0xbe68 A fQ==.reddshrimpandherring.com
 3972  20.316608  18.217.1.57 → 192.168.38.104 DNS 162 Standard query response 0xbe68 No such name A fQ==.reddshrimpandherring.com SOA a.gtld-servers.net
 3973  20.317649 192.168.38.104 → 18.217.1.57  DNS 127 Standard query 0xbaee A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3981  20.368147  18.217.1.57 → 192.168.38.104 DNS 199 Standard query response 0xbaee No such name A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 3982  20.369626 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local
 3984  20.420054  18.217.1.57 → 192.168.38.104 DNS 180 Standard query response 0x4068 No such name A fQ==.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
 4361  22.481648 192.168.38.104 → 18.217.1.57  DNS 89 Standard query 0xa740 A fQ==.reddshrimpandherring.com
 4364  22.532034  18.217.1.57 → 192.168.38.104 DNS 162 Standard query response 0xa740 No such name A fQ==.reddshrimpandherring.com SOA a.gtld-servers.net
 4365  22.533184 192.168.38.104 → 18.217.1.57  DNS 127 Standard query 0x683a A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4373  22.582748  18.217.1.57 → 192.168.38.104 DNS 199 Standard query response 0x683a No such name A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com SOA pdns1.ultradns.net
 4374  22.583745 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local
 4376  22.633047  18.217.1.57 → 192.168.38.104 DNS 180 Standard query response 0x7418 No such name A fQ==.reddshrimpandherring.com.windomain.local SOA a.root-servers.net
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/wireshark_02]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response              
 1633   9.334169 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0xdf26 A cGljb0NU.reddshrimpandherring.com
 1635   9.389117 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xa12d A cGljb0NU.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 1637   9.440363 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local
 2042  11.870534 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x3a30 A RntkbnNf.reddshrimpandherring.com
 2044  11.922284 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xec57 A RntkbnNf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2046  11.972605 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local
 2444  14.503146 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x531d A M3hmMWxf.reddshrimpandherring.com
 2446  14.554475 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0x3bd6 A M3hmMWxf.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 2448  14.605726 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local
 3140  16.404809 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x99dd A ZnR3X2Rl.reddshrimpandherring.com
 3144  16.456229 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0x028b A ZnR3X2Rl.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3153  16.506492 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local
 3429  18.239530 192.168.38.104 → 18.217.1.57  DNS 93 Standard query 0x16f6 A YWRiZWVm.reddshrimpandherring.com
 3434  18.289828 192.168.38.104 → 18.217.1.57  DNS 131 Standard query 0xe7cb A YWRiZWVm.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3442  18.340155 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local
 3969  20.266171 192.168.38.104 → 18.217.1.57  DNS 89 Standard query 0xbe68 A fQ==.reddshrimpandherring.com
 3973  20.317649 192.168.38.104 → 18.217.1.57  DNS 127 Standard query 0xbaee A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 3982  20.369626 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local
 4361  22.481648 192.168.38.104 → 18.217.1.57  DNS 89 Standard query 0xa740 A fQ==.reddshrimpandherring.com
 4365  22.533184 192.168.38.104 → 18.217.1.57  DNS 127 Standard query 0x683a A fQ==.reddshrimpandherring.com.us-west-1.ec2-utilities.amazonaws.com
 4374  22.583745 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/wireshark_02]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local 
 1637   9.440363 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local
 2046  11.972605 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local
 2448  14.605726 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local
 3153  16.506492 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local
 3442  18.340155 192.168.38.104 → 18.217.1.57  DNS 109 Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local
 3982  20.369626 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local
 4374  22.583745 192.168.38.104 → 18.217.1.57  DNS 105 Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/wireshark_02]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk -e '{print $12}' | sed -e 's/\..*//'
cGljb0NU
RntkbnNf
M3hmMWxf
ZnR3X2Rl
YWRiZWVm
fQ==
fQ==
                                                                                                            
┌──(kali㉿kali)-[~/…/parciales/parcial_02/parte_04_forensic_02/wireshark_02]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk -e '{print $12}' | sed -e 's/\..*//' | base64 -d
picoCTF{dns_3xf1l_ftw_deadbeef}}   
```

## Bandera
```css
flag: picoCTF{dns_3xf1l_ftw_deadbeef}
```
## Notas Adicionales

El comando `tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep local | awk -e '{print $12}' | sed -e 's/\..*//' | base64 -d` realiza los siguientes pasos:

1. **`tshark -nr shark2.pcapng -Y 'dns'`**: Analiza el archivo de captura de red `shark2.pcapng` buscando solo los paquetes de tipo DNS (`-Y 'dns'`).
2. **`grep -v '8.8.8.8'`**: Filtra las líneas que no contengan la dirección IP `8.8.8.8` (probablemente para excluir consultas a este servidor DNS).
3. **`grep -v response`**: Filtra las líneas que no contengan la palabra "response", eliminando las respuestas DNS.
4. **`grep local`**: Filtra las líneas que contengan la palabra "local", probablemente buscando solicitudes DNS relacionadas con dominios locales.
5. **`awk -e '{print $12}'`**: Extrae el valor de la columna 12 de la salida (probablemente donde está el dominio o la información codificada).
6. **`sed -e 's/\..*//'`**: Elimina todo lo que esté después del primer punto (probablemente para obtener solo el nombre del dominio principal o parte del dato).
7. **`base64 -d`**: Decodifica la cadena en base64 extraída, probablemente recuperando datos que estaban cifrados o codificados en la comunicación DNS.

En resumen, este comando extrae y decodifica datos codificados en base64 dentro de paquetes DNS capturados en el archivo `shark2.pcapng`, filtrando por solicitudes DNS locales y excluyendo ciertos servidores o respuestas específicas.
## Referencias
-  