from datetime import date, datetime

def dateTrackerFormat():
    return year(), month()

def datetimeFormat():
    return datetime.now()

def datenow():
    return str(date.today())

def minute():
    _min = datetime.now().minute
    return str(_min) if _min > 10 else f"0{_min}"

def hour():
    _hour = datetime.now().hour
    return str(_hour) if _hour > 10 else f"0{_hour}"

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

def csvTimeFormat() -> str:
    return f"{day()}-{month()}-{year()} {hour()}:{minute()}"
    
if __name__ == "__main__":
    print(csvTimeFormat())



