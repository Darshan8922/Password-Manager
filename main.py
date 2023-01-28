from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_area.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_area.get()
    email = email_area.get()
    paswd = pass_area.get()

    if len(web)==0 or len(email)==0 or len(paswd)==0:
        messagebox.showerror(title="Error", message="fill all text area !")
    else:
        Is_ok = messagebox.askokcancel(title="PASSWORD-MANAGER", message="Details are correct , And want to Save ?")
        if Is_ok:
            with open("data_pass.txt", "a") as data:
                data.write(f"{web} | {email} | {paswd}\n")
                web_area.delete(0, END)
                pass_area.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)
img = PhotoImage(file="logo.png")
canvas = Canvas(width=400, height=400)
canvas.create_image(200, 200, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:", font=("Arial", 10, "bold"))
web_label.grid(row=1, column=0)
web_area = Entry(windows, width=35)
web_area.focus()
web_area.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(row=2, column=0)
email_area = Entry(windows, width=35)
email_area.insert(0, "darshan@gmail.com")
email_area.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:", font=("Arial", 10, "bold"))
pass_label.grid(row=3, column=0)
pass_area = Entry(windows, width=35)
pass_area.grid(row=3, column=1, columnspan=2)

gen_pass = Button(text="Generate Password", command=pass_generator)
gen_pass.grid(row=3, column=2)

add_label = Button(text="Add", width=13, font=("Arial", 10, "bold"), command=save)
add_label.grid(row=4, column=2)










windows.mainloop()