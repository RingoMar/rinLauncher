from tkinter import *
import tkinter as tk
from datetime import datetime as dt
import json


class rinUi():
    def __init__(self):
        self.appMain = Tk()
        self.photoLogo = "src/dwin.png"
        self.leftFrame = Frame(self.appMain, width=200, height= 400, bg='#6f7676')
        self.rightFrame = Frame(self.appMain, width=650, height=400, bg='#6f7676')
        self.toolBar = Frame(self.leftFrame, width=180, height=185, bg='#6f7676')
        self.outputConsole = Text(self.rightFrame, bg="black", fg="green")

    def rinLoadJson(self, name):
        with open(name, "rb") as json_file:
            data = json.load(json_file)
        return data

    def rinSaveJson(self, infile, data):
        with open(infile, 'w') as outfile:
            json.dump(data, outfile, indent=4)
            outfile.close()
        return


    def setInterval(self):
        """ Sets the Interval for sending the facts out """

        self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Opening new window\n")
        intervalPopout = Toplevel(self.appMain)
        intervalPopout.title("Interval Settings")
        intervalPopout.geometry("530x320")
        intervalPopout.resizable(False, False)

        lowerFrame = Frame(intervalPopout, width=300, height= 200, bg='#212121')
        lowerFrame.grid(row=2, column=0, padx=5, pady=5)
        centerFrame = Frame(intervalPopout, width=300, height= 200, bg='#212121')
        centerFrame.grid(row=1, column=0, padx=25, pady=10)

        topLabel = Label(intervalPopout,  fg = "white", bg="#212121", text = " Interal Settings Page").grid(row=0, column=0, padx=5, pady=5)
        lbl = Label(centerFrame,  fg = "white", bg="#212121", text = "Enter time in seconds:")
        lbl.grid()

        txt = Entry(centerFrame, width=27, fg = "white", bg="#1a1a1a",)
        txt.grid(column = 1, row = 0, padx=10, pady=3, ipadx=40)


        def addInterval():
            try:
                getData = int(txt.get())
                if type(getData) == int:
                    self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Setting time to: {txt.get()}\n")
                    fileT = self.rinLoadJson("src/config.json")
                    fileT["interval"] = getData
                    self.rinSaveJson("src/config.json", fileT)
                else:
                    self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Can't set '{txt.get()}' as its not a number!!\n")
            except ValueError:
                self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Can't set '{txt.get()}' as its not a number!!\n")

        def applyExit():
            addInterval()
            intervalPopout.destroy()
            return

        btn = Button(centerFrame, text = "SET NEW TIME" , fg = "white", bg="#1a1a1a", height=1, command=addInterval)
        btn.grid(column=3, row=0)
        applyBut = Button(lowerFrame, text = "APPLY" , fg = "white", bg="#1a1a1a", height=2, command=applyExit)
        exitBut = Button(lowerFrame, text = "CANCEL" , fg = "white", bg="#f15363", height=2, command=intervalPopout.destroy)
        applyBut.grid(column=1, row=0, padx=10, pady=5, sticky='w'+'e'+'n'+'s')
        exitBut.grid(column=2, row=0, padx=10, pady=5, sticky='w'+'e'+'n'+'s')
        intervalPopout.configure(bg='#212121')

    def userAddFact(self):

        """ adds a new quote stright into to file """

        self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Opening new window\n")
        factWindow = Toplevel(self.appMain)
        factWindow.title("Adding Facts")
        factWindow.geometry("530x320")
        factWindow.resizable(False, False)

        lowerFrame = Frame(factWindow, width=300, height= 200, bg='#212121')
        lowerFrame.grid(row=2, column=0, padx=5, pady=5)
        centerFrame = Frame(factWindow, width=300, height= 200, bg='#212121')
        centerFrame.grid(row=1, column=0, padx=25, pady=10)

        topLabel = Label(factWindow,  fg = "white", bg="#212121", text = " Fact Edit Page").grid(row=0, column=0, padx=5, pady=5)
        lbl = Label(centerFrame,  fg = "white", bg="#212121", text = "Enter Fact")
        lbl.grid()

        txt = Entry(centerFrame, width=27, fg = "white", bg="#1a1a1a",)
        txt.grid(column = 1, row = 0, padx=10, pady=3, ipadx=40)


        def addQuote():
            if str(txt.get()) == "":
                self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Cant add a blank quote :p\n")
            else:
                self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Adding quote '{txt.get()}' into file.\n")
                configFile = self.rinLoadJson("src/facts.json")
                configFile["facts"].append(txt.get())
                self.rinSaveJson("src/facts.json", configFile)
                self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Quote added to file.\n")

        def applyExit():
            addQuote()
            factWindow.destroy()
            return

        btn = Button(centerFrame, text = "Add" , fg = "white", bg="#1a1a1a", height=1, command=addQuote)
        btn.grid(column=3, row=0)
        applyBut = Button(lowerFrame, text = "APPLY" , fg = "white", bg="#1a1a1a", height=2, command=applyExit)
        exitBut = Button(lowerFrame, text = "CANCEL" , fg = "white", bg="#f15363", height=2, command=factWindow.destroy)
        applyBut.grid(column=1, row=0, padx=10, pady=5, sticky='w'+'e'+'n'+'s')
        exitBut.grid(column=2, row=0, padx=10, pady=5, sticky='w'+'e'+'n'+'s')
        factWindow.configure(bg='#212121')

    def run(self):

        self.appMain.title("Rin Updater")
        self.appMain.geometry('850x450')
        self.appMain.resizable(False, False)

        # Grid #
        self.leftFrame.grid(row=0, column=0, padx=10, pady=5)
        self.rightFrame.grid(row=0, column=1, padx=10, pady=5)
        self.toolBar.grid(row=2, column=0, padx=5, pady=5)
        # End Grid #

        Label(self.leftFrame, text="DWIN BOT SETTINGS", relief=RAISED).grid(row=0, column=0, padx=5, pady=5)
        image = PhotoImage(file=self.photoLogo)
        logoImage = image.subsample(1,1)
        Label(self.leftFrame, image=logoImage).grid(row=1, column=0, padx=5, pady=5)

        # Console Output Look
        self.outputConsole.grid(row=0, column=0, padx=5, pady=5)
        self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Welcome to Dwin bot 2.0\n")
        self.outputConsole.insert(tk.END, f"[{('{:{tfmt}}'.format(dt.now(), tfmt='%H:%M:%S'))}]> Powered by Rin Engine®\n")

        Label(self.toolBar, text="General", relief=RAISED, fg = "white", bg="#1a1a1a",).grid(row=0, column=0, padx=5, pady=3, ipadx=40)

        Button(self.toolBar, text="SET INTERVAL", command=self.setInterval).grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
        Button(self.toolBar, text="ADD FACT", command=self.userAddFact).grid(row=2, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.appMain.configure(bg='#212121')
        self.appMain.mainloop()
        return

if __name__ == "__main__":
    rinUi().run()