import pyimgur

class Imgur:

	def __init__(self, client_id):
		self.client_id = client_id
		self.client = pyimgur.Imgur(client_id)

	def enviar_imagem(self, image_path):
		image = self.client.upload_image(image_path)
		return image.link