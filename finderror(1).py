from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "StreamingErrorCount")
ssc = StreamingContext(sc,10)

ssc.checkpoint("hdfs:///spark/streaming")
ds1 = ssc.socketTextStream("localhost",9999)
count = ds1.flatMap(lambda x:x.split(" ")).filter(lambda word:"ERROR" in word).map(lambda word:(word,1)).reduceByKey(lambda x,y:x+y)

count.pprint()
ssc.start()
ssc.awaitTermination()
