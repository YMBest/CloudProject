import os
os.environ['SPARK_HOME']="../"

#Create SparkContext for this section.
from pyspark.context import SparkContext
sc = SparkContext('local')

#Create SparkSession.
from pyspark.sql.session import SparkSession

spark = SparkSession.builder \
        .appName('Yiming') \
        .getOrCreate()

#Import VectorAssembler and get features transform.
from pyspark.ml.feature import VectorAssembler

validation_data_path = "ValidationDataset.csv"
validation_data = spark.read.option("delimiter", ";") \
                .option("header", "true") \
                .option("inferSchema","true") \
                .csv(validation_data_path)

feature_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                    'pH', 'sulphates', 'alcohol']

validation_assembler = VectorAssembler(inputCols=feature_columns,outputCol="features")
td_validation = validation_assembler.transform(validation_data)


#Import RandomForestClassificationModel and transform the dataset.
from pyspark.ml.classification import RandomForestClassificationModel

rfcfm = RandomForestClassificationModel.load("./model_Yiming")
predictions = rfcfm.transform(td_validation)

#Import evaluator and show the results.
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="quality", predictionCol="prediction",metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Accuracy = %s" % (accuracy))
predictions.select('quality', 'prediction', 'probability').show()

