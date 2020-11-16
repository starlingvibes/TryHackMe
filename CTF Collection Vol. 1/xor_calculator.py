#!usr/bin/python3

# This is a `message1 XOR message2` decoder written in Python3
from time import sleep

print("""
                 /$$   /$$  /$$$$$$  /$$$$$$$        /$$$$$$$ 
                | $$  / $$ /$$__  $$| $$__  $$      | $$__  $$
  /$$$$$$       |  $$/ $$/| $$  \ $$| $$  \ $$      | $$  \ $$
 |____  $$       \  $$$$/ | $$  | $$| $$$$$$$/      | $$$$$$$ 
  /$$$$$$$        >$$  $$ | $$  | $$| $$__  $$      | $$__  $$
 /$$__  $$       /$$/\  $$| $$  | $$| $$  \ $$      | $$  \ $$
|  $$$$$$$      | $$  \ $$|  $$$$$$/| $$  | $$      | $$$$$$$/
 \_______/      |__/  |__/ \______/ |__/  |__/      |_______/ 
                                                              """)

sleep(2)
message1 = input("Hello, please enter the first message: ")
message2 = input("Enter the second message: ")
# message1 = "1010101010101010101010101010101010"  # Insert Encoded message here
# message2 = "44585d6b2368737c65252166234f20626d"  # Insert second encoded message here

a = hex(int(message1, 16) ^ int(message2, 16))[2:]
output_msg = "The decoded XOR Message is: " + (bytes.fromhex(a).decode('utf-8'))
print(output_msg)
