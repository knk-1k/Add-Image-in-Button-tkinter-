import customtkinter
import os
from PIL import Image

app = customtkinter.CTk()

image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "images"), "home.png")), size=(20, 20))

button1 = customtkinter.CTkButton(app, text="Button1", image=image_icon_image, compound="left")
button1.grid(row=1, column=0, padx=20, pady=10)

button2 = customtkinter.CTkButton(app, text="Button2", image=image_icon_image, compound="right")
button2.grid(row=2, column=0, padx=20, pady=10)

button3 = customtkinter.CTkButton(app, text="Button3", image=image_icon_image, compound="top")
button3.grid(row=3, column=0, padx=20, pady=10)

button4 = customtkinter.CTkButton(app, text="Button4", image=image_icon_image, compound="bottom")#, anchor="w"
button4.grid(row=4, column=0, padx=20, pady=10)

app.mainloop()