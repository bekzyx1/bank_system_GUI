import customtkinter as ctk

#ctk.set_appearance_mode("light")

root = ctk.CTk()
root.geometry("1200x700")

#--- Main container ---
transactions_card = ctk.CTkFrame(root, corner_radius=15)
transactions_card.pack(fill="both", expand=True, padx=20, pady=20)

title = ctk.CTkLabel(
    transactions_card,
    text="Recent Transactions (12)",
    font=ctk.CTkFont(size=10, weight="bold")
)

title.pack(anchor="w", padx=20, pady=(20, 10))

table = ctk.CTkFrame(
    transactions_card,
    fg_color="transparent"
)

table.pack(fill="both", expand=True, padx=20, pady=(0, 20))

# Settings

table.grid_columnconfigure(0, weight=1)
table.grid_columnconfigure(1, weight=3)
table.grid_columnconfigure(2, weight=2)
table.grid_columnconfigure(3, weight=2)
table.grid_columnconfigure(4, weight=2)
table.grid_columnconfigure(5, weight=1)

headers = [
    "Date",
    "Description",
    "Category",
    "Account",
    "Status",
    "Amount"
]

for col, text in enumerate(headers):
    label = ctk.CTkLabel(
        table,
        text=text,
        font=ctk.CTkFont(weight="bold")
    )

    label.grid(
        row=0,
        column=col,
        padx=10,
        pady=10,
        sticky="w"
    )



#--- Data ---
transactions = [
    ("1/8/2025", "Cofee Shop", "Food & Dining",
     "Primary Checking", "Completed", "$5.75"),

    ("1/8/2025", "Gas Station", "Transportation",
     "Primary Checking", "Completed", "$35.15"),

    ("1/7/2025", "Grocery Store", "Food & Dining",
    "Primary Checking", "Completed", "75.31"),

    ("1/5/2025", "Salary Deposit", "Income",
     "Primary Chechking", "Completed", "+3500.00"),
]

#--- String ---

for row_num, transaction in enumerate(transactions, start=1):

    separator = ctk.CTkFrame(
        table,
        height=1,
        fg_color="#dddddd"
    )

    separator.grid(
        row=row_num * 2 - 1,
        column=0,
        columnspan=6,
        sticky="ew"
    )

    data_row = row_num * 2

    # Date

    ctk.CTkLabel(
        table,
        text=transaction[0]
    ).grid(
        row=data_row,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    # Description

    ctk.CTkLabel(
        table,
        text=transaction[1]
    ).grid(
        row=data_row,
        column=1,
        padx=10,
        pady=10,
        sticky="w"
    )

    # Category Badge

    category_frame = ctk.CTkFrame (
        table,
        corner_radius=13,
        height=28
    )

    category_frame.grid(
        row=data_row,
        column=2,
        padx=10,
        pady=5,
        sticky="w"
    )

    ctk.CTkLabel(
        category_frame,
        text=transaction[2]
    ).pack(
        padx=10,
        pady=3
    )

    # Account

    ctk.CTkLabel(
        table,
        text=transaction[3]
    ).grid(
        row=data_row,
        column=3,
        padx=10,
        pady=10,
        sticky="w"
    )

    # Status 

    status_frame = ctk.CTkFrame(
        table,
        fg_color="#d7f5df",
        corner_radius=15
    )

    status_frame.grid(
        row=data_row,
        column=4,
        padx=10,
        pady=5,
        sticky="w"
    )

    ctk.CTkLabel(
        status_frame,
        text=transaction[4],
        text_color="green"
    ).pack(
        padx=10,
        pady=3
    )

    #Amount

    amount = transaction[5]

    color = "green" if "+" in amount else "red"

    ctk.CTkLabel(
        table,
        text=amount,
        text_color=color
    ).grid(
        row=data_row,
        column=5,
        padx=10,
        pady=10,
        sticky="e"
    )

root.mainloop()



















