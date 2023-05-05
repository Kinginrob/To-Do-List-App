import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        input_temperature = float(temperature_entry.get())
        input_unit = unit_var.get()

        if input_unit == "Celsius":
            output_temperature = (input_temperature * 9/5) + 32
            output_unit = "Fahrenheit"
        else:
            output_temperature = (input_temperature - 32) * 5/9
            output_unit = "Celsius"

        result_var.set(f"{output_temperature:.2f} {output_unit}")

    except ValueError:
        result_var.set("Invalid input")

root = tk.Tk()
root.title("Temperature Converter")

# Set a custom window size
root.geometry("400x200")

# Use ttk widgets for better appearance
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=5)
style.configure('TLabel', font=('Helvetica', 12), padding=5)
style.configure('TEntry', font=('Helvetica', 12), padding=5)
style.configure('TOptionMenu', font=('Helvetica', 12), padding=5)

# Set a background color
root.configure(bg='#f0f0f0')

unit_var = tk.StringVar()
unit_var.set("Celsius")

result_var = tk.StringVar()
result_var.set("")

temperature_entry = ttk.Entry(root)
temperature_entry.grid(row=0, column=0, padx=20, pady=20)

unit_menu = ttk.OptionMenu(root, unit_var, "Celsius", "Fahrenheit")
unit_menu.grid(row=0, column=1, padx=20, pady=20)

convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()
