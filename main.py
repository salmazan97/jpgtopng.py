import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height=300, bg='azure3', bd=2, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File converter tool', bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

im1 = None

def getjpg():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path).convert('RGB')
    saveAsButton_png['state'] = 'normal'

browseButton_jpg = tk.Button(text=' import jpg file ', command=getjpg, bg='royalblue', fg='white', font=('helvetica',12,'bold'))
canvas1.create_window(150,130,window=browseButton_jpg)

def converttopng():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)
    im1 = None

saveAsButton_png = tk.Button(text='Convert png to jpg', command=converttopng, bg='royalblue', fg='white', font=('helvetica',12,'bold'))
canvas1.create_window(150,180,window=saveAsButton_png)


ACTIVE_LOOP = True
while ACTIVE_LOOP:
    if im1 == None:
        saveAsButton_png['state'] = 'disabled'
    else:
        browseButton_jpg['fg'] = 'red'
    root.update()