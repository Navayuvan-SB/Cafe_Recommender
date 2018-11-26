
from tkinter import filedialog
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import xlrd

mw = tkinter.Tk()


mw.title("Cafe")


mw.geometry("1200x800")



mw.resizable(0,0)



def load_cafe_data():
    
    global cafe_l
    cafe_l=()
    file_path = filedialog.askopenfilename()
    loc = (file_path)
    
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range (1,sheet.nrows):
        s = sheet.cell_value(i, 0)
        cafe_l = cafe_l + (s,)
    cb['values'] = cafe_l


def cbget(event):
    global cb_value
    cb_value=cb.get()


def addbtn():
    tree.insert('','end',text=cb_value, values=(str(scale.get())))



def removebtn():
    selected = tree.selection()[0]
    tree.delete(selected)


frame1 = Frame(mw, bg="#00e673", width=1200, height=120, highlightbackground="black", highlightcolor="black", highlightthickness=1)
frame1.grid(row=0,column=0,columnspan=3)



frame2 = Frame(mw, bg="#00e673", width=1200, height=120, highlightbackground="black", highlightcolor="black", highlightthickness=1)
frame2.grid(row=1,column=0,columnspan=3)


frame3 = Frame(mw, bg="yellow", width=1200, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
frame3.grid(row=2,column=0,columnspan=3)


frame4 = Frame(frame3, bg="#00e673", width=80, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
frame4.grid(row=0,column=0,columnspan=1)
frame5 = Frame(frame3, bg="#00e673", width=560, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
frame5.grid(row=0,column=1,columnspan=1)
frame6 = Frame(frame3, bg="#00e673", width=560, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
frame6.grid(row=0,column=2,columnspan=1)



frame1.grid_propagate(0)
cafe_l = Label(frame1,fg="red",text="CAFE RECOMMENDER",bg="#00e673")
cafe_l.config(font=("courier", 32))
cafe_l.place(x=600,y=56, anchor="center")



frame2.grid_propagate(0)
update_cafe = Button(frame2, text="Update Cafe Data", bg="red", fg="white", width=20, height=3,command = load_cafe_data)
update_cafe.config(font=("courier", 12))
update_cafe.place(x=360, y=56, anchor="center")
print(cafe_l)



upload_ratings = Button(frame2, text="Upload Ratings", bg="red", fg="white", width=20, height=3)
upload_ratings.config(font=("courier", 12))
upload_ratings.place(x=930, y=56, anchor="center")


frame4.grid_propagate(0)
rating = Button(frame4,bg="red",fg="white",width=4,height=11,text="RATING")
rating.place(x=40,y=100,anchor="center")



recommend = Button(frame4,bg="red",fg="white",width=4,height=11,text="RECOMMEND")
recommend.place(x=40,y=420,anchor="center")



frame5.grid_propagate(0)
choose_cafe = Label(frame5, bg="#00e673", fg="black", text="Choose Cafe")
choose_cafe.config(font=("courier", 20, 'bold'))
choose_cafe.place(x=280,y=50,anchor="center")




cb = ttk.Combobox(frame5,state="readonly")
cb.set("select")
cb.bind("<<ComboboxSelected>>",cbget)
cb.place(x=280,y=150,anchor="center")





choose_rating = Label(frame5, bg="#00e673", fg="black", text="Choose Rating")
choose_rating.config(font=("courier", 20, 'bold'))
choose_rating.place(x=280,y=250,anchor="center")




scale = Scale(frame5, from_=0, to=10, orient=HORIZONTAL,length=300)
scale.place(x=280,y=350,anchor="center")





add = Button(frame5, text="ADD", bg="red", fg="white", width=15, height=2,command=addbtn)
add.config(font=("courier", 12))
add.place(x=280, y=450, anchor="center")




frame6.grid_propagate(0)
style = ttk.Style(frame6)
style.configure('Treeview', rowheight=40)
tree = ttk.Treeview(frame6, columns=('Cafe'))
tree.heading('#0',text='Cafe')
tree.heading('#1',text='Rating')
tree.column('#0', stretch=tkinter.YES)
tree.column('#1', stretch=tkinter.YES)
tree.place(x=220,y=250,anchor="center")




remove = Button(frame6, text="REMOVE", bg="red", fg="white", width=8, height=2,command=removebtn)
remove.config(font=("courier", 12))
remove.place(x=500, y=300, anchor="center")



mw.mainloop()

