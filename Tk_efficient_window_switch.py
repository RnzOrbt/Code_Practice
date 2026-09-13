import tkinter as hotdog
window= hotdog.Tk()

window.title (" Window Frame")
window.geometry("400x300")

page1=hotdog.Frame(window)
page2=hotdog.Frame(window)

def Window_page1():
    page2.grid_forget()
    page1.grid(row=0, column=0)
    
def Window_page2():
    page1.grid_forget()
    page2.grid(row=0, column=0)



hotdog.Label(page1, text="Input a number: ").grid(row=0, column=0)
hotdog.Entry(page1).grid(row=0, column=1)
hotdog.Button(page1,text="Submit", command=Window_page2).grid(row=1, column=1)

hotdog.Label(page2, text="This is a Number!").grid(row=1, column=0)
hotdog.Button(page2, text="Back", command=Window_page1).grid(row=1, column=1)

page1.grid(row=0, column=0)


window.mainloop()