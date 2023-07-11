# This one only works while in combat

from pymem import *
from pymem.process import *

pm = Pymem("diceydungeons.exe")
targetModule = module_from_name(pm.process_handle, "diceydungeons.exe").lpBaseOfDll
offsets = [0x1B0]
baseOffset = 0x01D29950

def get_pointer_address(base, offsets):
# Only for 32 bit    addr = pm.read_int(base)
    addr = pm.read_longlong(base+baseOffset)
    print("addr:  ", hex(addr))
    for i in offsets:
        if(i != offsets[-1]):
            print("loop val i:  ",hex(i))
# Only for 32 bit            addr = pm.read_int(addr + i)
            addr = pm.read_longlong(addr + i)
    return addr + offsets[-1]

pm.write_int(get_pointer_address(targetModule, offsets), 500)