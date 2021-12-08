class BinaryToTextService:
	def execute(self, binary):
		letters = binary.split(" ")
		text = ""
		for letter in letters:
			text += chr(int(letter, 2))

		return text
