import json
import os
from flask import Flask
from flask import request, jsonify
from kafka import KafkaProducer
from dotenv import load_dotenv
from ..service.messageService import MessageService

# Load environment variables from the .env file in the parent 'app' directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
messageService = MessageService()

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda v: v.encode('utf-8')
)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.process_message(message)
    if producer:
        serialized_result = result.json()
        producer.send(os.getenv("KAFKA_TOPIC"), serialized_result)
        producer.flush()
    return jsonify(result.dict())
