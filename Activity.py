from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("Text editer")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)


# funtion to open a file
def openfile():
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    # if a file is open display the content of the file
    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"Text editor {filepath} ")


# funtion to savr a file
def savefile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    # if a file is open display the content of the file
    with open(filepath,"w") as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(Text)
    window.title(f"Text editor {filepath} ")
txt_edit=Text(window)
frame=Frame(window,relief=RAISED,bd=2)
button_open=Button(frame,text="open",command=openfile)
button_save=Button(frame,text="save",command=savefile)
button_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
button_save.grid(row=1,column=0,sticky="ew",padx=5)
frame.grid(row=0,column=0) 
txt_edit.grid(row=0,column=1)
window.mainloop()