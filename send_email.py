import smtplib
# for simple message transfer protocol
import getpass
# to share to, from, subject, body info
from email.mime.text import MIMEText


def send_mail():
    senders_addr = "emailID"
    # to get password from user
    password = getpass.getpass()
    subject = 'Machine Learning Session'
    msg = '''
    Hello Everyone,
        This is Lissa from Oracle. Here is the announcement of next meetup.
        Timing 11AM on 22nd aug, Friday. 
        
        Thank you,
        Shreya Kajbaje
    '''

    # SERVER INITIALIZATION
    # enable smtp server for connection smtp.gmail.com is the host and its port is by default 587
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # tls is the handshake which allows the connection
    # to login
    server.login(senders_addr, password)

    recipients = ['emailID_1', 'emailID_2']

    # DRAFT MESSAGE BODY
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = senders_addr
    msg['To'] = ", ".join(recipients)

    # msg.set_param('importance', 'high value')

    server.sendmail(senders_addr, recipients, msg.as_string())


send_mail()
