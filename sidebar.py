import customtkinter as ctk

root = ctk.CTk()
root.geometry("800x500")

# ====== SIDEBAR ======
sidebar = ctk.CTkFrame(root, width=150)
sidebar.pack(side="left", fill="y")

# ====== CONTAINER (pages) ======
container = ctk.CTkFrame(root)
container.pack(side="right", fill="both", expand=True)


# ====== PAGES ======
home_page = ctk.CTkFrame(container)
settings_page = ctk.CTkFrame(container)
profile_page = ctk.CTkFrame(container)

label1 = ctk.CTkLabel(home_page, text="Home Page", font=ctk.CTkFont(size=20, weight="bold"))
label1.pack(pady=35)

label2 = ctk.CTkLabel(settings_page, text="Settings Page", font=ctk.CTkFont(size=20, weight="bold"))
label2.pack(pady=35)

label3 = ctk.CTkLabel(profile_page, text="Profile Page", font=ctk.CTkFont(size=20, weight="bold"))
label3.pack(pady=35)


for page in (home_page, settings_page, profile_page):
    page.place(relwidth=1, relheight=1)


# ====== FUNCTIONS SWITCH ======
def show_page(page):
    page.tkraise()


# ====== BUTTONS IN SIDEBAR ======
btn1 = ctk.CTkButton(sidebar, text="Home", command=lambda: show_page(home_page))
btn2 = ctk.CTkButton(sidebar, text="Settings", command=lambda: show_page(settings_page))
btn3 = ctk.CTkButton(sidebar, text="Profile", command=lambda: show_page(profile_page))

btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)


# default page
show_page(home_page)

root.mainloop()