from tkinter import *
from random import randint
from tkinter import messagebox


root = Tk()
root.title('Password Picker')
root.iconbitmap('C:/Users/Sri Vaishnavi/OneDrive/Desktop/password picker/icon.ico')
root.geometry("500x300")


#generate password
def new_rand():
	#CLEAR entry box
	pw_entry.delete(0, END)

	#TO GET password length and convert to integer
	pw_length = int(my_entry.get())

	#create a password to hold password
	my_password = ''

	#loop through password length
	for x in range(pw_length):
		my_password += chr(randint(33,126))

	#output password to the screen
	pw_entry.insert(0, my_password)


#copy to clipboard
def clipper():
	try:
		#clear the clipboard
		root.clipboard_clear()
		#copy to clipboard
		root.clipboard_append(pw_entry.get())
		messagebox.showinfo("Success","Password copied to clipboard!")
	except TclError:
		messagebox.showerror("Error", "Failed to access clipboard.")

#LABEL FRAME for length
lf = LabelFrame(root, text = "Enter required length of the password:")
lf.pack(pady=20)

#ENTRY BOX to designated number of characters
my_entry = Entry(lf, font=("Lucida", 24))
my_entry.pack(pady=20,padx=20)

#ENTRY BOX for returned password
pw_entry = Entry(root, text='',font=("Lucida", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

#FRAME for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#BUTTONS
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()