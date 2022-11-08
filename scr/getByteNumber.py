from pymem import *
from pymem.process import *

pm = Pymem('010Editor.exe')

def GetByteNumber():
    def GetPtrAddr(base, offsets):
        addr = pm.read_longlong(base)
        for i in offsets:
            if i != offsets[-1]:
                addr = pm.read_longlong(addr + i)
        return addr + offsets[-1]
    try:
        return pm.read_int(GetPtrAddr(pm.base_address + 0x0074DE40, offsets=[0x8, 0x8, 0x60, 0x8, 0x10, 0xB0, 0xD0]))
    except:
        pass