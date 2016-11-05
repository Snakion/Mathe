#import
from Tkinter import *

Tk().title("zentr. Streckung")

#assign
E1 = float()
E1Y = float()
E2 = float()
E2Y = float()
E3 = float()
E3Y = float()
E4 = float()
E4Y = float()
E5 = float()
E5Y = float()
E6 = float()
E6Y = float()
E7 = float()
E7Y = float()
E12 = float()
E1Y2 = float()
E22 = float()
E2Y2 = float()
E32 = float()
E3Y2 = float()
E42 = float()
E4Y2 = float()
E52 = float()
E5Y2 = float()
E62 = float()
E6Y2 = float()
E72 = float()
E7Y2 = float()
S = float()
SY = float()
K = float()
m = int(25)
g = int(0)

#Entry
Label(text="P").grid(row=1, column=1)
E12e = Entry()
E12e.grid(row=1, column=0)
E12e.insert(0, "0")
E1Y2e = Entry()
E1Y2e.grid(row=1, column=2)
E1Y2e.insert(0, "0")
Label(text="Q").grid(row=2, column=1)
E22e = Entry()
E22e.grid(row=2, column=0)
E22e.insert(0, "0")
E2Y2e = Entry()
E2Y2e.grid(row=2, column=2)
E2Y2e.insert(0, "0")
Label(text="R").grid(row=3, column=1)
E32e = Entry()
E32e.grid(row=3, column=0)
E32e.insert(0, "0")
E3Y2e = Entry()
E3Y2e.grid(row=3, column=2)
E3Y2e.insert(0, "0")
Label(text="S").grid(row=4, column=1)
E42e = Entry()
E42e.grid(row=4, column=0)
E42e.insert(0, "0")
E4Y2e = Entry()
E4Y2e.grid(row=4, column=2)
E4Y2e.insert(0, "0")
Label(text="T").grid(row=5, column=1)
E52e = Entry()
E52e.grid(row=5, column=0)
E52e.insert(0, "0")
E5Y2e = Entry()
E5Y2e.grid(row=5, column=2)
E5Y2e.insert(0, "0")
Label(text="U").grid(row=6, column=1)
E62e = Entry()
E62e.grid(row=6, column=0)
E62e.insert(0, "0")
E6Y2e = Entry()
E6Y2e.grid(row=6, column=2)
E6Y2e.insert(0, "0")
Label(text="V").grid(row=7, column=1)
E72e = Entry()
E72e.grid(row=7, column=0)
E72e.insert(0, "0")
E7Y2e = Entry()
E7Y2e.grid(row=7, column=2)
E7Y2e.insert(0, "0")
Label(text="K").grid(row=8, column=1)
K_e = Entry()
K_e.grid(row=8, column=0)
K_e.insert(0, "1")
Label(text="Streckpunkt").grid(row=9, column=1)
S_e = Entry()
S_e.grid(row=9, column=0)
S_e.insert(0, "0")
SY_e = Entry()
SY_e.grid(row=9, column=2)
SY_e.insert(0, "0")
Label(text="Menge").grid(row=10, column=1)
menge_e = Entry()
menge_e.grid(row=10, column=0)
menge_e.insert(0, "1")

#can
canvas_width = 675
canvas_height = 675
can = Canvas(width=canvas_width, height=canvas_height)
can.grid(row=11, column=1)

#math
def math():
	#vars
	g = int(0)
	E1 = float(E12e.get())
	E1Y = float(E1Y2e.get())
	E2 = float(E22e.get())
	E2Y = float(E2Y2e.get())
	E3 = float(E32e.get())
	E3Y = float(E3Y2e.get())
	E4 = float(E42e.get())
	E4Y = float(E4Y2e.get())
	E5 = float(E52e.get())
	E5Y = float(E5Y2e.get())
	E6 = float(E62e.get())
	E6Y = float(E6Y2e.get())
	E7 = float(E72e.get())
	E7Y = float(E7Y2e.get())
	S = float(S_e.get())
	SY = float(SY_e.get())
	K = float(K_e.get())
	#measure
	E12 = K*abs(E1 - S) * m + E1 * m
	E1Y2 = K*abs(E1Y - SY) * m + E1Y * m
	E22 = K*abs(E2 - S) * m + E2 * m
	E2Y2 = K*abs(E2Y - SY) * m + E2Y * m
	E32 = K*abs(E3 - S) * m + E3 * m
	E3Y2 = K*abs(E3Y - SY) * m + E3Y * m
	E42 = K*abs(E4 - S) * m + E4 * m
	E4Y2 = K*abs(E4Y - SY) * m + E4Y * m
	E52 = K*abs(E5 - S) * m + E5 * m
	E5Y2 = K*abs(E5Y - SY) * m + E5Y * m
	E62 = K*abs(E6 - S) * m + E6 * m
	E6Y2 = K*abs(E6Y - SY) * m + E6Y * m
	E72 = K*abs(E7 - S) * m + E7 * m
	E7Y2 = K*abs(E7Y - SY) * m + E7Y * m
	#sys
	for x in range (0, 45):
		can.create_line(g, 0, g, canvas_height, fill="#7A7A7A")
		can.create_line(0, g, canvas_width, g, fill="#7A7A7A")
		g = g+15
	#draw
	if int(menge_e.get()) == 7:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
		can.create_line(E2*m, canvas_height - E2Y*m, E3*m, canvas_height - E3Y*m, fill="#666666")
		can.create_line(E3*m, canvas_height - E3Y*m, E4*m, canvas_height - E4Y*m, fill="#666666")
		can.create_line(E4*m, canvas_height - E4Y*m, E5*m, canvas_height - E5Y*m, fill="#666666")
		can.create_line(E5*m, canvas_height - E5Y*m, E6*m, canvas_height - E6Y*m, fill="#666666")
		can.create_line(E6*m, canvas_height - E6Y*m, E7*m, canvas_height - E7Y*m, fill="#666666")
		can.create_line(E7*m, canvas_height - E7Y*m, E1*m, canvas_height - E1Y*m, fill="#666666")
	elif int(menge_e.get()) == 6:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
		can.create_line(E2*m, canvas_height - E2Y*m, E3*m, canvas_height - E3Y*m, fill="#666666")
		can.create_line(E3*m, canvas_height - E3Y*m, E4*m, canvas_height - E4Y*m, fill="#666666")
		can.create_line(E4*m, canvas_height - E4Y*m, E5*m, canvas_height - E5Y*m, fill="#666666")
		can.create_line(E5*m, canvas_height - E5Y*m, E6*m, canvas_height - E6Y*m, fill="#666666")
		can.create_line(E6*m, canvas_height - E6Y*m, E1*m, canvas_height - E1Y*m, fill="#666666")
	elif int(menge_e.get()) == 5:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
		can.create_line(E2*m, canvas_height - E2Y*m, E3*m, canvas_height - E3Y*m, fill="#666666")
		can.create_line(E3*m, canvas_height - E3Y*m, E4*m, canvas_height - E4Y*m, fill="#666666")
		can.create_line(E4*m, canvas_height - E4Y*m, E5*m, canvas_height - E5Y*m, fill="#666666")
		can.create_line(E5*m, canvas_height - E5Y*m, E1*m, canvas_height - E1Y*m, fill="#666666")
	elif int(menge_e.get()) == 4:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
		can.create_line(E2*m, canvas_height - E2Y*m, E3*m, canvas_height - E3Y*m, fill="#666666")
		can.create_line(E3*m, canvas_height - E3Y*m, E4*m, canvas_height - E4Y*m, fill="#666666")
		can.create_line(E4*m, canvas_height - E4Y*m, E1*m, canvas_height - E1Y*m, fill="#666666")
	elif int(menge_e.get()) == 3:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
		can.create_line(E2*m, canvas_height - E2Y*m, E3*m, canvas_height - E3Y*m, fill="#666666")
		can.create_line(E3*m, canvas_height - E3Y*m, E1*m, canvas_height - E1Y*m, fill="#666666")
	elif int(menge_e.get()) == 2:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
		can.create_line(E2*m, canvas_height - E2Y*m, E1*m, canvas_height - E1Y*m, fill="#666666")
	elif int(menge_e.get()) == 1:
		can.create_line(E1*m, canvas_height - E1Y*m, E2*m, canvas_height - E2Y*m, fill="#666666")
	#streckung
	if int(menge_e.get()) == 7:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2*m, fill="#00ff00")
		can.create_line(E22*m, canvas_height - E2Y2*m, E32*m, canvas_height - E3Y2*m, fill="#000000")
		can.create_line(E32*m, canvas_height - E3Y2*m, E42*m, canvas_height - E4Y2*m, fill="#000000")
		can.create_line(E42*m, canvas_height - E4Y2*m, E52*m, canvas_height - E5Y2*m, fill="#000000")
		can.create_line(E52*m, canvas_height - E5Y2*m, E62*m, canvas_height - E6Y2*m, fill="#000000")
		can.create_line(E62*m, canvas_height - E6Y2*m, E72*m, canvas_height - E7Y2*m, fill="#000000")
		can.create_line(E72*m, canvas_height - E7Y2*m, E12*m, canvas_height - E1Y2*m, fill="#000000")
	elif int(menge_e.get()) == 6:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2*m, fill="#000000")
		can.create_line(E22*m, canvas_height - E2Y2*m, E32*m, canvas_height - E3Y2*m, fill="#000000")
		can.create_line(E32*m, canvas_height - E3Y2*m, E42*m, canvas_height - E4Y2*m, fill="#000000")
		can.create_line(E42*m, canvas_height - E4Y2*m, E52*m, canvas_height - E5Y2*m, fill="#000000")
		can.create_line(E52*m, canvas_height - E5Y2*m, E62*m, canvas_height - E6Y2*m, fill="#000000")
		can.create_line(E62*m, canvas_height - E6Y2*m, E12*m, canvas_height - E1Y2*m, fill="#000000")
	elif int(menge_e.get()) == 5:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2*m, fill="#111111")
		can.create_line(E22*m, canvas_height - E2Y2*m, E32*m, canvas_height - E3Y2*m, fill="#111111")
		can.create_line(E32*m, canvas_height - E3Y2*m, E42*m, canvas_height - E4Y2*m, fill="#111111")
		can.create_line(E42*m, canvas_height - E4Y2*m, E52*m, canvas_height - E5Y2*m, fill="#111111")
		can.create_line(E52*m, canvas_height - E5Y2*m, E12*m, canvas_height - E1Y2*m, fill="#111111")
	elif int(menge_e.get()) == 4:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2*m, fill="#000000")
		can.create_line(E22*m, canvas_height - E2Y2*m, E32*m, canvas_height - E3Y2*m, fill="#000000")
		can.create_line(E32*m, canvas_height - E3Y2*m, E42*m, canvas_height - E4Y2*m, fill="#000000")
		can.create_line(E42*m, canvas_height - E4Y2*m, E12*m, canvas_height - E1Y2*m, fill="#000000")
	elif int(menge_e.get()) == 3:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2*m, fill="#000000")
		can.create_line(E22*m, canvas_height - E2Y2*m, E32*m, canvas_height - E3Y2*m, fill="#000000")
		can.create_line(E32*m, canvas_height - E3Y2*m, E12*m, canvas_height - E1Y2*m, fill="#000000")
	elif int(menge_e.get()) == 2:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2*m, fill="#000000")
		can.create_line(E22*m, canvas_height - E2Y2*m, E12*m, canvas_height - E1Y2*m, fill="#000000")
	elif int(menge_e.get()) == 1:
		can.create_line(E12*m, canvas_height - E1Y2*m, E22*m, canvas_height - E2Y2 *m, fill="#000000")
	#point
	can.create_oval(S*m - 2.5, canvas_height - SY*m - 2.5, S*m+2.5, canvas_height - SY*m+2.5, fill="#000000")
	
	can.create_line(12 * m, canvas_height - 12 * m, 22 * m, canvas_height - 22 * m, fill="#111111")

def dele():
	can.delete("all")

Button(text="math", command=math, padx=10).grid(row=12, column=2)
Button(text="new", command=dele, padx=10).grid(row=12, column=0)
mainloop()
