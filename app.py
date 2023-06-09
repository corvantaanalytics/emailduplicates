import re
import os
import mailbox
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def extract_emails_from_mbox(mbox_file):
    emails = []
    mbox = mailbox.mbox(mbox_file)

    for message in mbox:
        email_body = message.get_payload()
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', email_body)
        emails.extend(email_addresses)

    unique_emails = list(set(emails))
    return unique_emails

@app.route('/api/emails')
def get_emails():
    print(os.path.join(os.path.dirname(__file__)))
    mbox_file_path = 'unix_email.mbox'
#     mbox_file_path = os.path.join(os.path.dirname(__file__), 'unix_email.mbox')
#     print(mbox_file_path)
    unique_emails = extract_emails_from_mbox(mbox_file_path)
    print(unique_emails)  # Print the emails to the console
    return jsonify(emails=unique_emails)

if __name__ == '__main__':
#     mbox_file_path = os.path.join(os.path.dirname(__file__), 'unix_email.mbox')
    mbox_file_path = 'unix_email.mbox'
    unique_emails = extract_emails_from_mbox(mbox_file_path)
    print(unique_emails)  # Print the emails to the console
    app.run(debug=True)
