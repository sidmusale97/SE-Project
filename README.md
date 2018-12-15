# Auto Park


## Pre reqs

install node\.js from any popular distributions 

node.js requires many modules so please navigate to webform folder and run the following command

```
npm install --save
```

python has some library dependecies as well. Please install all the following libs
```
mysql.connector
requests
json
twilio
matplotlib
```

## Running the tests

For demo 1 the program will be run in the console for garage logic and browser for the website

To run entire system navigate to garage folder and run EntranceGate.py in one terminal and ExitGate.py in another terminal
Follow the prompts on the screen.

Ex.
After EntranceGate.py is run the follow prompt and responses can be given
```
	Please position your car in the correct position and click the button:
	1
	Our camera scanned Y73JMU as your license plate. Enter 1 if this plate is correct or enter correct plate otherwise:
	1
	.....
```

In this implementation the responses for these prompts are very important. For the program to run correctly 
* the same car cannot enter the garage twice before exiting
	- this can be remedied by taking advantage of the prompt that allows you to enter your license plate. This unrealistic situation is not accounted for and will crash the program
	- Also if a mistake is made the clearHistory function in the Simulation file can be called to reset the database


To run website navigate to webform and run server.js file
	- go to browser and navigate to localhost 8000


## Pricing Algorithm

This project incorporates the dynamic pricing feature. All algorithm/analysis related codes are under `Pricing Algorithm` directory. We also add our price page on to the website (under `WebForm` directory) and present into the garage system (under `directory`). 

### pre-reqs

In this python code, the program heavily relies on the math calculation, data visualization and I/O operation.

So before run this code, one should make sure the python libraries installed in the PC.

```
import csv
import numpy as np
from scipy.optimize import leastsq
import math
import matplotlib.pyplot as plt

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import *
```

Make sure the other supporting files are also under the same directory.

### data preparation


The data can be re-generated via [here](https://github.com/rexthompson/DATA-512-Final-Project), or download directly [here](https://s3.us-west-2.amazonaws.com/rext-data512-final-project/ParkingTransaction_20120101_20170930_cleaned.csv). 


### generating parking demand

You will need `pyspark` to generate the parking demand, including hourly, daily, weekly and monthly, and also the length of stay. Results will be output as in `csv` format, which could be easily drawn into figures and curves. 

To run the pyspark, following is the configuration we used:
```
pyspark --driver-memory 20g --executor-memory 60g
```

As a result, here is an example of hourly parking demand we generated. 

![Hourly Parking Demand](/hourly.png)

