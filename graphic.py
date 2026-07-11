import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("1400x700")
app.title("Finance Dashboard")


# ==========================================
# Main Frame
# ==========================================

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(0, weight=1)


# ==========================================
# Left Graph Frame
# ==========================================

income_frame = ctk.CTkFrame(main_frame)
income_frame.grid(
    row=0,
    column=0,
    padx=(10, 5),
    pady=10,
    sticky="nsew"
)

income_title = ctk.CTkLabel(
    income_frame,
    text="Income vs Expenses",
    font=("Arial", 18, "bold")
)
income_title.pack(anchor="w", padx=15, pady=(15, 5))

# Figure
fig1 = Figure(figsize=(6, 4), dpi=100)
ax1 = fig1.add_subplot(111)

months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]

income = [4200, 4500, 4300, 4100, 4600, 4250]
expenses = [3100, 3300, 3400, 3200, 3500, 2900]

x = list(range(len(months)))

ax1.bar(
    [i + 0 for i in x],
    income,
    width=0.4,
    color="#30710D"
)

ax1.bar(
    [i + 0.4 for i in x],
    expenses,
    width=0.4,
    color="#ef4444"
)

ax1.set_xticks(x)
ax1.set_xticklabels(months)

ax1.set_ylim(0, 6000)

ax1.grid(
    True,
    linestyle="--",
    alpha=0.3
)

ax1.set_axisbelow(True)

canvas1 = FigureCanvasTkAgg(
    fig1,
    master=income_frame
)

canvas1.draw()
canvas1.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)


# ==========================================
# Right Graph Frame
# ==========================================

balance_frame = ctk.CTkFrame(main_frame)
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
balance_title.pack(anchor="w", padx=15, pady=(15, 5))


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
    "Feb 26",
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
    10500
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
    linestyle="--",
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


app.mainloop()