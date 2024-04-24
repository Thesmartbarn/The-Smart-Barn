import fileExistenceChecker, json, date_timeHandler

class csvTimeKeeper:
    month: int = 0
    year: int = 0
    
    def __init__(self) -> None:
        self.year, self.month = date_timeHandler.dateTrackerFormat()
        self.fixTrackerFile()
    
    def checkIfFileIsOutdated(self):
        if fileExistenceChecker.checkIfJsonDateTrackerFileExists():
            with open("software/datetracker.json") as fp:
                dateTracker = json.load(fp)
            self.year: int = dateTracker["year"]
            self.month: int = dateTracker["month"]
            
            if (self.year, self.month) != (newDate := date_timeHandler.dateTrackerFormat()):
                self.year, self.month = newDate
                return True
            if not fileExistenceChecker.checkIfCsvFileExists(self.year, self.month):
                return True
            return False
        self.fixTrackerFile()
        
    def fixTrackerFile(self):
        dump =  {
                "year": date_timeHandler.dateTrackerFormat()[0],
                "month": date_timeHandler.dateTrackerFormat()[1]
                }
        with open("software/datetracker.json", "w") as fp:
            json.dump(dump, fp, indent=4)
    
    def getCsvPath(self):
        return f"software/csvData/smartbarn_data_{self.year}_{self.month}.csv"
        