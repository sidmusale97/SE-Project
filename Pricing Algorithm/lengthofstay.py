"""
Copyright 2018, Chunhua Deng, Siyu Liao, Xianglong Feng
"""

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
    
    
    # configure time range
    everymin = 60 
    
    for year in range(2012, 2018):
        # filter out 0 mins stay
        dfs[year]['rdd'] = dfs[year]['rdd'].filter(dfs[year]['rdd']['Duration_mins'] > 0)  

        # group to get ['Duration_30min', 'hour(TransactionDateTime)', 'count']
        dfs[year]['hourly_{}min'.format(everymin)] = get_hourly(dfs[year]['rdd'], 60)

        
    # generate pandas results
    f = lambda left,right: pd.merge(left,right,on='hour', how='outer')
    l = []
    for year in dfs:
        d = dfs[year]['hourly_{}min'.format(everymin)]
        d = d.withColumnRenamed("avg", "{}".format(year))
        d = d.toPandas()
        l.append(d)

    hourly_df = hourly_df.sort_values('hour')
    hourly_df.to_csv('lengthofstay.csv')
    