import pika
import time
from config import Session, Message, get_rabbitmq_channel, redis_client

def consume_messages():
    session = Session()
    
    try:
        channel = get_rabbitmq_channel()
        print("Waiting for messages...")

        def callback(ch, method, properties, body):
            message = body.decode()
            print(f"Received: {message}")

            # Simpan ke database
            new_message = Message(content=message)
            session.add(new_message)
            session.commit()

        channel.basic_consume(queue='notification', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError:
        print("❌ RabbitMQ tidak bisa dihubungi. Coba cek apakah servernya berjalan.")
        time.sleep(5)
        consume_messages()

    except KeyboardInterrupt:
        print("\n❗ Subscriber dihentikan.")
    
    finally:
        session.close()
        print("💾 Database session ditutup.")

if __name__ == "__main__":
    consume_messages()
