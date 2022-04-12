from cgitb import text
from optparse import Option
import os
from sys import float_repr_style 
from tkinter import * 
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import * 
from tkinter.filedialog import *
from turtle import color 

def change_color(): 
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    #reset the name to untitled
    window.title("Untitled") 
    #delete everything in the window 
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"), ("Text Documents", "*.txt")])


    
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, 'r')
        text_area.insert(1.0, file.read())

    except Exception: 
        print("couldn't read file")

    finally: 
        file.close()

def save_file(): 
    file = filedialog.asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]) 

    if file is None:
        return 
    
    else: 
        try: 
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))
        except Exception:
            print("couldn't save file ")
        
        finally: 
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")
 

def copy(): 
    text_area.event_generate("<<Copy>>")
 

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About Prakriti's Text Editor", "Just a side project. It is a text editor created by Prakrit in Python")

def quit(): 
    window.destroy()


window = Tk()
window.title("Text Editor by Prakriti")
file = None 

window_width = 500 
window_height = 500 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.configure(bg='black')

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

# #geometry for the window 
window.geometry('{}x{}+{}+{}'.format(window_width, window_height,x,y))

#default font
font_name = StringVar(window)
font_name.set("Canela")

font_size = StringVar(window)
font_size.set("15")

text_area = Text(window, font=(font_name.get(), font_size.get()))

#adding a scroll bar
scroll_bar = Scrollbar(text_area) 
#allowing our text area to expand
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#text area should take most of window
text_area.grid(sticky=N+E+S+W)

#Creating buttons, option menu 
frame = Frame(window, highlightbackground='black', highlightcolor='black', bg='blue', relief=RAISED)
frame.grid()

#color button 
color_button = Button(frame, text='color',command=change_color)
color_button.grid(row=0, column=0)

#changing the font 
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

#spinbox 
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

#dropdown menus 
menu_bar = Menu(window)
window.config(menu=menu_bar)

#File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

#Edit Menu 
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# #help Menu 
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)
window.mainloop()