from csv import * #import the CSV module for functionality
from ImportCSV import Open, open


class ImportCsv(object):
    """This class is represents a CSV datastream from the local file system"""

    def _init_(self, strDelim: str, strFileP: str, strQuoteC: str, strNewL: str, ):
        self.strDeliminator = strDelim
        """:type :str"""
        self.strFilePath = strFileP
        """:type :str"""
        self.strQuoteChar = strQuoteC
        """:type :str"""
        self.strNewLineChar = strNewL
        """:type :str"""
        self.iColumnCount = 0
        """:type: int"""
        self.list = []
        """:type: list"""

    #Public Members - Do not Access From outside the Class!
    #########################################################

    #get the class attributes without calling them directly
    #This causes the class attributes to be private
    def __getattribute__(self, strName: str) -> str:
        return self._dict_[strName]

    #set the class attributes without calling them directly
    #This causes the class attributes to be private
    def __setattr__(self, strName: str, value) -> None:
        self._dict_[strName] = value

    #set the File path: thinking this will be used with a console read in 
    def SetFilePath(self, strPath: str):
        self.setattr(self, "strFilePath", strPath)

    #Open the datastream and begin reading from the file
    def ReadFromCurrentFile(self) -> list:
        list = []
        try:
            #Open the currently selected file to stream data through
            with open(self.filepath) as csvFile:
                reader = csv.reader(csvFile, deliminator=self.strDeliminator, quotechar=self.strQuoteChar)
                for row in reader:
                    list.append(row)
                return list
        except errorValue:
            list = []
            return list

    #Write to the datastream in csv format
    def WriteToFile(self, writeList: list) -> str:
        try:
            if (self.iColumnCount >= 0):
                raise NameError("Column Count is less than zero")
            else:
                with open(self.strFilePath) as csvFile:
                    writer = csv.Writer(self.strFilePath)
                for row in writeList:
                    writer.
        except errorValue:
            return errorValue

    #########################################################
             


    #Private Members - Do not Access From outside the Class!
    #########################################################