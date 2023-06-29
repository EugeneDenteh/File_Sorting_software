#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image

def browse_button():
    location=filedialog.askdirectory()
    filepath=Label(root,text=location).pack(padx=20,pady=0)
    
    
def extension():
    list_dir = os.listdir(foldername)
    for file_ in list_dir:  
        try:
            name, ext = os.path.splitext(file_)
            ext=ext[1:]
            if ext=='':
                continue 
            if os.path.exists(foldername+'/'+ext):
                shutil.move(foldername+'/'+file_, foldername+'/'+ext+'/'+file_)
            else:
                os.makedirs(foldername+'/'+ext)
                shutil.move(foldername+'/'+file_, foldername+'/'+ext+'/'+file_)
        except:
            pass

def extension():
    import datetime
    list_dir = os.listdir(foldername)

    try:
        for file_ in list_dir:
            file_path = os.path.join(foldername,file_)
            mod= os.path.getmtime(file_path)
            dt_m=datetime.datetime.fromtimestamp(mod).date()
            newfolder_path=os.path.join(foldername,str(dt_m))
            os.makedirs(newfolder_path,exist_ok=True)
            newfile_path=os.path.join(newfolder_path,file_)
            shutil.move(file_path,newfile_path)
    except:
        print('error occured')

root=Tk()
#img =Image.open('1.png')
#bg = ImageTk.PhotoImage(img)
#root.geometry("250x150")
#labelimage = Label(root, image=bg)
#labelimage.place(x = 0,y = 0)
#root.config(background = "white")
root.title("SORTED")

label=tk.Label(root,text="Mr.Sorted v1.0",font=('Arial',18))
label.pack(padx=20,pady=20)

browse=ttk.Button(root,text="Browse",command=browse_button)
browse.pack(padx=0,pady=0)

extension=ttk.Button(root,text="Sort by file extension",command=extension)
extension.pack(padx=0,pady=0)

root.mainloop()








