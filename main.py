from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            user_input = website_entry.get()

            try:
                messagebox.showinfo(title=f"{user_input}", message=f"Email: {data[user_input]['email']}"
                                                                   f"\nPassword: {data[user_input]['password']}")

            except KeyError:
                messagebox.showwarning(title="Error", message="No details for this website exists.")

    except JSONDecodeError:
        messagebox.showwarning(title="Error", message="No Data File Found.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    num_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symb_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_list = char_list + num_list + symb_list
    random.shuffle(pw_list)

    password = "".join(pw_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website_saved = website_entry.get()
    email_saved = email_entry.get()
    pw_saved = password_entry.get()
    new_data = {
        website_saved: {
            "email": email_saved,
            "password": pw_saved,
        }}

    if len(website_saved) == 0 or len(pw_saved) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        
        try:
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)
                # updating old data with new data
                data.update(new_data)
                
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(new_data, file, indent=4)
                
        else:
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
                
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sgao041230@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

gen_pw_button = Button(text="Generate password", command=generate_password)
gen_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
