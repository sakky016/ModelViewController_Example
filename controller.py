from tkinter import *
from model import *
import view_gui as v

class Controller:
    def __init__(self):
        # Create main window
        self.root = Tk()

        # Create an instance of model (data associated with application)
        self.model = Model()

        # Create an instance of View (Visual presentation of application)
        self.view = v.ViewGui(self.root, self)

        # Main window properties
        self.root.title("MVC example")
        self.root.resizable(0, 0)
        self.root.mainloop()

    def GetListBoxData(self):
        return self.model.GetDataFromList()

    # Button handlers
    def OnBtnAdd(self, val):
        print("OnBtnAdd: val = ", val)
        if (len(val)):
            self.model.AppendList(val)
            self.view.UpdateListbox()
            self.view.ClearInput()

    def OnBtnRemove(self, values):
        self.model.RemoveFromList(values)
        self.view.UpdateListbox()

    def OnBtnClear(self):
        print("OnBtnClear")
        self.model.ClearList()
        self.view.UpdateListbox()

    def OnBtnClose(self):
        self.root.quit()

