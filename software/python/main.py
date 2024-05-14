import random
temp = 0
hum = 0
def randomAlgorithm(previousNumber):
    for i in range(random.randint(1,20)):
        choice = random.randint(-10, 10)
        if i == random.randint(1, 20):
            break
    newNumber = previousNumber + choice
    if not newNumber in range(0, 101):
        newNumber = previousNumber
    return newNumber  

from fileExistenceChecker import checkIfFileExists

GRAPH_DATA_SAVE_FILEPATH = "software/graphData.json"
if not checkIfFileExists(GRAPH_DATA_SAVE_FILEPATH):
    open(GRAPH_DATA_SAVE_FILEPATH, "w").close()

from csvHandler import CSVhandler

csvHandler = CSVhandler()

from jsonDataFormater import JsonDataFormater

jsonDataFormater = JsonDataFormater(GRAPH_DATA_SAVE_FILEPATH)

import dataCalculator
from date_timeHandler import datetimeFormat

from time import time, sleep
import os

currentTime = time()
previousTime = 0
INTERVAL = 60

while True:
    currentTime = time()
    if currentTime - previousTime >= INTERVAL:
        
        temp = randomAlgorithm(temp)
        hum = randomAlgorithm(hum)
        
        fan = True if dataCalculator.checkIfTempIsGood(temp, hum) else False
        
        csvHandler.writeData([datetimeFormat(), temp, hum, fan])
        jsonDataFormater.overWriteJsonFileWithNewData()
        
        os.system(r"git add software/graphData.json")
        os.system(f'git commit -m "automatic data push {datetimeFormat()} [skip netlify]"')
        os.system('git push')
        
        previousTime = currentTime
    
    
    sleep(0.5)
    