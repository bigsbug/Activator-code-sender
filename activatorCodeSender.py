import smtplib,ssl,random
from email.mime.text import MIMEText as Text
from email.mime.multipart import MIMEMultipart

password = 'password Email'
addrese = 'address Email'
target = 'address target'

number = ''.join(str(random.randint(0,9))for i in range(5))

data = MIMEMultipart('data')
data['Subject'] = ' Activate Code'
data['From'] = addrese
data['To'] = target

text_data = f'''Activate code is : {number}'''

html_data = f"""<html> <body>
<h2> Activate code is  <h1>{number}</h1> </h2>
</body> </html>"""

part1 = Text(html_data,'html')
part2 = Text(text_data,'plain')
data.attach(part1)
data.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", context=context) as server:
    server.login(addrese, password)
    server.sendmail(addrese,target,data.as_string())