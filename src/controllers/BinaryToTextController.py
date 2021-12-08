from flask import jsonify

class BinaryToTextController:
	def handle(self, data, BinaryToTextService):
		binaryToTextService = BinaryToTextService()

		if not 'binary' in data:
			return jsonify({"error": "No binary provided."}), 400


		return jsonify(binaryToTextService.execute(data["binary"]))
