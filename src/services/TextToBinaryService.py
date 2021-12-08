class TextToBinaryService:
	def execute(self, text):
		text = " ".join(format(ord(x), 'b') for x in text)

		return text

