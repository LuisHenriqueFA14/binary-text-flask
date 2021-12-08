from flask import jsonify

class TextToBinaryController:
	def handle(self, data, TextToBinaryService):
		textToBinaryService = TextToBinaryService()

		if not 'text' in data:
			return jsonify({"error": "No text provided."}), 400

		return jsonify(textToBinaryService.execute(data["text"]))
