#import stuff
from Tkinter import *
from cmath import *

root= Tk()
root.title("Ergaenzung")
root.minsize(width=200, height=1)

#assign stuff
a = float()
b = float()
c = float()
final = StringVar()

#entrys
Label(root, text="a:").pack()
a_e = Entry(root, text="0")
a_e.pack()
a_e.insert(0, "1")
Label(root, text="b:").pack()
b_e = Entry(root)
b_e.pack()
b_e.insert(0, "0")
Label(root, text="c:").pack()
c_e = Entry(root)
c_e.pack()
c_e.insert(0, "0")

#I did le Math in short
def math():
	a = float(a_e.get())
	b = float(b_e.get())
	c = float(c_e.get())
	b2 = (b/a)/2
	b3 = b2*b2
	b4 = 0-b3
	c2 = c/a
	pre = [str(a), str("(x+"), str(b2), str(")^2+"), str(a*(b4+c2))]
	print pre
	final.set("".join(pre))
	root.update_idletasks()

button_gen = Button(root, text="math", command=math, padx=10)
button_gen.pack()

Label(root, textvariable=final).pack()
root.update_idletasks()

root.mainloop()
