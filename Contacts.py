from tkinter import *
window = Tk()
window.title('Contacts')


fr1 = Frame(window)
fr1.pack()

fr2 = Frame(window)
fr2.pack()

dict = {}

def add():
    window = Tk()
    window.title('New Contact')

    fr1 = Frame(window)
    fr1.pack()

    fr2 = Frame(window)
    fr2.pack()

    l1 = Label(fr1, text='Name :   ')
    l1.pack(side='left')

    e1 = Entry(fr1, width=20)
    e1.pack(side='right')

    l2 = Label(fr2, text='Number :')
    l2.pack(side='left')

    e2 = Entry(fr2, width=20)
    e2.pack(side='right')

    def addnew():
        a = e1.get()
        b = e2.get()
        dict[a] = b
        e1.delete(0,END)
        e2.delete(0,END)


    bu1 = Button(window,text = 'Save',command=addnew)
    bu1.pack()
    window.mainloop()

def search():
    window = Tk()
    window.title('Search Contact')

    fr1 = Frame(window)
    fr1.pack()

    l1 = Label(fr1, text='Name :   ')
    l1.pack(side='left')

    e1 = Entry(fr1, width=20)
    e1.pack(side='right')


    def searchcontact():
        a = e1.get()
        b = dict.keys()
        if( a in b):
            print(dict[a])
        else:
            print("No contact found")
        e1.delete(0,END)


    bu1 = Button(window, text='Search', command=searchcontact)
    bu1.pack()
    window.mainloop()



bu1 = Button(window,text = 'Add New',command=add)
bu1.pack()

bu2 = Button(window,text = 'Search',command=search)
bu2.pack()


window.mainloop()