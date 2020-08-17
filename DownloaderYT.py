#import library nya dulu
from tkinter import *
from pytube import YouTube

#Ini inisialisasi library tkinter
root = Tk()
root.geometry("600x350")
root.title("Youtube Downloader PutraMinang")
def download():
    try:
        Var.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Download Success!")
    except Exception as e:
        Var.set("Gagal")
        root.update()
        link.set("Masukkan link yang benar bossque")

Label(root, text=">>> Welcome to YouTube Downloader Application <<<",
      font="Consolas 15 bold").pack()
Var = StringVar()
Var.set("Masukkan Link dibawah")
Entry(root, textvariable=Var, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
#Button untuk memanggil fungsi download
Button(root, text="Download", padx=50,relief=RAISED,font=10,command=download).pack()
#Running the mainloop
root.mainloop()
