import os
import glob
from time import *

class Files:

	def __init__(self, path):
		self.path = path

	def deletar_arquivo(self, path):
		os.remove(path)

	def deletar_pasta(self, path):
		os.rmdir(path)

	def criar_pasta(self, path):
		os.mkdir(path)

	def criar_arquivo(self, path, content):
		with open(path, 'w') as file:
			file.write(content)

	def copiar_arquivo(self, path, path_destino):
		os.system('cp ' + path + ' ' + path_destino)

	def copiar_pasta(self, path, path_destino):
		os.system('cp -r ' + path + ' ' + path_destino)

	def mover_arquivo(self, path, path_destino):
		os.system('mv ' + path + ' ' + path_destino)

	def mover_pasta(self, path, path_destino):
		os.system('mv -r ' + path + ' ' + path_destino)
	
	def listar_arquivos(self, path):
		return glob.glob(path + '/*')

	def cortar_arquivo(self, path, path_destino, inicio, fim):
		os.system('cut -c ' + str(inicio) + '-' + str(fim) + ' ' + path + ' > ' + path_destino)

	def cortar_pasta(self, path, path_destino, inicio, fim):
		os.system('cut -c ' + str(inicio) + '-' + str(fim) + ' ' + path + '/* > ' + path_destino)

	def download_arquivo(self, path, path_destino):
		os.system('wget ' + path + ' -O ' + path_destino)

	def get_file_size(self, path):
		return os.path.getsize(path)

	def get_file_creation_time(self, path):
		return strftime('%Y-%m-%d %H:%M:%S', localtime(os.path.getctime(path)))

	def get_file_modification_time(self, path):
		return strftime('%Y-%m-%d %H:%M:%S', localtime(os.path.getmtime(path)))

	def get_file_access_time(self, path):
		return strftime('%Y-%m-%d %H:%M:%S', localtime(os.path.getatime(path)))

	def get_file_owner(self, path):
		return str(os.stat(path).st_uid)
		
	def get_file_type(self, path):
		return str(os.popen('file -b --mime-type ' + path).read())