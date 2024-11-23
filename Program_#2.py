import tkinter as tk
import tkinter.messagebox

# Joe's Automotive performs the following routine maintenance service:
#
# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to select any or all of these services.  When the user clicks a button, the total charges should be displayed.

class oil_change:
    def __init__(self):
        self.window = tk.Tk()
        self.top_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)

        self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()
        self.cb_var3 = tk.IntVar()
        self.cb_var4 = tk.IntVar()
        self.cb_var5 = tk.IntVar()
        self.cb_var6 = tk.IntVar()
        self.cb_var7 = tk.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, text = 'Oil Change - $30.00', variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.cb_var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.total = tk.Button(self.bottom_frame, text='Calculate total', command= self.calculate_total)
        self.quit = tk.Button(self.bottom_frame, text='Quit', command=self.window.destroy)

        self.total.pack(side='left')
        self.quit.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def calculate_total(self):
        price = 0
        if self.cb_var1.get() == 1:
            price += 30
        if self.cb_var2.get() == 1:
            price += 20
        if self.cb_var3.get() == 1:
            price += 40
        if self.cb_var4.get() == 1:
            price += 100
        if self.cb_var5.get() == 1:
            price += 35
        if self.cb_var6.get() == 1:
            price += 200
        if self.cb_var7.get() == 1:
            price += 20

        price_str = str(price)

        self.total_oc_price = tk.messagebox.showinfo('Your Total', 'Your total is $'+price_str)







if __name__ == '__main__':
    oil_gui = oil_change()

