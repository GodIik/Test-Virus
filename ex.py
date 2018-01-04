#!usr/bin/python

import sys, os


# Controllo se il File è già stato Infettato

def controllo_file(_file_):
	key = "#!Key: 1234"
	infect = "No"
	file = open(_file_, 'r')
	
	for line in file:
		
		if key in line:
			print("File Infect, Key Found: " + key)
			infect = "Yes"
			file.close()
			break
		
		else:
			pass
	
	if infect == "Yes":
		file.close()
		exit
	
	else:
		print("Not infect!")
	
	file.close()
	checker(_file_)
		

# Infetto i file e inserisco dei "marcatori"

def infect(_file_):
	exploit_ = "#!Key:Exploit Begin"
	_exploit = "print('Exploited')"
	_exploit_ = "#!Key:Exploit End"
	file = open(_file_, 'a')
	file.write("\n" + exploit_ + "\n" +  _exploit + "\n" +  _exploit_)
	file.close()
	file = open(_file_, 'r')
	
	for line in file:
		
		if exploit_ in line:
			print("\nFile Infect, Exploit Found: " + _exploit)
			infect = "Yes"
			break
		
		else:
			pass

def checker(_file_):
	infect(_file_)

if __name__ == '__main__':
	
	file = input("Path: ")
	controllo_file(file)
