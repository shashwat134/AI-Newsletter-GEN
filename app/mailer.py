import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, receivers, html_content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "AI Newsletter"
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receivers, msg.as_string())