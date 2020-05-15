from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.title("Pharmacy Management System")
root.geometry("590x335")


def buy():
    print("Packing...")
    print(f"{namevalue.get(), phonevalue.get(), addressvalue.get(), datevalue.get(), itemvalue.get(), costvalue.get()}")
    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), addressvalue.get(), datevalue.get(), itemvalue.get(), costvalue.get()}\n")
    f.close()

def clear():
    print("Clearing...")
    with open("records.txt", "w") as f:
        print("Cleared!")
    f.close()

def deletename():
    ele = namevalue.get()
    with open(r"records.txt") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(ele) not in line:
                working.write(line)
    os.remove(r"records.txt")
    os.rename(r"database_proj1", r"records.txt")
    print("Deleted!")
    f.close()
    working.close()


def deletephone():
    ele = phonevalue.get()
    with open(r"records.txt") as f, open(r"database_proj1", "w") as working:
        for line in f:
            if str(ele) not in line:
                working.write(line)
    os.remove(r"records.txt")
    os.rename(r"database_proj1", r"records.txt")
    print("Deleted!")
    f.close()
    working.close()


def recordsname():
    print("Checking records...")
    s = 0
    search = namevalue.get()
    with open("records.txt", 'r') as f:
        for line in f:
            if search in line:
                wordlist = line.split()
                print("\nName: ", wordlist[0])
                print("Phone: ", wordlist[1])
                print("Address: ", wordlist[2])
                print("Date: ", wordlist[3])
                print("Item bought: ", wordlist[4], "\tCost: ", wordlist[5])
                s = s + 1
    if(s == 0):
            print("No records found!")
    f.close()


def recordsphone():
    print("Checking records...")
    s = 0
    search = phonevalue.get()
    with open("records.txt", 'r') as f:
        for line in f:
            if search in line:
                wordlist = line.split()
                print("\nName: ", wordlist[0])
                print("Phone: ", wordlist[1])
                print("Address: ", wordlist[2])
                print("Date: ", wordlist[3])
                print("Item bought: ", wordlist[4], "\tCost: ", wordlist[5])
                s = s + 1
    if(s == 0):
        print("No records found!")
    f.close()


def Contact():
    messagebox.showinfo("Created by:", "Ritusman Kashyap Bhuyan\nHillul Chutia\nChandan Kumar Gupta\nHimadri Sikhar Gogoi")

menu= Menu(root)
root.config(menu=menu)
menu.add_command(label='Help', command =Contact)
menu.add_separator()
menu.add_command(label='Exit', command=root.quit)


name = Label(root, text="Name:", bg="grey", fg="white", padx=17, pady=5, relief=GROOVE, font=("Times New Roman", 15))
phone = Label(root, text="Phone No:", bg="grey", fg="white", pady=5, relief=GROOVE, font=("Times New Roman", 15))
address = Label(root, text="Address:", bg="grey", fg="white", padx=7, pady=5, relief=GROOVE, font=("Times New Roman", 15))
date = Label(root, text="Date: ", bg="grey", fg="white", padx=19, pady=5.5, relief=GROOVE, font=("Times New Roman", 15))
item = Label(root, text="Item: ", bg="grey", fg="white", padx=21, pady=5.5, relief=GROOVE, font=("Times New Roman", 15))
cost = Label(root, text="Cost: ", bg="grey", fg="white", padx=20,  pady=5.5, relief=GROOVE, font=("Times New Roman", 15))

name.grid(row=1, padx=10)
phone.grid(row=2)
address.grid(row=3)
date.grid(row=4)
item.grid(row=5)
cost.grid(row=6)

namevalue = StringVar()
phonevalue = StringVar()
addressvalue = StringVar()
datevalue = StringVar()
itemvalue = StringVar()
costvalue = StringVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
addressentry = Entry(root, textvariable=addressvalue)
dateentry = Entry(root, textvariable=datevalue)
itementry = Entry(root, textvariable=itemvalue)
costentry = Entry(root, textvariable=costvalue)

nameentry.grid(row=1, column=2)
phoneentry.grid(row=2, column=2)
addressentry.grid(row=3, column=2)
dateentry.grid(row=4, column=2)
itementry.grid(row=5, column=2)
costentry.grid(row=6, column=2)

b1 = Button(text="Buyout", bg="silver", padx=10, pady=2, relief=RAISED, font=("Times New Roman", 15), command=buy).grid(row=7, column=0, padx=10, pady=5)
b2 = Button(text="Search by Name", bg="silver", padx=10, pady=2, relief=RAISED, font=("Times New Roman", 15), command=recordsname).grid(row=7, column=1, padx=10, pady=5)
b3 = Button(text="Search by Phone", bg="silver", padx=10, pady=2, relief=RAISED, font=("Times New Roman", 15), command=recordsphone).grid(row=7, column=2, padx=10, pady=5)
b4 = Button(text="Clear", bg="silver", padx=10, pady=2, relief=RAISED, font=("Times New Roman", 15), command=clear).grid(row=7, column=3, padx=10, pady=5)
b5 = Button(text="Delete by Name", bg="silver", padx=10, pady=2, relief=RAISED, font=("Times New Roman", 15), command=deletename).grid(row=8, column=1, padx=10, pady=5)
b6 = Button(text="Delete by Phone", bg="silver", padx=10, pady=2, relief=RAISED, font=("Times New Roman", 15), command=deletephone).grid(row=8, column=2, padx=10, pady=5)


root.mainloop()
