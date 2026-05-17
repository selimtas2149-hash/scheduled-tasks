import smtplib
import datetime as dt
import time
import random
import pandas



names=pandas.read_csv("/Users/selimtas/Downloads/birthday-wisher-extrahard-start/birthdays.csv")
names=names.to_dict(orient="records")
print(names)
def writem(name):
    txts=["/Users/selimtas/Downloads/birthday-wisher-extrahard-start/letter_templates/letter_3.txt","/Users/selimtas/Downloads/birthday-wisher-extrahard-start/letter_templates/letter_2.txt","/Users/selimtas/Downloads/birthday-wisher-extrahard-start/letter_templates/letter_1.txt"]
    with open(random.choice(txts),"r") as selim:
        return selim.read().replace("[NAME]",name)


a=0
while True:
    
    now=dt.datetime.now()
    day=now.day
    
    month=now.month
    
    for i in names:
        if month==i["month"] and day==i["day"]:
            
                
                myemailaccount="selimtas.2149@gmail.com"
                sentemail=i["email"]
                txt=writem(i["name"])
                password="rnovbfjcqxjbdihx"
                with smtplib.SMTP("smtp.gmail.com") as email:
                    email.starttls()
                    email.login(user=myemailaccount,password=password)

                    email.sendmail(from_addr=myemailaccount,
                                    to_addrs=sentemail,
                                    msg=f"Subject:Test\nContent-Type: text/plain; charset=utf-8\n\n{txt}".encode("utf-8"))
                    
    time.sleep(60*60*24)
            
    """if a%2==0:
        time.sleep(60*60*1)
        
    else:
        time.sleep(60*60*23)
    with open("/Users/selimtas/Downloads/Birthday Wisher (Day 32) start/quotes.txt","r") as selim:
        lines=[i.strip() for i in selim.readlines()]
"""
   

    







