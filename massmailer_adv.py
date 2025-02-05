import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# Load the Excel file
df = pd.read_excel('john.xlsx')

# Display the first few rows to verify data
print(df.head())
# Email server configuration
image_path = 'image.jpg'
image_path2 = 'image2.jpg'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'xzoneandesports@gmail.com'
sender_password = 'fwtl jzkx ytaj rnrf'  # Consider using environment variables for security
# Establish a connection to the email server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)

# Iterate through the DataFrame and send emails
for index, row in df.iterrows():
    recipient_name = row['Name']
    recipient_email = row['Email']
    # Customize your message
    subject = ' Welcome to Lanstorm: Your Gaming Adventure Awaits!'
    body = """
    <html>
        <body>
            <p>Dear Participants,</p>
            <p>We are thrilled to announce that you have successfully registered for <b>Lanstorm</b>, our upcoming gaming tournament! We're excited to have you join us for this exhilarating event. Get ready for a competitive and fun-filled experience as we dive into the world of gaming from <b>February 6th to 9th, 2025</b>.</p>
            <h3>Join Our Discord Community!</h3>
            <p>To enhance your tournament experience, we invite you to join our dedicated Discord server! This is the perfect place to connect with fellow gamers, strategize, share tips, and stay updated on all tournament-related news. Here’s your exclusive link to join: <a href="https://discord.gg/9XhnYWKTpG">https://discord.gg/9XhnYWKTpG</a></p>
            <h3>Spread the Word!</h3>
            <p>We encourage you to invite your teammates and friends to join our Discord community as well! The more players we have, the more exciting the competition will be. Let’s build a vibrant and engaging community together!</p>
            <h3>Event Details:</h3>
            <ul>
                <li><b>Dates:</b> February 6-9, 2025</li>
                <li><b>Prize Pool:</b> ₹1,00,000</li>
                <li><b>Location:</b> Aaruush, SRM IST</li>
            </ul>
            <h3>Need Assistance?</h3>
            <p>If you have any questions or need further information, please feel free to reach out to our Points of Contact at Lanstorm:</p>
            <ul>
                <li><b>Ayush Mukherjee:</b> 9188655439</li>
                <li><b>Harsh Bansal:</b> 8630980965</li>
            </ul>
            <p>Thank you for registering and being a part of this thrilling journey. We are excited to see you compete in Lanstorm and wish you the best of luck in the tournament!</p>
            <p>Game on! 🎮</p>
            <p>Best regards,<br>
            Committee Head,<br>
            X-Zone & Esports,<br>
            Aaruush'24</p>
            <div style="text-align: left;">
                <img src="cid:image1" style="width: 150px; height: auto; margin-right: 2px;">
                <img src="cid:image2" style="width: 150px; height: auto;">
            </div>
        </body>
    </html>
    """
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Cc'] = 'xzone@aaruush.net'
    msg['Bcc'] = 'ramspam08@gmail.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    with open(image_path, 'rb') as img:
        mime = MIMEImage(img.read())
        # Define the image's ID as referenced above
        mime.add_header('Content-ID', '<image2>')
        msg.attach(mime)
    with open(image_path2, 'rb') as img:
        mime = MIMEImage(img.read())
        # Define the image's ID as referenced above
        mime.add_header('Content-ID', '<image1>')
        msg.attach(mime)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f"Email sent to {recipient_name} at {recipient_email}")

# Terminate the SMTP session
server.quit()
