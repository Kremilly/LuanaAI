import pyautogui

class Screenshots:

	def __init__(self, file_path, file_name, file_extension):
		self.path = file_path
		self.file_name = file_name
		self.file_extension = file_extension
		self.file_path = self.path + self.file_name + self.file_extension

	def capturar_tela(self, mensagem):
		pyautogui.screenshot(self.file_path)
		mensagem
		return self