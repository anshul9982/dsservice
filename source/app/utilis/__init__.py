import os
from flask import Flask
from flask import request, jsonify
from dotenv import load_dotenv
from ..service.messageService import MessageService

# Load environment variables from the .env file in the parent 'app' directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
messageService = MessageService()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.process_message(message)
    if result is not None:
        # Convert Pydantic model to dict for JSON serialization
        return jsonify(result.dict())
    else:
        return jsonify(None)
