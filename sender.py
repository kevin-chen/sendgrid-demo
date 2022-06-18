# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os
import base64
import csv

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Mail, Attachment, FileContent, FileName, FileType, Disposition

load_dotenv()

TEMPLATE_ID = 'd-57dfbfc5e6b7413db633c56cce560a4b'

# Original HTML Message
# message = Mail(
#     from_email='kevin@theheadstarter.com',
#     to_emails='kevinchen3856@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')


def addEmailAttachment(fileName):
    with open(fileName, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(fileName),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    return attachedFile


def sendEmailTo(emailAddress, firstName, lastName):
    TO_EMAIL = To(emailAddress, "{} {}".format(firstName, lastName))
    message = Mail(
        from_email=From("kevin@theheadstarter.com", "Kevin Chen"),
        to_emails=TO_EMAIL)
    message.dynamic_template_data = {
        'first_name': firstName,
        'last_name': lastName
    }
    message.template_id = TEMPLATE_ID

    # for fileName in ["Headstarter-New-Events.pdf"]:
    #     attachment = addEmailAttachment(fileName)
    #     message.add_attachment(attachment)

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

# sendEmailTo("kevinchen3856@gmail.com", "Bob", "Something")
# sendEmailTo("kc3585@nyu.edu", "Kevin", "Chen")

def readFromCsvAndSendEmail(csvFileName):
    with open(csvFileName) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            email, firstName, lastName = row
            print(email, firstName, lastName)
            sendEmailTo(email, firstName, lastName)

readFromCsvAndSendEmail("SampleStudentInfo.csv  - Sheet1.csv")

