#!/usr/bin/env python
import wx
import wx.lib.sized_controls as sc


class MainFrame(wx.Frame):
    """Main frame of the appliaction"""
    def __init__(self, parent, title):
        #creating the main frame        
        wx.Frame.__init__(self, parent, title=title, size=wx.DefaultSize)
        #creating the panel for buttons/functions
        panel = wx.Panel(self, -1)

        #Defining Buttons
        button_view_data = wx.Button(panel, wx.ID_ANY, "View Total Expenses")
        button_add_expenses = wx.Button(panel, wx.ID_ANY, 'Add Expenses')
        button_review_expenses = wx.Button(panel, wx.ID_ANY, 'Review Expenses')
        button_calculate_individual_balance = wx.Button(panel, wx.ID_ANY, 'Calculate Individual Balance')
        button_exit_app = wx.Button(panel, wx.ID_ANY, 'Bye')
        
        #Defining Position of each button
        ## Positions are absolute at the moment...will be made dynamic
##        button_view_data.SetPosition((15,15))
##        button_add_expenses.SetPosition((15,50))
##        button_review_expenses.SetPosition((15,100))
##        button_calculate_individual_balance.SetPosition((15,150))
##        button_exit_app.SetPosition((15,200))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button_view_data, 1, wx.ALIGN_CENTER, 6)
        sizer.Add(button_add_expenses, 1, wx.ALIGN_CENTER, 6)
        sizer.Add(button_review_expenses, 1, wx.ALIGN_CENTER, 6)
        sizer.Add(button_calculate_individual_balance, 1, wx.ALIGN_CENTER, 6)
        sizer.Add(button_exit_app, 1, wx.ALIGN_CENTER, 6)
        panel.SetSizer(sizer)

        
        #Bind Events to buttons

        self.Bind(wx.EVT_BUTTON, self.OnExit, button_exit_app)


    #Defining the button events

    def OnExit(self, event):
            self.Close(True)
       


app = wx.App(False)
frame = MainFrame(None, 'Hisaab')
#Show the Main Frame in center
frame.CenterOnScreen()
frame.Show(True)
app.MainLoop()
