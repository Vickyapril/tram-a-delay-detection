import json
from kafka import KafkaConsumer, KafkaProducer
import gtfs_realtime_pb2

# Replace with your Peychotte stop IDs you found before
PEYCHOTTE_STOP_IDS = {"5230", "5231", "5284", "5815", "9128"}

# Kafka setup
KAFKA_BROKER = 'localhost:9092'
RAW_TOPIC = 'tram_a_updates'
CLEAN_TOPIC = 'gtfs_json'

consumer = KafkaConsumer(
    RAW_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='latest',
    #consumer_timeout_ms=10000
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🟢 Transformer started, listening to raw GTFS-RT feed...")

for msg in consumer:
    feed = gtfs_realtime_pb2.FeedMessage()
    try:
        feed.ParseFromString(msg.value)
    except Exception as e:
        print(f"❌ Failed to parse protobuf: {e}")
        continue

    filtered_entities = []

    for entity in feed.entity:
        if entity.HasField("trip_update"):
            trip = entity.trip_update.trip
            print(f"👀 Route: {trip.route_id}, Trip: {trip.trip_id}")
            #print(f"👀 Received entity for route_id: {trip.route_id}")
            # Filter by route_id (Tram A is 74)
            if trip.route_id == "74":
                # Check if any stop_time_update stop_id is in Peychotte
                print(f"🔎 Incoming route_id: {trip.route_id}")
                for stu in entity.trip_update.stop_time_update:
                    if stu.stop_id in PEYCHOTTE_STOP_IDS:
                        print(f"📍 Match found: stop_id {stu.stop_id} on route {trip.route_id}")
                        # Build a dict with key info to send as JSON
                        entity_json = {
                            "trip_id": trip.trip_id,
                            "route_id": trip.route_id,
                            "start_date": trip.start_date,
                            "stop_id": stu.stop_id,
                            "arrival_delay": stu.arrival.delay if stu.HasField("arrival") else None,
                            "departure_delay": stu.departure.delay if stu.HasField("departure") else None,
                            "arrival_time": stu.arrival.time if stu.HasField("arrival") else None,
                            "departure_time": stu.departure.time if stu.HasField("departure") else None,
                        }
                        filtered_entities.append(entity_json)
                        break  # no need to check more stops for this entity

    if filtered_entities:
        # Send each filtered entity as a separate JSON message
        for entity_json in filtered_entities:
            producer.send(CLEAN_TOPIC, entity_json)
        print(f"✅ Sent {len(filtered_entities)} filtered entities to {CLEAN_TOPIC}")

producer.flush()
