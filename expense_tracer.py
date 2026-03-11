import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
DB_NAME = "expenses.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL)""")

    conn.commit()
    conn.close()

def add_expense(amount, category, description, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
def show_category_chart():
    expenses = get_expenses()
    if not expenses:
        messagebox.showinfo("Info", "No data to display.")
        return

    category_totals = defaultdict(float)

    for row in expenses:
        amount = row[1]
        category = row[2]
        category_totals[category] += amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Spending by Category")
    plt.show()


def show_monthly_chart():
    expenses = get_expenses()
    if not expenses:
        messagebox.showinfo("Info", "No data to display.")
        return

    monthly_totals = defaultdict(float)

    for row in expenses:
        amount = row[1]
        date = row[4]
        month = date[:7]
        monthly_totals[month] += amount

    months = list(monthly_totals.keys())
    totals = list(monthly_totals.values())

    plt.figure()
    plt.bar(months, totals)
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for row in get_expenses():
        tree.insert("", tk.END, values=row)

def add_expense_gui():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        date = date_entry.get()

        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        if not category:
            messagebox.showwarning("Error", "Category is required.")
            return

        add_expense(amount, category, description, date)
        refresh_table()
        clear_fields()
        messagebox.showinfo("Success", "Expense added!")

    except ValueError:
        messagebox.showerror("Error", "Invalid amount.")

def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Error", "Select an expense to delete.")
        return

    item = tree.item(selected[0])
    expense_id = item["values"][0]
    delete_expense(expense_id)
    refresh_table()

def clear_fields():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)


create_table()

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("750x500")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=0, column=2)
category_entry = tk.Entry(frame)
category_entry.grid(row=0, column=3)

tk.Label(frame, text="Description").grid(row=1, column=0)
description_entry = tk.Entry(frame)
description_entry.grid(row=1, column=1)

tk.Label(frame, text="Date (YYYY-MM-DD)").grid(row=1, column=2)
date_entry = tk.Entry(frame)
date_entry.grid(row=1, column=3)

tk.Button(frame, text="Add Expense", command=add_expense_gui).grid(row=2, column=1, pady=10)
tk.Button(frame, text="Delete Selected", command=delete_selected).grid(row=2, column=2)
tk.Button(frame, text="Category Chart", command=show_category_chart).grid(row=3, column=1)
tk.Button(frame, text="Monthly Chart", command=show_monthly_chart).grid(row=3, column=2)

columns = ("ID", "Amount", "Category", "Description", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill="both", expand=True)

refresh_table()

root.mainloop()
