#=========================================================================
#
#   How to send Email with Python by:  Babimetro
#
#==============================================================================
import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import base64

url = 'Sender@domain.com'
conn = smtplib.SMTP(url,587)
conn.starttls()
user,password = ('username','password')
conn.login(user,password)


fromaddr='Sender@domain.com'
toaddrs=['receiver1.@domain.com','receiver2.@domain.com',...]


filename = "azad_finial_page.zip"
filepath=r"D:\Data\Projects\Uni\azad_finial_page.zip"
msg = MIMEMultipart()

with open( filepath, 'rb') as fin:
    data = fin.read()

    part = MIMEBase( 'application', 'octet-stream' )
    part.set_payload( data )
    encode_base64( part )

    part.add_header( 'Content-Disposition', 'attachment; filename="%s"' % filename )
    msg.attach(MIMEText( """\
Your Text or HTML goes here!

""", 'html'))
    msg.attach( part )
    msg['subject'] = 'TDD Daily KML'
    msg['from']='babi'
    msg['to']='my_Users'
    message=str(msg)


conn.sendmail(fromaddr,toaddrs,message)

