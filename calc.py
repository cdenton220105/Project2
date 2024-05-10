# from tkinter import *
from gui import *
import math


# class Calc:
# test = 0
    # global strin
strin: str = ""
num_one_str: str  = ""
num_two_str: str  = ""
if_first_num: str  = True
symbol: str = ""
first_is_decimal: bool = False
second_is_decimal: bool = False
has_symbol: bool = False
calculation_done: bool = False
    # def __init__(self):
    #     self.strin = ""
    #     self.num_one_str = ""
    #     self.num_two_str = ""

def set_num(num: int):
    """
    function to set the next number pressed on the calculator
    :param num: value assigned to button pressed
    :return: None
    """
    add_to_str(str(num),False)

def ac():
    """
    function to clear calculator
    :return: None
    """
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global if_first_num
    global has_symbol
    global calculation_done
    if_first_num: = True
    strin = ""
    num_one_str = ""
    num_two_str = ""
    symbol = ""
    has_symbol = False
    calculation_done = False
def plus_minus():
    '''
    function to change calculator number from negative to positive and back
    :return: None
    '''
    global strin
    global num_one_str
    global num_two_str
    if if_first_num:
        strin = str(float(strin)*-1)
        num_one_str = str(float(num_one_str)*-1)
    else:
        strin_temp: str = strin[0:strin.index(num_two_str)]
        num_two_str = str(float(num_two_str)*-1)
        strin_temp += num_two_str
        strin = strin_temp
def percent():
    """
    function to turn screen value into a percentage
    :return: None
    """
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global if_first_num
    if not if_first_num:
        equals()
    strin = str(float(strin)*100)+"%"
def divide():
    """
    function to add division operator to calculator
    :return: None
    """
    add_to_str("/", True)
    # global strin
    # strin += "/"
def multiply():
    """
    function to add multiplication operator to calculator
    :return: None
    """
    add_to_str("X", True)
    # global strin
    # strin += "X"
def subtract():
    """
    function to add subtraction operator to calculator
    :return: None
    """
    add_to_str("-", True)
    # global strin
    # strin += "-"
def add():
    """
    function to add addition operator to calculator
    :return: None
    """
    add_to_str("+", True)
    # global strin
    # strin += "+"
def equals():
    """
    function to execute calculation
    :return: None
    """
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global has_symbol
    global is_first_num
    global calculation_done
    ans = 0
    if symbol == "/":
        ans = float(num_one_str)/float(num_two_str)
    elif symbol == "X":
        ans = float(num_one_str)*float(num_two_str)
    elif symbol == "-":
        ans = float(num_one_str)-float(num_two_str)
    elif symbol == "+":
        ans = float(num_one_str)+float(num_two_str)
    else:
        strin = "Error"
    strin = str(ans)
    has_symbol = False
    is_first_num = True
    calculation_done = True

def decimal():
    """
    function to add decimal to number
    :return: None
    """
    global first_is_decimal
    global second_is_decimal
    global has_symbol
    if if_first_num:
        if first_is_decimal:
            pass
        else:
            add_to_str(".", False)
            first_is_decimal = True
    else:
        if first_is_decimal:
            pass
        else:
            add_to_str(".", False)
            second_is_decimal = True





def add_to_str(add: str, is_symbol: bool):
    """
    function to add to the string and check that the addition is executed correctly
    :param add: sumbol to add
    :param is_symbol: boolean for if the addition is an operator
    :return: None
    """
    global strin
    global if_first_num
    global num_one_str
    global num_two_str
    global symbol
    global has_symbol
    global calculation_done
    if calculation_done:
        messagebox.showwarning(title="Clear calculation", message="To continue using the calculator, press the AC button")
    else:
        if not is_symbol:
            if if_first_num:
                num_one_str += add
                strin += add
            else:
                num_two_str += add
                strin += add
        else:
            if not has_symbol:
                if_first_num = False
                symbol = add
                has_symbol = True
                strin += add
            else:
                messagebox.showwarning(title="Only one symbol", message="Only one symbol is accepted")







def square(side: float):
    """
    function to calculate square area
    :param side: side length
    :return: area (or empty string if invalid)
    """
    if side != -1:
        return side*side
    else:
        return ""
def rectangle(length: float,width: float):
    """
    function to calculate area of rectangle
    :param length: length of rectangle
    :param width: width of rectangle
    :return: area (or empty string if invalid)
    """
    if length != -1 and width != -1:
        return length*width
    else:
        return ""
def triangle(base: float, height: float):
    """
    function to calculate area of triangle
    :param base: width of base
    :param height: vertical height
    :return: area (or empty string if invalid)
    """
    if base != -1 and height != -1:
        return base*height*0.5
    else:
        return ""
def circle(radius: float):
    """
    function to calculate area of circle
    :param radius: radius of circle
    :return: area (or empty string if invalid)
    """
    return radius*math.pi*radius
    if radius != -1:
        return radius * math.pi * radius
    else:
        return ""
def trapezoid(base: float, height: float):
    """
    function to calculate area of trapezoid
    :param base: wide base length
    :param height: vertical height
    :return: area (or empty string if invalid)
    """
    if base != -1 and height != -1:
        return base*height
    else:
        return ""


def tip(total: float, tip: float):
    """
    function to calculate tip
    :param total: meal total price
    :param tip: tip percentage
    :return: tip value
    """
    if total != -1 and tip != -1:
        return_tip = float(total)*(float(tip)*0.01)
        return return_tip



def get_str():
    """
    function to retrieve string for calculator
    :return: string
    """
    global strin
    # global num_one_str
    # global num_two_str
    return strin #+ "|" +num_one_str+ "|" +num_two_str
    # global strin
    # return strin

def __str__(self):
    """
    function to create string of module
    :param self: this module
    :return: string
    """
    global strin
    return strin