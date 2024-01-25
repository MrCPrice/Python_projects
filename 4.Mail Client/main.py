import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

with open('c:\\Users\\conno\\Coding projects\\Python\Mail Client\\pass.txt', 'r') as f:
    password = f.read()

server.login("connorprice111998@gmail.com", password)

msg = MIMEMultipart()
msg['From'] = 'connorprice111998@gmail.com'
msg['To'] = 'connorp2013@outlook.com'
msg['Subject'] = 'Just A Test!'

with open('c:\\Users\\conno\\Coding projects\\Python\Mail Client\\mess.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

attachment = open('c:\\Users\\conno\\Coding projects\\Python\Mail Client\\image.jpg', 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('connorprice111998@gmail.com', 'connorp2013@outlook.com', text)