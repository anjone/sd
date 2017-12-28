import win32gui
from win32com.client import Dispatch
import win32con
import pythoncom
import time

def TestObjectFromWindow():
    # Check we can use ObjectFromLresult to get the COM object from the
    # HWND - see KB Q249232
    # Locating the HWND is different than the KB says...
    # hwnd = win32gui.FindWindow('IEFrame', None)
    hwnd = win32gui.FindWindow('IEFrame', None)
    print(hwnd)
    for child_class in ['TabWindowClass', 'Shell DocObject View',
                        'Internet Explorer_Server']:
        hwnd = win32gui.FindWindowEx(hwnd, 0, child_class, None)
        # ack - not working for markh on vista with IE8 (or maybe it is the
        # lack of the 'accessibility' components mentioned in Q249232)
        # either way - not working!
        return
    # But here is the point - once you have an 'Internet Explorer_Server',
    # you can send a message and use ObjectFromLresult to get it back.
    msg = win32gui.RegisterWindowMessage("WM_HTML_GETOBJECT")
    rc, result = win32gui.SendMessageTimeout(hwnd, msg, 0, 0, win32con.SMTO_ABORTIFHUNG, 1000)
    ob = pythoncom.ObjectFromLresult(result, pythoncom.IID_IDispatch, 0)
    doc = win32com.client.Dispatch(ob)
    # just to prove it works, set the background color of the document.
    for color in "red green blue orange white".split():
        doc.bgColor = color
        time.sleep(0.2)


childList = []

def callback(hwnd, childList):
        childList.append(hwnd)

def getAllIEChildrenWindows():
    #handle = win32gui.FindWindow('IEFrame', None)
    handle = win32gui.FindWindow('360se6_Frame', None)
    print(handle)
    
    win32gui.EnumChildWindows(handle, callback, childList)

    for ch in childList:
        print(win32gui.GetClassName(ch))
        print(win32gui.GetWindowText(ch))
        if ('Internet Explorer_Server' == win32gui.GetClassName(ch)):

            innerChildList = []
            win32gui.EnumChildWindows(ch, callback, innerChildList)
            for ich in innerChildList:
                print("-------------------------------------------------------------")
                print(win32gui.GetClassName(ich))
                print(win32gui.GetWindowText(ich))
                if('SunAwtCanvas' == win32gui.GetClassName(ich)):
                    msg = win32gui.RegisterWindowMessage("WM_HTML_GETOBJECT")
                    rc, result = win32gui.SendMessageTimeout(ich, msg, 0, 0, win32con.SMTO_ABORTIFHUNG, 1000)
                    ob = pythoncom.ObjectFromLresult(result, pythoncom.IID_IDispatch, 0)
                    doc = Dispatch(ob)
                    print(doc.body.innerHtml)
                print("-------------------------------------------------------------")
            
            print(ch)
            msg = win32gui.RegisterWindowMessage("WM_HTML_GETOBJECT")
            rc, result = win32gui.SendMessageTimeout(ch, msg, 0, 0, win32con.SMTO_ABORTIFHUNG, 1000)
            ob = pythoncom.ObjectFromLresult(result, pythoncom.IID_IDispatch, 0)
            doc = Dispatch(ob)
            #print(doc.body.innerHtml)
            print(doc.body.innerHtml)

            while(doc.body.innerHtml.find("18923238393") == -1):
                msg = win32gui.RegisterWindowMessage("WM_HTML_GETOBJECT")
                rc, result = win32gui.SendMessageTimeout(ch, msg, 0, 0, win32con.SMTO_ABORTIFHUNG, 1000)
                ob = pythoncom.ObjectFromLresult(result, pythoncom.IID_IDispatch, 0)
                doc = Dispatch(ob)

            print(doc.body.innerHtml)
            
            
            doc.all['userCode'].value='zhangxinxin-006'
            doc.all['password'].value='Tbkfxt@1234'
            doc.all['login'].click()
            # just to prove it works, set the background color of the document.
            for color in "red green blue orange white".split():
                doc.bgColor = color
                time.sleep(0.2)


        if ('WorkerW' == win32gui.GetClassName(ch)):
            print(ch)

def inner_callback(chwnd, params):
    print(win32gui.GetClassName(ch))
    #return True

def getAllChildrenWindows():
    handle = win32gui.FindWindow('IEFrame', None)
    win32gui.EnumChildWindows(handle, inner_callback, None)


from win32com.client import Dispatch 
from win32gui import GetClassName

def ieConnect():
    ShellWindowsCLSID = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
    ShellWindows = Dispatch(ShellWindowsCLSID)
    print(ShellWindows)
    print(ShellWindows.Count)
    
    for i in range(ShellWindows.Count):
        #print(GetClassName(ShellWindows[i]))
        print(ShellWindows[i].Document)
        print(ShellWindows[i])
        print(ShellWindows[i].LocationName)
        print(ShellWindows[i].LocationURL)
        if(GetClassName(ShellWindows[i].HWND) == 'IEFrame'):
            print(ShellWindows[i].Document)
            print(ShellWindows[i].LocationName)
            print(ShellWindows[i].LocationURL)
            print(50 * '-')


if __name__ == '__main__':
    #TestObjectFromWindow()
    #getAllIEChildrenWindows()
    #getAllChildrenWindows()
    ieConnect()
