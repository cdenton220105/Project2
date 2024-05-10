from gui import *


def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('850x500')#('300x375')#
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()