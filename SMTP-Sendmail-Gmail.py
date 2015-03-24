import smtplib
import time
from email.mime.text import MIMEText

to_gmail = ('',)  # Gmail account which needs a constant flow of email.
from_email = ''  # Outgoing mail account that will be sending to the Gmail account.

mailz = smtplib.SMTP('')  # SMTP IP/dns
mailz.login('', '')  # SMTP login, and SMTP password

for to in to_gmail:
    msg = MIMEText('Nagios -- OK')
    msg['Subject'] = 'Server status '+time.ctime()
    msg['From'] = from_email
    msg['To'] = to
    print msg.as_string()
    mailz.sendmail(from_email, [to], msg.as_string())