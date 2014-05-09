import wx
import wx.grid as gridlib

class BudgetSheetGui(gridlib.PyGridTableBase):

    def __init__(self, log):
        gridlib.PyGridTablesBase(self).__init__(self)
        self.log = log

        self.odd = gridlib.GridCellAttr()
        self.odd.SetBackgroundColour('sky blue')
        self.even = gridlib.GridCellAttr()
        self.even.SetBackgroundColour("sea green")


    def GetAttr(self, row, col, kind):
        attr = [self.even, self.odd][row % 2]
        attr.IncRef()
        return attr


    def GetNuberRows(self):
        return 100

    def GetNumberCols(self):
        return 100

    def IsEmptyCell(self, row, col):
        return str((row,col))

    def SetValue(self, row, col, value):
        self.log.write('SetValue(%d, %d, "%s") ignored.\n'
                       % (row, col, value))

class BudgetSheetGuiGrid(gridlib.Grid):

    def __init__(self, parent, log):
        gridlib.Grid.__init__(self, parent, -1)

        table = HugeTable(log)
        self.SetTable(table, True)

        self.Bind(gridlib.EVT_GRID_RIGHT_CLICK, self.OnRightDown)

    def OnRightDown(self, event):
        print "Hello"
        print self.GetSelectedRows()

class TestFrame(wx.Frame):

    def __init__(self, parent, log):
        wx.Frame.__init__(self, parent, -1,
                          "Huge (virtual) Table Demo", size=(640, 480))
        grid = HugeTableGrid(self, log)

        grid.SetReadOnly(5, 5, True)
