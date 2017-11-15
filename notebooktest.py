from tkinter import *
from tkinter.ttk import *

from shutter.view.chart import Chart

root = Tk()
note = Notebook(root)

tab3 = Frame(note)

chart = Chart(tab3)

# **** STATUS ****
lbl_status = Label(tab3, text='STATUS')
lbl_status.grid(row=0, column=1, padx=5, pady=5, sticky=W)
lbl_status.config(font=("", 30))

lbl_light = Label(tab3, text='Lightintensity:')
lbl_light.grid(row=1, column=1, padx=5, pady=5, sticky=W)
lbl_light.config(font=("", 12))

lbl_temp = Label(tab3, text='Temperature:')
lbl_temp.grid(row=2, column=1, padx=5, pady=5, sticky=W)
lbl_temp.config(font=("", 12))

lbl_rolled = Label(tab3, text='Rolled:')
lbl_rolled.grid(row=3, column=1, padx=5, pady=5, sticky=W)
lbl_rolled.config(font=("", 12))

# **** STATUS BAR ****
status = Label(tab3, text="-", relief=SUNKEN)
status.grid(sticky=S)

note.add(tab1, text="Tab One", compound=TOP)
note.add(tab2, text="Tab Two")
note.add(tab3, text="Tab Three")
note.pack()
root.mainloop()
exit()
