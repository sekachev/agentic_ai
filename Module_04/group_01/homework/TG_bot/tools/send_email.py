import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(user_name: str, contact_info: str, message_content: str) -> str:
    """
    Sends an escalation email to the manager with user details and request content.
    """
    sender_email = os.getenv("GMAIL_USER")
    sender_password = os.getenv("GMAIL_APP_PASSWORD")
    receiver_email = os.getenv("MANAGER_EMAIL")

    if not all([sender_email, sender_password, receiver_email]):
        return "Email configuration missing in .env file."

    subject = f"TETkool Lead: {user_name}"
    body = f"""
    New lead from TETkool TG Bot:
    
    User Name: {user_name}
    Contact Info: {contact_info}
    
    Request Content:
    {message_content}
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return "Your request has been sent to our manager. We will contact you soon!"
    except Exception as e:
        print(f"Error sending email: {e}")
        return "Sorry, there was an error sending your request to the manager. Please try again later or contact us directly."

if __name__ == "__main__":
    # Test (will fail without real credentials)
    # print(send_email("Test User", "test@example.com", "I am interested in the IT course."))
    pass
