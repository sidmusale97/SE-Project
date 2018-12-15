from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import *
import numpy as np
import matplotlib.pyplot as plt
from util import *

import pandas as pd
from functools import reduce

if __name__ == "__main__":
    
    # create context
    sqlCtx = SQLContext(sc)

    # setting data scheme
    schema = StructType([
        StructField("TransactionId", IntegerType()),
        StructField("TransactionDateTime", TimestampType()),
        StructField("TransactionDate", TimestampType()),
        StructField("timeStart", StringType()),
        StructField("timeExpired", StringType()),
        StructField("Duration_mins", IntegerType()),
        StructField("Amount", DoubleType()),
        StructField("PaymentMean", StringType()),
        StructField("MeterCode", IntegerType()),
        StructField("ElementKey", IntegerType()),
    ])
    
    # read data
    data = sqlCtx.read.format('com.databricks.spark.csv').schema(
        schema).option('header', 'true').load('/raid/data/ParkingTransaction_20120101_20170930_cleaned.csv')

    # cache data 
    data.cache()
    data.printSchema()
    
    
    # generate dataframe for all years
    dfs = {}
    for year in range(2012, 2018):
        dfs[year] = {'rdd':None, 'hourly':None}
        dfs[year]['rdd'] = filter_by_date(data, ('{}-01-01'.format(year), '{}-12-31'.format(year)))
        dfs[year]['rdd'].cache()
        dfs[year]['hourly'] = count_by_time(dfs[year]['rdd'], 'hour')
        dfs[year]['hourly'].cache()
    
    # generate pandas results
    f = lambda left,right: pd.merge(left,right,on='hour', how='outer')
    l = []
    for year in dfs:
        d = dfs[year]['hourly']
        d = d.withColumnRenamed("count", "{}".format(year))
        d = d.toPandas()
        l.append(d)
    
    # write output
    hourly_df = reduce(f, l)
    hourly_df = hourly_df.set_index('hour')
    hourly_df.to_csv('hourly.csv')
    