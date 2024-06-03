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
        ###master window
        self.master = root
        #title of window
        self.master.title("Lexer Tinypie")
        ###frame widgets
        #main frame for window
        self.mainframe = Frame(self.master, width=2000,height=2000, bg= '#D4EEE3')
        self.mainframe.pack()

        #left frame
        self.leftframe = Frame(self.mainframe, width=500, height=500, bg='light blue')
        self.leftframe.grid(row=1, column=0, padx=10, pady=5)

        #midframe
        self.midframe = Frame(self.mainframe, width=500, height=500, bg='light blue')
        self.midframe.grid(row=1, column=1, padx=10, pady=5, sticky=N)

        #rightframe
        self.rightframe = Frame(self.mainframe, width=500, height=500, bg='light blue')
        self.rightframe.grid(row=1, column=2, padx=10, pady=5, sticky=N)

        ###variables
        global currentline #counter for current processing line and  index of line in list
        self.linecounter = StringVar() #counts line for gui box display current process line
        self.linecounter.set("0") #init to zero so when press next line it increasesto 1
        #obj
        self.tokenss = Lexer() #declare lexer obj to access functions using buttons in gui
        ###widgets
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

        ##middle widgets
        # label3 : result for tokens list
        self.labeltokens = Label(self.midframe, text="Tokens", bg='light blue')
        self.labeltokens.grid(row=0, column=0, sticky=W)
        # text box output multiline for label3
        self.texttokenbox = Text(self.midframe, width=30, height=30)
        self.texttokenbox.grid(row=1, column=0, columnspan=2, sticky=W, pady=(5,70))
        #button2: quit button
        self.buttonnext = Button(self.rightframe, text="Quit", command=self.quit)
        self.buttonnext.grid(row=3, column=1, sticky=SE,pady=(0,10), padx=5)
        ##righthand widgets
        #label4: parse tree
        self.labelparse = Label(self.rightframe, text="Parse Tree", bg='light blue')
        self.labelparse.grid(row=0, column=0, sticky=W)
        self.textparsebox= Text(self.rightframe, width=50, height=30)
        self.textparsebox.grid(row=1, column=0, columnspan=2, sticky=W, pady=(5, 32))

    def highlight(self,currentline): #add highlight
        self.textinput.tag_add("highlight", currentline+1, "{}+1lines".format(currentline+1)) #tag highlight
        self.textinput.tag_config("highlight", background='#badfda') #config tag to bg color as highlight

    def removehighlight(self,):
        self.textinput.tag_delete("highlight") #delete tag and remove config

    def quit(self): #quits prgrm
        self.master.destroy()

    def nextline(self):
        global currentline
        #remove prev highlight
        self.removehighlight()
        #get all text as list split by new line char
        self.alltxt = self.textinput.get('1.0', 'end-1c').split("\n")
        #exit function if current line is bigger than input so we dont get error
        if currentline >= len(self.alltxt): #if current line is less than length of list, end of txt reached
            return
        self.highlight(currentline)     #highlight current line we are working on

        line = self.alltxt[int(currentline)]   #make line = to element in alltxt arr
        linelist = self.tokenss.cut_one_line_tokens(line)       #linelist is token list for line

        for i in range(len(linelist)):      #print all tokens for line
            self.texttokenbox.insert("end", linelist[i] + '\n')

        currentline = currentline + 1 #increment currline by 1

        self.linecounter.set(str(int(currentline))) #set lincounter box to currentline
       # print(linelist) #print linelist in console
        print(currentline) #print line num in console
        self.tokenss.parser()
        self.textparsebox.insert("end" , "####Parse Tree: Line " + str(int(currentline)) +"####\n")
        for i in range(len(self.tokenss.tree_list)):
            self.textparsebox.insert("end", self.tokenss.tree_list[i] + '\n')
        self.tokenss.output_list.clear() #clear token list so we can get new list from nxt line
        self.tokenss.parse_list.clear()
        self.tokenss.tree_list.clear()

class Lexer:
    def __init__(self):
        # output list
        self.output_list = []
        self.parse_list=[]
        self.inToken = ("empty", "empty")
        self.typeT, self.tokenp = self.inToken
        self.tree_list = []
    ###LEXER##
    def cut_one_line_tokens(self, line):
        # loop until find all self.token
        for i in line:
            # Check for float literals
            match = re.match(r"\d+\.\d+", line)
            if match:
                token = match.group()
                self.output_list.append(("<float," + token + ">"))
                self.parse_list.append(("float", token))
                line = line[match.end():].strip()
                continue
            # Check for int literals
            match = re.match(r"\d+", line)
            if match:
                token = match.group()
                self.output_list.append(("<int," + token + ">"))
                self.parse_list.append(("int",token))
                line = line[match.end():].strip()
                continue
            # Check for string literals
            match = re.match(r"\".+\"", line)
            if match:
                token = match.group()
                self.output_list.append(("<lit," + token + ">"))
                self.parse_list.append(("lit", token))
                line = line[match.end():].strip()
                continue
            # Check keyword
            match = re.match(r"if|else|int|float", line)
            if match:
                token = match.group()
                self.output_list.append(("<key," + token + ">"))
                self.parse_list.append(("key", token))
                line = line[match.end():].strip()
                continue
            # Check for operators
            match = re.match(r"=|\+|>|\*", line)
            if match:
                token = match.group()
                self.output_list.append(("<op," + token + ">"))
                self.parse_list.append(("op", token))
                line = line[match.end():].strip()
                continue
            # Check for separators
            match = re.match(r"\(|\)|:|\"|;", line)
            if match:
                token = match.group()
                self.output_list.append(("<sep," + token + ">"))
                self.parse_list.append(("sep", token))
                line = line[match.end():].strip()
                continue
            # Check for identifiers
            match = re.match(r"[a-zA-Z]+[0-9]*", line)
            if match:
                token = match.group()
                self.output_list.append(("<id," + token + ">"))
                self.parse_list.append(("id", token))
                line = line[match.end():].strip()
                continue

        #print(self.output_list)
        print(self.parse_list)
        return self.output_list
    #PARSER#########################
    def accept_token(self):
        print(" accept token from the list:" + self.inToken[1])
        self.tree_list.append(" accept token from the list:" + self.inToken[1])
        if len(self.parse_list) != 0:
            self.inToken = self.parse_list.pop(0)

    def exp(self):
        print("\n----parent node exp, finding children nodes:")
        self.tree_list.append("\n----parent node exp, finding children nodes:")
        self.typeT, self.tokenp = self.inToken
        if(self.typeT == "key"):
            print("child node (internal): keyword")
            self.tree_list.append("child node (internal): keyword")
            print("   keyword has child node (token):" + self.tokenp)
            self.tree_list.append("   keyword has child node (token):" + self.tokenp)
            self.accept_token()
        else:
            print("expect keyword as the 1st element of the expression!\n")
            self.tree_list.append("expect keyword as the 1st element of the expression!\n")
            return
        self.typeT, self.tokenp = self.inToken
        if(self.typeT == "id"):
            print("child node (internal): identifier")
            self.tree_list.append("child node (internal): identifier")
            print("   identifier has child node (token):" + self.tokenp)
            self.tree_list.append("   identifier has child node (token):" + self.tokenp)
            self.accept_token()
        else:
            print("expect identifier as the 2nd element of the expression!\n")
            self.tree_list.append("expect identifier as the 2nd element of the expression!\n")
            return
        self.typeT, self.tokenp = self.inToken
        if(self.inToken[1]=="="):
            print("child node (token):"+self.inToken[1])
            self.tree_list.append("child node (token):"+self.inToken[1])
            self.accept_token()
        else:
            print("expect = as the 3rd element of the expression!")
            self.tree_list.append("expect = as the 3rd element of the expression!")
            return

        print("Child node (internal): math")
        self.tree_list.append("Child node (internal): math")
        self.math()

    def math(self):
        print("\n----parent node math, finding children nodes:")
        self.tree_list.append("\n----parent node math, finding children nodes:")
        print("child node (internal): multi")
        self.tree_list.append("child node (internal): multi")
        self.multi()
        #print("\n----parent node math, finding children nodes:")
        if(self.inToken[1] == "+"):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
        print("child node (internal): multi")
        self.tree_list.append("child node (internal): multi")
        self.multi()
    def multi(self):
        print("\n----parent node multi, finding children nodes:")
        self.tree_list.append("\n----parent node multi, finding children nodes:")
        if (self.inToken[0] == "float"):
            print("child node (internal): float")
            self.tree_list.append("child node (internal): float")
            print("   float has child node (token):" + self.inToken[1])
            self.tree_list.append("   float has child node (token):" + self.inToken[1])
            self.accept_token()
        elif (self.inToken[0] == "int"):
            print("child node (internal): int")
            self.tree_list.append("child node (internal): int")
            print("   int has child node (token):" + self.inToken[1])
            self.tree_list.append("   int has child node (token):" + self.inToken[1])
            self.accept_token()
            if (self.inToken[1] == '*'):
                print("child node (token):" + self.inToken[1])
                self.tree_list.append("child node (token):" + self.inToken[1])
                self.accept_token()
            print("child node (internal): multi")
            self.tree_list.append("child node (internal): multi")
            self.multi()

    def if_exp(self):
        #if_exp -> if ( comparison_exp ) :
        print("\n----parent node if_exp, finding children nodes:")
        self.tree_list.append("\n----parent node if_exp, finding children nodes:")
        self.typeT, self.tokenp = self.inToken
        if (self.typeT == "key"):
            print("child node (internal): keyword")
            self.tree_list.append("child node (internal): keyword")
            print("   identifier has child node (token):" + self.tokenp)
            self.tree_list.append("   identifier has child node (token):" + self.tokenp)
            self.accept_token()
        else:
            print("expect identifier as the first element of the expression!\n")
            self.tree_list.append("expect identifier as the first element of the expression!\n")
            return
        self.typeT, self.tokenp = self.inToken

        if (self.inToken[1] == '('):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
        else:
            print("expect ( as the second element of the expression!")
            self.tree_list.append("expect ( as the second element of the expression!")
            return
        print("Child node (internal): comparison_exp")
        self.tree_list.append("Child node (internal): comparison_exp")
        self.comparison_exp()
        if (self.inToken[1] == ')'):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
        if (self.inToken[1] == ':'):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
            print("\nparse tree building success!")
            self.tree_list.append("\nparse tree building success!")
            return


    def comparison_exp(self):
        print("\n----parent node comparison_exp, finding children nodes:")
        self.tree_list.append("\n----parent node comparison_exp, finding children nodes:")
        if (self.inToken[0] == 'id'):
            print("child node (internal): identifier")
            self.tree_list.append("child node (internal): identifier")
            print("   identifier has child node (token):" + self.inToken[1])
            self.tree_list.append("   identifier has child node (token):" + self.inToken[1])
            self.accept_token()
        if (self.inToken[1] == '>'):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
        if (self.inToken[0] == 'id'):
            print("child node (internal): identifier")
            self.tree_list.append("child node (internal): identifier")
            print("   identifier has child node (token):" + self.inToken[1])
            self.tree_list.append("   identifier has child node (token):" + self.inToken[1])
            self.accept_token()
    def print_exp(self):
        print("\n----parent node print_exp finding children nodes:")
        self.tree_list.append("\n----parent node print_exp finding children nodes:")
        self.typeT, self.tokenp = self.inToken
        if (self.typeT == "id"):
            print("child node (internal): identifier")
            self.tree_list.append("child node (internal): identifier")
            print("   identifier has child node (token):" + self.tokenp)
            self.tree_list.append("   identifier has child node (token):" + self.tokenp)
            self.accept_token()
        else:
            print("expect identifier as the first element of the expression!\n")
            self.tree_list.append("expect identifier as the first element of the expression!\n")
            return
        self.typeT, self.tokenp = self.inToken
        if (self.inToken[1] == '('):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
        self.typeT, self.tokenp = self.inToken
        if (self.inToken[0] == "lit"):
            print("child node (internal): string literal")
            self.tree_list.append("child node (internal): string literal")
            print("   string literal has child node (token):" + self.tokenp)
            self.tree_list.append("   string literal has child node (token):" + self.tokenp)
            self.accept_token()
        if (self.inToken[1] == ')'):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()
        if (self.inToken[1] == ';'):
            print("child node (token):" + self.inToken[1])
            self.tree_list.append("child node (token):" + self.inToken[1])
            self.accept_token()


    def parser(self):
        global currentline
        self.inToken = self.parse_list.pop(0)
        if currentline == 1.0:
            self.exp()
            if (self.inToken[1] == ";"):
                print("\nparse tree building success!")
                self.tree_list.append("\nparse tree building success!")
        if currentline == 2.0:
            self.exp()
            if (self.inToken[1] == ";"):
                print("\nparse tree building success!")
                self.tree_list.append("\nparse tree building success!")
        if currentline == 3.0:
            self.if_exp()
        if currentline == 4.0:
            self.print_exp()
            if (self.inToken[1] == ";"):
                print("\nparse tree building success!")
                self.tree_list.append("\nparse tree building success!")
        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = LexerGUI(myTkRoot)
    myTkRoot.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
