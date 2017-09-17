# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class Download
###########################################################################

class Download(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"下载器", pos=wx.Point(20, 20), size=wx.Size(226, 216),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"          输入想下载的图片", wx.Point(-1, -1), wx.Size(200, -1), 0)
        self.title.Wrap(-1)
        bSizer2.Add(self.title, 0, wx.ALL, 5)

        self.text_search = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer2.Add(self.text_search, 0, wx.ALL, 5)

        self.button_search = wx.Button(self, wx.ID_ANY, u"下载", wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer2.Add(self.button_search, 0, wx.ALL, 5)

        self.gauge_info = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(200, -1), wx.GA_HORIZONTAL)
        self.gauge_info.SetValue(0)
        bSizer2.Add(self.gauge_info, 0, wx.ALL, 5)

        self.text_info = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer2.Add(self.text_info, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_search.Bind(wx.EVT_BUTTON, self.button_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def button_click(self, event):
        event.Skip()
