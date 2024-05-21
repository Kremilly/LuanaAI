import requests

class Requests:
	
	def __init__(self, url, method, data, headers):
		self.url = url
		self.method = method
		self.data = data
		self.headers = headers

	def send(self):
		if self.method == 'GET':
			return requests.get(self.url, params=self.data, headers=self.headers)
		elif self.method == 'POST':
			return requests.post(self.url, data=self.data, headers=self.headers)
		elif self.method == 'PUT':
			return requests.put(self.url, data=self.data, headers=self.headers)
		elif self.method == 'DELETE':
			return requests.delete(self.url, data=self.data, headers=self.headers)
		else:
			return None

	def get_response(self):
		return self.send().json()

	def get_status_code(self):
		return self.send().status_code

	def get_response_code(self):
		return self.get_response()['code']

	def get_response_message(self):
		return self.get_response()['message']

	def get_response_data(self):
		return self.get_response()['data']