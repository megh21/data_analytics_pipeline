# generate_data.py
import json
import random
from datetime import datetime, timedelta
from kafka import KafkaProducer

def generate_random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

def generate_data(num_records):
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 1, 1)
    transaction_types = ['Sent', 'Received', 'Paid']
    
    for _ in range(num_records):
        transaction_type = random.choice(transaction_types)
        date = generate_random_date(start_date, end_date)
        amount = round(random.uniform(10, 1000), 2)
        
        message = {'Transaction_Type': transaction_type, 'Date': date.strftime('%Y-%m-%d'), 'Amount': amount}
        producer.send('transactions-topic', value=message)
    
    producer.flush()
    producer.close()

if __name__ == "__main__":
    generate_data(1000)  # Generate 1000 records
