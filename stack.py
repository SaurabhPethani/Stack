from tkinter import *

stack = []

def pushItem(event):
    global stack, entry, status
    value = entry.get()
    print(type(value))
    if value == '':
        pass
    else:
        stack[0:0] = [value]
        print(stack)
        print(value)
        entry.delete(0, END)
        ta.delete(1.0, END)
        ta.insert(END, stack)
        status['text'] = "Pushed "+value

def popItem(event):
    global stack, ta, status
    if stack == []:
        status['text'] = 'Stack Is Empty'
    else:
        value = stack[0]
        del stack[0]
        ta.delete(1.0 , END)
        ta.insert(END, stack)
        status['text'] = "Poped "+value

root = Tk()
root.title("Stack")
root.geometry("400x400")
Label(root, text="STACK").pack(side="top")

ta = Text(root, width=20, height=10)
ta.pack(side="top")
ta.insert(END, "STACK IS HERE")


frame = Frame(root)
frame.pack(side="top")

push = Button(frame, text="PUSH")
push.pack(side="left")
push.bind("<Button>",pushItem, )
entry = Entry(frame)
entry.pack(side="left")
pop = Button(frame, text="POP")
pop.pack(side="left")
pop.bind("<Button>", popItem)

status = Label(root, text="Stack empty")
status.pack(side="top")


root.mainloop()