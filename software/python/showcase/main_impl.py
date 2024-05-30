import sys, os
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from fileExistenceChecker import checkIfFileExists
# import fanSwitch
import os
from time import time, sleep
from date_timeHandler import csvTimeFormat
import dataCalculator
from jsonDataFormater import JsonDataFormater
from csvHandler import CSVhandler
import random
temp = 0
hum = 0


def randomAlgorithm(previousNumber):
    for i in range(random.randint(1, 20)):
        choice = random.randint(-10, 10)
        if i == random.randint(1, 20):
            break
    newNumber = previousNumber + choice
    if not newNumber in range(0, 101):
        newNumber = previousNumber
    return newNumber

def getFanSpeed(temperature, humidity):
    fan = dataCalculator.getFanSpeed(temp, hum)
    
    return fan


while True:
    currentTime = time()
    if currentTime - previousTime >= INTERVAL:

        temp = randomAlgorithm(temp)
        hum = randomAlgorithm(hum)

        fan = dataCalculator.getFanSpeed(temp, hum)
        # fanSwitch.setFanStatus(fan)

        csvHandler.writeData([csvTimeFormat(), temp, hum, fan])
        jsonDataFormater.overWriteJsonFileWithNewData(fan)

        os.system(r"git add software/graphData.json")
        os.system(
            f'git commit -m "automatic data push {csvTimeFormat()} [skip netlify]"')
        os.system('git push')

        previousTime = currentTime

    sleep(0.5)
