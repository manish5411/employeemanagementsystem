from re import search
from customtkinter import *
from PIL import Image
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import database
import time

# FUNCTIONS
def delete_all_employees():
    confirm = messagebox.askyesno('⚠ Confirmation', 'Are you sure you want to delete all employees?')
    if confirm:
        database.delete_all()
        treeview_data()
        clear()
        messagebox.showinfo('✅ Success', 'All employees deleted successfully')


def Show_All():
    treeview_data()
    SearchEntry.delete(0, END)
    searchBox.set('Search By')


def search_employee():
    search_value = SearchEntry.get().strip()
    search_field = searchBox.get()

    if search_value == '':
        messagebox.showerror('❌ Error', 'Enter value to search')
        return

    if search_field == 'Search By':
        messagebox.showerror('❌ Error', 'Please select a search category')
        return

    print(f"Searching for {search_value} in {search_field}")


    searched_data = database.search(search_field, search_value)

    print(f"Database Returned: {searched_data}")


    tree.delete(*tree.get_children())

    if searched_data:
        for emp in searched_data:
            tree.insert('', END, values=emp)
    else:
        messagebox.showinfo("🔍 Not Found", "No employee found matching your search.")


def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('❌ Error', 'Select an employee to update')
        return

    database.update(
        idEntry.get(), NameEntry.get(), PhoneEntry.get(), RoleBox.get(), GenderBox.get(), SalaryEntry.get()
    )

    print("✅ Employee updated!")  # Debugging

    treeview_data()  # Refresh treeview
    clear()  # Clear input fields
    messagebox.showinfo('✅ Success', 'Employee details updated successfully')


def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('❌ Error', 'Select an employee to delete')
        return

    row = tree.item(selected_item)['values']
    database.delete(row[0])

    print(f"❌ Deleted Employee ID: {row[0]}")  # Debugging

    treeview_data()  # Refresh treeview
    clear()  # Clear fields
    messagebox.showinfo('✅ Success', 'Employee deleted successfully')


def clear():
    idEntry.delete(0, END)
    NameEntry.delete(0, END)
    PhoneEntry.delete(0, END)
    SalaryEntry.delete(0, END)
    RoleBox.set('Web Developer')
    GenderBox.set('Male')


def treeview_data():
    employees = database.fetch_employee()

    # Clear old data
    tree.delete(*tree.get_children())

    # Insert new data
    for emp in employees:
        tree.insert('', END, values=emp)

    print("🔄 Treeview updated!")  # Debugging



def add_employee():
    if idEntry.get() == '' or PhoneEntry.get() == '' or NameEntry.get() == '' or SalaryEntry.get() == '':
        messagebox.showerror('❌ Error', 'All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('❌ Error', 'Employee ID already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('❌ Error', "Invalid ID format. Use 'EMP' followed by numbers (e.g., 'EMP1')")
    else:
        database.insert(idEntry.get(), NameEntry.get(), PhoneEntry.get(), RoleBox.get(), GenderBox.get(), SalaryEntry.get())
        treeview_data()
        clear()


window = CTk()
window.geometry('950x600+100+50')
window.resizable(False, False)
window.title('🏢 Employee Management System')
window.configure(fg_color='#EAEDED')


image_path = ''

try:
    bg_image = Image.open(image_path)  # Open the image
    bg_image = bg_image.resize((1250, 900))
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Set as background
    bg_label = CTkLabel(window, image=bg_photo, text="")


    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found. Check the path!")
except Exception as e:
    print(f"An error occurred: {e}")


# Background Image
logo = CTkImage(Image.open('EMSimg1.jpg'), size=(970, 190))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0, column=0, columnspan=2)

# Left Panel
leftFrame = CTkFrame(window, fg_color='#EAEDED')
leftFrame.grid(row=1, column=0)


idEntry = CTkEntry(leftFrame, placeholder_text='📌 Employee ID', width=200)
idEntry.grid(row=0, column=1, pady=5)

NameEntry = CTkEntry(leftFrame, placeholder_text='👤 Full Name', width=200)
NameEntry.grid(row=1, column=1, pady=5)

PhoneEntry = CTkEntry(leftFrame, placeholder_text='📞 Phone Number', width=200)
PhoneEntry.grid(row=2, column=1, pady=5)

RoleBox = CTkComboBox(leftFrame, values=['Web developer','Front-end Developer', 'Back-end Developer',
                                         'Mobile app Developer', 'Data Scientist','Network Engineer','DevOps Engineer',
                                         'CyberSecurity Analyst','Cloud Architect','UI/UX Designer',
                                         'Database Administrator','Data Engineer','IT Consultant',
                                         'Software Engineer','Database Developer','IT Trainer'], width=200)
RoleBox.grid(row=3, column=1, pady=5)
RoleBox.set('Web Developer')

GenderBox = CTkComboBox(leftFrame, values=['Male', 'Female'], width=200)
GenderBox.grid(row=4, column=1, pady=5)
GenderBox.set('Male')

SalaryEntry = CTkEntry(leftFrame, placeholder_text='💰 Salary', width=200)
SalaryEntry.grid(row=5, column=1, pady=5)

# Right Panel (Treeview)
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1, pady=10)

searchBox = CTkComboBox(rightFrame, values=['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary'], width=120)
searchBox.grid(row=0, column=0, padx=5)
searchBox.set('Id')

SearchEntry = CTkEntry(rightFrame, width=200)
SearchEntry.grid(row=0, column=1, padx=5)

searchButton = CTkButton(rightFrame, text='🔍 Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2, padx=5)

showButton = CTkButton(rightFrame, text='📋 Show All', width=100, command=Show_All)
showButton.grid(row=0, column=3, padx=5)

# Treeview
columns = ('Id', 'Name', 'Phone', 'Gender', 'Role', 'Salary')
tree = ttk.Treeview(rightFrame, columns=columns, show='headings', height=13)
tree.grid(row=1, column=0, columnspan=4)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=CENTER, width=100)

# Buttons
# Buttons Frame
buttonFrame = CTkFrame(window, fg_color='#EAEDED')
buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons
CTkButton(buttonFrame, text='➕ Add', width=150, command=add_employee).grid(row=0, column=1, padx=5)
CTkButton(buttonFrame, text='✏ Update', width=150, command=update_employee).grid(row=0, column=2, padx=5)
CTkButton(buttonFrame, text='❌ Delete', width=150, command=delete_employee).grid(row=0, column=3, padx=5)


CTkButton(buttonFrame, text='🗑 Delete All', width=150, fg_color="red", text_color="white", command=delete_all_employees).grid(row=0, column=4, padx=5)


scrollbar = ttk.Scrollbar(rightFrame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)


scrollbar.grid(row=1, column=4, sticky="ns")

def update_time():
    current_time = time.strftime("📅 %d-%b-%Y | ⏰ %I:%M:%S %p")
    time_label.configure(text=current_time)
    window.after(1000, update_time)


time_label = CTkLabel(window, text="", font=("Arial", 14, "bold"), text_color="#2E3A59")
time_label.grid(row=3, column=0, columnspan=2, pady=5)


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()  # Clear previous data
        idEntry.insert(0, row[0])
        NameEntry.insert(0, row[1])
        PhoneEntry.insert(0, row[2])
        GenderBox.set(row[3])
        RoleBox.set(row[4])
        SalaryEntry.insert(0, str(row[5]))

# Bind event
tree.bind('<ButtonRelease-1>', selection)


update_time()

window.bind('<ButtonRelease>', selection)
treeview_data()
window.mainloop()
