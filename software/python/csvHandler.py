from csvWriter import CSVWriter
from csvTimeKeeper import csvTimeKeeper


class CSVhandler(csvTimeKeeper, CSVWriter):
    def __init__(self) -> None:
        super().__init__()
        
    def writeData(self, data: str):
        print(super().month, super().year)
        if super().checkIfFileIsOutdated():
            CSVWriter.createNewCSVfile(super().getCsvPath(), super().year, super().month)
        CSVWriter.writeData(super().getCsvPath(), data)