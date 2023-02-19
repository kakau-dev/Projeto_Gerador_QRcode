from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import random 
import time
import qrcode 
def reset():
  global input_entry;
  global box_list;
  input_entry = Entry(window,width=30)
  input_entry.grid(row=3,column=2,padx=0)
  box_list = Combobox(window,values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  box_list.set("Tamanho em px:")
  box_list.grid(row=4,column=2,pady=15)

def generator_qr (link,size):
    qr = qrcode.QRCode(version = 1, box_size = size,border = 2)
    qr.add_data(link)
    qr.make(fit="true")
    img=qr.make_image(fill_color='black',back_color='white')
    name_image=str("image_Qr{}{}.jpg".format(random.randint(1,8),random.randint(2,9)))
    img.save(name_image)
    time.sleep(1)
    os.system("move /y {} {}".format(name_image,os.path.expanduser("~")+"/Pictures"))
    reset()
    messagebox.showinfo("Aviso!" ,"Arquivo movido pasta fotos")
window = Tk()
window.title("Qr generator")
window.geometry("320x155")
p1 = PhotoImage(file="q.png")
window.iconphoto(False,p1)
l1 = Label(window,text=" Gerador De QR  ",font="arial 14 ")
l1.grid(row=0,column=2,padx=15,pady=5)
l2 = Label(window,text="Insira o link:")
l2.grid(row=3,column=1,pady=4)
button_active = Button(window,width=30,text="Gerar QRcode", command = lambda: generator_qr(input_entry.get(),box_list.get()))
button_active.grid(row=5,column=2)
reset()
window.mainloop()
 