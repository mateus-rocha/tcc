from pyspark import SparkContext

logFile = "teste.csv"
sc = SparkContext("local",  "SimpleApp")
logData = sc.textFile(logFile).cache()

numAs = logData.count()

print ("Linhas : %i" % numAs)

sc.stop()
