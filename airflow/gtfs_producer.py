from datetime import datetime
import time, requests
from kafka import KafkaProducer

url = "https://bdx.mecatran.com/utw/ws/gtfsfeed/realtime/bordeaux?apiKey=opendata-bordeaux-metropole-flux-gtfs-rt"
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        max_request_size=5 * 1024 * 1024  # 5 MB
)

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content
            timestamp = datetime.now().isoformat()
            print(f"[{timestamp}] Attempting to send {len(data)} bytes")

            # Send and flush to force delivery
            result = producer.send('tram_a_updates', value=data)
            metadata = result.get(timeout=10)  # This will raise if it fails

            print(f"✅ [{timestamp}] Sent to topic {metadata.topic} partition {metadata.partition} offset {metadata.offset}")
        else:
            print(f"❌ HTTP error {response.status_code}")
    except Exception as e:
        print(f"❌ [{datetime.now().isoformat()}] Error sending to Kafka: {e}")
    time.sleep(30)

