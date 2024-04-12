import tkinter as tk
from tkinter import messagebox
from math import sqrt, pow

class Calculator(tk.Tk):

    # The main calculator class

    def __init__(self):

        # initialize the calculator class and set up the GUI.

        super().__init__()
        self.title("CALCULATOR")
        self.geometry("387x350")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        # display area

        self.display = tk.Entry(self, font=("Arial", 24), justify="right", bg="#ffffff", fg="#333333")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Buttons:

        buttons = [
            ("7", "#e0e0e0"), ("8", "#e0e0e0"), ("9", "#e0e0e0"), ("/", "cyan"),
            ("4", "#e0e0e0"), ("5", "#e0e0e0"), ("6", "#e0e0e0"), ("*", "cyan"),
            ("1", "#e0e0e0"), ("2", "#e0e0e0"), ("3", "#e0e0e0"), ("-", "cyan"),
            ("0", "#e0e0e0"), (".", "#e0e0e0"), ("=", "#90D26D"), ("+", "cyan"),
            ("C", "#f44336"), ("√", "#607D8B"), ("^", "#607D8B"), ("%", "#607D8B")
        ]

        row = 1
        col = 0

        for button, color in buttons:
            tk.Button(self, text=button, font=("Arial", 16), bg=color, fg="black", command=lambda x=button: self.add_to_display(x)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
             
    def add_to_display(self, value):

        if value == "=":
            self.evaluate()
        elif value == "C":
            self.clear()
        elif value == "√":
            self.square_root()
        elif value == "^":
            self.exponent()
        elif value == "%":
            self.percent()
        else:
            self.display.insert(tk.END, value)


    def clear(self):

        # Clear the display.

        self.display.delete(0, tk.END)

    def evaluate(self):

        try:
            result = str(eval(self.display.get()))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)

        except Exception as e:
            messagebox.showerror("Error", "Invalid expression!")
            self.display.delete(0, tk.END)

    def square_root(self):

        try:
            result = str(sqrt(float(self.display.get())))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            messagebox.showerror("Error", "Invalid input!")

    def exponent(self):

        try:
            base = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, "")
            self.wait_variable(self.display)
            exponent = float(self.display.get())
            result = str(pow(base, exponent))
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            messagebox.showerror("Error", "Invalid input!")

    def percent(self):

        try:
            result = str(float(self.display.get()) / 100)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            messagebox.showerror("Error", "Invalid input!")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()



