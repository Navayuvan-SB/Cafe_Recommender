from tkinter import filedialog
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import pandas as pd
import xlrd

class GUI:

	def __init__(self):

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

		self.Update_cafe_btn = Button(self.Update_cafe_frame, text="Update Cafe Data", bg="red", fg="white", width=20, height=3)
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


start = GUI()
start.mw.mainloop()
