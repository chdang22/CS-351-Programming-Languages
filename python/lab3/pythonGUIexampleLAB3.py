#This is an example of using the tkinter python extension to create a basic window with button

from tkinter import *
from tkinter import messagebox

class CatDatabase: #class def for cat database
    #init list to carry tuple
    def __init__(self):
        self.kittylistty = []

    #add kitty to kittylistty
    def add_cat(self, catinfo):
        self.kittylistty.append(catinfo)

    #print the database (kitty litty)
    def print_cat_database(self):
        print("~uwu~"*3)
        print("My Kitty Litty (Litter Registration)")
        print("~uwu~"*3)
        print("Cat Name", "Cat ID")
        for i in self.kittylistty:
            print(i[0] + ',' + '{:0>4}'.format(i[1]))


class MyFirstGUI: #class definition

    #This is the initialize function for a class.
    #Variables belonging to this class will get created and initialized in this function
    #What is the self parameter? It represents this class itself.
    #By using self.functionname, you can call functions belonging to this class.
    #By using self.variablename, you can create and use variables belonging to this class.
    #It needs to be the first parameter of all the functions in your class

    def __init__(self, root):
        #added
        self.id = StringVar()
        self.name = StringVar()
        self.database = CatDatabase()
        #Master is the default prarent object of all widgets.
        #You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("My Cat Registration System")


        #grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        #it will make self.label=none and you will no longer be able to change the label's content

        #cat name label and entry box
        self.labelname = Label(self.master, text="Cat Name: ")
        self.labelname.grid(row=0,column=0,sticky=E)

        self.catnameentry = Entry(self.master, bg = "#d8f0e3")
        self.catnameentry.grid(row=0, column=1, sticky =E)

        #id lbl and entry box
        self.labelID = Label(self.master, text="Cat ID: ")
        self.labelID.grid(row=0, column=2, sticky=E)

        self.catIDentry = Entry(self.master, bg = "#c7ebe0")
        self.catIDentry.grid(row=0, column=3, sticky = E)

        #submit bttn
        self.submitbutton = Button (self.master, text="Submit name", command=self.submitname)
        self.submitbutton.grid(row=0, column=4, sticky=E)

        #registered name lbl and output entry box

        self.labelregname = Label(self.master, text = "Registered Name")
        self.labelregname.grid(row = 1, column = 0, sticky = E)

        self.regname = Entry(self.master, text="", textvariable = self.name)
        self.regname.grid(row=1, column=1, sticky=E)
        self.regname['state'] = 'disabled'  #to make entry box uneditable by user (grayed out)

        #registered name lbl and output entry box
        self.labelregID = Label(self.master, text="Registered ID")
        self.labelregID .grid(row=1, column=2, sticky=E)

        self.regID  = Entry(self.master, text="", textvariable=self.id)
        self.regID.grid(row=1, column=3, sticky=E)
        self.regID['state'] = 'disabled'


        self.printdatabasebutton = Button(self.master, text = "Print database", command = self.printdatabase)
        self.printdatabasebutton.grid(row=1, column=4, sticky=E)


    def submitname (self):
        if not self.catnameentry.get() == "" and not self.catIDentry.get() == "":
            self.name.set(self.catnameentry.get())
            self.id.set(self.catIDentry.get())
            print ("a cat name submitted: ", self.catnameentry.get())
            self.database.add_cat((self.catnameentry.get(), self.catIDentry.get()))
        else:
            print("ERROR: Please filll out all fields :3")
            messagebox.showerror(title = "ERROR", message= "Fill out both fields >:3")


    def printdatabase(self):
        self.database.print_cat_database()
if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()

