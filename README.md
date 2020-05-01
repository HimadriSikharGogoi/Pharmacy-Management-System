# Pharmacy-Management-System
The project has been made using Python 3.8.1, a language neutral application software in the community edition of PyCharm, a hybrid-platform developed by JetBrains as an IDE for Python.
The application uses Tkinter. Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. Python with tkinter is the fastest and easiest way to create the GUI applications.

Dependencies used:
1.	from tkinter import * : Importing library.
2.	from tkinter import messagebox : To create and display messagebox.
3.	import os : To create and edit files.

Methods Used:
1.	Tk() – To create the main window with the title Pharmacy Management System and provide suitable geometry to the window.
2.	mainloop() – It is an infinite loop that runs the application until the window is closed.

Geometry Manager Classes Used:
1.	grid() method – To organize the widgets in grid(table-like structure) before placing in the parent widget.

Widgets Used:
1.	Button – To add buttons to our application with certain parameters:
  •	bg : background color
  •	font : font inside the button
  •	padx : padding in x-axis
  •	pady : padding in y-axis
  •	relief : aspect of the buttons
2.	Entry – To input the single line of text entry from the user.
3.	Label – To add the display box where we have put the texts with certain parameters:
  •	bg : background color
  •	fg : foreground color
  •	font : font inside the label
  •	padx : padding in x-axis
  •	pady : padding in x-axis
  •	relief: aspect of the Labels
4.	Menu – To create a menu with the following parameters:
  •	Help : To display a messagebox
  •	Exit : To exit the application

Functions provided :

1.	buy() – To write the details of the customer on a file named “records.txt”
2.	clear() – To clear the entire records.
3.	deletename() – To delete details of a customer when searched by name.
4.	deletephone() - To delete details of a customer when searched by phone number.
5.	recordsname() – To search for a record with name.
6.	recordsphone() – To search for a record with phone number.
7.	Contact() – To display a message in the messagebox.


How the app works:

1.	The module tkinter is imported.
2.	The main window (container) is created.
3.	Widgets are added to the main window
4.	The event Trigger are applied on the widgets.


How to run the application:

1.	Open the python file.
2.	Run the program.
3.	The main window of the program will appear. It contains the fields to enter the records of any customer.
4.	Enter the customer details and click to buyout.
5.	The application provides the user with the ability to store details of a customer in a file named “records.txt”
6.	Customer details can be searched by name or by their phone number.
7.	Customer records can be deleted by name or by their phone number. The application also provides the option to completely wipe out all the records.
