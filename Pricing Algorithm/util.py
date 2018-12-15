"""
Copyright 2018, Chunhua Deng, Siyu Liao, Xianglong Feng
"""

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import *
import numpy as np


def filter_by_date(data, dates=("2012-01-01", "2012-12-31"), col='TransactionDateTime'):
    """
    data : input rdd data
    dates: the time range for filtering
    col  : column name where to put filter on
    """
    
    date_from, date_to = [to_date(lit(s)).cast(TimestampType()) for s in dates]
    res = data.where((data[col] >= date_from) & (data[col] <= date_to))
    return res


def count_by_time(df, timetype='hour', col='TransactionDateTime'):
    """
    df  : input data frame
    timetype : it can be hour, month, dayofyear or dayofweek
    col : the column we want to format as timetype
    """
    
    if timetype=='hour':
        res = df.groupBy(hour(col).alias(timetype))
    elif timetype=='month':
        res = df.groupBy(month(col).alias(timetype))
    elif timetype=='dayofyear':  # daily
        res = df.groupBy(dayofyear(col).alias(timetype))
    elif timetype=='dayofweek':
        res = df.select('TransactionId', date_format(col, 'E').alias(timetype)).groupBy(timetype)
    else:
        print("unsupported", timetype)
        return None
    
    res = res.agg(count(lit(1)))
    res = res.withColumnRenamed("count(1)", "count")
    res = res.orderBy(timetype)
    return res


def get_hourly(df, everymin=60):
    """
    df : input dataframe
    everymin: every certain minutes is counted as a time range
    """
    
    f = udf(lambda minutes: minutes // everymin, IntegerType())
    colname = "Duration_{}min".format(everymin)
    tmpdf = df.withColumn(colname, f(df['Duration_mins']))
    tmpdf = tmpdf.groupBy(
        colname, 
        hour('TransactionDateTime').alias('hour')).agg(count("*"))
    tmpdf = tmpdf.withColumnRenamed("count(1)", "count")
    tmpdf = tmpdf.groupBy('hour').agg(avg(col(colname)).alias('avg'))
    tmpdf = tmpdf.withColumnRenamed("count(1)", "count")
    tmpdf.cache()
    return tmpdf
