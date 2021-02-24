import datetime

def namingFile():
    ct = datetime.datetime.now() 
    name = str(ct)
    name = name[0:19].replace(" ", "-")
    name = name.replace("-","_")
    return name