import random

class Random:

	def string(size = 10):
		return ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_') for i in range(size)
		)

	def number(size = 10):
		return ''.join(
			random.choice('0123456789') for i in range(size)
		)

	def color():
		return '#' + ''.join(
			random.choice('0123456789ABCDEF') for i in range(6)
		)

	def password(size = 10):
		return ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_#@!+()[]{}&*!?<>;: ') for i in range(size)
		)

	def uuid():
		return ''.join(
			random.choice('0123456789ABCDEF') for i in range(32)
		)

	def ip():
		return '.'.join(
			str(random.randint(0, 255)) for i in range(4)
		)

	def phrase(min = 8, max = 128):
		return ' '.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_ ') for i in range(random.randint(min, max))
		)

	def email():
		return ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_@.') for i in range(10)
		) + '@' + ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_.') for i in range(10)
		) + '.' + ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_') for i in range(3)
		)

	def url():
		return ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_.') for i in range(10)
		) + '.' + ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_') for i in range(10)
		) + '.' + ''.join(
			random.choice('ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz0123456789-_') for i in range(3)
		)

	def phone():
		return ''.join(
			random.choice('0123456789') for i in range(10)
		)

	def date():
		return ''.join(
			random.choice('0123456789') for i in range(4)
		) + '-' + ''.join(
			random.choice('0123456789') for i in range(2)
		) + '-' + ''.join(
			random.choice('0123456789') for i in range(2)
		)