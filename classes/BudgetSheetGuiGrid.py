import wx
import wx.grid as gridlib
import mysql.connector

class BudgetSheetGui(gridlib.PyGridTableBase):

    def __init__(self, log, DBQuery):
        gridlib.PyGridTableBase.__init__(self)
        self.log = log
        self.DBQuery = DBQuery

        self.colnames = ['Transaction ID','Item Bought', 'Amount Spent',
                         'Who spent?' ,'Expenditure Shared among?',
                         'Expense Date','Comments']

        self.odd = gridlib.GridCellAttr()
        #self.odd.SetBackgroundColour('sky blue')
        self.even = gridlib.GridCellAttr()
        #self.even.SetBackgroundColour("sea green")


##    def GetAttr(self, row, col, kind):
##        attr = [self.even, self.odd][row % 2]
##        attr.IncRef()
##        return attr

    def GetNumberRows(self):
        return self.DBQuery.budget_rows_count

    def GetNumberCols(self):
        return 7

    def GetColLabelValue(self, col):
        return self.colnames[col]
    
    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        if col == 0:
            return self.DBQuery.store_rows_a[row]
        elif col == 1:
            return self.DBQuery.store_rows_b[row]
        elif col == 2:
            return self.DBQuery.store_rows_c[row]
        elif col == 3:
            return self.DBQuery.store_rows_d[row]
        elif col == 4:
            return self.DBQuery.store_rows_e[row]
        elif col == 5:
            return self.DBQuery.store_rows_f[row]
        else:
            #we are displaying on other columns
            return ''
    
    def SetValue(self, row, col, value):
        self.log.write('SetValue(%d, %d, "%s") ignored.\n'
                       % (row, col, value))
        
#------------------------------------------------------------------------------------

class BudgetSheetGuiGrid(gridlib.Grid):

    def __init__(self, parent, log, DBQuery):
        gridlib.Grid.__init__(self, parent, -1)

        table = BudgetSheetGui(log, DBQuery)
        self.SetTable(table, True)

        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightDown)
        self.AutoSizeColumns(True)

    def OnRightDown(self, event):
        print self.GetSelectedRows()

#------------------------------------------------------------------------------------
        
class TestFrame(wx.Frame):

    def __init__(self, parent, log,DB_NAME):
        wx.Frame.__init__(self, parent, -1,
                          "Budget Sheet", size=(800, 400))
        
        DBQuery = BudgetSheetDBQuery(DB_NAME)
        grid = BudgetSheetGuiGrid(self, log,DBQuery)

        grid.EnableEditing(False)
        
#------------------------------------------------------------------------------------
        
class BudgetSheetDBQuery():

    def __init__(self,dbname):
        connection = mysql.connector.connect(user='root')
        cursor = connection.cursor()
        connection.database = dbname

        self.store_rows_a = []
        self.store_rows_b = []
        self.store_rows_c = []
        self.store_rows_d = []
        self.store_rows_f = []
        self.store_rows_e = []
        
        query_flatmates = "Select * from flatmates"
        query_budget_sheet = "Select * from budget_sheet"

##        cursor.execute(query_flatmates)
##
##        for (fid, name) in cursor:
##            print "{}, {}".format(fid, name)
        
        cursor.execute(query_budget_sheet)

        for (a,b,c,d,e,f) in cursor:
            self.store_rows_a.append(a)
            self.store_rows_b.append(b)
            self.store_rows_c.append(c)
            self.store_rows_d.append(d)
            self.store_rows_e.append(e)
            self.store_rows_f.append(f)
##            print "{},{},{},{},{},{}".format(a,b,c,d,e,f)

##      we get the number of results returned to populate later our rows in sheet      
        self.budget_rows_count = cursor.rowcount

        cursor.close()

        #cursor = connection.cursor()
