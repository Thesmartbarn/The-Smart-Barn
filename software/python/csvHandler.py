from csvWriter import CSVWriter
from csvTimeKeeper import csvTimeKeeper


class CSVhandler(csvTimeKeeper, CSVWriter):
    def __init__(self) -> None:
        super().__init__()
        
    def writeData(self, data: str):
        if super().checkIfFileIsOutdated():
            CSVWriter.createNewCSVfile(super().getCsvPath(), self.year, self.month)
        CSVWriter.writeData(super().getCsvPath(), data)