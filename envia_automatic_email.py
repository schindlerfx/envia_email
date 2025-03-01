import os
import smtplib
from email.message import EmailMessage

email = "seuemail@gmail.com"

with open('senha.txt') as f:
   senha = f.readlines()
   f.close()
senha_do_email = senha[0]

msg = EmailMessage()
msg['Subject'] = 'Enviando e-mail com Python'
msg['From'] = 'seuemail@gmail.com'
msg['To'] = 'qualquercoisa@gmail.com'
msg.set_content("Segue o relatório diário")

with open('relatorio_diario.pdf', 'rb') as content_file:
   content = content_file.read()
   msg.add_attachment(content, maintype='application', subtype='pdf', filename='relatorio_diario.pdf')

with open('dolar.png', 'rb') as content_file:
   content = content_file.read()
   msg.add_attachment(content, maintype='application', subtype='png', filename='dolar.png')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
   smtp.login(email, senha_do_email)
   smtp.send_message(msg)