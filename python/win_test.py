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
    handle = win32gui.FindWindow('IEFrame', None)
    print(handle)
    
    win32gui.EnumChildWindows(handle, callback, childList)

    for ch in childList:
        print(win32gui.GetClassName(ch))
        if ('Internet Explorer_Server' == win32gui.GetClassName(ch)):
            print(ch)
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

if __name__ == '__main__':
    #TestObjectFromWindow()
    getAllIEChildrenWindows()
