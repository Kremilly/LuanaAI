from time import *

class DataHora:
	def __init__(self):
		self.data = strftime("%d/%m/%Y")
		self.hora = strftime("%H:%M:%S")
		self.timezone = "America/Sao_Paulo"

	def get_data(self):
		return self.data

	def get_hora(self):
		return self.hora

	def get_timezone(self):
		return self.timezone

	def get_data_hora(self):
		return self.data + " " + self.hora
	
	def set_data(self, data):
		self.data = data

	def set_hora(self, hora):
		self.hora = hora

	def set_data_hora(self, data, hora):
		self.data = data
		self.hora = hora

	def timezone(self, timezone):
		self.timezone = timezone