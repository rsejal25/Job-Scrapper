import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def sendEmail(toaddr):
 formaddr='nuakrijob@gmail.com'
 msg=MIMEMultipart()
 msg['From']=formaddr
 msg['To']=toaddr
 msg['Subject']='Job portal'
 body='Hello '+toaddr;
 msg.attach(MIMEText(body,'plain'))
 filename="Job_List_File.csv"
 attachment=open('Naukri_File.csv','rb')
 p=MIMEBase('application','octet-stream')
 p.set_payload((attachment).read())
 encoders.encode_base64(p)
 p.add_header('Content-Disposition','attachment;filename="Job_List_File.csv"')
 msg.attach(p)
 s=smtplib.SMTP('smtp.gmail.com',587)
 s.starttls()
 s.login(formaddr,'cuxuqwvfhlkytemg')
 text=msg.as_string()
 s.sendmail(formaddr,toaddr,text)
 s.quit()
 print('sending email')

sendEmail('sejalrawat25@gmail.com')