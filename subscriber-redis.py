from flask import Flask, render_template
from flask_socketio import SocketIO
import redis
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Inisialisasi Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
pubsub = redis_client.pubsub()
pubsub.subscribe('notification')  # Channel untuk notifikasi real-time

# Fungsi untuk listen Redis dan kirim ke WebSocket
def redis_listener():
    for message in pubsub.listen():
        if message['type'] == 'message':
            socketio.emit('new_alert', {'message': message['data']})

# Jalankan listener Redis di thread terpisah
threading.Thread(target=redis_listener, daemon=True).start()

@app.route('/')
def index():
    return render_template('message.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)
