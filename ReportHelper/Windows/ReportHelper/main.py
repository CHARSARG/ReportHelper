import tkinter as tk
global report
report=""
def basicSentanceCode(name,subject,how):
    global report
    with open("report_template.template","r") as template:
        text=template.read()
    report = report+text.format(name=name,how=how,subject=subject)
    return(report)
def CustomSentance():
    global report
    report = report+entry4.get()
    label2 = tk.Label(root, text= report)
    canvas1.create_window(200, 330, window=label2)
def  BasicSentance():  
    name = entry1.get()
    subject= entry2.get()
    howgood = entry3.get()
    label1 = tk.Label(root, text= basicSentanceCode(name,subject,howgood))
    canvas1.create_window(200, 230, window=label1)

root=tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
entry1 = tk.Entry (root) 
canvas1.create_window(200, 60, window=entry1)
entry2 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry2)
entry3 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry3)
entry4 = tk.Entry (root) 
canvas1.create_window(200, 260, window=entry4)

button1 = tk.Button(text='Add Basic Sentance', command=BasicSentance)
canvas1.create_window(200, 180, window=button1)
button2 = tk.Button(text='Add Custom Sentance', command=CustomSentance)
canvas1.create_window(200, 300, window=button2)
root.mainloop()
