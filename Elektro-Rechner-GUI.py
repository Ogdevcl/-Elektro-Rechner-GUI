import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        selected_calculation = calculation_var.get()
        value1 = float(value1_entry.get())
        value2 = float(value2_entry.get())
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Werte ein.")
        return

    if selected_calculation == "Spannung (U)":
        result = value2 / value1
    elif selected_calculation == "Stromstärke (I)":
        result = value2 / value1
    elif selected_calculation == "Widerstand (R)":
        result = value1 / value2
    elif selected_calculation == "Leistung (P)":
        result = value1 * value2

    result_label.config(text=f"{selected_calculation} = {result:.2f} {unit_dict[selected_calculation]}")

root = tk.Tk()
root.title("Elektro-Rechner")

frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

calculation_var = tk.StringVar()
calculation_var.set("Spannung (U)") 
calculation_menu = ttk.Combobox(frame, textvariable=calculation_var, values=["Spannung (U)", "Stromstärke (I)", "Widerstand (R)", "Leistung (P)"])
calculation_menu.grid(row=0, column=0, padx=10, pady=10)

value1_label = ttk.Label(frame, text="Wert 1:")
value1_label.grid(row=1, column=0, padx=10, pady=10)
value1_entry = ttk.Entry(frame)
value1_entry.grid(row=1, column=1, padx=10, pady=10)

value2_label = ttk.Label(frame, text="Wert 2:")
value2_label.grid(row=2, column=0, padx=10, pady=10)
value2_entry = ttk.Entry(frame)
value2_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(frame, text="Berechnen", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2)

unit_dict = {
    "Spannung (U)": "Volt",
    "Stromstärke (I)": "Ampere",
    "Widerstand (R)": "Ohm",
    "Leistung (P)": "Watt"
}

root.mainloop()
