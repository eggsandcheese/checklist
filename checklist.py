from tkinter import *
class Checklist(Tk):
    def __init__(self):
        super().__init__()
        self.title("Checklist")    
        self.addbutton = Button( text="Add Task", command= self.addtask)
        self.addbutton.pack()
        self.textinput = Entry(width=15)
        self.textinput.pack()
        
    def deletetask(self):
        print("egg")
        self.task.destroy()
        self.deletebutton.destroy()
        print("egg")
    def addtask(self):
        egg = self.textinput.get()
        self.task = Label(text= egg)
        self.task.pack()
        self.deletebutton = Button(text="Delete", command=self.deletetask)
        self.deletebutton.pack()
        self.textinput.delete(0, END)



if __name__ == "__main__":
  checklist = Checklist()
  checklist.mainloop()