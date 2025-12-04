import os
from dotenv import load_dotenv
from src.transformer_agent import run_transformation_agent
from src.html_generator import generate_html_email
from src.mailer import send_email

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receivers = os.getenv("EMAIL_RECEIVER").split(",")

    with open("examples/input_digest_example.md") as f:
        text = f.read()

    data = run_transformation_agent(api_key, text)
    html = generate_html_email(data)
    send_email(sender, password, receivers, html)

if __name__ == "__main__":
    main()