Auto Park
-------------------------------------------------

Description of Files
-------------------------------------------------
Garage:
authCode.py: generates and sends security authentication code to customer
billing.py: creates a bill and communicates the final price to the customer
database.py: queries the database to check for billing and authentication code verification
Elevator.py: script that acts as the elevator (traveling to floor for parking)
EntranceGate.py: entrance gate simulation script (sign in)
ExitGate.py: exit gate simulation script (exit and pricing)
Notifications.py: sends codes to customer email or text (interacts with authCode.py)
SpotVerify.py: verifies customer parked in the correct parking spot 
SpotView.py: allows customer to view current state of garage (generates GUI)
test.py: testing script (not used)
TrafficManagement.py: interacts with elevator module to make sure one driver is driving on each floor 

Routes:
admin.js: routing for the admin pages and login
Entrance.js: displays the entrance gate page
index.js: homepage and routing to other pages
parkmap.js: displays our real-time GUI of the parking garage status
reservation.js: routing for pages concerning reservations
users.js: routing for pages concerning customer profiles and logins




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


