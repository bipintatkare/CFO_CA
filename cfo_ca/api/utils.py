import threading
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content,sender, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
        msg.content_subtype = 'html'
        msg.send()


def send_html_mail(subject, html_content,sender, recipient_list ):
    EmailThread(subject, html_content,sender, recipient_list).start()

class Email_text_Thread(threading.Thread):
    def __init__(self, subject, message, sender,recipient,cc_list):
        self.subject = subject
        self.recipient = recipient
        self.message = message
        self.sender = sender
        self.cc_list = cc_list
        threading.Thread.__init__(self)

    def run(self):
        try:

            msg =EmailMultiAlternatives(self.subject, self.message, self.sender, self.recipient,cc=self.cc_list)
            msg.send()
            print('email sent')
        except Exception as e:
            print('exception occured email not sent'+str(e))
            pass


def send_text_mail(subject, message, sender, recipient,cc_list):
    Email_text_Thread(subject, message, sender, recipient,cc_list).start()
