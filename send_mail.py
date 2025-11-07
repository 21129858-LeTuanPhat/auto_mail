import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email():
    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver_email = os.getenv("EMAIL_TO")

    subject = "Thư tự động từ GitHub Actions"
    body = "Xin chào!\nĐây là email được gửi tự động bằng Python qua GitHub Actions 🚀"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Gửi qua SMTP Gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

    print("✅ Gửi mail thành công!")

if __name__ == "__main__":
    send_email()
