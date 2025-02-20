# Emails in python
''' Create you own debug server with following command -
python3 -m smtpd -c DebuggingServer -n localhost:1025

'''

import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
ID = os.getenv('EMAIL_ID')
PW = os.getenv('PASSWORD')
TO = os.getenv('RECEIVER')

''' Below 2 methods are giving Bad Credentials Error - So have to solve it later.'''
# ## Method - 1 : Using gmail 
# print('\n-------------------------------Using gmail and SMTP---------------------------\n')
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(ID, PW)

#     subject = 'Daiict Fest 2025 - Using SMTP'
#     body = 'Hey, How are you doing? You up for Daiict Fest this Saturday? Respond ASAP.'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(ID, TO, msg)


# ## Method - 3 : Alternative for Method -1 using SMTP_SSL
# print('\n-------------------------------Using SMTP_SSL---------------------------\n')
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(ID, PW)

#     subject = 'Daiict Fest 2025 - Using SMTP_SSL'
#     body = 'Hey, How are you doing? You up for Daiict Fest this Saturday? Respond ASAP.'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(ID, TO, msg)


## Method - 3 : Using Debug Server.
print('\n---------------------Using Debug Server - Localhost---------------------\n')
with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Daiict Fest 2025 - Using Debug Server'
    body = 'Hey, How are you doing? You up for Daiict Fest this Saturday? Respond ASAP.'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(ID, TO, msg)


## Formatting Msg
print('\n--------------------------Formatting Msg-----------------------------\n')
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Daiict Fest 2025 - Formatting Msg'
msg['From'] = ID
msg['To'] = TO
msg.set_content('Hey, How are you doing? You up for Daiict Fest this Saturday? Respond ASAP.')

with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.send_message(msg)


## Adding Attachments
print('\n--------------------------Adding Attachments---------------------------\n')
from email.message import EmailMessage
import imghdr # Built-in module for images

msg = EmailMessage()
msg['Subject'] = 'Checkout the outputs of Multiprocessing!'
msg['From'] = ID
msg['To'] = TO
msg.set_content('Images attached...')

files = [
    'images/Img-Sizing-Multiprocessing.png',
    'images/Multiprocessing.png',
    'images/Threading.png'
]

for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    # For generic data. Google it!
    # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.send_message(msg)


## Sending Multiple Emails
print('\n------------------------Sending Multiple Emails-------------------------\n')
from email.message import EmailMessage
import imghdr # Built-in module for images

contacts = [TO, 'test@gmail.com', 'test1@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Daiict Fest 2025 - Sending Multiple Emails'
msg['From'] = ID
msg['To'] = TO
msg.set_content('Hey, How are you doing? You up for Daiict Fest this Saturday? Respond ASAP.')

with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.send_message(msg)


## Mail with HTML
print('\n--------------------------Mail with HTML--------------------------------\n')
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'HTML Content!'
msg['From'] = ID
msg['To'] = TO

msg.set_content('This is a plain text email')

msg.add_alternative('''\
<!DOCTYPE html>
<html>
    <body>
        <h1 style='color:SlateGray;'>This is an HTML Email!</h1>
    </body>
</html>                    
''', subtype='html')

with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.send_message(msg)