import pulsar
import time
import json
from Movie_Streaming.Database.movie_repo import get_movies

client = pulsar.Client("pulsar://localhost:6650")

dlq_policy = pulsar.ConsumerDeadLetterPolicy(
    max_redeliver_count=3,
    dead_letter_topic="persistent://public/default/movies_dlq"
)

consumer = client.subscribe(
    topic='persistent://public/default/movie_streaming',
    subscription_name='db_store_sub',
    consumer_type=pulsar.ConsumerType.Shared,
    dead_letter_policy=dlq_policy,
    negative_ack_redelivery_delay_ms=3000
)
total_movies_consumed = 0

try:
    while True:
        msg = consumer.receive()

        raw_data = msg.data().decode('utf-8')
        print(f"Received Message: {raw_data}")

        movie_data = json.loads(raw_data)

        get_movies(movie_data)
        total_movies_consumed += 1
        consumer.acknowledge(msg)
        time.sleep(2)
except KeyboardInterrupt as e:
    print(f"Error in consuming Messages: {e}")
    consumer.negative_acknowledge(msg)

finally:
    print(f"Total movies consumed: {total_movies_consumed}")
    consumer.close()
    client.close()
