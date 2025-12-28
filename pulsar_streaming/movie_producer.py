import pulsar
import json
import time
from Movie_Streaming.Pipelines.load_movies import run_pipeline


client = pulsar.Client("pulsar://localhost:6650")

producer = client.create_producer(
    topic='persistent://public/default/movie_streaming'
)

movies_lst = run_pipeline()
total_movies = 0
try:
    for movie in movies_lst:
        producer.send(json.dumps(movie).encode("utf-8"))
        print(f"🎬 Sent movie: {movie['title']}")
        total_movies += 1
        time.sleep(1)

    print("\n✅ All movies have been sent successfully!")
    print(f'Total new Movies updated: {total_movies}')

except Exception as e:
    print(f"❌ Producer error: {e}")

finally:
    producer.close()
    client.close()
