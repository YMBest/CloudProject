# CloudProject

Cloud Computing Project2

In this project, we learn to use Apache Spark in EC2 to train a model. Then we use this model to predict verification data.

First of all, we are supposed to use EWR to create spark cluster. When setting the configuration, we need to choose spark: Spark2.4.8 on Hadoop 2.10.1. Also we should set the number of instances to 5 (1 master and 4 slaves), and disable auto-termination. We should create a new key pair to get access from our own laptop. Then in the first instance we created, we should click edit inbound rules and add Custom TCP, search for SSH. Then connect to the EMR with my own computer.Then run jupyter on it. We should develop a Spark application then to use MLlib to train the quality prediction using the training data parallelly. After all of this done, we will get a model file.

With this model file, we should create a docker image. The base image should be gcr.io/datamechanics/spark:platform-3.2.1-latest. It should also contain information about the prediction python file, model generated in the previous step and the environment information.  Then I wrote a prediction python file to build the docker image. After running it, it will show the estimated result and accuracy. The final step is to upload the docker image.

