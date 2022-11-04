from tkinter import *
from tkinter import messagebox
import random

root =Tk()
root.title("Hello")
root.geometry("300x300")
root.configure(bg="sky blue")

list1 = ["hello","bye" ,"Read","Color","sky","anaconda"]
dic1 = {"plant":"lemon" , "flower":"lotus","paint":"red","pen":"saino softek"}

try:
    ran = random.randint(1,10)
    print(list1[ran])
    print(dic1["plant"])
except IndexError:
    messagebox.showinfo("Invalid Code!","The index value is not present in the list")
    
except KeyError:
    messagebox.showinfo("Invalid Code!","The Key is not present in the the Dictionary")
    
root.mainloop()