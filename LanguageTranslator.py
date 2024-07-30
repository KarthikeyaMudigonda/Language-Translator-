from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
# pip install googletrans==3.1.0a0

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text = msg, src = s, dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("Language Translator")
root.geometry("800x800")
root.config(bg='black')

lab_txt=Label(root,text=" Language Translator",font=("Time New Roman",20,"bold"),bg="dark grey")
lab_txt.place(x=230,y=40,height=100,width=350)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source text",font=("Time New Roman",20,"bold"),fg="red",bg="black")
lab_txt.place(x=250,y=160,height=30,width =300)

Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=170,y=210,height=100,width=480)


list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text,font=("Time New Roman",13,"bold"))
comb_sor.place(x=170,y=320,height=40,width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate ",relief=RAISED,command=data,bg="dark grey", font=("Time New Roman",13,"bold"))
button_change.place(x=335,y=320,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text,font=("Time New Roman",13,"bold"))
comb_dest.place(x=500,y=320,height=40,width=150)
comb_dest.set("English")


lab_txt=Label(root,text="Translated text",font=("Time New Roman",20,"bold"),fg="red",bg="black")
lab_txt.place(x=250,y=400,height=30,width =300)


dest_txt = Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
dest_txt.place(x=170,y=450,height=100,width=480)


root.mainloop()