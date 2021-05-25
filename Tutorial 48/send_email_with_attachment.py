import smtplib
from email.message import EmailMessage
import imghdr
email_sender = "anotheremail@gmail.com"
email_sender_password = "YourPassword123"
message1 = EmailMessage()
message1["Subject"] = "Image Attached"
message1["From"] = email_sender
message1["To"] = "anotheremail@gmail.com"
message1.set_content("See image below.")
with open("python-logo.png","rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
message1.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(email_sender,email_sender_password)
    smtp.send_message(message1)