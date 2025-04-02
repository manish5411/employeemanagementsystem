from customtkinter import *
from PIL import Image
from tkinter import messagebox

# Toggle Password Visibility
def toggle_password():
    if passwordEntry.cget("show") == "*":
        passwordEntry.configure(show="")
        toggleButton.configure(text="🙈")  # Hide icon
    else:
        passwordEntry.configure(show="*")
        toggleButton.configure(text="👁")  # Show icon

# Login Function
def login():
    username = usernameEntry.get().strip()
    password = passwordEntry.get().strip()

    if username == '' or password == '':
        messagebox.showerror('Error', '⚠ All fields are required!')
    elif username == '@manishkumar' and password == '322251':
        messagebox.showinfo('Success', '🎉 Login Successful!')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', '❌ Invalid Username or Password')

# Main Window
root = CTk()
root.geometry('930x478')
root.resizable(False, False)
root.title('🔐 Login Page')

# Background Image
bg_image = CTkImage(Image.open('LOGIN25.jpg'), size=(930, 478))
bg_label = CTkLabel(root, image=bg_image, text="")
bg_label.place(x=0, y=0)

# Center Frame
frame = CTkFrame(root, width=350, height=320, corner_radius=15, fg_color="transparent")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Heading
headingLabel = CTkLabel(
    frame,
    text='🏢 Employee Management System',
    font=('Goudy Old Style', 18, 'bold'),
    text_color='white',
    fg_color='#2E3A59',
    width=350, height=40,
    corner_radius=10
)
headingLabel.pack(pady=15)



# Username Field
usernameEntry = CTkEntry(frame, placeholder_text='👤 Enter Username', width=260, font=("Arial", 14))
usernameEntry.pack(pady=10)

# Password Field
passwordFrame = CTkFrame(frame, fg_color="transparent")
passwordFrame.pack()

passwordEntry = CTkEntry(passwordFrame, placeholder_text='🔒 Enter Password', width=220, font=("Arial", 14), show="*")
passwordEntry.pack(side=LEFT, pady=10)

# Toggle Password Button
toggleButton = CTkButton(passwordFrame, text="👁", width=30, height=30, command=toggle_password, fg_color="#D3D3D3", text_color="black")
toggleButton.pack(side=RIGHT, padx=5)

# Login Button
loginButton = CTkButton(frame, text='🚀 Login', width=260, font=("Arial", 14, "bold"), cursor='hand2', command=login)
loginButton.pack(pady=15)

root.mainloop()

frame = CTkFrame(root, width=400, height=350, corner_radius=20, fg_color="#2E3A59")  # Dark blue transparent style
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

