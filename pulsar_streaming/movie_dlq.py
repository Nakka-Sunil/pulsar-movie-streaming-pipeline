import pulsar
# import time
import json

client = pulsar.Client("pulsar://localhost:6650")

consumer = client.subscribe(
    topic='persistent://public/default/movies_dlq', 
    subscription_name='dlq_movies_sub'
)

try:
    while True:
        msg = consumer.receive()
        try:
            failed_data = json.loads(msg.data().decode('utf-8'))
            
            print("-" * 30)
            print(f"💾 STORING FAILED TASK: {failed_data}")
            # Example: db.failed_orders.insert_one(failed_data)
            
            consumer.acknowledge(msg)
            print("✅ Error logged and message cleared from DLQ.")
        except Exception as e:
            print(f"Failed to store error record: {e}")
# except Exception as e:
#     print(f'❌ Error in DLQ consumer: {e}')

finally:
    consumer.close()
    client.close()
