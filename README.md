# Mile-To-Km-Converter-using-TKinter
Mile to Km Converter (Tkinter)  A beginner-friendly **Python Tkinter GUI project** that converts miles into kilometers.   This project was created as part of practicing GUI programming in Python.

## ✨ Features
- Simple Tkinter interface with an **Entry box**, **Labels**, and a **Button**.
- Converts miles to kilometers using the formula:  
1 mile = 1.60934 kilometers

- Default result starts at `0`.
- Displays the calculated value dynamically when the **Calculate** button is pressed.
- Two layout approaches included:
- **Basic version** using `place()` for positioning:contentReference[oaicite:0]{index=0}.
- **Advanced version** using `grid()` and `StringVar` for cleaner, scalable layout:contentReference[oaicite:1]{index=1}.


## 🧰 Requirements
- Python 3 or higher (no external libraries needed).

## ▶️ Usage
1. Clone the repository:
 git clone https://github.com/your-username/mile-to-km-converter.git
 cd mile-to-km-converter
Run either version:

python main.py
or
python mile_to_km_advanced.py
Enter a number of miles in the input field and click Calculate.
The result will display in kilometers.

📂 Project Structure

.
├── main.py                  # Basic implementation (place-based layout)
├── mile_to_km_advanced.py   # Advanced implementation (grid layout + StringVar)
└── images/
    ├── layout.png           # Screenshot of layout
    └── result.png           # Example calculation result
📸 Screenshots
Initial state

After calculation

🚀 Future Improvements
Add reverse conversion (Km → Miles).

Support decimal precision options.

Improve design with Tkinter themes or ttk widgets.

Add error handling for invalid inputs in the basic version.
