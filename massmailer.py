import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'

# List of recipients
recipients = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

# Email content
subject = 'Your Subject Here'
body = '''\
Dear [Name],

This is a test email sent using a Python script.

Best regards,
Your Name
'''

# Create the SMTP session
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Send emails
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    # Personalize the email body
    personalized_body = body.replace('[Name]', recipient.split('@')[0])
    msg.attach(MIMEText(personalized_body, 'plain'))

    # Send the email
    server.sendmail(sender_email, recipient, msg.as_string())

# Close the SMTP session
server.quit()

print("Emails sent successfully!")
