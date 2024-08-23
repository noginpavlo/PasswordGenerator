from tkinter import *
from tkinter import messagebox
import sqlite3
import random
import pyperclip

#--------------------------------------------------GENERATE PASSWORD---------------------------------------------------#
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_field.delete(0, END)
    password_field.insert(0, password)
    pyperclip.copy(password)

#----------------------------------------------------SAVE PASSWORD-----------------------------------------------------#
def record_data():
    website = website_field.get()
    username = username_field.get()
    password = password_field.get()
    is_ok_to_save = messagebox.askokcancel(title="Validate data saving", message=f"Website: {website}\n"
                                                                                 f"Username: {username}\n"
                                                                                 f"Password: {password}")
    if is_ok_to_save:
        if website != "" and username != "" and password != "":
            with sqlite3.connect("database.db") as connect:
                cursor = connect.cursor()
                cursor.execute('''
                INSERT INTO password_data (website, username, password)
                           VALUES (?, ?, ?);
                       ''', (website, username, password))
            website_field.delete(0, END)
            password_field.delete(0, END)
        else:
            warning_window = Toplevel(window, bg="white")
            warning_window.title("Provide data")
            warning_window.minsize(400, 50)

            warning_label = Label(warning_window, text="Please ensure all fields are completed before proceeding.",
                                  bg="white")
            warning_label.pack()

            close_button = Button(warning_window, text="Close", command=warning_window.destroy, font=("Arial", 10))
            close_button.pack()


#----------------------------------------------------------UI----------------------------------------------------------#
window = Tk()

window.title("Password Generator")
window.geometry("400x400")
window.configure(bg="white")

canvas = Canvas(window, width=150, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(75, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(window, text="Website:", bg="white")
website_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

email_label = Label(window, text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

password_label = Label(window, text="Password:", bg="white")
password_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

website_field = Entry(window, width=45)
website_field.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")
website_field.focus()

username_field = Entry(window, width=45)
username_field.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="w")
username_field.insert(0, "Email@gmail.com")

password_field = Entry(window, width=23)
password_field.grid(row=3, column=1, padx=5, pady=5, sticky="w")

password_button = Button(window, text="Generate password", command=password_generator, font=("Arial", 10))
password_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")

add_button = Button(window, text="Add", command=record_data, font=("Arial", 10))
add_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

window.mainloop()
