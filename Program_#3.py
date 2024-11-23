import tkinter as tk
import tkinter.messagebox

class ldc_gui:
    def __init__(self):
        self.window=tk.Tk()
        self.frame_1 = tk.Frame(self.window)
        self.frame_2 = tk.Frame(self.window)
        self.frame_3 = tk.Frame(self.window)
        self.frame_4 = tk.Frame(self.window)

        self.rb_var = tk.IntVar()


        self.rb_var.set(1)


        self.rb1 = tk.Radiobutton(self.frame_1, text='Daytime (6:00 A.M. through 5:59 P.M.)', variable = self.rb_var, value=1)
        self.rb2 = tk.Radiobutton(self.frame_1, text='Evening (6:00 P.M.  through 11:59 P.M.)', variable = self.rb_var, value=2)
        self.rb3 = tk.Radiobutton(self.frame_1, text='Off-Peak (midnight through 5:59 P.M.) ', variable = self.rb_var, value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.min_prompt = tk.Label(self.frame_2, text= 'Enter the length of your call in minutes:')
        self.minutes = tk.Entry(self.frame_2, width=15)

        self.total = tk.Button(self.frame_3, text='Calculate Price', command= self.calculate_price)
        self.quit = tk.Button(self.frame_3, text='Quit', command = self.window.destroy)

        self.min_prompt.pack(side='left')
        self.minutes.pack(side='left')

        self.total.pack(side='left')
        self.quit.pack(side='left')

        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()

        tk.mainloop()


    def calculate_price(self):
        minutes = float(self.minutes.get())
        price = 0
        if self.rb_var.get() == 1:
            price = minutes * 0.02
        if self.rb_var.get() == 2:
            price = minutes * 0.12
        if self.rb_var.get() == 3:
            price = minutes * 0.05

        price_str = str(f'{price:.2f}')


        self.show_price = tk.messagebox.showinfo('Your Total Price', 'The price of your call is $'+price_str)

if __name__ == '__main__':
    my_gui = ldc_gui()