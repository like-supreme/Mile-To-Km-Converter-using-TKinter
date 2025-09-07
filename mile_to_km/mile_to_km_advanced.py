from tkinter import *

def calculate():
    try:
        miles = float(miles_var.get() or 0)
        result_var.set(f"{miles * 1.60934:.2f}")
    except ValueError:
        result_var.set("0")

window = Tk()
window.title("Mile to Km Converter")

miles_var  = StringVar()
result_var = StringVar(value="0")

# row 0: [Entry] [Miles]
Entry(textvariable=miles_var, width=12).grid(row=0, column=1, pady=10)
Label(text="Miles").grid(row=0, column=2, padx=6)

# row 1: [Is equal to] [RESULT] [Km]
Label(text="Is equal to").grid(row=1, column=0, pady=10)
Label(textvariable=result_var, font=("Times New Roman", 10, "bold")).grid(row=1, column=1)
Label(text="Km").grid(row=1, column=2)

# row 2: [boş] [Button] [boş]
Button(text="Calculate", command=calculate).grid(row=2, column=1, pady=12)

# give rows a weight for adjusting
for c in range(3):
    window.columnconfigure(c, weight=1)

window.mainloop()
