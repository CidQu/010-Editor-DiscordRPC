import win32gui
import win32process
import psutil
import ctypes

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

def getFileName():
    def getProcessIDByName():
        zeroonezero_pids = []
        process_name = "010Editor.exe"

        for proc in psutil.process_iter():
            if process_name in proc.name():
                zeroonezero_pids.append(proc.pid)

        return zeroonezero_pids

    def get_hwnds_for_pid(pid):
        def callback(hwnd, hwnds):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

            if found_pid == pid:
                hwnds.append(hwnd)
            return True
        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds 

    def getWindowTitleByHandle(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        return buff.value

    def getHandle():
        pids = getProcessIDByName()

        for i in pids:
            hwnds = get_hwnds_for_pid(i)
            for hwnd in hwnds:
                if IsWindowVisible(hwnd):
                    return hwnd

    hwnd_010 = getHandle()
    windows_name = getWindowTitleByHandle(hwnd=hwnd_010)

    if "\\" in windows_name:
        remove_010 = str(windows_name).split(' - ')[-1:][0]
        file_name = str(remove_010).split('\\')[-1:][0]
        return file_name
    else:
        remove_010 = str(windows_name).split(' - ')[-1:][0]
        file_name = remove_010
        return file_name