#!/usr/bin/python

import os
import zipfile
import exiftool


filelist=os.listdir("./ZipConfusion")
textfiles=0

for z in filelist:
	if zipfile.is_zipfile(z):
		with zipfile.ZipFile("./ZipConfusion/"+z, "r") as zip_file:
			zip_file.extractall("./ZipConfusion/")
	else:
		textfiles+=1
		print('{} is not a zip file').format(z)

print('Unzipped files: {}').format(textfile)