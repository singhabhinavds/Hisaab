import wx
import wx.grid as gridlib
import mysql.connector

class BudgetSheetGui(gridlib.PyGridTableBase):

    def __init__(self, log, budget_rows_count):
        print budget_rows_count
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
        return 6

    def GetNumberCols(self):
        return 7

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        #return str((row, col))
        return 'lol'
    
    def SetValue(self, row, col, value):
        self.log.write('SetValue(%d, %d, "%s") ignored.\n'
                       % (row, col, value))

class BudgetSheetGuiGrid(gridlib.Grid):

    def __init__(self, parent, log, budget_rows_count):
        gridlib.Grid.__init__(self, parent, -1)

        table = BudgetSheetGui(log, budget_rows_count)
        self.SetTable(table, True)

        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightDown)

    def OnRightDown(self, event):
        print self.GetSelectedRows()

class TestFrame(wx.Frame):

    def __init__(self, parent, log,DB_NAME):
        wx.Frame.__init__(self, parent, -1,
                          "Budget Sheet", size=(640, 480))
        
        DBQuery = BudgetSheetDBQuery(DB_NAME)
        grid = BudgetSheetGuiGrid(self, log,DBQuery.budget_rows_count)

        #grid.SetReadOnly(5, 5, True)

class BudgetSheetDBQuery():

    def __init__(self,dbname):
        connection = mysql.connector.connect(user='root')
        cursor = connection.cursor()
        connection.database = dbname

        query_flatmates = "Select * from flatmates"
        query_budget_sheet = "Select * from budget_sheet"

        cursor.execute(query_flatmates)

        for (fid, name) in cursor:
            print "{}, {}".format(fid, name)
        
        cursor.execute(query_budget_sheet)

        for (a,b,c,d,e,f) in cursor:
            print "{},{},{},{},{},{}".format(a,b,c,d,e,f)

        self.budget_rows_count = cursor.rowcount
