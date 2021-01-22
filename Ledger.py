from tkinter import *

window = Tk()
window.title('Transactions')

fr1 = Frame(window)
fr1.pack()

fr2 = Frame(window)
fr2.pack()


l1 = Label(fr1,text='Name :   ')
l1.pack(side='left')

e1 = Entry(fr1,width=20)
e1.pack(side='right')

l2 = Label(fr2,text='Amount :')
l2.pack(side='left')

e2 = Entry(fr2,width=20)
e2.pack(side='right')

def submit():
    n = e1.get()
    p = e2.get()
    f = open('C:\\Users\shanw\Desktop\File.txt','a+')
    f.write(f'{p}Rs given to {n}\n')
    f.close()

def check():
    f = open('C:\\Users\shanw\Desktop\File.txt', 'r')
    r = f.read()
    print(f'{r}')
    f.close()

    e1.delete(0,END)
    e2.delete(0,END)


bu1 = Button(window,text = 'Save',command=submit)
bu1.pack()

bu2 = Button(window,text = 'Check',command=check)
bu2.pack()

window.mainloop()