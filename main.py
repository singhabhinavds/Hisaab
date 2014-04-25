#!/usr/bin/env python
import wx


class MainFrame(wx.Frame):
    """Main frame of the appliaction"""
    def __init__(self, parent, title):
        #creating the main frame        
        wx.Frame.__init__(self, parent, title=title, size=wx.DefaultSize)
        #creating the panel for buttons/functions
        panel = wx.Panel(self, -1)

        #Defining Buttons
        button_view_data = wx.Button(panel, 1003, "View Total Expenses")
        button_add_expenses = wx.Button(panel, 1004, 'Add Expenses')
        button_review_expenses = wx.Button(panel, 1005, 'Review Expenses')
        button_calculate_individual_balance = wx.Button(panel, 1006, 'Calculate Individual Balance')

        #Defining Position of each button
        ## Positions are absolute at the moment...will be made dynamic
        button_view_data.SetPosition((15,15))
        button_add_expenses.SetPosition((15,50))
        button_review_expenses.SetPosition((15,100))
        button_calculate_individual_balance.SetPosition((15,150))

        #Show the Main Frame
        self.Show(True)


app = wx.App(False)
frame = MainFrame(None, 'Hisaab')
app.MainLoop()
