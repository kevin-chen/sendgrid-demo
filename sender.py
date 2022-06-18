# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from distutils.command.install_egg_info import to_filename
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

TEMPLATE_ID = 'd-57dfbfc5e6b7413db633c56cce560a4b'

# Original HTML Message
# message = Mail(
#     from_email='kevin@theheadstarter.com',
#     to_emails='kevinchen3856@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')

TO_EMAIL="kevinchen3856@gmail.com"
message = Mail(
    from_email="kevin@theheadstarter.com",
    to_emails=TO_EMAIL)
message.dynamic_template_data = {
    'first': 'SendGrid Development',
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
