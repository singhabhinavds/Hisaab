#!/usr/bin/env python
import wx


class MainFrame(wx.Frame):
    """Main frame of the appliaction"""
    def __init__(self, parent, title):
        
        wx.Frame.__init__(self, parent, title=title, size=wx.DefaultSize)
        
        self.Show(True)


app = wx.App(False)
frame = MainFrame(None, 'Hisaab')
app.MainLoop()
