from Tkinter import *
import dataview

tablename = 'COMPANY'
tablename2 = 'DEPARTMENTS'
DBname='test.db'

root = Tk()
root.title('Pyforms')
menubar = Menu(root)   

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Record view Test Table", command=lambda: dataview.scrolled_view(root,DBname,tablename,'r',0))
filemenu.add_command(label="Grid view Test Table", command=lambda: dataview.scrolled_view(root,DBname,tablename,'g',0))
filemenu.add_command(label="Record view Test Table2", command=lambda: dataview.scrolled_view(root,DBname,tablename2,'r',0))
filemenu.add_command(label="Grid view Test Table2", command=lambda: dataview.scrolled_view(root,DBname,tablename2,'g',0))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Records", menu=filemenu)

root.config(menu=menubar)

root.mainloop()
