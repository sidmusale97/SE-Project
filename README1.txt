Auto Park
-------------------------------------------------

Pre reqs
-------------------------------------------------
install node.js from any popular distributions 

node.js requires many modules so please navigate to webform folder and run the following command

	npm install --save

python has some library dependecies as well. Please install all the following libs

mysql.connector
requests
json
twilio
matplotlib


Running the tests
-------------------------------------------------
For demo 1 the program will be run in the console for garage logic and browser for the website

To run entire system navigate to garage folder and run EntranceGate.py in one terminal and ExitGate.py in another terminal
Follow the prompts on the screen.

Ex.
After EntranceGate.py is run the follow prompt and responses can be given

	Please position your car in the correct position and click the button:
	1
	Our camera scanned Y73JMU as your license plate. Enter 1 if this plate is correct or enter correct plate otherwise:
	1
	.....

In this implementation the responses for these prompts are very important. For the program to run correctly 
* the same car cannot enter the garage twice before exiting
	- this can be remedied by taking advantage of the prompt that allows you to enter your license plate. This unrealistic situation is not accounted for and will crash the program
	- Also if a mistake is made the clearHistory function in the Simulation file can be called to reset the database


To run website navigate to webform and run server.js file
	- go to browser and navigate to localhost 8000


