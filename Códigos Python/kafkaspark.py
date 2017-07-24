from pyspark import SparkConf, SparkContext
from operator import add
import sys
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from kafka import SimpleProducer, KafkaClient
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='vm-cdl-d-10:9092')

def handler(message):
    records = message.collect()
    for record in records:
        producer.send('Hello-Kafka', str(record))
        producer.flush()

def main():
    sc = SparkContext(appName="PythonStreamingDirectKafkaWordCount")
    ssc = StreamingContext(sc, 10)

    #brokers, topic = sys.argv[1:]
    #kvs = KafkaUtils.createDirectStream(ssc, ['topic-test'], {"metadata.broker.list": 'vm-cdl-d-10:9092'})
    lines = ssc.socketTextStream('172.16.20.39', 9999)
    lines.foreachRDD(handler)

    ssc.start()
    ssc.awaitTermination()
if __name__ == "__main__":

   main()