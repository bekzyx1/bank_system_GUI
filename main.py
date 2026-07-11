import customtkinter as ctk

# ---------------- НАСТРОЙКИ ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- ОКНО ----------------

root = ctk.CTk()

root.title("CustomTkinter Base")
root.geometry("900x700")

# ---------------- FUNCTIONS ----------------

def button_click():
    label_result.configure(text=f"Hello, {entry.get()}")

def switch_theme():
    current = ctk.get_appearance_mode()

    if current == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def checkbox_event():
    print("checkbox:", checkbox.get())

def slider_event(value):
    progressbar.set(value / 100)
    slider_value.configure(text=f"{int(value)}")

def optionmenu_event(choice):
    print("selected:", choice)

# ---------------- TITLE ----------------

title = ctk.CTkLabel(
    root,
    text="CustomTkinter Showcase",
    font=("Arial", 32, "bold")
)

title.pack(pady=20)

# ---------------- MAIN FRAME ----------------

main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# ---------------- LEFT FRAME ----------------

left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# ---------------- RIGHT FRAME ----------------

right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# =========================================================
# LEFT SIDE
# =========================================================

# TEXT

label = ctk.CTkLabel(
    left_frame,
    text="Enter your name:",
    font=("Arial", 18)
)

label.pack(pady=10)

# ENTRY

entry = ctk.CTkEntry(
    left_frame,
    placeholder_text="Type here...",
    width=250,
    height=40
)

entry.pack(pady=10)

# BUTTON

button = ctk.CTkButton(
    left_frame,
    text="Submit",
    command=button_click,
    width=200,
    height=40
)

button.pack(pady=10)

# RESULT LABEL

label_result = ctk.CTkLabel(
    left_frame,
    text="Result...",
    font=("Arial", 16)
)

label_result.pack(pady=10)

# TEXTBOX

textbox = ctk.CTkTextbox(
    left_frame,
    width=350,
    height=150
)

textbox.pack(pady=20)

textbox.insert(
    "0.0",
    "This is CTkTextbox.\n\n"
    "You can write long text here.\n"
    "Like notes, chat, logs, etc."
)

# =========================================================
# RIGHT SIDE
# =========================================================

# SWITCH

switch = ctk.CTkSwitch(
    right_frame,
    text="Toggle Theme",
    command=switch_theme
)

switch.pack(pady=15)

# CHECKBOX

checkbox = ctk.CTkCheckBox(
    right_frame,
    text="Remember Me",
    command=checkbox_event
)

checkbox.pack(pady=15)

# RADIO BUTTONS

radio_var = ctk.StringVar(value="Python")

radio1 = ctk.CTkRadioButton(
    right_frame,
    text="Python",
    variable=radio_var,
    value="Python"
)

radio1.pack(pady=5)

radio2 = ctk.CTkRadioButton(
    right_frame,
    text="C++",
    variable=radio_var,
    value="C++"
)

radio2.pack(pady=5)

radio3 = ctk.CTkRadioButton(
    right_frame,
    text="Rust",
    variable=radio_var,
    value="Rust"
)

radio3.pack(pady=5)

# OPTION MENU

optionmenu = ctk.CTkOptionMenu(
    right_frame,
    values=["Dark", "Light", "System"],
    command=optionmenu_event
)

optionmenu.pack(pady=20)

# COMBOBOX

combobox = ctk.CTkComboBox(
    right_frame,
    values=["Admin", "User", "Guest"]
)

combobox.pack(pady=15)

# SLIDER

slider = ctk.CTkSlider(
    right_frame,
    from_=0,
    to=100,
    command=slider_event
)

slider.pack(pady=20)

slider_value = ctk.CTkLabel(
    right_frame,
    text="0"
)

slider_value.pack()

# PROGRESSBAR

progressbar = ctk.CTkProgressBar(
    right_frame,
    width=250
)

progressbar.pack(pady=20)

progressbar.set(0)

# SEGMENTED BUTTON

segmented = ctk.CTkSegmentedButton(
    right_frame,
    values=["Home", "Profile", "Settings"]
)

segmented.pack(pady=20)

# =========================================================
# BOTTOM FRAME
# =========================================================

bottom_frame = ctk.CTkFrame(root, height=100)
bottom_frame.pack(fill="x", padx=20, pady=10)

bottom_label = ctk.CTkLabel(
    bottom_frame,
    text="Bottom Panel",
    font=("Arial", 20)
)

bottom_label.pack(side="left", padx=20, pady=20)

bottom_button = ctk.CTkButton(
    bottom_frame,
    text="Exit",
    command=root.destroy
)

bottom_button.pack(side="right", padx=20)

# ---------------- START ----------------

root.mainloop()
