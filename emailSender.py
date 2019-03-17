from db_functions import get_incomplete
htmlformat= "<html><body><tr><th>priority</th><th>task</th></tr>"
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
    

def getData():
    global htmlformat
    incompleteItems = get_incomplete()
    for task in incompleteItems:
        htmlformat = htmlformat + "<tr>"+ str(task[0])+"</tr>"+"<tr>"+task[1]+"</tr>"
    htmlformat = htmlformat +"</body></html>"    
    print(htmlformat)

def testEmailSending():
         getData()
         global htmformat
         sender_email = "sreesaran.developer@gmail.com"
         receiver_email = "r.sreesaran@gmail.com"
         
         message = MIMEMultipart("alternative")
         message["Subject"] = "Pending List"
         message["From"] = sender_email
         message["To"] = receiver_email
         part1 = MIMEText("Please check out the pending list and try to progress on them", "Plain")
         part2 = MIMEText(htmlformat, "html")
         message.attach(part1)
         message.attach(part2)

     
         context = ssl.create_default_context()
         with  smtplib.SMTP_SSL("smtp.gmail.com", "465",context=context) as server:
                server.login("sreesaran.developer@gmail.com", password)
                server.sendmail("sreesaran.developer@gmail.com", "r.sreesaran@gmail.com", message.as_string())
                server.quit()
            

#getData()
testEmailSending()