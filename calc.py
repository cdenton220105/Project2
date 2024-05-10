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
    # def __init__(self):
    #     self.strin = ""
    #     self.num_one_str = ""
    #     self.num_two_str = ""

def set0():
    add_to_str("0",False)
    # return test +1
def set1():
    add_to_str("1", False)
    # global strin
    # strin += "1"
def set2():
    add_to_str("2", False)
    # global strin
    # strin += "2"
def set3():
    add_to_str("3", False)
    # global strin
    # strin += "3"
def set4():
    add_to_str("4", False)
    # global strin
    # strin += "4"
def set5():
    add_to_str("5", False)
    # global strin
    # strin += "5"
def set6():
    add_to_str("6", False)
    # global strin
    # strin += "6"
def set7():
    add_to_str("7", False)
    # global strin
    # strin += "7"
def set8():
    add_to_str("8", False)
    # global strin
    # strin += "8"
def set9():
    add_to_str("9", False)
    # global strin
    # strin += "9"
def ac():
    global strin
    global num_one_str
    global num_two_str
    global symbol
    global if_first_num
    if_first_num = True
    strin = ""
    num_one_str = ""
    num_two_str = ""
    symbol = ""
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

def decimal():
    global first_is_decimal
    global second_is_decimal
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
    if not is_symbol:
        if if_first_num:
            num_one_str += add
        else:
            num_two_str += add
    else:
        if_first_num = False
        symbol = add


    strin += add


def square(side):
    return side*side
def rectangle(length,width):
    return length*width
def triangle(base, height):
    return base*height*0.5
def circle(radius):
    return radius*math.pi*radius
def trapezoid(base, height):
    return base*height

def tip(total, tip):
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