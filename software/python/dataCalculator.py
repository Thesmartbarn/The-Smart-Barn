
def checkIfTempIsGood(temperature: float, humidity: float) -> tuple[bool, float]:
    humidity /= 100
    maxTemp = 10 * (humidity **2) - 19 * humidity + 31.5
    return temperature < maxTemp, maxTemp
# # A = 10 | B = -19 | C = 31.5

def calculateScore(): 
    pass

def calculateFanSpeed(temperature, humidity):
    temperatureStatus, maxTemp = checkIfTempIsGood(temperature, humidity)
    if temperatureStatus:
        if temperature / maxTemp > 0.80:
            return min(255, 255 * ((temperature / maxTemp) - 0.8) * 5)
        return 0
    else:
        return 255

def invertFanSpeed(temperature, humidity):
    return abs(calculateFanSpeed(temperature, humidity) - 255)
    
def getFanSpeed(temperature, humidity):
    return invertFanSpeed(temperature, humidity)
    
    
if __name__ == "__main__":
    import gFrame
    
    app = gFrame.AppConstructor(300, 300)
    tempSlider = gFrame.Slider((250, 10), 0, 50, gFrame.Color.RED, gFrame.Color.RED)
    tempSlider.setKnob(8, gFrame.Color.BLACK)
    humSlider = gFrame.Slider((250, 10), 0, 100, gFrame.Color.BLUE, gFrame.Color.BLUE)
    humSlider.setKnob(8, gFrame.Color.BLACK)
    
    
    while True:
        app.eventHandler()
        app.fill(gFrame.Color.WHITE)
        
        tempSlider.place(25, 20)
        humSlider.place(25, 100)
        
        print(f"temp: {tempSlider.getValue()} | hum: {humSlider.getValue()} | fan: {getFanSpeed(tempSlider.getValue(), humSlider.getValue())}")
        
        
    
