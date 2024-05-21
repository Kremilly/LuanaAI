import pyttsx3
import speech_recognition as sr

class Comandos:

	def falar(mensagem):
		engine = pyttsx3.init()
		engine.say(mensagem)
		engine.runAndWait()

	def ouvir():
		r = sr.Recognizer()
		
		with sr.Microphone() as source:
			print('Aguardando...')
			audio = r.listen(source)
			
		try:
			frase = r.recognize_google(audio, language='pt-BR')
			print('Você disse: {}'.format(frase))
			return frase.lower()

		except:
			print('Não entendi')
			return None
		
	def executar(tarefa, mensagem):
		if tarefa != '':
			tarefa
			Comandos.falar(mensagem)