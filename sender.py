# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from distutils.command.install_egg_info import to_filename
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import From, To, Mail

load_dotenv()

TEMPLATE_ID = 'd-57dfbfc5e6b7413db633c56cce560a4b'

# Original HTML Message
# message = Mail(
#     from_email='kevin@theheadstarter.com',
#     to_emails='kevinchen3856@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')


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
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

# sendEmailTo("kevinchen3856@gmail.com", "Kevin", "Chen")
