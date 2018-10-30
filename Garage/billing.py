from ExitGate import scanPlate,get_datetime_hours
#import print_options
#print_options.set_float_precision(2)
import smtplib
import math



def email(user_name,user_email,hours): 
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("chdeng518@gmail.com", "L123456abc")
  charge = hours * 5
  hour = math.floor(hours)
  minite = round((hours-hour)*60)
  msg = "Hi %s, \nYour parking time is %s hours %s minites, charge is %s $\nThe charge will deduct from your registered credit card.\n" % (user_name, str(hour), str(minite), str(charge))
  msg = msg + 'Thank you for your parking!'
  server.sendmail("chdeng518@gmail.com", user_email, msg)
  server.quit()

def test(hours):
  user_name = "chunhua"
  user_email = "chunhua.deng518@gmail.com"
  email(user_name, user_email, hours)

if __name__ == "__main__":
  park_start_time,current_time,hours = get_datetime_hours("W92HSD")
  test(hours)

