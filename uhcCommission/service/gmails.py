from email.header import decode_header
from colorama import Fore,init
from bs4 import BeautifulSoup
import imaplib,email

class OTP:
    def __init__(self, usrgmail, apppassword):
        self.email_user = usrgmail
        self.app_password = apppassword
        init()

    def GetOtp(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self.email_user, self.app_password)
        mail.select('inbox')
        status, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()
        latest_email_id = email_ids[-1]
        status, data = mail.fetch(latest_email_id, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = decode_header(msg['subject'])[0][0]
                email_from = decode_header(msg['from'])[0][0]
                if isinstance(email_subject, bytes):
                    email_subject = email_subject.decode()
                if isinstance(email_from, bytes):
                    email_from = email_from.decode()
                if email_from == "One Healthcare ID-NoReply <noreply@onehealthcareid.com>":
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get('Content-Disposition'))
                            if 'attachment' not in content_disposition:
                                if content_type == 'text/html':
                                    body = part.get_payload(decode=True).decode()
                                    soup = BeautifulSoup(body, 'lxml')
                                    span_value = soup.find('span', class_='textRegularBold')
                                    if span_value:
                                        print(Fore.YELLOW + 'One-Time Access Code:', span_value.text.strip())
                    else:
                        if msg.get_content_type() == 'text/html':
                            body = msg.get_payload(decode=True).decode()
                            soup = BeautifulSoup(body, 'lxml')
                            span_value = soup.find('span', class_='textRegularBold')
                            if span_value:
                                return span_value.text.strip()
                else:
                    print(Fore.RED + "not retreive otp!")
        mail.close()
        mail.logout()
# otp = OTP(usrgmail="mprisco@betafits.com",apppassword="ttop zgif erqd ggqa")
# print(otp.GetOtp())