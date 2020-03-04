from tkinter import *
import xlrd
def tableintable():
        window=Tk()
        window.geometry("900x510")
        window.resizable(0,0)
        window.title("Ethiopian Football League  Management System")
        frame = Frame(window)
        frame.grid()
        headerLabel = Label(frame, width = 70 , height = 3 ,\
        text = "Ethiopian Premier League Table", \
        bg = "lightblue" , fg = "black" ,font=('Verdana',15))
        headerLabel.grid(row = 0 , columnspan = 14)
        file=('league.xlsx')
        sheet_opening=xlrd.open_workbook(file)
        sheet_number=sheet_opening.sheet_by_index(1)
        for i in range(17):
            for j in range(14):
                cell = sheet_number.cell(i,j)
                Label(frame , text=str(cell.value)).grid(row=i+1 , column=j)
        window.mainloop()