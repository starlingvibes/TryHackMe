#!/usr/bin/python3

import requests

url = 'http://10.10.169.100:3000/'
path = ''
flag = ''

while (path != 'end'):
	response = requests.get(url + path)
	jsonresponse = response.json()
	print(jsonresponse)
	nextpath = (jsonresponse['next'])
	path = nextpath
	flag += jsonresponse['value']
	#print(flag) 		#If you want the cool effect, remove the hash sign
print('\n'f'The flag is: {flag[:-3]}')
