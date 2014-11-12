import wx

def uiget_dir(message):
	'''
	SUMMARY: 				User Interface function to get a file-path.
	AUTHOR: 				Jacopo Solari (solari@amolf.nl)
	DATE ADDED/MODIFIED: 	2014-11-05
	
	INPUT:		
	message : message to be displayed in the pop up window

	OUTPUT:		
	path : string containing the full path to the selected directory
	'''
    app = wx.App(None)
    style = wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST
    dialog = wx.DirDialog(None, message,  style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
  
    return path