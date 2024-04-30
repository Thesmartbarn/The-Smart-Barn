import sys, os, json
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from csvWriter import CSVWriter
from jsonDataFormater import JsonDataFormater
from main import randomAlgorithm
from time import perf_counter
from dataCalculator import checkIfTempIsGood
from date_timeHandler import datetimeFormat

dataTimeList = [["1000", "08"], 
                ["1000", "09"],
                ["1000", "10"],
                ["1000", "11"],
                ["1000", "12"],
                ["1001", "01"],
                ["1001", "02"],
                ["1001", "03"],
                ["1001", "04"],
                ["1001", "05"],
                ["1001", "06"],
                ["1001", "07"],
                ["1001", "08"]
                ]

def getPath(date):
    return f"software/csvData/smartbarn_data_{date[0]}_{date[1]}.csv"

jsonPath = "software/python/testing/jsontesting.json"

starttime = perf_counter()
jsonMock = JsonDataFormater(jsonPath)
# temp = 0
# hum = 0
# for date in dataTimeList:
#     CSVWriter.createNewCSVfile(getPath(date), *date)
#     for i in range(60 * 24 * 30):
#         temp = randomAlgorithm(temp)
#         hum = randomAlgorithm(hum)
        
#         fan = True if checkIfTempIsGood(temp, hum) else False
        
#         CSVWriter.writeData(getPath(date), [datetimeFormat(), temp, hum, fan])

jsonMock.overWriteJsonFileWithNewDataMock()

with open(jsonPath) as fp:
    data = json.load(fp)
print(len(data["min"]))
print(len(data["hour"]))
print(len(data["day"]))

print(f"complete in {perf_counter() - starttime}")