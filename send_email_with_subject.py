#Python code sending mail with attachments from your Gmail account 
#libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#additinal part for send email multiple user from gmail account
# list of email_id to send the mail
li = ["manishraj9214@gmail.com", "manrajmanish94@gmail.com","mamatha@ekagga.com"]
for i in range(len(li)):
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("maneesh@ekagga.com", "7577012050")
  #message = "I am maneesh"
  #s.sendmail("sender_email_id", li[i], message)

#end code for send multiple user

fromaddr = "maneesh@ekagga.com"
toaddr = "manishraj9214@gmail.com"
     
   # instance of MIMEMultipart
msg = MIMEMultipart()
      
   # storing the senders email address  
msg['From'] = fromaddr
       
   # storing the receivers email address 
msg['To'] = toaddr
   # storing the subject 
msg['Subject'] = "Write mail for send the documents"
   # string to store the body of the mail
body = "Body_of_the_mail"
	  
   # attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))
	   
   # open the file to be sent 
filename = "email.txt"
attachment = open("/home/ekagga/Desktop/email.txt", "rb")
  # instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')
  # To change the payload into encoded form
p.set_payload((attachment).read())
  # encode into base64
encoders.encode_base64(p)
	        
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		 
  # attach the instance 'p' to instance 'msg'
msg.attach(p)
		  
  # creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  # start TLS for security
s.starttls()
		    
   # Authentication
s.login(fromaddr, "7577012050")
		     
   # Converts the Multipart msg into a string
text = msg.as_string()
   # sending the mail
s.sendmail(fromaddr, toaddr, text)
		       
   # terminating the session
s.quit()
		       
