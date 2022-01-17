import smtplib
email_sender = "youremail@gmail.com"
email_sender_password = "YourPassword123"
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(email_sender,email_sender_password)
    subject = "Test"
    body = "How are you?"
    message = f"Subject:{subject}\n\n{body}"
    smtp.sendmail(email_sender,"anotheremail@gmail.com",message)