import os

def checkIfCsvFileExists(year: int, month: int):
    return os.path.isfile(f"software/csvData/smartbarn_data_{year}_{'0' + str(month) if month < 10 else month}.csv")
        
def checkIfJsonDateTrackerFileExists():
    return os.path.isfile("software/datetracker.json")

def checkIfFileExists(path: str):
    return os.path.isfile(path)