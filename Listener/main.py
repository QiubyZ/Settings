from subprocess import Popen, STDOUT, PIPE
from  time import sleep

def cmd (comd):
	test = Popen(comd, shell=True, stdout=PIPE, stderr=STDOUT)
	return test.communicate()[0].decode("utf-8")

Tulis = lambda x, t: open(x, "w").write(t)
list_kategori  = ["global", "secure", "system"]

def DumpsSettings():
	file_dump = []
	for kategori in list_kategori:
		isi = cmd(f"su -c settings list {kategori}")
		Tulis(f"./.cache/{kategori}.txt", isi )
		file_dump.append(f"./.cache/{kategori}.txt")
	return file_dump
	
def Bacafile(path) :
	with open(path) as e:
		return e.read()
		
def ListeningData():
	DumpsSettings()
	for kategori in list_kategori:
		berkas_dump = Bacafile(f"./.cache/{kategori}.txt")
		berkas_asli = cmd(f"su -c settings list {kategori}")
		for dumpsNo, dumpsIsi in enumerate(berkas_dump.splitlines()):
			    for asliNo, asliIsi in enumerate(berkas_asli.splitlines()):
			    	if(dumpsNo == asliNo):
			    		if(dumpsIsi != asliIsi):
			    			print(f"{dumpsNo}{dumpsIsi} | {asliNo}. {asliIsi}")
			    			
			    			
			    			
print("Goto Settings, this will Listening Your Touch...")
while 1:
	ListeningData()
