# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 15 15:34:39 2022

# @author: Jayesh
# """

# from tkinter import *
# import tkinter as tk
# import time as t
# operation =""
# # main_window = Tk()
# number1 = tk.StringVar(main_window)

# #Text Field
# myentry = Entry(main_window, width = 32, borderwidth= 5, textvariable= number1)
# myentry.grid(row = 0, column = 0,columnspan = 4)

# #Title
# main_window.title("Calculator")

# #Functions
# list_of_numbers = []
# def input_value(number):
#     curr = number1.get()
#     myentry.delete(0,END)
#     myentry.insert(0,curr + number)
    
    
    
# def cls():
#     myentry.delete(0,END)
#     list_of_numbers.clear()
#     SUM = 0
    
    
# def add():
#     curr = number1.get()
#     try:
#         list_of_numbers.append(float(curr))
#     except:
#         myentry.delete(0,END)  
#     myentry.delete(0,END)
#     global operation 
#     operation = "+"
    
# def sub():
#     curr = number1.get()
#     try:
#         list_of_numbers.append(float(curr))
#     except:
#         myentry.delete(0,END) 
#     myentry.delete(0,END)
#     global operation 
#     operation = "-"
 
# def mul():
#     curr = number1.get()
#     try:
#         list_of_numbers.append(float(curr))
#     except:
#         myentry.delete(0,END) 
#     myentry.delete(0,END)
#     global operation 
#     operation = "*"
    
# def divide():
#     curr = number1.get()
#     try:
#         list_of_numbers.append(float(curr))
#     except:
#         myentry.delete(0,END) 
#     myentry.delete(0,END)
#     global operation 
#     operation = "/"


# def equals(operation):
#     list_of_numbers.append(int(number1.get()))
#     SUM =0
#     if operation == "+":
#         for values in list_of_numbers:
#             SUM = SUM + values
#     elif operation == "-":
#         SUM = list_of_numbers[0] - list_of_numbers[1]
#     elif operation == "*":
#         SUM = list_of_numbers[0] * list_of_numbers[1]
#     else:
#         if list_of_numbers[1] == 0:
#             SUM = "Invalid Operation, / by 0"
#         else:
#             SUM = list_of_numbers[0] / list_of_numbers[1]
#     myentry.delete(0,END)
#     list_of_numbers.clear()
#     myentry.insert(0,SUM)

# #Buttons
# Button(main_window,width = 8, text="7",command=lambda : input_value("7")).grid(row = 1, column =0,padx= 2, pady= 2)
# Button(main_window,width = 8, text="8",command=lambda : input_value("8")).grid(row = 1, column =1,padx= 2, pady= 2)
# Button(main_window,width = 8, text="9",command=lambda : input_value("9")).grid(row = 1, column =2,padx= 2, pady= 2)
# Button(main_window,width = 8, text="+",command=add).grid(row = 1, column =3,padx= 2, pady= 2)

# Button(main_window,width = 8, text="4",command=lambda : input_value("4")).grid(row = 2, column =0,padx= 2, pady= 2)
# Button(main_window,width = 8, text="5",command=lambda : input_value("5")).grid(row = 2, column =1,padx= 2, pady= 2)
# Button(main_window,width = 8, text="6",command=lambda : input_value("6")).grid(row = 2, column =2,padx= 2, pady= 2)
# Button(main_window,width = 8, text="-",command=sub).grid(row = 2, column =3,padx= 2, pady= 2)

# Button(main_window,width = 8, text="1",command=lambda : input_value("1")).grid(row = 3, column =0,padx= 2, pady= 2)
# Button(main_window,width = 8, text="2",command=lambda : input_value("2")).grid(row = 3, column =1,padx= 2, pady= 2)
# Button(main_window,width = 8, text="3",command=lambda : input_value("3")).grid(row = 3, column =2,padx= 2, pady= 2)
# Button(main_window,width = 8, text="*",command=mul).grid(row = 3, column =3,padx= 2, pady= 2)

# Button(main_window,width = 8, text="cls",command=cls).grid(row = 4, column =0,padx= 2, pady= 2)
# Button(main_window,width = 8, text="0",command=lambda : input_value("0")).grid(row = 4, column =1,padx= 2, pady= 2)
# Button(main_window,width = 8, text="/",command=divide).grid(row = 4, column =2,padx= 2, pady= 2)
# Button(main_window,width = 8, text="=",command=lambda : equals(operation)).grid(row = 4, column =3,padx= 2, pady= 2)


# main_window.mainloop()