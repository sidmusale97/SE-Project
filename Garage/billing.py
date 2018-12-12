
#import print_options
#print_options.set_float_precision(2)
import smtplib
import math


#send email to customer for their bill. For now amount owed is based on a flat rate of $5/hr
def email(user_name,user_email,startTime,endTime): 
  server = smtplib.SMTP('smtp.gmail.com', 587)#configure email
  server.starttls()
  server.login("chdeng518@gmail.com", "L123456abc")#login to email
  h = endTime - startTime
  hours = round(h.total_seconds()/3600.00*100)/100.0
  charge = hours * 5 #calculate amount owed
  hour = math.floor(hours) #extract amount of hours 
  minite = round((hours-hour)*60) #extract num minutes
  
  #compose message
  msg = "Hi %s, \nYour parking time is %s hours %s minites, charge is %s $\nThe charge will deduct from your registered credit card.\n" % (user_name, str(hour), str(minite), str(charge))
  msg = msg + 'Thank you for your parking!'

  #send mail
  server.sendmail("chdeng518@gmail.com", user_email, msg)
  server.quit()






