import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):  #yo object lai access garna milnu paro 
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test! ")
    stdscr.addstr("\nPress any key to start ")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}" )
        
    for idx, char in enumerate(current):
        correct_char =target[idx]
        color =curses.color_pair(1)
        if char!= correct_char:
            color = curses.color_pair(2)
            
            
        stdscr.addstr(0, idx, char, color)
            
def load_text():
    try:
        with open("text.txt", "r") as file:
            lines = file.readlines()
            return random.choice(lines).strip()        # harek line paxi invisible \n hunxa so to remove it .strip()  
    except FileNotFoundError:
        return "Error: text.txt not found!"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm=0
    start_time = time.time()
    stdscr.nodelay(True)  #kei na dabda ni wpm ghatos vanera
    
    stdscr.clear()   #ya screen clear vayena vane harek char sita target_text print vako vae garxa
    stdscr.addstr(target_text)

    while True:
        time_elapsed =max(time.time() - start_time, 1)#suru ma duitei time same hunxa max use garera 0 vayeni 1 dinxa to avoid zero division error hatako
        wpm = round((len(current_text) / (time_elapsed / 60))/ 5)
        stdscr.clear()   #ya screen clear vayena vane harek char sita target_text print vako vae garxa
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        
        if target_text == "".join(current_text):
            stdscr.nodelay(False)
            break
        
        try:  # nodelay le garda tala error aauxa so yesto gareko
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) >0:
                current_text.pop()
        # yesle chai aba text lekhda lekhdei deko vand abesi vayo vane jati type gareni kei nagarne vo
        elif len(current_text)< len(target_text):
            current_text.append(key)
            
        
            
        
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) #yo bahira mileina garna tala call garesi initialize vayesi matra chalauna paiyo
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # (pairs, ani TEXT colors, background color)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) 
    
    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
    
        stdscr.addstr(2, 0, "You completed the text test and your accuracy was 100%!! Press any key to continue")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
        
    
    
wrapper(main)  # yesle main fucntion call garxa tya vako jati sablai initialize garera
    
    
    # stdscr.clear() #screen sab clear garxa
    # stdscr.addstr(0,0,"hello world")  #(row(vertical), column(horizontal))
    # stdscr.addstr(1,80,"hello world") # yesto sangei vo vane text override garxa 2nd ko mathi first aauxa
    
    # stdscr.addstr("hello world", curses.color_pair(2))
    # stdscr.refresh()  
    # key= stdscr.getkey()  #immediately close gardeina user le kei dabesi matra
    # print(key)
    
