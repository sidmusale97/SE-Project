import mysql.connector
import smtplib




def email(user_name,user_email,hours): 
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("chdeng518@gmail.com", "L123456abc")
  charge = hours * 5
  msg = "Hi %s, \nYour parking hours is %s, charge is %s $\nThe charge will deduct from your registered credit card.\n" % (user_name, str(hours), str(charge))
  msg = msg + 'Thank you for your parking!'
  server.sendmail("chdeng518@gmail.com", user_email, msg)
  server.quit()

def test():
  user_name = "chunhua"
  user_email = "chunhua.deng518@gmail.com"
  hours = 5.5
  email(user_name, user_email, hours)

if __name__ == "__main__":
  test()

