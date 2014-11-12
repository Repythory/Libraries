import wx

def uiget_file(wildcard='',message='pick a file'):
	'''
	SUMMARY:			User Interface function to get a file-path.
	AUTHOR:				Jacopo Solari (solari@amolf.nl)
	DATE ADDED:			2014-10-31

	INPUT:
	wildcard : string for file extension filter ( examples: '*.py', '*.jpg', '*.tif' .. etc.) default is "All files"
	message : message to be displayed in the pop up window

	OUTPUT:		
	path : string containing the full path to the selected file
	'''
    app = wx.App(None)        
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, message, wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        print 'An error occurred ..'
        path = None
    dialog.Destroy()
  
    return path