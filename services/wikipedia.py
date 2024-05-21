import wikipedia

class Wikipedia:

	def __init__(self, lang = "pt"):
		self.lang = lang

	def get_summary(self, query, sentences = 2):
		wikipedia.set_lang(self.lang)
		summary = wikipedia.summary(query, sentences)
		return summary

	def get_page(self, query):
		wikipedia.set_lang(self.lang)
		page = wikipedia.page(query)
		return page

	def search(query, results = 10):
		search = wikipedia.search(query, results)
		return search
	