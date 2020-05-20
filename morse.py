import RPi.GPIO as GPIO
import time
from Tkinter import *
import tkFont
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def dot():
    print('dot')
    GPIO.output(11,GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.25)
def dash():
    print('dash')
    GPIO.output(11,GPIO.HIGH)
    time.sleep(0.55)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.55)
    
    
def char():
    print('character_change')
    GPIO.output(11,GPIO.HIGH)
    time.sleep(1.0)
    GPIO.output(11,GPIO.LOW)
    time.sleep(1.0)
def multipleDash(n):
    i=0
    for i in range(n):
        dash()
        i=i+1

def multipleDot(n):
    i=0
    for i in range(n):
        dot()
        i=i+1
        
    
def morseCode(c):
    print(c);
    if(c=='a'):
        dot()
        dash()
        
    elif(c=='b'):
        dash()
        multipleDot(3)
        
    elif(c=='c'):
        dash()
        dot()
        dash()
        dot()
        
    elif(c=='d'):
        dash()
        multipleDot(2)
        
    elif(c=='e'):
        dot()
    elif(c=='f'):
        multipleDot(2)
        dash()
        dot()
        
        
    elif(c=='g'):
        multipleDash(2)
        dot()
        
    elif(c=='h'):
        multipleDot(4)
        
    elif(c=='i'):
        multipleDot(2)
        
    elif(c=='j'):
        dot()
        multipleDash(3)
        
    elif(c=='k'):
        dash()
        dot()
        dash()
        
        
    elif(c=='l'):
        dot()
        dash()
        multipleDot(2)
        
        
    elif(c=='m'):
        multipleDash(2)
        
    elif(c=='n'):
        dash()
        dot()
        
        
    elif(c=='o'):
        multipleDash(3)
        
        
    elif(c=='p'):
        dot()
        multipleDash(2)
        dot()
        
        
    elif(c=='q'):
        multipleDash(2)
        dot()
        dash()
        
        
    elif(c=='r'):
        dot()
        dash()
        dot()
        
    elif(c=='s'):
        multipleDot(3)
        
        
    elif(c=='t'):
        dash()
        
    elif(c=='u'):
        multipleDot(2)
        dash()
        
        
    elif(c=='v'):
        multipleDot(3)
        dash()
        
        
    elif(c=='w'):
        dot()
        multipleDash(2)
        
        
    elif(c=='x'):
        dash()
        multipleDot(2)
        dash()
      
    
    elif(c=='y'):
        dash()
        dot()
        multipleDash(2)
      
        
    elif(c=='z'):
        multipleDash(2)
        multipleDot(2)
    else:
        print("Invalid character for a name")
        

def Name(v):
    for i in v:
        morseCode(i);
        char();


win=Tk()
win.title("Morse Code")
myFont=tkFont.Font(family = 'Comic Sans MS', size = 15, weight ="bold")
ledCode='';
def ledShow():
    ledCode = code.get()
    print("LED code: ", ledCode) 
    Name(ledCode.lower())

    
def close(): 
    GPIO.cleanup()
    win.destroy()
### WIDGETS ###
ledButton = Button(win, text='Enter your name', font=myFont,command=ledShow, bg='yellow', height=1)
ledButton.grid(row=0,column=1)
code = Entry(win, font=myFont, width=12)
code.grid(row=0,column=0)
exitButton = Button(win, text='Exit', font=myFont, command=close,bg='red', height=1, width=6)
exitButton.grid(row=3,column=1, sticky=E)


win.protocol("WM_DELETE_WINDOW", close) 
win.mainloop()
