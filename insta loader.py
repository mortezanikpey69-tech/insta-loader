from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image,ImageTk
import io

def get_image():
   l=instaloader.Instaloader()
   profile=instaloader.Profile.from_username(l.context,f"{username.get()}")
   a=urlopen(profile.get_profile_pic_url())
   data=a.read()
   a.close()
   image=Image.open(io.BytesIO(data))
   pic=ImageTk.PhotoImage(image)
   label.config(image=pic)
   label.image=pic
   label.pack()

window=Tk()
window.geometry("600x600")
window.maxsize(800,900)
window.minsize(200,300)
window.title("insta profile downloder")
#label
label=Label(window,text= "please enter your id instagram",fg="red",bg="yellow")
label.pack()


#input
username=Entry(window,width=50)
username.pack()


#button:
button=Button(window,text="download profile",fg="red",bg="blue")
button.pack()
button.config(command=get_image)

window.mainloop()

