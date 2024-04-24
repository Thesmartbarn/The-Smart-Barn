import csv, fileExistenceChecker, json, date_timeHandler


class CSVWriter:
    def writeData(path: str, data: str):
        with open(path, "a", newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data)

    def createNewCSVfile(path: str, year: int, month: int): # for easy testing
        file = open(path, "w")
        file.close()
        newDateTracker = {"year": year, "month": month}
        with open("software/datetracker.json", "w") as fp:
            json.dump(newDateTracker, fp, indent = 4, separators=(',',': '))
    
