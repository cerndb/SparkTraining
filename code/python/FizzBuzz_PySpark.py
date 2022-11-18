#!/usr/bin/env python

# Example of runnig Spark code using Python
#
# Dependency: download Spark binaries and run from Spark Home
#
# Run with bin/spark-submit FizzBuzz_PySpark.py

from pyspark.sql import SparkSession
spark = (SparkSession.
         builder.
         appName("testSparkScala").
         getOrCreate()
        )
    
print("FizzBuzz example!")

spark.sql("""
      select case
        when id % 15 = 0 then 'FizzBuzz'
        when id % 3 = 0 then 'Fizz'
        when id % 5 = 0 then 'Buzz'
        else cast(id as string)
        end as FizzBuzz
      from range(1,20)
      order by id""").show()

print("End of the example")

