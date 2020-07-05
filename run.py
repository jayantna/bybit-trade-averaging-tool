import tkinter as tk
from tkinter import ttk
import os
os.system('active_order.py')
scores = tk.Tk() 

import json
fhandle=open("activeorder.json").read()
jsdata=json.loads(fhandle)


def selectItem(a):
    curItem = listBox.focus()
    print (listBox.item(curItem))
    print (listBox.selection())

def calc():
    p=e1.get()
    print (p)
    s=e2.get()
    print(s,type(s))
    num=float(0)
    den=float(0)
    for ids in listBox.selection():
        #print(float(listBox.item(ids)['values'][3]))
        num=num+(float(listBox.item(ids)['values'][3])*float((listBox.item(ids))['values'][4]))
        den=den+((listBox.item(ids)['values'][4]))
        if (p=="Price" or s=="Size") and type(p) is str:
        	result=tk.Label(scores, text=(num/den), font=("Arial",30))
        	result.grid(row=10, column=0)
        else:
            p=float(p)
            s=float(s)
            res= ((num+(s*p))/(den+s))
            result=tk.Label(scores, text=res)
            result.grid(row=10, column=0)
            
def show():	#Shows Table data values
    tempList=list()
    for trades in jsdata["result"]["data"]:
        list_1=list()
        list_1.clear()
        list_1.append(trades['symbol'])
        list_1.append(trades['side'])
        list_1.append(trades["price"])
        list_1.append(trades["cum_exec_qty"])
        list_1.append(trades["cum_exec_value"])
        list_1.append(trades["order_type"])
        list_1.append(trades["order_status"])
        list_1.append(trades["cum_exec_fee"])
        tempList.append(list_1)
	#tempList.sort(key=lambda e: e[1], reverse=True)
    for i, (pair, side, price, sizeu,sizeb, typ, status, fees) in enumerate(tempList, start=0):
        if i % 2 is 0:
            c = tk.Checkbutton(scores, text="filename", variable=i)
            listBox.insert("", "end", values=(i , pair, side, price, sizeu, sizeb, typ, status, fees), tags = ('odd',))
        else:
            listBox.insert("", "end", values=(i , pair, side, price, sizeu, sizeb, typ, status, fees), tags = ('even',))

def Entrycall1(event):
	e1.selection_range(0, tk.END)
def Entrycall2(event):
	e2.selection_range(0, tk.END)

#Main program starts-------------------------------------------------------------------------------------------

label = tk.Label(scores, text="Trades", fg= "Green", font=("Arial",30)).grid(row=0, columnspan=3) #Headiing

#styles of treeview##########################################################################################
style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
#############################################################################################################


# create Treeview with 8 columns#############################################################################
cols = ('Select' ,'Pair', 'Side', 'Price', 'Size (USD)', 'Size(BTC)', 'Type', 'Status', 'Fees')
listBox = ttk.Treeview(scores ,columns=cols, selectmode="extended", show='headings',style="mystyle.Treeview")
listBox.tag_configure('odd', background='#E8E8E8')
listBox.tag_configure('even', background='#DFDFDF')
#############################################################################################################



# set column headings names##################################################################################
for col in cols:
	if col is 'Select':
	    listBox.heading(col, text=col)
	    listBox.column(col, minwidth=0, width=50)
	else:
	    listBox.heading(col, text=col)
	    listBox.column(col, minwidth=0, width=100)
#############################################################################################################
listBox.grid(row=1, column=0, columnspan=1)
showScores = tk.Button(scores, text="Show Trades", width=15, command=show).grid(row=2, column=0)

e1=tk.Entry(scores, width=20, font=('Helvetica', 24))
e1.insert(0, "Price")
e1.bind("<FocusIn>",Entrycall1)
e1.grid(row=5, column=0)

e2=tk.Entry(scores, width=20, font=('Helvetica', 24))
e2.insert(0, "Size")
e2.bind("<FocusIn>", Entrycall2)
e2.grid(row=6, column=0)

calcButton = tk.Button(scores, text="Calculate", width=15, command=calc).grid(row=8, column=0)
#closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=9, column=0)
#listBox.bind('<ButtonRelease-1>', selectItem)
scores.mainloop()
