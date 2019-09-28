import pyautogui as pgi
from tkinter import *

def uptopower():
    pgi.moveTo(34,1066,1)
    pgi.click()
    pgi.moveTo(30,995,1)
    pgi.click()

def sbutton():
    uptopower()
    pgi.moveTo(42,894,1)
    pgi.click()
    pgi.click()

def restart():
    uptopower()
    pgi.moveTo(30,935,1)
    pgi.click()
    pgi.click()

def sleep():
    uptopower()
    pgi.moveTo(51,852,1)
    pgi.click()
    pgi.click()

#ch=input("Enter ur choice \n1.Shutdown\n2.Restart\n3.Sleep")
root=Tk()
root.geometry("300x200")

b1=Button(root,text='Shutdown',command=sbutton)
b1.grid(row=0,column=0)

b2=Button(root,text='Restart',command=restart)
b2.grid(row=1,column=0)

b3=Button(root,text='Sleep',command=sleep)
b3.grid(row=2,column=0)


root.mainloop()
#if ch=='1':
#uptopower()
#pgi.moveTo(42,894,1)
#shutdown
#elif ch=='2':
#uptopower()
#pgi.moveTo(30,935,1)
#restart
#elif ch=='3':
#uptopower()
#pgi.moveTo(51,852,1)
#sleep
#else:
#print("Invalid choice")
