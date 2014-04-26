#!/usr/bin/env python
import wx
import sys

sys.path.append("classes")

import MainFrame


app = wx.App(False)
frame = MainFrame.MainFrame(None, 'Hisaab')
#Show the Main Frame in center
frame.CenterOnScreen()
frame.Show(True)
app.MainLoop()
