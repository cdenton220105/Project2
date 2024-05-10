from gui import *


def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('800x800')#('300x375')#
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()