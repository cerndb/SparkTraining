# testSparkScala

This is an example of how you can write a Scala application to run Spark jobs.   
Build the project using `sbt` and run with spark-submit  

How to test:  
```
# build the jar
sbt clean package

bin/spark-submit --class ch.cern.test.testSparkScala <path>/target/scala-2.12/testsparkscala_2.12-0.1.jar
```
