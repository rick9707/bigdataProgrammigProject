from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("bigdata").getOrCreate()

    df1 = spark.read.load("hdfs:///user/maria_dev/data/final2.csv",
                          format="csv", sep=",", inferSchema="true", header="true")

    df1.createOrReplaceTempView("bitcoin")

    result = spark.sql("""
        select date, time, btc from
        (select date, time, btc, row_number() over (partition by date order by date, btc) as score 
        from bitcoin ) 
        where score='1'
    """)

    for row in result.collect():
        print(row.date, row.time, row.btc)
