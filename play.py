import curses
from curses import wrapper
import time
import random

def load_text():
    with open("text.txt" , 'r') as file:
        return random.choice(file.readlines()).strip()
    

def start_screen(stdscr):
    stdscr.clear()
    
    stdscr.addstr("Welcome to the game!")
    stdscr.addstr("\nPress any key yo start!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target_text,current_text,wpm=0):
    stdscr.addstr(target_text)  
    stdscr.addstr(f"\nWPM: {wpm}")
    
    for i, char in enumerate(current_text):
        correct_char= target_text[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
       time_elapesed = max(time.time() - start_time,1)
       wpm = round((len(current_text) / (time_elapesed / 60))/5)
       stdscr.clear()
       display_text(stdscr,target_text,current_text,wpm)
       stdscr.refresh()
       
       
       
       try:
           key = stdscr.getkey()
       except:
           continue
       
       if "".join(current_text) == target_text:
           stdscr.nodelay(False)
           break
       
       if ord(key) == 27:
           break
       if key in ("KEY_BACKSPACE",'\x7f','\b'):
           current_text.pop() if current_text else None
       elif len(current_text) < len(target_text):
           current_text.append(key)
       
       
      
       
    

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
    
        stdscr.addstr(2,0, "You Completed the test! Press any key to continue")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
        
wrapper(main)