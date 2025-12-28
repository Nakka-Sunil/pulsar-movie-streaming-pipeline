import pulsar
import time
import json
from Movie_Streaming.mailing_service.send_mail_serv import send_email

client = pulsar.Client("pulsar://localhost:6650")

consumer = client.subscribe(
    topic="persistent://public/default/movie_streaming",
    subscription_name="email_movie_sub",
    consumer_type=pulsar.ConsumerType.Shared
)

print("📨 Email Consumer Started...")

try:
    while True:
        msg = consumer.receive()
        try:
            data = msg.data().decode("utf-8")
            movie_data = json.loads(data)

            print(f"📩 New movie received for email: {movie_data['title']}")

            send_email(movie_data)
            consumer.acknowledge(msg)
            print("✅ Email sent successfully")

        except Exception as e:
            print(f"❌ Email failed, retrying: {e}")
            consumer.negative_acknowledge(msg)
            time.sleep(2)

except KeyboardInterrupt:
    print("Email consumer stopped manually")

finally:
    consumer.close()
    client.close()
