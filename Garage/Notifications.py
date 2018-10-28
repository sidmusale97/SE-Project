from twilio.rest import Client
import authCode

# Your Account SID from twilio.com/console
account_sid = "ACa4b7d28b61df55846c11b7289c745035"
# Your Auth Token from twilio.com/console
auth_token  = "e9955df2d9a3f028f0a318cb7707858a"    
# twilio client init
client = Client(account_sid, auth_token)

# right now this just sends a randomly generated code to the phone number without saving
# need to save and store a unique code per user to check against
def sendAuth(userPhone):
    message = client.messages.create(
        to=userPhone,          
        from_="+19735471673",       # number given for free trial by twilio - dont change for now
        body='Your unique code is ' + authCode.generateCode()
    )
    print('twilio message id (debug): ' + message.sid)
    