
def checkIfTempIsGood(temperature: float, humidity: float) -> bool:
    humidity /= 100
    maxTemp = 10 * (humidity **2) - 19 * humidity + 31.5
    # print(temperature, maxTemp)
    return temperature < maxTemp
# # A = 10 | B = -19 | C = 31.5

