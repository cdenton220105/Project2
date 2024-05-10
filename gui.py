from tkinter import *
import calc
#messagebox.showwarning(title="", message="")

class Gui:
    font_size = 20
    font_style = "Arial"
    def __init__(self, window):
        self.window = window
        self.frame_one = Frame(self.window)
        self.calculation_label = Label(self.frame_one, font = f'{self.font_style} {self.font_size}', width=100, height=3, text = '', borderwidth=1, relief="solid")

        self.calculation_label.pack()
        self.frame_one.pack()

        self.frame_two = Frame(self.window,width=30)
        self.button_AC = Button(self.frame_two, text="AC", width=3, height=3, command=lambda: self.update_string(10))
        self.button_AC.pack(side='left')
        self.button_plus_minus = Button(self.frame_two, text="±", width=3, height=3, command=lambda: self.update_string(11))
        self.button_plus_minus.pack(side='left')
        self.button_percent = Button(self.frame_two, text="%", width=3, height=3, command=lambda: self.update_string(12))
        self.button_percent.pack(side='left')
        self.button_divide = Button(self.frame_two, text="÷", width=3, height=3, command=lambda: self.update_string(13))
        self.button_divide.pack(side='left')
        self.frame_two.pack(anchor='w')

        self.frame_three = Frame(self.window)
        self.button_7 = Button(self.frame_three, text="7", width=3, height=3, command=lambda: self.update_string(7))
        self.button_7.pack(side='left')
        self.button_8 = Button(self.frame_three, text="8", width=3, height=3, command=lambda: self.update_string(8))
        self.button_8.pack(side='left')
        self.button_9 = Button(self.frame_three, text="9", width=3, height=3, command=lambda: self.update_string(9))
        self.button_9.pack(side='left')
        self.button_multiply = Button(self.frame_three, text="x", width=3, height=3, command=lambda: self.update_string(14))
        self.button_multiply.pack(side='left')
        self.frame_three.pack(anchor='w')

        self.frame_four = Frame(self.window)
        self.button_4 = Button(self.frame_four, text="4", width=3, height=3, command=lambda: self.update_string(4))
        self.button_4.pack(side='left')
        self.button_5 = Button(self.frame_four, text="5", width=3, height=3, command=lambda: self.update_string(5))
        self.button_5.pack(side='left')
        self.button_6 = Button(self.frame_four, text="6", width=3, height=3, command=lambda: self.update_string(6))
        self.button_6.pack(side='left')
        self.button_subtract = Button(self.frame_four, text="-", width=3, height=3,command=lambda: self.update_string(15))
        self.button_subtract.pack(side='left')
        self.frame_four.pack(anchor='w')

        self.frame_five = Frame(self.window)
        self.button_1 = Button(self.frame_five, text="1", width=3, height=3, command=lambda: self.update_string(1))
        self.button_1.pack(side='left')
        self.button_2 = Button(self.frame_five, text="2", width=3, height=3, command=lambda: self.update_string(2))
        self.button_2.pack(side='left')
        self.button_3 = Button(self.frame_five, text="3", width=3, height=3, command=lambda: self.update_string(3))
        self.button_3.pack(side='left')
        self.button_multiply = Button(self.frame_five, text="+", width=3, height=3,command=lambda: self.update_string(16))
        self.button_multiply.pack(side='left')
        self.frame_five.pack(anchor='w')

        self.frame_six = Frame(self.window)
        self.button_0 = Button(self.frame_six, text="0", width=10, height=3, command=lambda: self.update_string(0))
        self.button_0.pack(side='left')

        self.button_decimal = Button(self.frame_six, text=".", width=3, height=3, command=lambda: self.update_string(17))
        self.button_decimal.pack(side='left')
        self.button_equals = Button(self.frame_six, text="=", width=3, height=3, command=lambda: self.update_string(18))
        self.button_equals.pack(side='left')
        self.frame_six.pack(anchor='w')

        self.frame_seven = Frame(self.window)
        self.shape_val = IntVar()
        self.shape_val.set(-1)
        self.square = Radiobutton(self.frame_seven, text = "square", variable= self.shape_val, value= 0, command = self.shape)
        self.square.pack(side = 'left')
        self.rectangle = Radiobutton(self.frame_seven, text="rectangle", variable=self.shape_val, value=1, command = self.shape)
        self.rectangle.pack(side='left')
        self.triangle = Radiobutton(self.frame_seven, text="triangle", variable=self.shape_val, value=2, command = self.shape)
        self.triangle.pack(side='left')
        self.circle = Radiobutton(self.frame_seven, text="circle", variable=self.shape_val, value=3, command = self.shape)
        self.circle.pack(side='left')
        self.trapezoid = Radiobutton(self.frame_seven, text="trapezoid", variable=self.shape_val, value=4, command = self.shape)
        self.trapezoid.pack(side='left')
        self.frame_seven.pack(anchor = 'w')

        self.frame_eight = Frame(self.window)
        self.area_label = Label(self.frame_eight, text = "Area calculator:")
        self.area_label.pack(side = 'left')
        self.frame_eight.pack(anchor='w')

        self.frame_nine = Frame(self.window)
        self.base_label = Label(self.frame_nine)
        self.base_entry = Entry(self.frame_nine, width=20)
        self.height_label = Label(self.frame_nine)
        self.height_entry = Entry(self.frame_nine, width=20)
        self.base_label.pack(side='left', padx = 10)
        # self.base_entry.pack(side='left')
        # self.height_label.pack(side='left',padx= 10)
        # self.height_entry.pack(side='left')
        self.calc_button = Button(self.frame_nine, text = 'Calculate', command = self.area_calc)
        self.result = Label(self.frame_nine)
        self.frame_nine.pack(anchor='w')

        self.frame_ten = Frame(self.window)
        self.total_label = Label(self.frame_ten, text = "Total (before tax):")
        self.total_entry = Entry(self.frame_ten)
        self.tip_label = Label(self.frame_ten, text = "Tip:")
        self.tip_percent = Entry(self.frame_ten)
        self.percent = Label(self.frame_ten, text = "%")
        self.total_label.pack(side = 'left')
        self.total_entry.pack(side = 'left')
        self.tip_label.pack(side = 'left')
        self.tip_percent.pack(side = 'left')
        self.percent.pack(side = 'left')
        self.tip_button = Button(self.frame_ten, text = "Calculate", command = self.tip_calc)
        self.tip_button.pack(side = 'left')
        self.tip = Label(self.frame_ten)
        self.frame_ten.pack(anchor = 'w')




    def update_string(self, val):
        self.funcs = [calc.set0, calc.set1, calc.set2, calc.set3, calc.set4, calc.set5, calc.set6, calc.set7, calc.set8, calc.set9, calc.ac, calc.plus_minus, calc.percent, calc.divide, calc.multiply, calc.subtract, calc.add, calc.decimal, calc.equals]
        self.funcs[val]()
        self.calculation_label.config(text=calc.get_str())

    def shape(self):
        val = self.shape_val.get()
        if val == 0:
            self.base_label.config(text = 'Side')
            self.height_label.pack_forget()
            self.height_entry.pack_forget()
            self.base_label.pack(side='left')
            self.base_entry.pack(side='left')
        elif val == 1:
            self.base_label.config(text='Length')
            self.base_label.pack(side='left')
            self.base_entry.pack(side='left', padx = 10)
            self.height_label.config(text='Width')
            self.height_label.pack(side='left')
            self.height_entry.pack(side='left', padx = 10)

        elif val == 2:
            self.base_label.config(text='Base')
            self.base_label.pack(side='left')
            self.base_entry.pack(side='left', padx=10)
            self.height_label.config(text='Height')
            self.height_label.pack(side='left')
            self.height_entry.pack(side='left', padx=10)
        elif val == 3:
            self.base_label.config(text='Radius')
            self.base_label.pack(side='left')
            self.height_label.pack_forget()
            self.height_entry.pack_forget()
            self.base_entry.pack(side='left')
        elif val == 4:
            self.base_label.config(text='Base')
            self.base_label.pack(side='left')
            self.base_entry.pack(side='left', padx=10)
            self.height_label.config(text='Height')
            self.height_label.pack(side='left')
            self.height_entry.pack(side='left', padx=10)
        self.calc_button.pack_forget()
        self.calc_button.pack(side = 'left')

    def area_calc(self):
        val = self.shape_val.get()

        if val == 0:
            side = float(self.base_entry.get())
            self.result.config(text = f"Result: {calc.square(side)}")
            self.result.pack(side = 'left')
        elif val == 1:
            length = float(self.base_entry.get())
            width = float(self.height_entry.get())
            self.result.config(text = f"Result: {calc.rectangle(length, width)}")
            self.result.pack(side = 'left')
        elif val == 2:
            base = float(self.base_entry.get())
            height = float(self.height_entry.get())
            self.result.config(text=f"Result: {calc.triangle(base, height)}")
            self.result.pack(side='left')
        elif val == 3:
            radius = float(self.base_entry.get())
            self.result.config(text=f"Result: {calc.circle(radius)}")
            self.result.pack(side='left')
        elif val == 4:
            base = float(self.base_entry.get())
            height = float(self.height_entry.get())
            self.result.config(text=f"Result: {calc.trapezoid(base, height)}")
            self.result.pack(side='left')

    def tip_calc(self):
        total = self.total_entry.get()
        tip_percent = self.tip_percent.get()
        self.tip.config(text = f"Tip: ${calc.tip(total,tip_percent)} | Total: ${float(total)+calc.tip(total,tip_percent)}")
        self.tip.pack(side = 'left')







