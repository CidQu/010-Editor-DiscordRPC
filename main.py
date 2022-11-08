import psutil
from pypresence import Presence 
import time

start = int(time.time())
client_id = "1039279536027738163"

if "Discord.exe" in (p.name() for p in psutil.process_iter()):
    RPC = Presence(client_id)
    RPC.connect()
else:
    print('Open Discord then try again.')

if not "010Editor.exe" in (p.name() for p in psutil.process_iter()):
    print('Please Open 010 Editor')
    exit()
    
import scr.getByteNumber as getByteNumber
import scr.getFileName as getFileName
byte = getByteNumber.GetByteNumber()
fileName = getFileName.getFileName()

old_byte = ''
old_fileName = ''

while not False:

    if not "010Editor.exe" in (p.name() for p in psutil.process_iter()):
        print('Please Open 010 Editor')
        try:
            RPC.close()
        except:
            time.sleep(1)
        time.sleep(1)
    
    else:
        byte = getByteNumber.GetByteNumber()
        fileName = getFileName.getFileName()

        state_byte = "At Byte: " + str(byte)
        details_file = "Editing " + fileName

        if not old_byte == byte:
            old_byte == byte
            RPC.update(
                large_image = "0x303130",
                large_text = "HEX File",
                details = details_file,
                state = state_byte,
                start = start,
                small_image = '010editor',
                small_text = '010 Editor'
            )
            
        elif not old_fileName == fileName:
            old_fileName == fileName
            RPC.update(
                large_image = "0x303130",
                large_text = "HEX File",
                details = details_file,
                state = state_byte,
                start = start,
                small_image = '010editor',
                small_text = '010 Editor'
            )
    