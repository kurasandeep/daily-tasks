from tkinter import *

class TriangleAreaCalculator:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Base:')
        self.lbl2 = Label(win, text='Height:')
        self.lbl3 = Label(win, text='Area:')
        self.base_entry = Entry(bd=3)
        self.height_entry = Entry()
        self.area_result = Entry()
        self.calculate_button = Button(win, text='Calculate Area', command=self.calculate_area)
        
        self.lbl1.grid(row=0, column=0)
        self.base_entry.grid(row=0, column=1)
        self.lbl2.grid(row=1, column=0)
        self.height_entry.grid(row=1, column=1)
        self.calculate_button.grid(row=2, columnspan=2)
        self.lbl3.grid(row=3, column=0)
        self.area_result.grid(row=3, column=1)

    def calculate_area(self):
        base = float(self.base_entry.get())
        height = float(self.height_entry.get())
        area = 0.5 * base * height
        self.area_result.delete(0, END)
        self.area_result.insert(END, str(area))


window = Tk()
calculator = TriangleAreaCalculator(window)
window.title('Triangle Area Calculator')
window.geometry("300x150")
window.mainloop()

                       

       
                 
