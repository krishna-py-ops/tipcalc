from tkinter import Tk,Radiobutton,Button,StringVar,IntVar,Entry,Label

#Tk for application window
#intVar is a numerical value of datatype

class TipCalculator():
    def __init__(self):  #for class initiation
        window = Tk()
        window.title("TipCalculator")
        window.configure(background="blue")
        window.geometry("375x250")
        window.resizable(width=False,height=False)
        
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percents = Label(window,text = "Tip percentages",bg = "purple",fg = "white")
        tip_percents.grid(column=0,row=0,padx=15)

        bill_amount = Label(window,text = "Bill amount",bg = "black",fg = "white")
        bill_amount.grid(column=1,row=0,padx=15)


        bill_amount_entry = Entry(window,textvariable = self.meal_cost,width=14)
        bill_amount_entry.grid(column=2,row=0)


        five_percent_tip = Radiobutton(window,text="0.5%",variable = self.tip_percent,value=5)
        five_percent_tip.grid(column=0,row=1)

        ten_percent_tip = Radiobutton(window,text="10%",variable = self.tip_percent,value=10)
        ten_percent_tip.grid(column=0,row=2)

        fifteen_percent_tip = Radiobutton(window,text="15%",variable = self.tip_percent,value=15)
        fifteen_percent_tip.grid(column=0,row=3)

        twenty_percent_tip = Radiobutton(window,text="20%",variable = self.tip_percent,value=20)
        twenty_percent_tip.grid(column=0,row=4)

        twentyfive_percent_tip = Radiobutton(window,text="25%",variable = self.tip_percent,value=25)
        twentyfive_percent_tip.grid(column=0,row=5)

        thirty_percent_tip = Radiobutton(window,text="30%",variable = self.tip_percent,value=30)
        thirty_percent_tip.grid(column=0,row=6)
        
        tip_amount_lb1 = Label(window,text = "Tip Amount",bg = "brown",fg = "White")
        tip_amount_lb1.grid(column=1,row=3,padx=15)

        tip_amount_entry = Entry(window,textvariable=self.tip,width=14)
        tip_amount_entry.grid(column=2,row=3)

        bill_total_lb1 = Label(window,text = "Bill Total",bg = "blue",fg = "white")
        bill_total_lb1.grid(column=1,row=5,padx=15)
        bill_total_entry = Entry(window,textvariable =self.total_cost,width =14)
        bill_total_entry.grid(column=2,row=5)

        
        calculate_btn = Button(window,text = "Calculate",bg = "green",fg = "white",command=self.calculate)
        calculate_btn.grid(column=1,row=7,padx=15)

        clear_btn = Button(window,text = "clear",bg = "black",fg = "white",command = self.clear)
        clear_btn.grid(column=2,row=7)
        window.mainloop()

        


    def calculate(self):
        
        
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)
        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")
    
      


TipCalculator() #it helps the application to launch from the mainloop



        
