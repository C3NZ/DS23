from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.regression import LinearRegressionWithSGD as lrSGD
from pyspark.sql import SparkSession


def main():
    spark = (
        SparkSession.builder.appName("python spark regression example")
        .config("spark.some.config.option", "some-value")
        .getOrCreate()
    )

    regressionDataFrame = spark.read.csv(
        "Advertising.csv", header=True, inferSchema=True
    )

    # Drop the first column
    regressionDataFrame = regressionDataFrame.drop("_c0")

    # Show the first 10 items inside of the dataframe
    regressionDataFrame.show(10)

    print(regressionDataFrame.describe())

    #
    regressionDataRDD = regressionDataFrame.rdd.map(list)

    regressionDataLabelPoint = regressionDataRDD.map(
        lambda data: LabeledPoint(data[3], data[0:3])
    )

    regressionLabelPointSplit = regressionDataLabelPoint.randomSplit([0.7, 0.3])

    regressionLabelPointTrainData = regressionLabelPointSplit[0]

    regressionLabelPointTestData = regressionLabelPointSplit[1]

    ourModelWithLinearRegression = lrSGD.train(
        data=regressionLabelPointTrainData, iterations=100, step=0.0002, intercept=True
    )

    print(ourModelWithLinearRegression)

    ourModelWithLinearRegression.predict(regressionLabelPointTestData)


if __name__ == "__main__":
    main()
