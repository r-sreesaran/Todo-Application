from db_functions import get_incomplete
htmlformat="<body><tr><th>priority</th><th>task</th></tr>"
    

def getData():
    global htmlformat
    incompleteItems = get_incomplete()
    for task in incompleteItems:
        htmlformat = htmlformat + "<tr>"+ str(task[0])+"</tr>"+"<tr>"+task[1]+"</tr>"
    htmlformat = htmlformat +"</body>"    
    print(htmlformat)
getData()