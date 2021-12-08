from flask import Flask, request, jsonify

from controllers.BinaryToTextController import BinaryToTextController
from controllers.TextToBinaryController import TextToBinaryController

from services.BinaryToTextService import BinaryToTextService
from services.TextToBinaryService import TextToBinaryService

app = Flask(__name__)

binaryToTextController = BinaryToTextController()
textToBinaryController = TextToBinaryController()


@app.route('/binary', methods=['POST'])
def binary():
	if request.method == 'POST':
		data = request.get_json()
		return binaryToTextController.handle(data, BinaryToTextService)
	else:
		return jsonify({'error': 'Invalid request method'})


@app.route('/text', methods=['POST'])
def text():
	if request.method == 'POST':
		data = request.get_json()
		return textToBinaryController.handle(data, TextToBinaryService)
	else:
		return jsonify({'error': 'Invalid request method'})


if __name__ == '__main__':
	app.run(host='localhost', port=3000, debug=False)
