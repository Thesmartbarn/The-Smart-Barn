from datetime import date, datetime

def dateTrackerFormat():
    return year(), month()

def datetimeFormat():
    return datetime.now()

def datenow():
    return str(date.today())

def minute():
    return datetime.now().minute

def hour():
    return datetime.now().hour

def day():
    return date.today().day

def month():
    return date.today().month

def year():
    return date.today().year



