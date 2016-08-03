import smtplib
from email.mime.text import MIMEText
mailto_list=['*******']       #mail receiver
mail_host="smtp.163.com"      #smtp server
mail_user="******"            #string before @
mail_pass="******"            #passport
mail_postfix="163.com"        #string after @

def send_mail(to_list,sub,content):
    me="hello"+"<"+ mail_user +"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #receivers seperate by ';'
    
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            
        server.login(mail_user,mail_pass)              
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False




