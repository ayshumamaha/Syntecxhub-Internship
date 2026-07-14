import smtplib
import ssl
import csv
import os
import time
import logging

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ==========================================
# AUTOMATED EMAIL SENDER BOT
# ==========================================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

CSV_FILE = "recipients.csv"

ATTACHMENT = "sample_attachment.pdf"

LOG_FILE = "email_log.txt"

MAX_RETRY = 3

# ==========================================
# LOGGER CONFIGURATION
# ==========================================

logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)

# ==========================================
# READ SENDER DETAILS
# ==========================================

def get_sender_credentials():

    print("\n========== SENDER LOGIN ==========\n")

    sender_email = input("Enter Gmail Address : ").strip()

    app_password = input("Enter Gmail App Password : ").strip()

    return sender_email, app_password


# ==========================================
# LOAD RECIPIENTS
# ==========================================

def load_recipients():

    recipients = []

    try:

        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                recipients.append({

                    "name": row["Name"],

                    "email": row["Email"]

                })

    except FileNotFoundError:

        print("Recipient CSV File Not Found.")

    except Exception as error:

        print("Error :", error)

    return recipients


# ==========================================
# CREATE EMAIL MESSAGE
# ==========================================

def create_email(sender, recipient):

    message = MIMEMultipart()

    message["From"] = sender

    message["To"] = recipient["email"]

    message["Subject"] = "Automated Email From Python"

    body = f"""

Hello {recipient['name']},

This email was sent automatically using the
Automated Email Sender Bot developed in Python.

Please find the attached document.

Regards,
Python Automation System

"""

    message.attach(MIMEText(body, "plain"))

    return message


# ==========================================
# ADD ATTACHMENT
# ==========================================

def add_attachment(message):

    if not os.path.exists(ATTACHMENT):

        print("Attachment Not Found.")

        return

    with open(ATTACHMENT, "rb") as file:

        attachment = MIMEBase("application", "octet-stream")

        attachment.set_payload(file.read())

    encoders.encode_base64(attachment)

    attachment.add_header(

        "Content-Disposition",

        f"attachment; filename={os.path.basename(ATTACHMENT)}"

    )

    message.attach(attachment)
# ==========================================
# SEND EMAIL
# ==========================================

def send_email(sender, password, recipient, message):

    context = ssl.create_default_context()

    for attempt in range(1, MAX_RETRY + 1):

        try:

            with smtplib.SMTP_SSL(

                SMTP_SERVER,

                SMTP_PORT,

                context=context

            ) as server:

                server.login(sender, password)

                server.sendmail(

                    sender,

                    recipient["email"],

                    message.as_string()

                )

            logging.info(

                f"SUCCESS : {recipient['email']}"

            )

            print(

                f"Email sent to {recipient['name']}"

            )

            return True

        except Exception as error:

            logging.warning(

                f"Attempt {attempt} Failed : "

                f"{recipient['email']}"

            )

            print(

                f"Retry {attempt}/{MAX_RETRY}"

            )

            time.sleep(2)

    logging.error(

        f"FAILED : {recipient['email']}"

    )

    print(

        f"Failed to send email to "

        f"{recipient['name']}"

    )

    return False


# ==========================================
# SEND EMAILS TO ALL RECIPIENTS
# ==========================================

def send_bulk_emails():

    sender, password = get_sender_credentials()

    recipients = load_recipients()

    if len(recipients) == 0:

        print("No Recipients Found.")

        return

    success = 0

    failed = 0

    print("\nStarting Email Delivery...\n")

    for recipient in recipients:

        print("-" * 40)

        print(

            f"Sending to : "

            f"{recipient['name']}"

        )

        message = create_email(

            sender,

            recipient

        )

        add_attachment(message)

        status = send_email(

            sender,

            password,

            recipient,

            message

        )

        if status:

            success += 1

        else:

            failed += 1

    print("\n" + "=" * 45)

    print("EMAIL DELIVERY COMPLETED")

    print("=" * 45)

    print(f"Successful : {success}")

    print(f"Failed     : {failed}")

    print(f"Total      : {len(recipients)}")

    print("=" * 45)


# ==========================================
# VIEW EMAIL LOG
# ==========================================

def view_log():

    if not os.path.exists(LOG_FILE):

        print("Log File Not Found.")

        return

    print("\n========== EMAIL LOG ==========\n")

    with open(

        LOG_FILE,

        "r",

        encoding="utf-8"

    ) as file:

        print(file.read())
# ==========================================
# CLEAR EMAIL LOG
# ==========================================

def clear_log():

    choice = input(

        "\nClear Log File? (Y/N): "

    ).upper()

    if choice == "Y":

        with open(

            LOG_FILE,

            "w",

            encoding="utf-8"

        ) as file:

            file.write("")

        print("Log File Cleared.")

    else:

        print("Operation Cancelled.")


# ==========================================
# ABOUT APPLICATION
# ==========================================

def about():

    print("\n" + "=" * 45)

    print("      AUTOMATED EMAIL SENDER BOT")

    print("=" * 45)

    print("Version      : 1.0")

    print("Language     : Python")

    print("SMTP Server  : Gmail SMTP")

    print("CSV Support  : Yes")

    print("Attachment   : Yes")

    print("Retry Logic  : Yes")

    print("Logging      : Yes")

    print("=" * 45)


# ==========================================
# MAIN MENU
# ==========================================

def menu():

    while True:

        print("\n")

        print("=" * 45)

        print("   AUTOMATED EMAIL SENDER BOT")

        print("=" * 45)

        print("1. Send Bulk Emails")

        print("2. View Email Log")

        print("3. Clear Email Log")

        print("4. About")

        print("5. Exit")

        print("=" * 45)

        choice = input(

            "Enter Choice : "

        )

        if choice == "1":

            send_bulk_emails()

        elif choice == "2":

            view_log()

        elif choice == "3":

            clear_log()

        elif choice == "4":

            about()

        elif choice == "5":

            print(

                "\nThank you for using "

                "Email Sender Bot."

            )

            break

        else:

            print("Invalid Choice.")


# ==========================================
# PROGRAM ENTRY
# ==========================================

if __name__ == "__main__":

    try:

        print("\n")

        print("=" * 45)

        print("WELCOME TO")

        print("AUTOMATED EMAIL SENDER BOT")

        print("=" * 45)

        menu()

    except KeyboardInterrupt:

        print("\nProgram Interrupted.")

    # ==========================================
# PROGRAM ENTRY
# ==========================================

if __name__ == "__main__":

    try:

        print("\n")

        print("=" * 45)

        print("WELCOME TO")

        print("AUTOMATED EMAIL SENDER BOT")

        print("=" * 45)

        menu()

    except KeyboardInterrupt:

        print("\nProgram Interrupted.")

    except Exception as error:

        print(f"\nUnexpected Error: {error}")

        logging.error(f"Application Error: {error}")
