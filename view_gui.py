from tkinter import *
from tkinter import ttk
import controller as c

class ViewGui:
    def __init__(self, root, controller):
        self.listBoxData = []
        self.controller = controller
        self.AddWidgets(root)

    def AddWidgets(self, root):
        rowIndex = 0
        colIndex = 0

        self.frame = ttk.Frame(root)
        self.frame.grid(padx=2, pady=2)

        # Row 0
        self.lblEntry = ttk.Label(self.frame, text="Enter value to add")
        self.lblEntry.grid(row=rowIndex, column=colIndex, padx=2, pady=2)

        self.inpEntry = ttk.Entry(self.frame)
        self.inpEntry.grid(row=rowIndex, column=colIndex + 1, padx=2, pady=2)
        self.inpEntry.focus_set()

        self.btnAdd = ttk.Button(self.frame, text="Add", command=lambda: self.controller.OnBtnAdd(self.inpEntry.get()))
        self.btnAdd.grid(row=rowIndex, column=colIndex + 2, padx=2, pady=2)

        # Row 1
        rowIndex = rowIndex + 1
        self.lbDataList = Listbox(self.frame, selectmode='multiple')
        self.lbDataList.grid(row=rowIndex, column=colIndex + 1, columnspan=1, padx=2, pady=2)

        # Row 2
        rowIndex = rowIndex + 1
        self.btnRemove = ttk.Button(self.frame, text="Remove", command=lambda: self.controller.OnBtnRemove(self.lbDataList.curselection()))
        self.btnRemove.grid(row=rowIndex, column=colIndex, padx=2, pady=2)

        self.btnClear = ttk.Button(self.frame, text="Clear", command=lambda : self.controller.OnBtnClear())
        self.btnClear.grid(row=rowIndex, column=colIndex + 1, padx=2, pady=2)

        self.btnClose = ttk.Button(self.frame, text="Close", command=lambda : self.controller.OnBtnClose())
        self.btnClose.grid(row=rowIndex, column=colIndex + 2, padx=2, pady=2)

    def UpdateListbox(self):
        idx = 1
        self.lbDataList.delete(0, 'end')
        self.listBoxData = self.controller.GetListBoxData()
        for val in self.listBoxData:
            self.lbDataList.insert(idx, val)
            idx = idx + 1

        self.inpEntry.focus_set()

    def ClearInput(self):
        self.inpEntry.delete(0, 'end')
        self.inpEntry.focus_set()