from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("bigdata").getOrCreate()

    df1 = spark.read.load("hdfs:///user/maria_dev/data/final.csv",
                          format="csv", sep=",", inferSchema="true", header="true")

    df1.createOrReplaceTempView("bitcoin")

    result = spark.sql("""
        select time, avg(btc) as btc
        from bitcoin
        where time like '211204%' 
        group by time
        order by btc
    """)

    for row in result.collect():
        print(row.time, row.btc)
