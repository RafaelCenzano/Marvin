#import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#sending email must be gmail to use this script as it is right now
email_user = 'yourusername@gmail.com'
email_receiver = 'receiver@domain.com'
subject = 'Your subject here'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_receiver
msg['Subject'] = subject

#message area
email_message = 'message that can be changed.\nMulti-Line'
body = "Hello sent from program\n {}" .format(email_message)
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()

#sending code
server = smtplib.SMTP('smtp.gmail.com',587)
#'plus.smtp.mail.yahoo.com',465 for yahoo
server.starttls()
server.login(email_user,'your password')

server.sendmail(email_user,email_receiver,text)
server.quit()
#done
