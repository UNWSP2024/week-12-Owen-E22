import tkinter as tk
import tkinter.messagebox

class gas_mileage:
    def __init__(self):

        self.window = tk.Tk()
        self.top_frame = tk.Frame(self.window)
        self.middle_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)

        self.gallons_prompt = tk.Label(self.top_frame, text = 'Enter the number of gallons of gallons the car holds: ')
        self.gallons = tk.Entry(self.top_frame, width=10)

        self.miles_prompt = tk.Label(self.middle_frame, text = 'Enter the number of miles the car can drive on a full tank:')
        self.miles = tk.Entry(self.middle_frame, width=10)

        self.calculate = tk.Button(self.bottom_frame, text='Calculate', command= self.calculate_mpg, relief='ridge')
        self.quit = tk.Button(self.bottom_frame, text='Quit', command=self.window.destroy, relief='ridge')

        self.top_frame.pack()
        self.gallons_prompt.pack(side = 'left')
        self.gallons.pack(side='left')

        self.middle_frame.pack()
        self.miles_prompt.pack(side='left')
        self.miles.pack(side='left')

        self.bottom_frame.pack()
        self.calculate.pack(side='left')
        self.quit.pack(side='left')
        tk.mainloop()
    def calculate_mpg(self):
        gallons = float(self.gallons.get())
        miles = float(self.miles.get())
        mpg = str(f'{miles/gallons:.2f}')

        tk.messagebox.showinfo('Gas Mileage', "Your car's gas mileage is "+ mpg+ " miles per gallon")


if __name__ == '__main__':
    gas_mileage_calculator = gas_mileage()
