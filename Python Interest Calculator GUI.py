import tkinter as tk
from tkinter import *

def calc():
    val = opt.get()
    principal = p.get()
    rate = r.get()
    time = t.get()
    if val == "":
        si = (principal * rate * time)/100
        ans.set(si)
    else:
        Amount = principal * (pow((1 + rate/100), time))
        ci = Amount - principal
        ans.set(ci)




window = tk.Tk()

window.geometry("400x200")

window.title("Interest Calculator")

tk.Label(window, text="Enter Principal ", width="10", font=("arial", 12, "bold"), padx="5", pady="5", bg="blue", fg="white").place(x=10, y=10)
tk.Label(window, text="Enter Rate ", width="10", font=("arial", 12, "bold"), padx="5", pady="5", bg="blue", fg="white").place(x=10, y=50)
tk.Label(window, text="Enter Time ", width="10", font=("arial", 12, "bold"), padx="5", pady="5", bg="blue", fg="white").place(x=10, y=90)
p = tk.IntVar()
r = tk.IntVar()
t = tk.IntVar()
tk.Entry(window, textvariable=p, font=(10)).place(x=150, y=10)
tk.Entry(window, textvariable=r, font=(10)).place(x=150, y=50)
tk.Entry(window, textvariable=t, font=(10)).place(x=150, y=90)
opt = IntVar()
tk.Radiobutton(window, text="Simple Interest", font=(15), variable=opt, value=0).place(x=10, y=130)
tk.Radiobutton(window, text="Compound Interest", font=(15), variable=opt, value=1).place(x=170, y=130)
tk.Button(window, text="Calculate", command=calc).place(x=10, y=170)
ans = tk.StringVar()
tk.Label(window, textvariable=ans, font=(15)).place(x=80, y=170)
window.mainloop()