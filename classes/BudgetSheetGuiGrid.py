import wx
import wx.grid as gridlib

class BudgetSheetGui(gridlib.PyGridTableBase):

    def __init__(self, log):
        gridlib.PyGridTableBase.__init__(self)
        self.log = log

        self.odd = gridlib.GridCellAttr()
        #self.odd.SetBackgroundColour('sky blue')
        self.even = gridlib.GridCellAttr()
        #self.even.SetBackgroundColour("sea green")


    def GetAttr(self, row, col, kind):
        attr = [self.even, self.odd][row % 2]
        attr.IncRef()
        return attr


    def GetNumberRows(self):
        return 100

    def GetNumberCols(self):
        return 100

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        #return str((row, col))
        return 'lol'
    
    def SetValue(self, row, col, value):
        self.log.write('SetValue(%d, %d, "%s") ignored.\n'
                       % (row, col, value))

class BudgetSheetGuiGrid(gridlib.Grid):

    def __init__(self, parent, log):
        gridlib.Grid.__init__(self, parent, -1)

        table = BudgetSheetGui(log)
        self.SetTable(table, True)

        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightDown)

    def OnRightDown(self, event):
        print self.GetSelectedRows()

class TestFrame(wx.Frame):

    def __init__(self, parent, log):
        wx.Frame.__init__(self, parent, -1,
                          "Budget Sheet", size=(640, 480))
        grid = BudgetSheetGuiGrid(self, log)

        #grid.SetReadOnly(5, 5, True)
