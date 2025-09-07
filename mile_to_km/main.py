from tkinter import *
# ==============imports====================================================
def calculate():
    miles = float(input_entries.get())
    km = miles*1.60934
    result_lable.config(text=f"{km}")
#=======Window Setup=======================================================
window = Tk()
window.title("Mile to Km Converter ")
window.minsize(height=250 , width=400)
#========= Labels ==========================================================
mile_lable = Label(text="Miles" , font=("Times New Roman" , 8 , "normal"))
mile_lable.place(x=250 , y=50)
mile_lable.config(padx=5 , pady=5)
is_equal = Label(text="Is equal to" , font=("Times New Roman" , 8 , "normal"))
is_equal.place(x=75 , y=100)
is_equal.config(padx=5 , pady=5)
result_lable = Label(text="0" , font=("Times New Roman" , 8 , "bold"))
result_lable.place(x=150 , y=100)
result_lable.config(padx=5 , pady=5)
km_lable = Label(text="Km" , font=("Times New Roman" , 8 , "normal"))
km_lable.place(x=250 , y=100)
km_lable.config(padx=5 , pady=5)
#================= Button ================================================
calc_button = Button(text="Calculate" , command=calculate)
calc_button.place(x=150 , y=150)
calc_button.config(padx=5 , pady=5)
#======================Entries============================================
input_entries = Entry(width=15)
input_entries.place(x=150 , y=50)
#==================loop===================================================
window.mainloop()

