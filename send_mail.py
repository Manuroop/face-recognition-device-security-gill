from datetime import datetime
import yagmail

def send_mail():
    
    temp = ''
    with open('info.txt','r') as f:
        temp = f.read()

    reciever,sender_e, sender_pass = temp.split('+')

    msg = 'Movement detected in the system on '+str(datetime.now())
    reciever = str(reciever)

    yag = yagmail.SMTP(sender_e, sender_pass)

    yag.send(
        to=reciever,
        subject="Motion notification",
        contents=msg
    )
