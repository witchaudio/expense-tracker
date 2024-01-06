import tkinter as tk
from tkinter import messagebox



def calculate_expenses():
    expenses = list(map(float, expenses_entry.get().split(',')))
    total = sum(expenses)
    result_label.config(text=f"Total Expenses: ${total:.2f}")

def cal_savings():
    income = float(income_entry.get())
    expenses = list(map(float, expenses_entry.get().split(',')))
    savings = income - sum(expenses)
    result_label.config(text=f"Your savings are ${savings:.2f}")

def cal_interest():
    try:
        principal_str = principal_entry.get()
        rate_str = rate_entry.get()
        time_str = time_entry.get()

        # Check if any field is empty
        if not (principal_str and rate_str and time_str):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Convert to float and calculate interest
        principal = float(principal_str)
        rate = float(rate_str)
        time = float(time_str)
        interest_rate = rate / 100
        interest = principal * interest_rate * time
        result_label.config(text=f"Your interest is ${interest:.2f}")

    except ValueError:
        # Handle the case where conversion to float fails
        messagebox.showerror("Error", "Please enter valid numbers")


def cal_compound():
    try:
        compound_principal = float(compound_principal_entry.get())
        compound_rate = float(compound_rate_entry.get())
        time_compounded = int(time_compounded_entry.get())
        years = float(years_entry.get())
        amount = compound_principal * (1 + (compound_rate / 100 / time_compounded)) ** (time_compounded * years)
        interest = amount - compound_principal
        result_label.config(text=f"Your compound interest is ${interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for compound interest calculation")


# Create the main UI window 
root = tk.Tk()
root.title("Expense Tracker")

# Create frames
left_frame = tk.Frame(root)
left_frame.pack(side="left", padx=10, pady=10)

right_frame = tk.Frame(root)
right_frame.pack(side="right", padx=10, pady=10)

# Calculate_expenses:
expenses_label = tk.Label(left_frame, text="Enter expenses, separated by commas:")
expenses_label.pack()

expenses_entry = tk.Entry(left_frame)
expenses_entry.pack()

expenses_button = tk.Button(left_frame, text="Calculate Expenses", command=calculate_expenses)
expenses_button.pack()

# Savings widgets
income_label = tk.Label(left_frame, text="Enter income:")
income_label.pack()

income_entry = tk.Entry(left_frame)
income_entry.pack()

savings_button = tk.Button(left_frame, text="Calculate Savings", command=cal_savings)
savings_button.pack()

# Interest widgets
principal_label = tk.Label(right_frame, text="Enter principal:")
principal_label.pack()

principal_entry = tk.Entry(right_frame)
principal_entry.pack()

rate_label = tk.Label(right_frame, text="Enter interest rate:")
rate_label.pack()

rate_entry = tk.Entry(right_frame)
rate_entry.pack()

time_label = tk.Label(right_frame, text="Enter time (years):")
time_label.pack()

time_entry = tk.Entry(right_frame)
time_entry.pack()

interest_button = tk.Button(right_frame, text="Calculate Interest", command=cal_interest)
interest_button.pack()

# ... [previous sections of your code] ...

# Compound Interest widgets
compound_principal_label = tk.Label(right_frame, text="Enter principal for compound interest:")
compound_principal_label.pack()

compound_principal_entry = tk.Entry(right_frame)
compound_principal_entry.pack()

compound_rate_label = tk.Label(right_frame, text="Enter interest rate for compound interest:")
compound_rate_label.pack()

compound_rate_entry = tk.Entry(right_frame)
compound_rate_entry.pack()

time_compounded_label = tk.Label(right_frame, text="Number of times interest is compounded (year):")
time_compounded_label.pack()

time_compounded_entry = tk.Entry(right_frame)
time_compounded_entry.pack()

years_label = tk.Label(right_frame, text="Enter number of years for compound interest:")
years_label.pack()

years_entry = tk.Entry(right_frame)
years_entry.pack()

compound_button = tk.Button(right_frame, text="Calculate Compound Interest", command=cal_compound)
compound_button.pack()

# Result label to display the output
result_label = tk.Label(root, text="", font=("Helvetica", 16), fg="green")
result_label.pack(pady=20) 

# Start the GUI event loop
root.mainloop()
