# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
import re

currentline = 0.0


class LexerGUI:  # class def

    # init function
    def __init__(self, root):
        # master parent obj

        self.master = root
        # title of window
        self.master.title("Lexer Tinypie")
        # frame widget
        self.mainframe = Frame(self.master, width=2000,height=2000, bg= '#D4EEE3')
        self.mainframe.pack()
        self.leftframe = Frame(self.mainframe, width=500, height=500, bg='light blue')
        self.leftframe.grid(row=1, column=0, padx=10, pady=5)

        self.rightframe = Frame(self.mainframe, width=500, height=500, bg='light blue')
        self.rightframe.grid(row=1, column=1, padx=10, pady=5, sticky=N)


        # variables
        global currentline
        self.linecounter = StringVar()
        self.linecounter.set("0")
        lines =''
        linelist = []
        #obj
        self.tokenss = Lexer()


        # lefthand side of gui
        # label1 : source code
        self.labelsrcin = Label(self.leftframe, text="Source Code:", bg='light blue')
        self.labelsrcin.grid(row=0, column=0, sticky=W)

        # input text box multiline for label1
        self.textinput = Text(self.leftframe, width=40, height=30)
        self.textinput.grid(row=1, column=0, pady=5, columnspan=2)

        # label2: processing line
        self.labelcurrentline = Label(self.leftframe, text="Current Processing Line:", bg='light blue')
        self.labelcurrentline.grid(row=2, column=0, sticky=W)

        # entry text box for current line dispaly
        self.entrylinecount = Entry(self.leftframe, width=5, textvariable=self.linecounter, relief='sunken')
        self.entrylinecount.grid(row=2, column=1, sticky=E,pady=5, padx=5)
        self.entrylinecount['state'] = 'disabled'

        # button1: next line button
        self.buttonnext = Button(self.leftframe, text="Next Line", command=self.nextline)
        self.buttonnext.grid(row=3, column=1, sticky=E,pady=(0,10), padx=5)

        ##righthand side
        # label3 : result for
        self.labelresult = Label(self.rightframe, text="Tokens", bg='light blue')
        self.labelresult.grid(row=0, column=0, sticky=W)
        # text box output multiline for label3
        self.outputbox = Text(self.rightframe, width=40, height=30)
        self.outputbox.grid(row=1, column=0, columnspan=2, sticky=W, pady=(5,32))
        #button2: quit button
        self.buttonnext = Button(self.rightframe, text="Quit", command=self.quit)
        self.buttonnext.grid(row=3, column=1, sticky=SE,pady=(0,10), padx=5)

    def highlight(self,currentline):
        self.textinput.tag_add("highlight", currentline+1, "{}+1lines".format(currentline+1))
        self.textinput.tag_config("highlight", background='#badfda')

    def removehighlight(self,):

        self.textinput.tag_delete("highlight")

    def quit(self):
        self.master.destroy()

    def nextline(self):
        global currentline
        # linetxt.set(self.inputbox.get(currentline+1, "1.0 lineend"))
        #remove prev highlight
        self.removehighlight()
        #get all text as list
        self.alltxt = self.textinput.get('1.0', 'end-1c').split("\n")
        #exit function if current line is bigger than input so we dont get error
        if currentline >= len(self.alltxt):
            return

        self.highlight(currentline)     #highlight current line we are working on

        line = self.alltxt[int(currentline)]   #make line = to element in alltxt arr
        linelist = self.tokenss.cut_one_line_tokens(line)       #linelist is token list for line

        #to help me count see whihc tokens belong to which line bc i get confused#self.outputbox.insert("end", "Line " + str(int(currentline)+1) + "\n")

        for i in range(len(linelist)):      #print all tokens for line
            self.outputbox.insert("end", linelist[i] + '\n')
        currentline = currentline + 1

        self.linecounter.set(str(int(currentline)))
        print(linelist)
        print(currentline)
        self.tokenss.output_list.clear()


class Lexer:
    def __init__(self):
        # output list
        self.output_list = []

    def cut_one_line_tokens(self, line):
        # loop until find all self.token
        for i in line:
            # Check for int literals
            match = re.match(r"\d+", line)
            if match:
                token = match.group()
                self.output_list.append(("<lit," + token + ">"))
                line = line[match.end():].strip()
                continue

            # Check for float literals
            match = re.match(r"\d+\.\d+", line)
            if match:
                token = match.group()
                self.output_list.append(("<lit," + token + ">"))
                line = line[match.end():].strip()
                continue

            # Check for string literals
            match = re.match(r"\".+\"", line)
            if match:
                token = match.group()
                self.output_list.append(("<lit," + token + ">"))
                line = line[match.end():].strip()
                continue
            # Check keyword
            match = re.match(r"if|else|int|float", line)
            if match:
                token = match.group()
                self.output_list.append(("<key," + token + ">"))
                line = line[match.end():].strip()
                continue
            # Check for operators
            match = re.match(r"=|\+|>|\*", line)
            if match:
                token = match.group()
                self.output_list.append(("<op," + token + ">"))
                line = line[match.end():].strip()
                continue

            # Check for separators
            match = re.match(r"\(|\)|:|\"|;", line)
            if match:
                token = match.group()
                self.output_list.append(("<sep," + token + ">"))
                line = line[match.end():].strip()
                continue

            # Check for identifiers
            match = re.match(r"[a-zA-Z]+[0-9]*", line)
            if match:
                token = match.group()
                self.output_list.append(("<id," + token + ">"))
                line = line[match.end():].strip()
                continue

        print(self.output_list)
        return self.output_list
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = LexerGUI(myTkRoot)
    myTkRoot.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
