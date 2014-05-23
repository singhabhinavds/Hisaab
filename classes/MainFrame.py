#!/usr/bin/env python
import wx
import sys

import BudgetSheetGuiGrid

sys.path.append("config")

import create_sheet


class MainFrame(wx.Frame):
    """Main frame of the appliaction"""
    def __init__(self, parent, title):
        #creating the main frame        
        wx.Frame.__init__(self, parent, title=title, size=wx.DefaultSize, style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        #creating the panel for buttons/functions
        panel = wx.Panel(self, -1)

        #Defining Buttons
        button_add_budget = wx.Button(panel, wx.ID_ANY, "Add a New Budget Sheet")
        button_view_data = wx.Button(panel, wx.ID_ANY, "View Total Expenses")
        button_add_expenses = wx.Button(panel, wx.ID_ANY, 'Add Expenses')
        button_review_expenses = wx.Button(panel, wx.ID_ANY, 'Review Expenses')
        button_calculate_individual_balance = wx.Button(panel, wx.ID_ANY, 'Calculate Individual Balance')
        button_exit_app = wx.Button(panel, wx.ID_ANY, 'Bye')
        
        #Defining Position of each button

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button_add_budget, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(button_view_data, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(button_add_expenses, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(button_review_expenses, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(button_calculate_individual_balance, 1, wx.ALIGN_CENTER, 0)
        sizer.Add(button_exit_app, 1, wx.ALIGN_CENTER, 0)
        panel.SetSizer(sizer)

        
        #Bind Events to buttons

        self.Bind(wx.EVT_BUTTON, self.AddBudget, button_add_budget)
        self.Bind(wx.EVT_BUTTON, self.ViewBudget, button_view_data)
        self.Bind(wx.EVT_BUTTON, self.OnExit, button_exit_app)


    #Defining the button events

    def AddBudget(self, event):
        CreateDBObject = create_sheet.ConnectToDB()
        sheet_created = CreateDBObject.create_selected_DB()
        if sheet_created == True:
            wx.MessageBox("Success!! Your Flat Budget Sheet has been Added!!!")
        else:
            wx.MessageBox("Aww Crap!!! You will have to Retry!!")

    def ViewBudget(self, event):

        
        view_budget_sheet = BudgetSheetGuiGrid.TestFrame(None, sys.stdout,
                                                         create_sheet.DB_NAME)
        view_budget_sheet.Show(True)

        
        
        
    def OnExit(self, event):
        self.Close(True)
       
