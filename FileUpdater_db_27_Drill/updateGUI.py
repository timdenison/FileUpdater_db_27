import wx, time, os, copy_new


class NewFrame(wx.Frame):
    def __init__(self, parent, title, width, height):
        wx.Frame.__init__(self, parent, title = title, size = (
            width, height))
        self.basicGUI()

    def OnQuit(self, e):
        self.Close()
    
    def mainMenu(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        fitem = filemenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
    
    def DirSelect(self, event):
        label = event.GetEventObject().GetLabel()
        if label == 'Select Source':
            dlg = wx.DirDialog(None,'Please select Source Directory:', style = wx.DD_DEFAULT_STYLE)
            dlg.ShowModal()
            self.sourcePath = dlg.GetPath()
            self.sourceText.SetLabel('Source Directory: ' + self.sourcePath)
            self.sourceText.Wrap(300)
        elif label == 'Select Destination':
            dlg = wx.DirDialog(None,'Please select Destination Directory:', style = wx.DD_DEFAULT_STYLE)
            dlg.ShowModal()
            self.destPath = dlg.GetPath()
            self.destText.SetLabel('Destination Directory: ' + self.destPath)
            self.destText.Wrap(300)

    def copyFiles(self, event):
        destPath = str(self.destPath)
        sourcePath = str(self.sourcePath)

        summary = copy_new.copyUpdatedFiles(sourcePath, destPath)
        sumMessage = wx.MessageBox(summary, 'Title', style = wx.OK)

  #  def outputSummary(summary):
        


    def basicGUI(self):
        self.mainMenu()
        self.Panel = wx.Panel(self, size = (500, 300), style = wx.SUNKEN_BORDER, pos = (0,0))
        sourcePanel = wx.Panel(self.Panel, size = (500, 50), style = wx.SUNKEN_BORDER, pos = (0,0))
        self.sourceText = wx.StaticText(sourcePanel, id = -1, label = 'Source Directory: ', pos = (0, 18), style = 0)
        sourceButton = wx.Button(sourcePanel, id = -1, label = 'Select Source', pos = (385, 15))
        sourceButton.Bind(wx.EVT_BUTTON, self.DirSelect)

        destPanel = wx.Panel(self.Panel, size = (500, 50), style = wx.SUNKEN_BORDER, pos = (0,50))
        self.destText = wx.StaticText(destPanel, id = -1, label = 'Destination Directory: ', pos = (0, 18), style = 0)
        destButton = wx.Button(destPanel, id = -1, label = 'Select Destination', pos = (360, 15))
        destButton.Bind(wx.EVT_BUTTON, self.DirSelect)

        copyPanel = wx.Panel(self.Panel, size = (500, 50), style = wx.SUNKEN_BORDER, pos = (0, 100))
        copyButton = wx.Button(copyPanel, id = -1, label = 'Copy New & Modified Files', pos =(320, 15))
        copyButton.Bind(wx.EVT_BUTTON, self.copyFiles)

  
        self.Show(True)
       

app = wx.App(False)
frame = NewFrame(None, 'Select Files to Copy for Update', 500, 300)
app.MainLoop()
        