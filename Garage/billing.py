
#import print_options
#print_options.set_float_precision(2)
import smtplib
import math
import numpy as np

def pricing(s, e, method="ours"):
    if method == "ours":
        a = np.array([2.5,  2.5,  1.69734764, 2.29426227, 2.47006172, 2.49789661,  3.3515253,  
             4.20149163, 4.8811098,  4.92963575, 4.33614674, 3.52301568,  2.4992227,  
             2.48908476, 2.425155,   2.19162042, 1.64449852, 0.78895209,  2.5,
             2.5,        2.5,        2.5,        2.5,        2.5]) * 5
    else: # model in paper 
        a = np.array([1.        , 1.        , 3.5472664 , 2.86023068, 2.46170826,
           2.18194879, 1.96788501, 1.79601016, 1.65391848, 1.53434042,
           1.43272072, 1.34607337, 1.27237107, 1.21018075, 1.15841983,
           1.11617668, 1.08257446, 1.0566772 , 1.03744631, 1.02375297,
           1.01443887, 1.00840236, 1.00467948, 1.00249501]) * 8
    
    d = e - s
    res = 0
    if d.days > 0:
        res = (d.days-1) * a.sum() + np.sum(a[s.hour-1:24])+np.sum(a[:e.hour-1])
    else:
        res = np.sum(a[s.hour-1:e.hour-1])
    
    return res

#send email to customer for their bill. For now amount owed is based on a flat rate of $5/hr
def email(user_name,user_email,startTime,endTime): 
  server = smtplib.SMTP('smtp.gmail.com', 587)#configure email
  server.starttls()
  server.login("chdeng518@gmail.com", "L123456abc")#login to email
  h = endTime - startTime
  hours = round(h.total_seconds()/3600.00*100)/100.0
  charge = pricing(startTime, endTime, "ours") #hours * 5 #calculate amount owed
  hour = math.floor(hours) #extract amount of hours 
  minite = round((hours-hour)*60) #extract num minutes
  
  #compose message
  msg = "Hi %s, \nYour parking time is %s hours %s minites, charge is %s $\nThe charge will deduct from your registered credit card.\n" % (user_name, str(hour), str(minite), str(charge))
  msg = msg + 'Thank you for your parking!'

  #send mail
  server.sendmail("chdeng518@gmail.com", user_email, msg)
  server.quit()






