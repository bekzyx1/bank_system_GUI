import customtkinter as ctk
from PIL import Image
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import hashlib
from tkinter import messagebox


root = ctk.CTk()
root.geometry("500x400")
root.title("Login System")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

border = ctk.CTkFrame(root, width=5, fg_color="green")
border.grid(row=0, column=1, sticky="ns")

sidebar = ctk.CTkFrame(root, width=220, corner_radius=0)
sidebar.grid(row=0, column=0, sticky="ns")


logo = ctk.CTkLabel(sidebar, text="Secure Bank", font=ctk.CTkFont(size=20, weight="bold"))
logo.pack(pady=20)



container = ctk.CTkFrame(root)
container.grid(row=0, column=2, sticky="nsew")

dashboard_page = ctk.CTkFrame(container, fg_color="green")
account_page = ctk.CTkFrame(container, fg_color="gray")
transactions_page = ctk.CTkFrame(container, fg_color="transparent")
transfer_page = ctk.CTkFrame(container, fg_color="green")
analyze_page = ctk.CTkFrame(container, fg_color="#83855d")
profile_page = ctk.CTkFrame(container, fg_color="red")

def show_page(page):
    page.tkraise()

for page in (dashboard_page, account_page, transactions_page, transfer_page, analyze_page, profile_page):
    page.place(relwidth=1, relheight=1)

btn_dashboard = ctk.CTkButton(sidebar, text="Dashboard", command=lambda: show_page(dashboard_page))
btn_account = ctk.CTkButton(sidebar, text="Account", command=lambda: show_page(account_page))
btn_transactions = ctk.CTkButton(sidebar, text="Transactions", command=lambda: show_page(transactions_page))
btn_transfer= ctk.CTkButton(sidebar, text="Transfer", command=lambda: show_page(transfer_page))
btn_analyze = ctk.CTkButton(sidebar, text="Analytics", command=lambda: show_page(analyze_page))
btn_profile = ctk.CTkButton(sidebar, text="Profile", command=lambda: show_page(profile_page))

#for page in (dashboard_)

btn_dashboard.pack(pady=10)
btn_account.pack(pady=10)
btn_transactions.pack(pady=10)
btn_transfer.pack(pady=10)
btn_analyze.pack(pady=10)
btn_profile.pack(pady=10)


# --- Dashboard ---
#main = ctk.CTkFrame(dashboard_page)

header = ctk.CTkFrame(dashboard_page)
cards = ctk.CTkFrame(dashboard_page)
extra = ctk.CTkFrame(dashboard_page)
#extra.grid_rowconfigure(0, weight=1)
extra.grid_columnconfigure(0, weight=1)

header.pack(fill="x")
cards.pack(fill="both", expand=True)
extra.pack(fill="both", expand=True)

main_label = ctk.CTkLabel(header, text="Welcome back, bekzy!", font=ctk.CTkFont(size=25))
main_label.pack(anchor="w",padx=15, pady=15)

cards.grid_columnconfigure(0, weight=1)
cards.grid_columnconfigure(1, weight=1)

#----Cards----
card1 = ctk.CTkFrame(cards) # Total Balance
card1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

label = ctk.CTkLabel(card1, text="Total Balance")
label.pack(pady=15)

value = ctk.CTkLabel(card1, text="$11,353.00", font=("Arial", 31, "bold"))
value.pack(pady=(0, 35))

#---Monthly Income Card---
card2 = ctk.CTkFrame(cards) 
card2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

card2_label = ctk.CTkLabel(card2, text="Monthly Income")
card2_label.pack(pady=15)

card2_value = ctk.CTkLabel(card2, text="+$ 5,000.00", font=("Arial", 31, "bold"))
card2_value.pack(pady=(0, 35))
                           
#--- card 3 ---
card3 = ctk.CTkFrame(cards)
card3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

card3_label = ctk.CTkLabel(card3, text="Monthly Expenses")
card3_label.pack(pady=15)

card3_value = ctk.CTkLabel(card3, text="-$ 2,000.00", font=("Arial", 31, "bold"))
card3_value.pack(pady=(0, 35))

card4 = ctk.CTkFrame(cards)
card4.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

card4_label = ctk.CTkLabel(card4, text="Savings Goal")
card4_label.pack(pady=15)

card4_value = ctk.CTkLabel(card4, text="68%", font=("Arial", 31, "bold"))
card4_value.pack(pady=(0, 35))


#----Buttons----
btn_box = ctk.CTkFrame(cards)
btn_box.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# btn_box.grid_columnconfigure(0, weight=1)
# btn_box.grid_columnconfigure(1, weight=1)

btn_transfer = ctk.CTkButton(btn_box, text="Transfer", height=35)
btn_transfer.pack(side="left", pady=15, padx=15)

btn_pay = ctk.CTkButton(btn_box, text="Pay Bills", height=35)
btn_pay.pack(side="left", pady=15, padx=15)

btn_deposit = ctk.CTkButton(btn_box, text="Deposit", height=35)
btn_deposit.pack(side="left", pady=15, padx=15)

btn_statements = ctk.CTkButton(btn_box, text="View Statements", height=35)
btn_statements.pack(side="left", pady=15, padx=15)

transaction_frame = ctk.CTkFrame(extra)
transaction_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
transaction_frame.grid_columnconfigure(0, weight=1)
transaction_frame.grid_columnconfigure(1, weight=1)
def create_transaction(row, name, amount):


    # --- Name Label ---
    transaction_label_name = ctk.CTkLabel(transaction_frame, text=f"{name}", font=ctk.CTkFont(size=15, weight="bold"))
    transaction_label_name.grid(row=row, column=0, padx=10, sticky="w")

    # --- Amount Label ---
    transaction_label_amount = ctk.CTkLabel(transaction_frame, text=f"{amount}", font=ctk.CTkFont(size=15, weight="bold"))
    transaction_label_amount.grid(row=row, column=1, padx=10, sticky="e")

transaction = [
    ("bekzy", "$555.00"),
    ("shmegzy", "$1,300.000.00"),
    ("Nalog", "$4.00")
]

for row, (name, amount) in enumerate(transaction):
    create_transaction(row, name, amount)


#---Account Page---
#account_page.grid_rowconfigure(0, weight=0)
account_page.grid_rowconfigure(1, weight=0)
account_page.grid_rowconfigure(2, weight=0)

account_page.grid_columnconfigure(1, weight=1)
account_page.grid_columnconfigure(2, weight=1)

account_navbar = ctk.CTkFrame(account_page)
account_navbar.grid(row=0, column=1, pady=15, columnspan=2)


account_label = ctk.CTkLabel(account_navbar, text="Account Page", font=ctk.CTkFont(size=20, weight="bold"))
account_label.grid(row=0, column=0, padx=10, pady=(15, 0))

account_label2 = ctk.CTkLabel(account_navbar, text="Manage yout back accounts and view balances.")
account_label2.grid(row=1, column=0, padx=10, pady=(0, 15))

account_navbar_btn1 = ctk.CTkButton(account_navbar, text="Hide Balance", height=25)
account_navbar_btn1.grid(row=0, column=1, padx=5, pady=(25, 0))

account_navbar_btn2 = ctk.CTkButton(account_navbar, text="Add Account", height=25)
account_navbar_btn2.grid(row=0, column=2, padx=5, pady=(25, 0))

account_navbar_total_balance_1 = ctk.CTkLabel(account_navbar, text="Total Balance Across All Accounts", font=ctk.CTkFont(size=13))
account_navbar_total_balance_1.grid(row=2, column=0, padx=(0, 30), pady=(0, 15))

account_navbar_total_balance_2 = ctk.CTkLabel(account_navbar, text="$55,999.15", font=ctk.CTkFont(size=25, weight="bold"))
account_navbar_total_balance_2.grid(row=3, column=0, padx=(0, 30), pady=(0, 15))

#--- Primary Checking Card ---
account_card_1 = ctk.CTkFrame(account_page)
account_card_1.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")



account_card_1_text1 = ctk.CTkLabel(account_card_1, text="Primary Checking", font=ctk.CTkFont(size=15, weight="bold"))
account_card_1_text1.grid(row=0, column=0, pady=(15, 0))

account_card_1_text2 = ctk.CTkLabel(account_card_1, text="Checking ****1234", font=ctk.CTkFont(size=10, weight="bold"))
account_card_1_text2.grid(row=1, column=0, pady=(0, 15))


account_card_1_text3 = ctk.CTkLabel(account_card_1, text="Current Balance", font=ctk.CTkFont(size=10, weight="bold"))
account_card_1_text3.grid(row=2, column=0, pady=0)

account_card_1_text4 = ctk.CTkLabel(account_card_1, text="$11,353.00", font=ctk.CTkFont(size=15, weight="bold"))
account_card_1_text4.grid(row=3, column=0, pady=(0, 15))

account_card_1_text5 = ctk.CTkLabel(account_card_1, text="Interest Rate", font=ctk.CTkFont(size=10, weight="bold"))
account_card_1_text5.grid(row=4, column=0, pady=0)

account_card_1_text6 = ctk.CTkLabel(account_card_1, text="0.01% APY", font=ctk.CTkFont(size=15, weight="bold"))
account_card_1_text6.grid(row=5, column=0, pady=(0, 15))

account_card_1_btn1 = ctk.CTkButton(account_card_1, text="Transfer", height=25)
account_card_1_btn1.grid(row=6, column=0, pady=15, padx=10)

account_card_1_btn2 = ctk.CTkButton(account_card_1, text="View Statements", height=25)
account_card_1_btn2.grid(row=6, column=1, pady=15, padx=10)


#--- High Yield Savings Card ---
account_card_2 = ctk.CTkFrame(account_page)
account_card_2.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# account_card_2.grid_rowconfigure(1, weight=1)
# account_card_2.grid_columnconfigure(0, weight=1)

account_card_2_text1 = ctk.CTkLabel(account_card_2, text="High Yield Savings", font=ctk.CTkFont(size=15, weight="bold"))
account_card_2_text1.grid(row=0, column=0, pady=(15, 0))

account_card_2_text2 = ctk.CTkLabel(account_card_2, text="Savings ****5678", font=ctk.CTkFont(size=10))
account_card_2_text2.grid(row=1, column=0, pady=(0, 15))

account_card_2_text3 = ctk.CTkLabel(account_card_2, text="Current Balance", font=ctk.CTkFont(size=10))
account_card_2_text3.grid(row=2, column=0, pady=0)

account_card_2_text4 = ctk.CTkLabel(account_card_2, text="$25,000.00", font=ctk.CTkFont(size=15, weight="bold"))
account_card_2_text4.grid(row=3, column=0, pady=(0, 15))

account_card_2_text5 = ctk.CTkLabel(account_card_2, text="Interest Rate", font=ctk.CTkFont(size=10 ))
account_card_2_text5.grid(row=4, column=0, pady=0)

account_card_2_text6 = ctk.CTkLabel(account_card_2, text="0.50% APY", font=ctk.CTkFont(size=10, weight="bold"))
account_card_2_text6.grid(row=5, column=0, pady=(0, 15))

account_card_2_btn1 = ctk.CTkButton(account_card_2, text="Transfer", height=25)
account_card_2_btn1.grid(row=6, column=0, pady=15, padx=10)

account_card_2_btn2 = ctk.CTkButton(account_card_2, text="View Statements", height=25)
account_card_2_btn2.grid(row=6, column=1, pady=15, padx=10)

# Business Account Card
account_card_3 = ctk.CTkFrame(account_page)
account_card_3.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

account_card_3_text1 = ctk.CTkLabel(account_card_3, text="Business Account", font=ctk.CTkFont(size=15, weight="bold"))
account_card_3_text1.grid(row=0, column=0, pady=(15, 0))

account_card_3_text2 = ctk.CTkLabel(account_card_3, text="Business ****9013", font=ctk.CTkFont(size=13))
account_card_3_text2.grid(row=1, column=0, pady=(0, 15))

account_card_3_text3 = ctk.CTkLabel(account_card_3, text="Current Balance", font=ctk.CTkFont(size=13))
account_card_3_text3.grid(row=2, column=0, pady=0)

account_card_3_text4 = ctk.CTkLabel(account_card_3, text="$50,000.00", font=ctk.CTkFont(size=15, weight="bold"))
account_card_3_text4.grid(row=3, column=0, pady=(0, 15))

account_card_3_text5 = ctk.CTkLabel(account_card_3, text="Interest Rate", font=ctk.CTkFont(size=13))
account_card_3_text5.grid(row=4, column=0, pady=0)

account_card_3_text6 = ctk.CTkLabel(account_card_3, text="0.15% APY", font=ctk.CTkFont(size=13))
account_card_3_text6.grid(row=5, column=0, pady=(0, 15))

account_card_3_btn1 = ctk.CTkButton(account_card_3, text="Transfer", height=25)
account_card_3_btn1.grid(row=6, column=0, padx=10, pady=15)

account_card_3_btn2 = ctk.CTkButton(account_card_3, text="View Details", height=25)
account_card_3_btn2.grid(row=6, column=1, padx=10, pady=15)

#--- Emergency Fund ---
account_card_4 = ctk.CTkFrame(account_page)
account_card_4.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

# account_card_4.grid_rowconfigure(0, weight=1)
# account_card_4.grid_columnconfigure(1, weight=1)

account_card_4_text1 = ctk.CTkLabel(account_card_4, text="Emergency Fund", font=ctk.CTkFont(size=13, weight="bold"))
account_card_4_text1.grid(row=1, column=0, pady=(15, 0))

account_card_4_text2 = ctk.CTkLabel(account_card_4, text="Savings ****3355", font=ctk.CTkFont(size=13))
account_card_4_text2.grid(row=2, column=0, pady=(0, 15))

account_card_4_text3 = ctk.CTkLabel(account_card_4, text="Current Balance", font=ctk.CTkFont(size=15))
account_card_4_text3.grid(row=3, column=0, pady=0)

account_card_4_text4 = ctk.CTkLabel(account_card_4, text="$5,000.00", font=ctk.CTkFont(size=15, weight="bold"))
account_card_4_text4.grid(row=4, column=0, pady=(0, 15))

account_card_4_text5 = ctk.CTkLabel(account_card_4, text="Interest Rate", font=ctk.CTkFont(size=13))
account_card_4_text5.grid(row=5, column=0, pady=0)

account_card_4_text6 = ctk.CTkLabel(account_card_4, text="3.9% APY", font=ctk.CTkFont(size=13))
account_card_4_text6.grid(row=6, column=0, pady=(0, 15))

account_card_4_btn1 = ctk.CTkButton(account_card_4, text="Transfer", height=25)
account_card_4_btn1.grid(row=7, column=0, padx=10, pady=15)

account_card_4_btn2 = ctk.CTkButton(account_card_4, text="View Details", height=25)
account_card_4_btn2.grid(row=7, column=1, padx=10, pady=15)

#--- Account Footer ---
account_foot = ctk.CTkFrame(account_page)
account_foot.grid(row=8, column=1, padx=5, pady=15, sticky="nsew", columnspan=2)

account_foot.grid_columnconfigure(0, weight=1)
account_foot.grid_columnconfigure(1, weight=1)
account_foot.grid_columnconfigure(2, weight=1)
account_foot.grid_columnconfigure(3, weight=1)

account_foot_label = ctk.CTkLabel(account_foot, text="Account Services", font=ctk.CTkFont(size=15, weight="bold"))
account_foot_label.grid(row=0, column=0, pady=15)

account_foot_btn1 = ctk.CTkButton(account_foot, text="Open New Account", height=35, width=15 )
account_foot_btn1.grid(row=1, column=0, padx=5, pady=(5, 15))

account_foot_btn2 = ctk.CTkButton(account_foot, text="Other Checks", height=35, width=15)
account_foot_btn2.grid(row=1, column=1, padx=5, pady=(5, 15))

account_foot_btn3 = ctk.CTkButton(account_foot, text="Account Statements", height=35, width=15)
account_foot_btn3.grid(row=1, column=2, padx=5, pady=(5, 15))

account_foot_btn4 = ctk.CTkButton(account_foot, text="Account Settings", height=35, width=15)
account_foot_btn4.grid(row=1, column=3, padx=5, pady=(5, 15))



#--- Transactions ---
transactions_label = ctk.CTkLabel(transactions_page, text="Transactions Page", font=ctk.CTkFont(size=20, weight="bold"))
transactions_label.pack(pady=35)

title_transaction = ctk.CTkLabel(
    transactions_page,
    text="Recent Transaction (12)",
    font=ctk.CTkFont(size=15, weight="bold")
)

table = ctk.CTkFrame(
    transactions_page,
    fg_color="transparent"
)

table.pack(fill="both", expand=True, padx=20, pady=10)

table.grid_columnconfigure(0, weight=1)
table.grid_columnconfigure(1, weight=3)
table.grid_columnconfigure(2, weight=2)
table.grid_columnconfigure(3, weight=2)
table.grid_columnconfigure(4, weight=2)
table.grid_columnconfigure(5, weight=1)

table_headers = [
    "Date",
    "Description",
    "Category",
    "Account",
    "Status",
    "Amount"
]

for col, text in enumerate(table_headers):
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
    ("1/8/2025", "Coffee Shop", "Food & Dining",
     "Primary Checking", "Completed", "$5.35"),

    ("1/8/2025", "Gas Station", "Transportation",
     "Primary Checking", "Completed", "$45.20"),

    ("1/8/2025", "Transfer from Checking", "Transfer",
     "Primary Cheking", "Completed", "$85.23"),

     ("1/5/2025", "Salary Deposit", "Income",
     "Primary Chechking", "Completed", "+3500.00"),
]

for row_num, transaction in enumerate(transactions, start=1):


    #Date

    ctk.CTkLabel(
        table,
        text=transaction[0]
    ).grid(
        row=row_num,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    #Description

    ctk.CTkLabel(
        table,
        text=transaction[1]
    ).grid(
        row=row_num,
        column=1,
        padx=10,
        pady=10,
        sticky="w"
    )

    # Category Badge

    category_frame = ctk.CTkFrame(
        table,
        corner_radius=13,
        height=28
    )

    category_frame.grid(
        row=row_num,
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

    #Account

    ctk.CTkLabel(
        table,
        text=transaction[3]
    ).grid(
        row=row_num,
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
        row=row_num,
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
        row=row_num,
        column=5,
        padx=(20,0),
        pady=10,
        sticky="w"
    )



#--- Transfer ---
transfer_page.grid_rowconfigure(0, weight=0)
transfer_page.grid_columnconfigure(0, weight=3)
transfer_page.grid_rowconfigure(1, weight=1)
transfer_page.grid_columnconfigure(1, weight=1)

transfer_header = ctk.CTkFrame(transfer_page)
transfer_header.grid(row=0, column=0,padx=15, pady=15, sticky="nsew", columnspan=2)

transfer_header_text1 = ctk.CTkLabel(
    transfer_header, 
    text="Transfer Money",
    font=ctk.CTkFont(size=15, weight="bold")
    ).grid(
        row=0,
        column=0,
        padx=(15,0),
        pady=(15, 0),
        sticky="w"
    )

transfer_header_text2 = ctk.CTkLabel(
    transfer_header,
    text="Send money between accounts to external recipients.",
    font=ctk.CTkFont(size=13),
    text_color="#7E7E84"
).grid(
    row=1,
    column=0,
    padx=(15, 0),
    pady=(0, 15),
)

transfer_leaf_container = ctk.CTkFrame(
    transfer_page,
)

transfer_leaf_container.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")

transfer_leaf_amounts = ctk.CTkFrame(transfer_page)
transfer_leaf_amounts.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")

transfer_leaf_amounts_label = ctk.CTkLabel(transfer_leaf_amounts, text="Quick Amounts", font=ctk.CTkFont(size=15, weight="bold"))
transfer_leaf_amounts_label.grid(row=0, column=0, padx=15, pady=15)

transfer_leaf_amounts_btn1 = ctk.CTkButton(transfer_leaf_amounts, text="$25")
transfer_leaf_amounts_btn1.grid(row=1, column=0, padx=15, pady=15)

transfer_leaf_amounts_btn2 = ctk.CTkButton(transfer_leaf_amounts, text="$50")
transfer_leaf_amounts_btn2.grid(row=1, column=1, padx=15, pady=15)

transfer_leaf_amounts_btn3 = ctk.CTkButton(transfer_leaf_amounts, text="$100")
transfer_leaf_amounts_btn3.grid(row=2, column=0, padx=15, pady=15)

transfer_leaf_amounts_btn4 = ctk.CTkButton(transfer_leaf_amounts, text="$500")
transfer_leaf_amounts_btn4.grid(row=2, column=1, padx=15, pady=15)

# --- page 1 --- New Transfer

transfer_leaf_1 = ctk.CTkFrame(
    transfer_leaf_container, 
    )

transfer_leaf_1_header = ctk.CTkFrame(transfer_leaf_1)
transfer_leaf_1_header.grid(row=0, column=0, padx=5, pady=15)

transfer_leaf_1_header_label = ctk.CTkLabel(transfer_leaf_1_header, text="Transfer Details", font=ctk.CTkFont(size=25))
transfer_leaf_1_header_label.grid(row=0, column=0, padx=5, pady=15)

button_frame = ctk.CTkFrame(transfer_leaf_1_header)
button_frame.grid(row=1, column=0)

transfer_leaf_1_header_btn1 = ctk.CTkButton(
    button_frame,
    text="Between My Accounts",
    height=55
)

transfer_leaf_1_header_btn1.grid(row=1, column=0, padx=5, pady=10, )

transfer_leaf_1_header_btn2 = ctk.CTkButton(
    button_frame,
    text="To Someone Else",
    width=130,
    height=55
)

transfer_leaf_1_header_btn2.grid(row=1, column=1, padx=5, pady=10)

# --- page 2 --- Scheduled Transfers
transfer_leaf_2 = ctk.CTkFrame(
    transfer_leaf_container,
    )

def show_transfer_page(page):
    if page == "New Transfer":
        transfer_leaf_1.tkraise()
    else:
        transfer_leaf_2.tkraise()

for page in (transfer_leaf_1, transfer_leaf_2):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)


transfer_header_segment = ctk.CTkSegmentedButton(
    transfer_header,
    values=["New Transfer", "Scheduled Transfers"],
    command=show_transfer_page
).grid(
    row=2,
    column=0,
    padx=(15, 0),
    pady=(0,15),
    sticky="w"
)

#--- page 1 elements ---

transfer_leaf_1_header_label2 = ctk.CTkLabel(transfer_leaf_1_header, text="From Account")
transfer_leaf_1_header_label2.grid(row=2, column=0, padx=15, pady=(15, 5))

transfer_leaf_1_header_entry1 = ctk.CTkEntry(transfer_leaf_1_header, placeholder_text="Select source account", width=275, height=35)
transfer_leaf_1_header_entry1.grid(row=3, column=0, padx=15, pady=(0, 15))

transfer_leaf_1_header_label3 = ctk.CTkLabel(transfer_leaf_1_header, text="To Account", font=ctk.CTkFont(size=13, weight="bold"))
transfer_leaf_1_header_label3.grid(row=4, column=0, padx=15, pady=(15, 5))


transfer_leaf_1_header_opmenu = ctk.CTkOptionMenu(
    transfer_leaf_1_header, 
    values=["Primary Checking - $8,567.89",
            "High Yield Savings 0 $15,430.5",
            "Business Account - $25,890.75"], width=275, height=55
    )
transfer_leaf_1_header_opmenu.grid(row=5, column=0, padx=5, pady=(0, 15))

transfer_leaf_1_header_label4 = ctk.CTkLabel(transfer_leaf_1_header, text="Amount", font=ctk.CTkFont(size=15, weight="bold"))
transfer_leaf_1_header_label4.grid(row=6, column=0, padx=5, pady=(0,0))

transfer_leaf_1_header_entry2 = ctk.CTkEntry(transfer_leaf_1_header, placeholder_text="$ 0.00", width=275, height=35)
transfer_leaf_1_header_entry2.grid(row=7, column=0, padx=5, pady=(5, 15))

transfer_leaf_1_header_label5 = ctk.CTkLabel(transfer_leaf_1_header, text="Memo (Optional)")
transfer_leaf_1_header_label5.grid(row=8, column=0, pady=(5, 10))

transfer_leaf_1_header_entry3 = ctk.CTkTextbox(transfer_leaf_1_header, width=275, height=75)
transfer_leaf_1_header_entry3.grid(row=9, column=0, pady=(0, 15))

# --- page 2 elements ---
transfer_leaf_2.grid_columnconfigure(0, weight=1)

transfer_leaf_2_container = ctk.CTkFrame(transfer_leaf_2, fg_color="green")
transfer_leaf_2_container.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

transfer_leaf_2_container.grid_columnconfigure(0, weight=1)

transfer_leaf_2_container_header= ctk.CTkFrame(transfer_leaf_2_container)
transfer_leaf_2_container_header.grid(row=0, column=0, padx=5, pady=5, sticky="we")

transfer_leaf_2_container_header.grid_columnconfigure(0, weight=1)
transfer_leaf_2_container_header.grid_columnconfigure(1, weight=1)

# --- Scheduled Transfers ---

transfer_leaf_2_header_label = ctk.CTkLabel(transfer_leaf_2_container_header, text="Scheduld Transfer", font=ctk.CTkFont(size=15, weight="bold"))
transfer_leaf_2_header_label.grid(row=0, column=0, padx=5, pady=(0, 0), sticky="w")

transfer_leaf_2_header_container_btn = ctk.CTkButton(transfer_leaf_2_container_header, text="Add Scheduld Transfer", font=ctk.CTkFont(size=15), height=35)
transfer_leaf_2_header_container_btn.grid(row=0, column=1, padx=5, pady=5, sticky="e")

#      Scheduled Transfers, frame 1 ---

transfer_leaf_2_frame_1 = ctk.CTkFrame(transfer_leaf_2_container)
transfer_leaf_2_frame_1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

transfer_leaf_2_frame_1_label_frame = ctk.CTkFrame(transfer_leaf_2_frame_1)
transfer_leaf_2_frame_1_label_frame.grid(row=0, column=0, padx=5, pady=5)

transfer_leaf_2_label_1 = ctk.CTkLabel(transfer_leaf_2_frame_1_label_frame, text="Transfer to High Yield Savings")
transfer_leaf_2_label_1.grid(row=0, column=0, padx=5, pady=(5,0))

transfer_leaf_2_label_2 = ctk.CTkLabel(transfer_leaf_2_frame_1_label_frame, text="Monthly*Next: 2025-02-01")
transfer_leaf_2_label_2.grid(row=1, column=0, padx=5, pady=(0,5))

#---------------------------------------------------------------

# ____ btn box 1 configure

transfer_leaf_2_frame_1.grid_columnconfigure(1, weight=1)

transfer_leaf_2_btn_box_1 = ctk.CTkFrame(transfer_leaf_2_frame_1)
transfer_leaf_2_btn_box_1.grid(row=0, column=1, padx=5, pady=5, sticky="e")

transfer_leaf_2_btn_box_1_label = ctk.CTkLabel(transfer_leaf_2_btn_box_1, text="$500")
transfer_leaf_2_btn_box_1_label.grid(row=0, column=1, padx=5, pady=5)

transfer_leaf_2_btn_box_1_btn1 = ctk.CTkButton(transfer_leaf_2_btn_box_1, text="Edit")
transfer_leaf_2_btn_box_1_btn1.grid(row=1, column=0, padx=5, pady=5)

transfer_leaf_2_btn_box_1_btn2 = ctk.CTkButton(transfer_leaf_2_btn_box_1, text="Cancel")
transfer_leaf_2_btn_box_1_btn2.grid(row=1, column=1, padx=5, pady=5)

#     Scheduled Transfers, frame 2 ---
transfer_leaf_2_frame_2 = ctk.CTkFrame(transfer_leaf_2_container, fg_color="white") # white
transfer_leaf_2_frame_2.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

transfer_leaf_2_frame_2_label_frame = ctk.CTkFrame(transfer_leaf_2_frame_2)
transfer_leaf_2_frame_2_label_frame.grid(row=0, column=0, padx=5, pady=(5, 5))

transfer_leaf_2_frame_2_label_1 = ctk.CTkLabel(transfer_leaf_2_frame_2_label_frame, text="Transfer to Emergency Fund")
transfer_leaf_2_frame_2_label_1.grid(row=0, column=0, padx=5, pady=5)

transfer_leaf_2_frame_2_label_2 = ctk.CTkLabel(transfer_leaf_2_frame_2_label_frame, text="Bi-weekly*Next: 2025-01-15")
transfer_leaf_2_frame_2_label_2.grid(row=1, column=0, padx=5, pady=(0, 15))

# _____ btn box 2 configure

transfer_leaf_2_frame_2.grid_columnconfigure(1, weight=1)

transfer_leaf_2_btn_box_2 = ctk.CTkFrame(transfer_leaf_2_frame_2)
transfer_leaf_2_btn_box_2.grid(row=0, column=1, padx=5, pady=5, sticky="e")

transfer_leaf_2_btn_box_2_label = ctk.CTkLabel(transfer_leaf_2_btn_box_2, text="$200")
transfer_leaf_2_btn_box_2_label.grid(row=0, column=1, padx=5, pady=(5, 0))

transfer_leaf_2_btn_box_2_btn1 = ctk.CTkButton(transfer_leaf_2_btn_box_2, text="Edit")
transfer_leaf_2_btn_box_2_btn1.grid(row=1, column=0, padx=5, pady=(0, 5))

transfer_leaf_2_btn_box_2_btn2 = ctk.CTkButton(transfer_leaf_2_btn_box_2, text="Cancel")
transfer_leaf_2_btn_box_2_btn2.grid(row=1, column=1, padx=5, pady=(0, 5))


# Section - Financial Analytics
# analyze_page.grid_rowconfigure(0, weight=1)
analyze_page.grid_columnconfigure(0, weight=1)

analyze_header = ctk.CTkFrame(analyze_page)
analyze_header.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

analyze_header.grid_columnconfigure(1, weight=1)

analyze_header_text_1 = ctk.CTkLabel(analyze_header, text="Financial Analytics", font=ctk.CTkFont(size=25, weight="bold"))
analyze_header_text_1.grid(row=0, column=0, padx=5, pady=(0, 5))

analyze_header_text_2 = ctk.CTkLabel(analyze_header, text="Track your spending patterns and financial goals.", font=ctk.CTkFont(size=15))
analyze_header_text_2.grid(row=1, column=0, padx=5, pady=(0, 5))

analyze_header_drop_menu = ctk.CTkOptionMenu(analyze_header, values=["Last Months", "Last 3 Months", "Last 6 Months", "Last Year"])
analyze_header_drop_menu.grid(row=0, column=1, padx=5, pady=(20, 0), sticky="e")

# Analyze Cards
analyze_cards = ctk.CTkFrame(analyze_page)
analyze_cards.grid_columnconfigure(0, weight=1)
analyze_cards.grid_columnconfigure(1, weight=1)
analyze_cards.grid_columnconfigure(2, weight=1)
analyze_cards.grid_columnconfigure(3, weight=1)
analyze_cards.grid(row=1, column=0, sticky="nsew")

# income
analyze_income_card = ctk.CTkFrame(analyze_cards)
analyze_income_card_frame_top = ctk.CTkFrame(analyze_income_card)
analyze_income_card_frame_top_label = ctk.CTkLabel(analyze_income_card_frame_top, text="Avg Monthly Income")
analyze_income_card_frame_top_icon = ctk.CTkLabel(analyze_income_card_frame_top, text="#")
analyze_income_card_frame_bottom = ctk.CTkFrame(analyze_income_card)
analyze_income_card_frame_bottom_text_1 = ctk.CTkLabel(analyze_income_card_frame_bottom, text="$4,333")
analyze_income_card_frame_bottom_text_2 = ctk.CTkLabel(analyze_income_card_frame_bottom, text="+5.2% from last period")



# expenses
analyze_expenses_card = ctk.CTkFrame(analyze_cards)
analyze_expenses_card_frame_top = ctk.CTkFrame(analyze_expenses_card)
analyze_expenses_card_frame_top_label = ctk.CTkLabel(analyze_expenses_card_frame_top, text="Avg Monthly Expenses")
analyze_expenses_card_frame_top_icon = ctk.CTkLabel(analyze_expenses_card_frame_top, text="#")
analyze_expenses_card_frame_bottom = ctk.CTkFrame(analyze_expenses_card)
analyze_expenses_card_frame_bottom_text_1 = ctk.CTkLabel(analyze_expenses_card_frame_bottom, text="$3,235")
analyze_expenses_card_frame_bottom_text_2 = ctk.CTkLabel(analyze_expenses_card_frame_bottom, text="-2.1% from last period")



# savings
analyze_savings_card = ctk.CTkFrame(analyze_cards)
analyze_savings_card_frame_top = ctk.CTkFrame(analyze_savings_card)
analyze_savings_card_frame_top_label = ctk.CTkLabel(analyze_savings_card_frame_top, text="Savings Rate")
analyze_savings_card_frame_top_icon = ctk.CTkLabel(analyze_savings_card_frame_top, text="#")
analyze_savings_card_frame_bottom = ctk.CTkFrame(analyze_savings_card)
analyze_savings_card_frame_bottom_text_1 = ctk.CTkLabel(analyze_savings_card_frame_bottom, text="25.3%")
analyze_savings_card_frame_bottom_text_2 = ctk.CTkLabel(analyze_savings_card_frame_bottom, text="+3.1% from last period")



# goals
analyze_goal_card = ctk.CTkFrame(analyze_cards)
analyze_goal_card_frame_top = ctk.CTkFrame(analyze_goal_card)
analyze_goal_card_frame_top_label = ctk.CTkLabel(analyze_goal_card_frame_top, text="Savings Goal")
analyze_goal_card_frame_top_icon = ctk.CTkLabel(analyze_goal_card_frame_top, text="#")
analyze_goal_card_frame_bottom = ctk.CTkFrame(analyze_goal_card)
analyze_goal_card_frame_bottom_text_1 = ctk.CTkLabel(analyze_goal_card_frame_bottom, text="68%")
analyze_goal_card_frame_bottom_text_2 = ctk.CTkLabel(analyze_goal_card_frame_bottom, text="$6,800 of $10,000 goal")




analyze_income_card.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
analyze_expenses_card.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
analyze_savings_card.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
analyze_goal_card.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

analyze_income_card.grid_rowconfigure(0, weight=1)
analyze_income_card.grid_columnconfigure(0, weight=1)
analyze_expenses_card.grid_rowconfigure(0, weight=1)
analyze_expenses_card.grid_columnconfigure(0, weight=1)
analyze_savings_card.grid_rowconfigure(0, weight=1)
analyze_savings_card.grid_columnconfigure(0, weight=1)
analyze_goal_card.grid_rowconfigure(0, weight=1)
analyze_goal_card.grid_columnconfigure(0, weight=1)

# page cards configure
analyze_income_card_frame_top.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
analyze_income_card_frame_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
analyze_expenses_card_frame_top.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
analyze_expenses_card_frame_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
analyze_savings_card_frame_top.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
analyze_savings_card_frame_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
analyze_goal_card_frame_top.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
analyze_goal_card_frame_bottom.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
# cards elements
# card 1 "income"
analyze_income_card_frame_top_label.grid(row=0, column=0, padx=5, pady=5)
analyze_income_card_frame_top_icon.grid(row=0, column=1, padx=(5,0), pady=5)
analyze_income_card_frame_bottom_text_1.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="w")
analyze_income_card_frame_bottom_text_2.grid(row=2, column=0, padx=5, pady=(0, 5))
# card 2 "expenses"
analyze_expenses_card_frame_top_label.grid(row=0, column=0, padx=5, pady=5)
analyze_expenses_card_frame_top_icon.grid(row=0, column=1, padx=(5, 5), pady=5)
analyze_expenses_card_frame_bottom_text_1.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="w")
analyze_expenses_card_frame_bottom_text_2.grid(row=2, column=0, padx=5, pady=(0, 5))
# card 3 "savings"
analyze_savings_card_frame_top_label.grid(row=0, column=0, padx=5, pady=5)
analyze_savings_card_frame_top_icon.grid(row=0, column=1, padx=5, pady=5)
analyze_savings_card_frame_bottom_text_1.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="w")
analyze_savings_card_frame_bottom_text_2.grid(row=2, column=0, padx=5, pady=(0, 5))
#card 4 "goal"
analyze_goal_card_frame_top_label.grid(row=0, column=0, padx=5, pady=5)
analyze_goal_card_frame_top_icon.grid(row=0, column=1, padx=5, pady=5)
analyze_goal_card_frame_bottom_text_1.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="w")
analyze_goal_card_frame_bottom_text_2.grid(row=2, column=0, padx=5, pady=(0, 5))



# BIG frame for Analyze Page
analyze_graphic_system = ctk.CTkFrame(analyze_page)
analyze_graphic_system.grid(row=3, column=0, padx=5, pady=5)

analyze_page.grid_rowconfigure(3, weight=1)
analyze_page.grid_columnconfigure(0, weight=1)

analyze_graphic_system.grid_rowconfigure(1, weight=1)
analyze_graphic_system.grid(
    row=3,
    column=0,
    sticky="nsew"
)

analyze_graphic_system.grid_rowconfigure(0, weight=1)
analyze_graphic_system.grid_columnconfigure(0, weight=1)

# Overview page
analyze_graphic_system_overview = ctk.CTkFrame(analyze_graphic_system)
# analyze_graphic_system_overview.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Spendind page
analyze_graphic_system_spending = ctk.CTkFrame(analyze_graphic_system, fg_color="gray")
# analyze_graphic_system_spending.grid(row=0, column=0, padx=5, pady=5)

# Settings
analyze_graphic_system_savings = ctk.CTkFrame(analyze_graphic_system, fg_color="white")
# analyze_graphic_system_savings.grid(row=0, column=5, padx=5, pady=5)

# Trends
analyze_graphic_system_trends = ctk.CTkFrame(analyze_graphic_system, fg_color="green")
# analyze_graphic_system_trends.grid(row=0, column=5, padx=5, pady=5)

# Analyze Segment Button
def analyze_show_pages(page):
    if page == "Overview":
        analyze_graphic_system_overview.tkraise()
    elif page == "Spending":
        analyze_graphic_system_spending.tkraise()
    elif page == "Savings":
        analyze_graphic_system_savings.tkraise()
    elif page == "Trends":
        analyze_graphic_system_trends.tkraise()

for page in (analyze_graphic_system_overview, analyze_graphic_system_spending, analyze_graphic_system_savings, analyze_graphic_system_trends):
    page.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        


analyze_btn_box = ctk.CTkSegmentedButton(analyze_page, values=["Overview", "Spending", "Savings", "Trends"], command=analyze_show_pages)
analyze_btn_box.grid(row=2, column=0, padx=5, pady=5, sticky="w")



analyze_income_graphic_frame = ctk.CTkFrame(analyze_graphic_system_overview)
analyze_income_graphic_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nsew")

analyze_graphic_system_overview.grid_columnconfigure(0, weight=1)
analyze_graphic_system_overview.grid_columnconfigure(1, weight=1)
analyze_graphic_system_overview.grid_rowconfigure(0, weight=1)

analyze_graphic_frame_title = ctk.CTkLabel(analyze_income_graphic_frame, text="Income vs Expenses", font=("Arial", 18, "bold"))
analyze_graphic_frame_title.pack(anchor="w", padx=15, pady=15)

# Figure "Income vs Expenses" graph
analyze_graphic_frame_figure = Figure(figsize=(6, 4), dpi=100)
analyze_ax1 = analyze_graphic_frame_figure.add_subplot(111)

months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]

income = [4200, 4500, 4300, 4100, 4600, 4250]
expenses = [3100, 3300, 3400, 3200, 3500, 2900]

x = list(range(len(months)))

analyze_ax1.bar(
    [i + 0 for i in x],
    income,
    width=0.4,
    color="#30710D"
)

analyze_ax1.bar(
    [i + 0.4 for i in x],
    expenses,
    width=0.4,
    color="#ef4444"
)

analyze_ax1.set_xticks(x)
analyze_ax1.set_xticklabels(months)

analyze_ax1.set_ylim(0, 6000)

analyze_ax1.grid(True, linestyle="--", alpha=0.3)

analyze_ax1.set_axisbelow(True)

canvas1 = FigureCanvasTkAgg(analyze_graphic_frame_figure, master=analyze_income_graphic_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)

# Right Graph Frame

balance_frame = ctk.CTkFrame(analyze_graphic_system_overview)
balance_frame.grid(
    row=0,
    column=1,
    padx=(5, 10),
    pady=10,
    sticky="nsew"
)

balance_title = ctk.CTkLabel(
    balance_frame,
    text="Account Balance Trend",
    font=("Arial", 18, "bold")
)
balance_title.pack(anchor="w", padx=15, pady=(15, 0))

fig2 = Figure(figsize=(6, 4), dpi=100)
ax2 = fig2.add_subplot(111)

weeks = [
    "Jan 1",
    "Jan 8",
    "Jan 15",
    "Jan 22",
    "Jan 29",
    "Feb 5",
    "Feb 12",
    "Feb 19",
    "Feb 29",
    "Mar 5"
]

balance = [
    8500,
    9200,
    8800,
    9500,
    8900,
    9800,
    9200,
    10100,
    9600,
    10500,
]

x2 = list(range(len(weeks)))

ax2.plot(
    x2,
    balance,
    linewidth=2
)

ax2.fill_between(
    x2,
    balance,
    alpha=0.3
)

ax2.set_xticks(x2)
ax2.set_xticklabels(
    weeks,
    rotation=0
)

ax2.set_ylim(0, 12000)

ax2.grid(
    True,
    linestyle='--',
    alpha=0.3
)

ax2.set_axisbelow(True)

canvas2 = FigureCanvasTkAgg(
    fig2,
    master=balance_frame
)

canvas2.draw()
canvas2.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)



# Father grid configurations
profile_page.grid_columnconfigure(0, weight=1)
profile_page.grid_rowconfigure(1, weight=1)


# Profile page
profile_page_header = ctk.CTkFrame(profile_page)
profile_page_header_text_1 = ctk.CTkLabel(profile_page_header, text="Profile Settings", font=("Italic", 19, "bold"))
profile_page_header_text_2 = ctk.CTkLabel(profile_page_header, text="Manage your account settings and preferences", font=ctk.CTkFont(size=11, weight="bold"))
profile_page_person_info = ctk.CTkFrame(profile_page)
profile_page_person_info_Profile = ctk.CTkFrame(profile_page_person_info, fg_color="white")
profile_page_person_info_Security = ctk.CTkFrame(profile_page_person_info, fg_color="#fcba03")
profile_page_person_info_Notifications = ctk.CTkFrame(profile_page_person_info, fg_color="green")
profile_page_person_info_Privacy = ctk.CTkFrame(profile_page_person_info, fg_color="gray")

#Profile reg page
profile_page_person_info_Profile_header = ctk.CTkFrame(profile_page_person_info_Profile)
#profile_page_person_info_Profile_header_icon = ctk.CTkLabel(profile_page_person_info_Profile_header, text="#")
profile_page_person_info_Profile_header_label = ctk.CTkLabel(profile_page_person_info_Profile_header, text="Personal Information")

#Profile avatar
profile_page_person_avatar_frame_1 = ctk.CTkFrame(profile_page_person_info_Profile)
profile_page_person_avatar_frame_1.grid(row=1, column=1, padx=5, pady=5)

save_btn = False

def clickBtn():
    global save_btn

    save_btn = not save_btn

    if save_btn:
        profile_page_person_info_Profile_header_btn_edit.grid_forget()
        profile_page_person_info_Profile_header_btn_save.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
    else:
        profile_page_person_info_Profile_header_btn_save.grid_forget()
        profile_page_person_info_Profile_header_btn_edit.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

profile_page_person_info_Profile_header_btn_edit = ctk.CTkButton(profile_page_person_info_Profile_header, text="Edit Profile", command=clickBtn)
profile_page_person_info_Profile_header_btn_save = ctk.CTkButton(profile_page_person_info_Profile_header, text="Save Change", command=clickBtn)
#Inputs nickname
profile_page_person_info_Profile_nickname_frame = ctk.CTkFrame(profile_page_person_info_Profile)
profile_page_person_info_Profile_nickname_frame_name_text = ctk.CTkLabel(profile_page_person_info_Profile_nickname_frame, text="First Name")
profile_page_person_info_Profile_nickname_frame_lastname_text = ctk.CTkLabel(profile_page_person_info_Profile_nickname_frame, text="Last Name")
profile_page_person_info_Profile_nickname_frame_name_input = ctk.CTkEntry(profile_page_person_info_Profile_nickname_frame, placeholder_text="name")
profile_page_person_info_Profile_nickname_frame_lastname_input = ctk.CTkEntry(profile_page_person_info_Profile_nickname_frame, placeholder_text="last name")
#inputs other
profile_page_person_info_Profile_inputs_frame = ctk.CTkFrame(profile_page_person_info_Profile)
profile_page_person_info_Profile_inputs_frame_email_address_text = ctk.CTkLabel(profile_page_person_info_Profile_inputs_frame, text="Email Address")
profile_page_person_info_Profile_inputs_frame_email_address_input = ctk.CTkEntry(profile_page_person_info_Profile_inputs_frame, placeholder_text="paloncha@gmail.com")
profile_page_person_info_Profile_inputs_frame_phone_number_text = ctk.CTkLabel(profile_page_person_info_Profile_inputs_frame, text="Phone Number")
profile_page_person_info_Profile_inputs_frame_phone_number_input = ctk.CTkEntry(profile_page_person_info_Profile_inputs_frame, placeholder_text="+998 00-111-11-11")
profile_page_person_info_Profile_inputs_frame_address_text = ctk.CTkLabel(profile_page_person_info_Profile_inputs_frame, text="Address")
profile_page_person_info_Profile_inputs_frame_address_input = ctk.CTkEntry(profile_page_person_info_Profile_inputs_frame, placeholder_text="123 Ipak Yuli, City, State 12345")
profile_page_person_info_Profile_inputs_frame_date_of_birth_text = ctk.CTkLabel(profile_page_person_info_Profile_inputs_frame, text="Date of Birth")
profile_page_person_info_Profile_inputs_frame_date_of_birth = ctk.CTkEntry(profile_page_person_info_Profile_inputs_frame, placeholder_text="01 / 01 / 1990")




def show_profile_menu(page):
    if page == "Profile":
        profile_page_person_info_Profile.tkraise()
    elif page == "Security":
        profile_page_person_info_Security.tkraise()
    elif page == "Notifications":
        profile_page_person_info_Notifications.tkraise()
    elif page == "Privacy":
        profile_page_person_info_Privacy.tkraise()
    else:
        profile_page_person_info_Profile.tkraise()

for page in (profile_page_person_info_Profile, profile_page_person_info_Security, profile_page_person_info_Notifications, profile_page_person_info_Privacy):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)
        
profile_page_header_option = ctk.CTkSegmentedButton(profile_page_header, values=["Profile", "Security", "Notifications", "Privacy"], command=show_profile_menu)

# childrens grid configurations

#Grids
profile_page_header.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
profile_page_header_text_1.grid(row=0, column=0, padx=5, pady=(5, 0))
profile_page_header_text_2.grid(row=1, column=0, padx=5, pady=(0, 15))
profile_page_header_option.grid(row=2, column=0, padx=5, pady=5)
profile_page_person_info.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Profile grides
profile_page_person_info_Profile_header.grid(row=0, column=0, padx=5, pady=5)

profile_page_person_info_Profile_header_label.grid(row=0, column=1, padx=(15, 0), pady=5)
profile_page_person_info_Profile_header_btn_edit.grid(row=0, column=3, padx=5, pady=5)
# Profile inputs grides
profile_page_person_info_Profile_inputs_frame.grid(row=1, column=0, padx=5, pady=5)
profile_page_person_info_Profile_inputs_frame_email_address_text.grid(row=0, padx=5, pady=(5, 0))
profile_page_person_info_Profile_inputs_frame_email_address_input.grid(row=1, padx=5, pady=(0, 5))
profile_page_person_info_Profile_inputs_frame_phone_number_text.grid(row=2, column=0, padx=5, pady=(5, 0))
profile_page_person_info_Profile_inputs_frame_phone_number_input.grid(row=3, column=0, padx=5, pady=(0, 5))
profile_page_person_info_Profile_inputs_frame_address_text.grid(row=4, column=0, padx=5, pady=(5, 0))
profile_page_person_info_Profile_inputs_frame_address_input.grid(row=5, column=0, padx=5, pady=(0, 5))
profile_page_person_info_Profile_inputs_frame_date_of_birth_text.grid(row=6, column=0, padx=5, pady=(5, 0))
profile_page_person_info_Profile_inputs_frame_date_of_birth.grid(row=7, column=0, padx=5, pady=(0, 5))

img = ctk.CTkImage(light_image=Image.open("avatar.png"), size=(115, 115))
profile_page_person_avatar_frame_1_avatar = ctk.CTkLabel(profile_page_person_avatar_frame_1, image=img, text="")
profile_page_person_avatar_frame_1_avatar.grid(row=0, column=0, padx=5, pady=5)

def change_img():
    path = filedialog.askopenfilename(initialdir="",
        filetypes=[("Images", "*.png *.jpg *.jpeg *.webp")]
    )

    if not path:
        return
    
    new_img = ctk.CTkImage(light_image=Image.open(path), size=(115, 115))
    profile_page_person_avatar_frame_1_avatar.configure(image=new_img)

    profile_page_person_avatar_frame_1_avatar.image = new_img

change_btn = ctk.CTkButton(profile_page_person_avatar_frame_1, text="Change Image", command=change_img)
change_btn.grid(row=1, column=0, padx=5, pady=15)


show_transfer_page("New Transfer")
show_page(dashboard_page) 
root.mainloop()


