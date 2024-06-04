import gFrame
import sys
import os
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
import dataCalculator
import fanControl
import pygame

temp = hum = fanSpeed = 0

app = gFrame.AppConstructor("100dw", "100dh", pygame.FULLSCREEN)

getFanSpeedBasedOnRealData = False

tempSlider = gFrame.Slider((gFrame.ScreenUnit.vw(70), gFrame.ScreenUnit.vh(7)), 0, 50, gFrame.Color.RED, gFrame.Color.GRAY, 20)
humSlider = gFrame.Slider((gFrame.ScreenUnit.vw(70), gFrame.ScreenUnit.vh(7)), 0, 100, gFrame.Color.BLUE, gFrame.Color.GRAY, 20)

hideSliderCover = gFrame.Button(("100vw", "30vh"), gFrame.Color.RED)
hideSliderCover.text("Actuele data wordt gemeten", gFrame.Font.FONT50, gFrame.Color.WHITE, bold=True)

switchToManualDataButton = gFrame.Button(("50vw", "7vh"), gFrame.Color.LIGHT_GREEN)
switchToManualDataButton.text("Data manipuleren", gFrame.Font.XLARGE, gFrame.Color.BLACK)

switchToRealDataButton = gFrame.Button(("50vw", "7vh"), gFrame.Color.LIGHT_GRAY)
switchToRealDataButton.text("Actuele data meten", gFrame.Font.XLARGE, gFrame.Color.BLACK)

temperatureInfo = gFrame.Text("huidige temperatuur: Null°C", gFrame.Font.XXLARGE, gFrame.Color.RED)
humidityInfo = gFrame.Text("huidige luchtvochtigheid: Null%", gFrame.Font.XXLARGE, gFrame.Color.BLUE)
fanInfo = gFrame.Text("huidige ventilator snelheid: Null%", gFrame.Font.XXLARGE, gFrame.Color.GREEN)

# grafiek
GRAPH_PATH = "Foto/software/grafiek.png"

graph = gFrame.Image(GRAPH_PATH)
graph.resize(gFrame.ScreenUnit.vw(40), gFrame.ScreenUnit.vh(40))
graphInnerRect = gFrame.Rect("55vw", "54vh", "34vw", "30vh")
graphInnerRect = gFrame.Rect(gFrame.ScreenUnit.vw(54.7), gFrame.ScreenUnit.vh(53.5), gFrame.ScreenUnit.vw(33.6), gFrame.ScreenUnit.vh(29.4))

def placePointOnGraph(temp, hum):
    humPos = graphInnerRect.pw(hum)
    
    if temp >= 20 and temp <= 50:
        tempPos = graphInnerRect.ph(abs((100 / 30 * (temp - 20))- 100))
        color = gFrame.Color.BLACK
    else:
        color = gFrame.Color.RED
        if temp < 20:
            tempPos = graphInnerRect.ph(100)
        else:
            tempPos = graphInnerRect.ph(0)
        
    gFrame.Draw.circle((humPos, tempPos), 5, color)

def switchMode(status):
    global getFanSpeedBasedOnRealData
    if status:
        switchToRealDataButton.updateColor(gFrame.Color.LIGHT_GRAY)
        switchToManualDataButton.updateColor(gFrame.Color.LIGHT_GREEN)
        getFanSpeedBasedOnRealData = False
        tempSlider.enable()
        humSlider.enable()
    else:
        switchToManualDataButton.updateColor(gFrame.Color.LIGHT_GRAY)
        switchToRealDataButton.updateColor(gFrame.Color.LIGHT_GREEN)
        getFanSpeedBasedOnRealData = True
        tempSlider.disable()
        humSlider.disable()
    

while True:
    app.eventHandler(60)
    app.fill(gFrame.Color.DARKMODE)

    if app.everySecond():
        if getFanSpeedBasedOnRealData:
            newTemp = fanControl.readTempSensor() 
            newHum = fanControl.readHumSensor()
            temp = newTemp if newTemp != None else temp
            hum = newHum if newHum != None else hum
        else:
            temp = tempSlider.getValue()
            hum = humSlider.getValue()
        temp, hum = int(temp), int(hum)   
        temperatureInfo.setText("huidige temperatuur: %s°C" %temp)
        humidityInfo.setText(f"huidige luchtvochtigheid: {hum}%")

        fanSpeed = dataCalculator.getFanSpeed(temp, hum)
        fanInfo.setText(f"huidige ventilator snelheid: {round(fanSpeed)}%")

        fanControl.setFanSpeed(fanSpeed)
    
    if gFrame.Interactions.isKeyReleased(pygame.K_ESCAPE):
        fanControl.setFanSpeed(0)
        exit()

    if gFrame.Interactions.isKeyClicked(pygame.K_SPACE):
        switchMode(getFanSpeedBasedOnRealData)

        
    if switchToManualDataButton.isClicked():
        switchMode(True)
        
    if switchToRealDataButton.isClicked():
        switchMode(False)
        
        
    tempSlider.place("15vw", "5vh")
    humSlider.place("15vw", "20vh")
    
    if getFanSpeedBasedOnRealData:
        hideSliderCover.place(0, 0, 120)
        
    switchToManualDataButton.place(0, "30vh")
    switchToRealDataButton.place("50vw", "30vh")
    
    temperatureInfo.place("5vw", "40vh")
    humidityInfo.place("5vw", "50vh")
    fanInfo.place("5vw", "60vh")
    
    graph.place(gFrame.ScreenUnit.vw(50), gFrame.ScreenUnit.vh(50))
    gFrame.Draw.borderFromRect(graphInnerRect, 1, gFrame.Color.BLACK)
    placePointOnGraph(temp, hum)
    
    gFrame.Draw.rectangle(0, gFrame.ScreenUnit.vh(100) - 10, gFrame.vars.appWidth / 60 * (app.getFrameCounter % 60), 10, gFrame.Color.LIGHT_GREEN)
