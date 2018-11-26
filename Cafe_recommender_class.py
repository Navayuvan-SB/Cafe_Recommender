from tkinter import filedialog
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import xlrd

class Action():

	def __init__(self):
		#global GUI
		#self.GUI = GUI()
		print("")

	def cbget(self,event):
	    global cb_value
	    self.cb_value=self.cb.get()


	def addbtn(self):
	    self.tree.insert('','end',text=self.cb_value, values=(str(self.scale.get())))


	def removebtn(self):
	    selected = self.tree.selection()[0]
	    self.tree.delete(selected)

	def load_cafe_data(self):
    
	    global cafe_l
	    self.cafe_l=()
	    self.file_path = filedialog.askopenfilename()
	    self.loc = (self.file_path)
	    
	    self.wb = xlrd.open_workbook(self.loc)
	    self.sheet = self.wb.sheet_by_index(0)
	    for self.i in range (1,self.sheet.nrows):
	        self.s = self.sheet.cell_value(self.i, 0)
	        self.cafe_l = self.cafe_l + (self.s,)
	    self.cb['values'] = self.cafe_l





class GUI(Action):

	

	def __init__(self):

		Action.__init__(self)

		"""
		Construction the GUI
		"""
		self.mw = tkinter.Tk()
		self.mw.title("Cafe Recommender 1.0")
		self.mw.geometry("1200x800")
		self.mw.resizable(0,0)

		# Top frame
		self.frame1 = Frame(self.mw, bg="#00e673", width=1200, height=120, highlightbackground="black", highlightcolor="black", highlightthickness=1)
		self.frame1.grid(row=0,column=0,columnspan=3)
		self.frame1.pack_propagate(0)

		# Mid frame
		self.frame2 = Frame(self.mw, bg="#00e673", width=1200, height=120, highlightbackground="black", highlightcolor="black", highlightthickness=1)
		self.frame2.grid(row=1,column=0,columnspan=3) 
		self.frame2.grid_propagate(0)

		# Bottom frame
		self.frame3 = Frame(self.mw, bg="#00e673", width=1200, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
		self.frame3.grid(row=2,column=0,columnspan=3)
		self.frame3.grid_propagate(0)

		# Sub Frames of Frame 3
		self.frame4 = Frame(self.frame3, bg="#00e673", width=80, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
		self.frame4.grid(row=0,column=0,columnspan=1)
		self.frame4.grid_propagate(0)
		self.frame5 = Frame(self.frame3, bg="#00e673", width=560, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
		self.frame5.grid(row=0,column=1,columnspan=1)
		self.frame5.grid_propagate(0)
		self.frame6 = Frame(self.frame3, bg="#00e673", width=560, height=560, highlightbackground="black", highlightcolor="black", highlightthickness=1)
		self.frame6.grid(row=0,column=2,columnspan=1)
		self.frame6.grid_propagate(0)
		
		# Cafe recommender lable on top
		self.cafe_l = Label(self.frame1,fg="red",text="CAFE RECOMMENDER",bg="#00e673")
		self.cafe_l.config(font=("courier", 32))
		self.cafe_l.pack(side=TOP, expand=YES, fill=BOTH)

		# Two Update buttons on Mid
		self.Update_cafe_frame = Frame(self.frame2, bg="#00e673", width=600, height=120)
		self.Update_cafe_frame.grid(row=0,column=0,columnspan=1)

		self.Update_ratings_frame = Frame(self.frame2, bg="#00e673", width=600, height=120)
		self.Update_ratings_frame.grid(row=0,column=1,columnspan=1)

		self.Update_cafe_btn = Button(self.Update_cafe_frame, text="Update Cafe Data", bg="red", fg="white", width=20, height=3,command=self.load_cafe_data)
		self.Update_cafe_frame.pack_propagate(0)
		self.Update_cafe_btn.config(font=("courier", 12))
		self.Update_cafe_btn.pack(side=TOP, expand=YES)

		self.Update_ratings_btn = Button(self.Update_ratings_frame, text="Update rating", bg="red", fg="white", width=20, height=3)
		self.Update_ratings_frame.pack_propagate(0)
		self.Update_ratings_btn.config(font=("courier", 12))
		self.Update_ratings_btn.pack(side=TOP, expand=YES)

		# Rating and Recommend Button 
		self.Rating_frame = Frame(self.frame4, bg="#00e673",width=80,height=280)
		self.Rating_frame.grid(row=0,column=0,rowspan=1)

		self.Recommend_frame = Frame(self.frame4, bg="#00e673",width=80,height=280)
		self.Recommend_frame.grid(row=1,column=0,rowspan=1)		

		self.Rating_btn = Button(self.Rating_frame,bg="red",fg="white",width=4,height=11,text="RATING")
		self.Rating_frame.pack_propagate(0)
		self.Rating_btn.pack(side=TOP,expand=YES)

		self.Recommend_btn = Button(self.Recommend_frame,bg="red",fg="white",width=4,height=11,text="RECOMMEND")
		self.Recommend_frame.pack_propagate(0)
		self.Recommend_btn.pack(side=TOP,expand=YES)

		# Scale widget in Frame 5
		self.Choose_cafe_frame = Frame(self.frame5, bg="#00e673", width=560, height=102)
		self.Choose_cafe_frame.grid(row=0,column=0,columnspan=1)
		self.Choose_cafe_frame.pack_propagate(0)

		self.cb_frame = Frame(self.frame5, bg="#00e673", width=560, height=102)
		self.cb_frame.grid(row=1,column=0,columnspan=1)
		self.cb_frame.pack_propagate(0)

		self.Choose_rating_frame = Frame(self.frame5, bg="#00e673", width=560, height=102)
		self.Choose_rating_frame.grid(row=2,column=0,columnspan=1)
		self.Choose_rating_frame.pack_propagate(0)

		self.Scale_frame = Frame(self.frame5, bg="#00e673", width=560, height=102)
		self.Scale_frame.grid(row=3,column=0,columnspan=1)
		self.Scale_frame.pack_propagate(0)

		self.add_frame = Frame(self.frame5, bg="#00e673", width=560, height=152)
		self.add_frame.grid(row=4,column=0,columnspan=1)
		self.add_frame.pack_propagate(0)


		self.choose_cafe = Label(self.Choose_cafe_frame, bg="#00e673", fg="black", text="Choose Cafe")
		self.choose_cafe.config(font=("courier", 20, 'bold'))
		self.choose_cafe.pack(side=TOP,expand=YES)

		self.cb = ttk.Combobox(self.cb_frame,state="readonly")
		self.cb.set("select")
		self.cb.bind("<<ComboboxSelected>>",self.cbget)
		self.cb.pack(side=TOP,expand=YES)

		self.choose_rating = Label(self.Choose_rating_frame, bg="#00e673", fg="black", text="Choose Rating")
		self.choose_rating.config(font=("courier", 20, 'bold'))
		self.choose_rating.pack(side=TOP,expand=YES)

		self.scale = Scale(self.Scale_frame, from_=0, to=10, orient=HORIZONTAL,length=300)
		self.scale.pack(side=TOP,expand=YES)

		self.add = Button(self.add_frame, text="ADD", bg="red", fg="white", width=15, height=2,command=self.addbtn)
		self.add.config(font=("courier", 12))
		self.add.pack(side=TOP,expand=YES)


		# Treeview and Remove button
		self.Tree_frame = Frame(self.frame6, bg="#00e673", height=560, width=420)
		self.Tree_frame.grid(row=0,column=0,rowspan=1)
		self.Tree_frame.pack_propagate(0)

		self.Remove_frame = Frame(self.frame6, bg="#00e673", height=560, width=140)
		self.Remove_frame.grid(row=0,column=1,rowspan=1)
		self.Remove_frame.pack_propagate(0)		

		self.style = ttk.Style(self.frame6)
		self.style.configure('Treeview', rowheight=40)
		self.tree = ttk.Treeview(self.Tree_frame, columns=('Cafe'))
		self.tree.heading('#0',text='Cafe')
		self.tree.heading('#1',text='Rating')
		self.tree.column('#0', stretch=tkinter.YES)
		self.tree.column('#1', stretch=tkinter.YES)
		self.tree.pack(side=TOP, expand=YES)

		self.remove = Button(self.Remove_frame, text="REMOVE", bg="red", fg="white", width=8, height=2,command=self.removebtn)
		self.remove.config(font=("courier", 12))
		self.remove.pack(side=TOP, expand=YES)


start = GUI()
start.mw.mainloop()
