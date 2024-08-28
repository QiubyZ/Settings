from subprocess import Popen, STDOUT, PIPE
from  time import sleep
from os import path, getcwd, makedirs

def cmd (comd):
	test = Popen(comd, shell=True, stdout=PIPE, stderr=STDOUT)
	return test.communicate()[0].decode("utf-8")

def buat_folder(nama_folder):
  folder_path = path.join(getcwd(), nama_folder)
  if not path.exists(folder_path):
    makedirs(folder_path)
  return folder_path

def Bacafile(**var) :
	with open(**var) as e:
		return e.read()
			 
def DumpsSettings():
	path = []
	for kategori in ["global", "secure", "system"]:
		piles = f"./.cache/{kategori}.txt"
		with open(file=piles, mode="w") as tulis:
			isi = cmd(f"su -c settings list {kategori}")
			tulis.write(isi)
			path.append([piles, kategori])
	return  path
		
def ListeningData():
	for kategori in DumpsSettings():
		file_name = kategori[0]
		file_kate = kategori[1]
		berkas_dump = Bacafile(file=file_name).splitlines()
		berkas_asli = str(cmd(f"su -c settings list {file_kate}")).splitlines()
		for dumps, cmds in zip(berkas_dump, berkas_asli):
			if(dumps != cmds):
				print(f"{file_kate} {cmds} | {file_kate} {dumps} ")

def main():
	buat_folder(".cache")
	while 1:
		ListeningData()
main()