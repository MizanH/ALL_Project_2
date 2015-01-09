import Tkinter
import tkMessageBox
window = Tkinter.Tk()
window.wm_withdraw()

class messageBox():
    def __init__(self, message, name):
        self.message = message
        self.name = name 

    def displayInfo(self):
        tkMessageBox.showinfo(title=self.name,message=self.message)

BigBen = messageBox("This is Big Ben!", "Big Ben")
BigBen.displayInfo()
