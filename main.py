from tkinter import *
from tkinter import messagebox
import password_generator
import credentials_repository


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    generated_password = password_generator.generate_password()
    password_entry.insert(END, generated_password)
    return generated_password

def search_website():
    website = website_entry.get()
    credentials = credentials_repository.search_website(website)
    if credentials is not None:
        email = credentials[0]
        password = credentials[1]
        messagebox.showinfo(title=f"Credentials Search",
                            message=f"Credentials for Website: {website}\n Email: {email}\n Password: {password}")
    else:
        messagebox.showinfo(title=f"Credentials Search",
                            message=f"Credentials dont exist for Website {website}!")

# ---------------------------- SAVE CREDENTIALS ------------------------------- #
def save_credentials():
    website = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()

    is_ok = messagebox.askokcancel(title="Password for Website", message="Do you want to save entered password?")

    if is_ok:
        credentials_repository.add_credentials(website=website, email=email_value, password=password_value)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Courier"

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, width=300, height=300)

canvas = Canvas(width=200, height=200)

photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)

website_label = Label(width=20, text="Website")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", command=search_website)
search_button.grid(row=1, column=2)

email_label = Label(width=20, text="Email/UserName")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(width=20, text="Password")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate password", width=10, command=generate_password)
password_button.grid(row=3, column=2)

save_credentials_button = Button(width=33, text="Save Credentials", command=save_credentials)
save_credentials_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
