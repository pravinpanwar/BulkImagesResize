import os
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import PIL
from PIL import Image

window = tk.Tk()
window.geometry("500x180")
window.eval('tk::PlaceWindow . center')
window.title("Image Resize Tool ")

NSpath = StringVar()
NDpath = StringVar()
minSize = IntVar()


def open_src(var):
    s = filedialog.askdirectory(title="Select Source Folder")
    var.set(s)


def open_dst(var1):
    d = filedialog.askdirectory(title="Select Destination Folder")
    var1.set(d)


def submit(spath, dpath):
    if len(spath) == 0 or len(dpath) == 0:
        tkinter.messagebox.showerror("Fill Path", "Please Fill Data Path.")
    else:
        minSize = int(Min.get())

        if not os.path.exists(dpath):
            os.makedirs(dpath)

        for filename in os.listdir(spath):
            try:
                im = PIL.Image.open(spath + "/" + filename)
                print(filename)
                print(im.size)
                w, h = im.size
                ar = h / w
                print(ar)
                print(minSize)

                if w > minSize or h > minSize:
                    if w > minSize:
                        nw = minSize
                        nh = nw * ar
                    if h > minSize:
                        nh = minSize
                        nw = nh / ar
                    print(filename)
                    img = Image.open(spath + "/" + filename).resize((int(nw), int(nh),))
                    img.save('{}{}{}'.format(dpath, '/', os.path.split(spath + "/" + filename)[1]))
                    print("saved")

            except Exception as ex:
                print(ex)

        # window.quit()
        Sentry.delete(0, END)
        Dentry.delete(0, END)

        tkinter.messagebox.showinfo("Sucessfull", "Done")


button1 = tk.Button(text="Resize", command=lambda: submit(NSpath.get(), NDpath.get()), height=1, width=8,
                    font=('arial', 9, 'bold'))
# button1.grid(column=1,row=2)
button1.place(x=180, y=120)

cnclbtn = tk.Button(text="Close", command=lambda: window.destroy(), height=1, width=8, font=('arial', 9, 'bold'))
cnclbtn.place(x=250, y=120)

open_btn_src = tk.Button(text="Select", command=lambda: open_src(NSpath), height=1).place(x=402, y=53)
open_btn_dst = tk.Button(text="Select", command=lambda: open_dst(NDpath), height=1).place(x=402, y=85)

Sentry = tk.Entry(window, textvariable=NSpath, width=50)
Sentry.grid(row=1, column=1)
Sentry.place(x=95, y=57)

Dentry = tk.Entry(window, textvariable=NDpath, width=50)
Dentry.grid(row=3, column=2)
Dentry.place(x=95, y=88)

Min = tk.Entry(window, width=10)
Min.insert(0, 1200)
Min.grid(row=3, column=2)
Min.place(x=95, y=34)

lbl_src = Label(text="Source Path ", font=('arial', 8)).place(x=26, y=55)
lbl_dst = Label(text="Destination Path ", font=('arial', 8)).place(x=9, y=85)
lbl_min = Label(text="Min Size ", font=('arial', 8)).place(x=35, y=35)

window.mainloop()
