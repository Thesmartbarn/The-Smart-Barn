import json, csv, date_timeHandler
from fileExistenceChecker import checkIfFileExists

class GraphSimulator:  
    def __init__(self) -> None:
        self.currentHour = date_timeHandler.hour()
        self.currentDay = date_timeHandler.day()
        self.currentYear = date_timeHandler.year()
        self.simulatedGraphData = {"min": [], "hour": [], "day": []}
    
    def simulate(self, csvRow):
        self.simulatedGraphData["hour"].append([None, int(csvRow[1]), int(csvRow[2])])
        if self.currentHour != date_timeHandler.hour():
            pass
        
        if self.currentDay != date_timeHandler.day():
            pass
        # if len(self.simulatedGraphData["hour"]) > :
            # pass
        
    def simulateMock(self, csvRow):
        time = f"{date_timeHandler.hour()}:{date_timeHandler.minute()}"
        self.simulatedGraphData["min"].append([time, int(csvRow[1]), int(csvRow[2])])
        if len(self.simulatedGraphData["min"]) > 60:
            time = f"{date_timeHandler.hour()}:00"
            hourData = [time, *GraphSimulator.averageOfDataList(self.simulatedGraphData["min"])]
            self.simulatedGraphData["hour"].append(hourData)
            self.simulatedGraphData["min"] = []
        if len(self.simulatedGraphData["hour"]) > 24:
            dayData = [date_timeHandler.datenow(), *GraphSimulator.averageOfDataList(self.simulatedGraphData["hour"])]
            self.simulatedGraphData["day"].append(dayData)
            self.simulatedGraphData["hour"] = []
        if len(self.simulatedGraphData["day"]) > 365:
            self.simulatedGraphData["day"].pop(0)
            
    @staticmethod
    def averageOfDataList(list):
        temp = []
        hum = []
        for dataPoint in list:
            temp.append(dataPoint[1])
            hum.append(dataPoint[2])
            
        return [round(sum(temp) / len(temp), 2), round(sum(hum) / len(hum), 2)]
            
        
        

class JsonDataFormater(GraphSimulator):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.path: str = path
        self.yearSpanCsvPaths: list = []
    
    def overWriteJsonFileWithNewData(self):
        self.getYearSpanCsvPaths()
        self.simulatedGraphData = {"min": [], "hour": [], "day": []}
        for csvFilePath in self.yearSpanCsvPaths:
            with open(csvFilePath) as csvFile:
                csvData = csv.reader(csvFile)
                for row in csvData:
                    super().simulate(row)
        self._writeDataToJson(self.simulatedGraphData)
        
    def overWriteJsonFileWithNewDataMock(self):
        self.yearSpanCsvPaths = [
            "software/csvData/smartbarn_data_1000_08.csv",
            "software/csvData/smartbarn_data_1000_09.csv",
            "software/csvData/smartbarn_data_1000_10.csv",
            "software/csvData/smartbarn_data_1000_11.csv",
            "software/csvData/smartbarn_data_1000_12.csv",
            "software/csvData/smartbarn_data_1001_01.csv",
            "software/csvData/smartbarn_data_1001_02.csv",
            "software/csvData/smartbarn_data_1001_03.csv",
            "software/csvData/smartbarn_data_1001_04.csv",
            "software/csvData/smartbarn_data_1001_05.csv",
            "software/csvData/smartbarn_data_1001_06.csv",
            "software/csvData/smartbarn_data_1001_07.csv",
            "software/csvData/smartbarn_data_1001_08.csv"
        ]
        for csvFilePath in self.yearSpanCsvPaths:
            with open(csvFilePath) as csvFile:
                csvData = csv.reader(csvFile)
                for row in csvData:
                    super().simulateMock(row)
        self._writeDataToJson(self.simulatedGraphData)
                    
    def _writeDataToJson(self, data: dict):
        with open(self.path, "w") as fp:
            json.dump(data, fp, indent=4)
        
    def getYearSpanCsvPaths(self):
        self.yearSpanCsvPaths = []
        yearNow, monthNow = tuple([int(date) for date in date_timeHandler.dateTrackerFormat()])
        pathCounter = 0
        while True:
            if pathCounter > 100:
                break
            path = f"software/csvData/smartbarn_data_{str(yearNow)}_{'0' + str(monthNow) if monthNow < 10 else str(monthNow)}.csv"
            if checkIfFileExists(path):
                self.yearSpanCsvPaths.append(path)
            
            monthNow -= 1
            if monthNow == 0:
                monthNow = 12
                yearNow -= 1
            pathCounter += 1
            
        self.yearSpanCsvPaths.reverse() # start with oldest data
        
    

    
            

if __name__ == "__main__":
    test = JsonDataFormater("hello")
    test.getYearSpanCsvPaths()
    print(test.overWriteJsonFileWithNewData())
    print(test.yearSpanCsvPaths)
