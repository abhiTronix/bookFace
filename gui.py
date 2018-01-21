import Tkinter as tk
import cv2
from PIL import Image, ImageTk
import facial

width, height = 800, 800
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()

root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain2 = tk.Label(root, text="Okay this is it")

lmain.pack(side=tk.LEFT)
lmain2.pack()

def show_frame():
    frame, people = facial.recog()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()