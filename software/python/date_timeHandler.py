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

def getMinuteFromDateTime(dateTime):
    _time = dateTime.split(" ")[1].split(":")
    return f"{_time[0]}:{_time[1]}"

def getHourFromDateTime(dateTime):
    return f"{dateTime.split(" ")[1].split(":")[0]}:00"

def getDayFromDateTime(dateTime):
    return dateTime.split(" ")[0]



