import json
import os
import time
from confluent_kafka import Consumer
from db import Base, engine, SessionLocal
from models import AnalyticsData

# Create the database tables
Base.metadata.create_all(bind=engine)

KAFKA_HOST = os.environ.get('KAFKA_HOST')

# Kafka configuration
bootstrap_servers = f'{KAFKA_HOST}:9092'
topic = 'analytics_topic'
group_id = 'analytics_consumer_group'

# Create a Kafka consumer instance
consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id
})

# Subscribe to the Kafka topic
consumer.subscribe([topic])

# Consume and process the analytics events
while True:
    # Poll for new messages
    message = consumer.poll(1.0)

    if message is None:
        continue

    if message.error():
        print(f"Consumer error: {message.error()}")
        continue

    # Retrieve the event data from the message
    event_json = message.value().decode('utf-8')

    try:
        # Parse the event data as JSON
        event = json.loads(event_json)

        # Generate a timestamp
        timestamp = int(time.time())

        # Create an instance of AnalyticsData
        analytics_data = AnalyticsData(
            timestamp=timestamp,
            event_type=event['event_type'],
            user_id=event['user_id'],
            page_id=event['page_id'],
            duration=event['duration']
        )

        # Insert the analytics data into the database
        db = SessionLocal()
        db.add(analytics_data)
        db.commit()
        db.refresh(analytics_data)

        print("Received and stored event:", event)

    except json.JSONDecodeError:
        print("Invalid JSON format:", event_json)

# Close the Kafka consumer
consumer.close()
