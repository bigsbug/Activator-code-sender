import smtplib,ssl,random
from email.mime.text import MIMEText as Text
from email.mime.multipart import MIMEMultipart

class ActivatorCodeSender:
    def __init__(self,address_email,password):
        self.addrese = address_email
        self.password = password
        self.target = None
        self.activate_code = None

    def generate_acitvateCode(self):
        self.activate_code = ''.join(str(random.randint(0,9))for i in range(5)) 

    def SendCode(self,taget):
        self.target = taget
        data = MIMEMultipart('data')
        data['Subject'] = ' Activate Code'
        data['From'] = self.addrese
        data['To'] = self.target

        text_data = f'''Activate code is : {self.activate_code}''' 

        html_data = f"""<html> <body>
        <h2> Activate code is  <h1>{self.activate_code}</h1> </h2> 
        </body> </html>"""

        part1 = Text(html_data,'html')
        part2 = Text(text_data,'plain')
        data.attach(part1)
        data.attach(part2)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", context=context) as server:
            server.login(self.addrese, self.password)
            server.sendmail(self.addrese,self.target,data.as_string())