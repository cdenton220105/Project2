# from tkinter import *
from gui import *
import math


# class Calc:
# test = 0
    # global strin
strin = ""
num_one_str = ""
num_two_str = ""
if_first_num = True
arr_of_symbols = [""]
symbol = ""
first_is_decimal = False
second_is_decimal = False
has_symbol = False
    # def __init__(self):
    #     self.strin = ""
    #     self.num_one_str = ""
    #     self.num_two_str = ""

def set_num(num):
    add_to_str(str(num),False)

def ac():
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global if_first_num
    global has_symbol
    if_first_num = True
    strin = ""
    num_one_str = ""
    num_two_str = ""
    symbol = ""
    has_symbol = False
def plus_minus():
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
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global if_first_num
    if not if_first_num:
        equals()
    strin = str(float(strin)*100)+"%"
def divide():
    add_to_str("/", True)
    # global strin
    # strin += "/"
def multiply():
    add_to_str("X", True)
    # global strin
    # strin += "X"
def subtract():
    add_to_str("-", True)
    # global strin
    # strin += "-"
def add():
    add_to_str("+", True)
    # global strin
    # strin += "+"
def equals():
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global has_symbol
    global is_first_num
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

def decimal():
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





def add_to_str(add, is_symbol):
    global strin
    global if_first_num
    global num_one_str
    global num_two_str
    global symbol
    global has_symbol
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
            messagebox.showwarning(title="EOnly one symbol", message="Only one symbol is accepted")







def square(side):
    if side != -1:
        return side*side
    else:
        return ""
def rectangle(length,width):

    if length != -1 and width != -1:
        return length*width
    else:
        return ""
def triangle(base, height):

    if base != -1 and height != -1:
        return base*height*0.5
    else:
        return ""
def circle(radius):
    return radius*math.pi*radius
    if radius != -1:
        return radius * math.pi * radius
    else:
        return ""
def trapezoid(base, height):
    if base != -1 and height != -1:
        return base*height
    else:
        return ""


def tip(total, tip):
    if total != -1 and tip != -1:
        return_tip = float(total)*(float(tip)*0.01)
        return return_tip



def get_str():
    global strin
    # global num_one_str
    # global num_two_str
    return strin #+ "|" +num_one_str+ "|" +num_two_str
    # global strin
    # return strin

def __str__(self):
    global strin
    return strin