import imapclient
from typing import Optional

# set up an App password
# if 2fa is enabled
# https://is.gd/zz2IfV
username: Optional[str] = None
password: Optional[str] = None


async def inbox_count():

    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(username, password)
    inbox = imap_obj.select_folder('INBOX', readonly=True)

    # Getting Amex statement emails
    # everything_folder = imap_obj.select_folder('[Gmail]/All Mail',readonly=True)
    # messages = imap_obj.search(['SUBJECT','Your latest statement is ready'])

    # for msgid, data in imap_obj.fetch(messages, ['ENVELOPE']).items():
        # envelope = data[b'ENVELOPE']
        # print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))


    try:
        return inbox[b'EXISTS']
    except KeyError:
        return ''
