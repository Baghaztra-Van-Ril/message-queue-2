from config import Session, Message, get_rabbitmq_channel
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
session = Session()
channel = get_rabbitmq_channel()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            requests.post("http://localhost:5000/publish", json={"message": message})
    return render_template('index.html')

@app.route('/publish', methods=['POST'])
def publish_message():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({"error": "Message is required"}), 400
    
    # Simpan ke database
    new_message = Message(content=message)
    session.add(new_message)
    session.commit()
    
    # Kirim ke RabbitMQ
    channel.basic_publish(exchange='', routing_key='notification', body=message)
    
    return jsonify({"status": "Message sent and stored"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
