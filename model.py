# This stores only the underlying data model of our application
class Model:
    def __init__(self):
        self.data = []
        self.eventList = []

    # Adds value to the list
    def AppendList(self, val):
        self.data.append(val)

    def RemoveFromList(self, indices):
        tmp = []
        index = 0
        for val in self.data:
            if (index not in indices):
                tmp.append(val)

        self.data = tmp

    # Clears the list
    def ClearList(self):
        self.data.clear()

    # Fetches list content
    def GetDataFromList(self):
        return self.data

    # Fetches number of entries in list
    def GetNumDataInList(self):
        return len(self.data)
