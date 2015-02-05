import wx


def uiget_dir(message=''):
    """
    SUMMARY:                User Interface function to get a file-path.
    AUTHOR:                 Jacopo Solari, 2014-11-05
    
    Args:
        message (str): message to be displayed in the pop up window
    
    Returns:
        path (str): string containing the full path to the selected directory
    """

    app = wx.App(None)
    style = wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST
    dialog = wx.DirDialog(None, message,  style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
  
    return path


def uiget_file(wildcard='', message='pick a file'):
    """
    SUMMARY:            User Interface function to get a file-path.
    AUTHOR:             Jacopo Solari, 2014-10-31

    Args:
        wildcard (str): string for file extension filter ( examples: '*.py', '*.jpg', '*.tif' .. etc.) default is "All files"
        message (str): message to be displayed in the pop up window

    Returns:
        path (str): string containing the full path to the selected file
    """

    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, message, wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        print('An error occurred ..')
        path = None
    dialog.Destroy()

    return path