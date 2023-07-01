import os
import time
import json
import random
from confluent_kafka import Producer

KAFKA_HOST = os.environ.get('KAFKA_HOST')

# Kafka configuration
bootstrap_servers = f'{KAFKA_HOST}:9092'
topic = 'analytics_topic'

# Create a Kafka producer instance
producer = Producer({'bootstrap.servers': bootstrap_servers})

# List of possible event types
event_types = ['click', 'purchase', 'login', 'logout', 'view']

# List of user IDs
user_ids = ['user123', 'user456', 'user789', 'userabc', 'userxyz']

# List of page IDs
page_ids = ['page123', 'page456', 'page789', 'pageabc', 'pagexyz']


# Mock analytics data
def run():
    while True:
        # Generate random values for event fields
        event_type = random.choice(event_types)
        user_id = random.choice(user_ids)
        page_id = random.choice(page_ids)
        duration = random.randint(1, 10)

        # Create the analytics event
        event = {
            'timestamp': int(time.time()),
            'event_type': event_type,
            'user_id': user_id,
            'page_id': page_id,
            'duration': duration
        }

        # Convert event data to JSON
        event_json = json.dumps(event)
        print(event_json)

        # Produce the event to the Kafka topic
        producer.produce(topic, value=event_json)

        # Flush the producer to ensure the message is sent
        producer.flush()

        # Sleep for a certain duration to control the data flow rate
        time.sleep(10)  # Adjust the sleep duration as needed


if __name__ == '__main__':
    run()
