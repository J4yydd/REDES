
### descripcion

Cryptography  
Medium  
100 pts  
20,436 solves  
by Will Hong / LT 'syreal' Jones  
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?

  

Download the leak here.

  

The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

### solucion 
```
jayyd@MacBook-Pro-de-Victor lskdj % tar -xf leak.tar

jayyd@MacBook-Pro-de-Victor lskdj % ls

leak picker-IV timer_apk

leak.tar picker-IV.c timer.apk

message.txt SafeOpener.class

jayyd@MacBook-Pro-de-Victor lskdj % cd leak

jayyd@MacBook-Pro-de-Victor leak % ls

passwords.txt usernames.txt

jayyd@MacBook-Pro-de-Victor leak % grep -n "cultiris" usernames.txt

378:cultiris

jayyd@MacBook-Pro-de-Victor leak % sed -n '378p' passwords.txt

cvpbPGS{P7e1S_54I35_71Z3}

jayyd@MacBook-Pro-de-Victor leak % echo "cvpbPGS{P7e1S_54I35_71Z3}" | tr 'A-Za-z' 'N-ZA-Mn-za-m'

picoCTF{C7r1F_54V35_71M3}

jayyd@MacBook-Pro-de-Victor leak %
```