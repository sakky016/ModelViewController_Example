from tkinter import *
from model import *
import view_gui as v

class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.view = v.ViewGui(self.root, self)
        self.root.title("MVC example")
        self.root.resizable(0, 0)
        self.root.mainloop()

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

    def GetListBoxData(self):
        return self.model.GetDataFromList()