"""
This sample connects to the running instances of IE on your computer and prints out
the URL, Cookie- if any, and the HTML content of the site.

You need to generate stub files for IE and MSHTML using the readtlb tool of ctypes.

python ctypes\com\tools\readtlb.py c:\winnt\system32\MSHTML.TLB > mshtml.py
python ctypes\com\tools\readtlb.py C:\windows\system32\SHDOCVW.DLL > ie6.py

Known Issues:
Filters out Explorer sinces we don't expect it to have HTML content or cookies. Explorer and IExplore are part of the Shell and therefore IShellWindows.

The mshmtl.py file must be fixed manually by inserting this at the top, otherwise you get NameErrors:
 
 LONG_PTR = c_long
 UINT_PTR = c_uint 
 wireHGLOBAL = wireHWND = wireHDC = wireHBITMAP = c_int 
 SAFEARRAY = POINTER # I"m quite sure this is wrong

usage:
python IEconnect.py

You need the good ctypes module from http://starship.python.net/crew/theller/ctypes/

Sample based on information from 
http://support.microsoft.com/default.aspx?scid=http://support.microsoft.com:80/support/kb/articles/Q176/7/92.ASP&NoWebContent=1

By Eric Koome
email ekoome@yahoo.com

"""
from ctypes import *
from ctypes.com import GUID, HRESULT, IUnknown, CreateInstance
from ctypes.com.automation import IDispatch, VARIANT, BSTR, oleaut32
from ctypes.wintypes import DWORD
from win32con import NULL
from ie6 import ShellWindows, IShellWindows, InternetExplorer, IWebBrowser2 #generated from SHDOCVW.DLL
from mshtml import IHTMLDocument2, IHTMLElement # generated using MSHTML.TLB

            
win1 = win32gui.FindWindow('IEFrame', 'Test main page - Windows Internet Explorer') #IE window handle
win1 = winGuiAuto.findControl(win1, None, 'Internet Explorer_Server', None)	    # get the 'Internet Explorer_Server	

# get the IHTMLDocument2 of the popup dialog
oleacc = oledll.LoadLibrary ( 'oleacc.dll' )
WM_HTML_GETOBJECT = windll.user32.RegisterWindowMessageA ('WM_HTML_GETOBJECT' )
lResult = c_ulong ( )
ret = windll.user32.SendMessageTimeoutA ( c_int ( win1 ), c_int (WM_HTML_GETOBJECT),c_int ( 0 ), c_int ( 0 ), c_int ( SMTO_ABORTIFHUNG ), c_int ( 1000 ), byref (lResult ) )
pIHTMLDocument2 = POINTER ( IHTMLDocument2 ) ( )
oleacc.ObjectFromLresult ( lResult, byref ( IHTMLDocument2._iid_ ), 0,byref (pIHTMLDocument2 ) ) # title of the page verifies
ihtmlwin = pIHTMLDocument2.parentWindow

# and the IServiceProvider
pIServiceProvider = POINTER ( IServiceProvider ) ()
pIServiceProvider = ihtmlwin.QueryInterface(IServiceProvider, IServiceProvider._iid_)

ie = POINTER(IWebBrowser2) ()
ie = pIServiceProvider.QueryService(IWebBrowserApp._iid_, IWebBrowser2._iid_)    
    
