from kafka import KafkaConsumer

consumer = KafkaConsumer("Hello-Kafka", bootstrap_servers='vm-cdl-d-10:9092')

for msg in consumer:
	print (msg)
