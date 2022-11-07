import psutil
from pypresence import Presence 
import time
import getByteNumber

start = int(time.time())
client_id = "1039279536027738163"

if "Discord.exe" in (p.name() for p in psutil.process_iter()):
    RPC = Presence(client_id)
    RPC.connect()
else:
    print('Open Discord then try again.')


while not False:

    if not "010Editor.exe" in (p.name() for p in psutil.process_iter()):
        print('Please Open 010 Editor')
        time.sleep(1)
    
    else:
        byte = getByteNumber.GetByteNumber()
        state_byte = "At Byte: " + str(byte)

        RPC.update(
            large_image = "0x303130", #name of your asset
            large_text = "HEX File",
            details = "Editing Hex File",
            state = state_byte,
            start = start,
            small_image = '010editor',
            small_text = '010 Editor'
        )
        time.sleep(3)
    