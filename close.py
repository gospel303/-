def closesoft():
    print('''挂载程序关闭中……
          ''')
    import win32com
    import win32com.client
    wc = win32com.client.constants

    try:
        wps = win32com.client.gencache.EnsureDispatch('kwps.application')
    except:
        wps = win32com.client.gencache.EnsureDispatch('wps.application')
    else:
        wps = win32com.client.gencache.EnsureDispatch('word.application')
    try:
        wps.Documents.Close()
        wps.Documents.Close(wc.wdDoNotSaveChanges)
        wps.Quit
    except:
        pass

closesoft()
