from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=600, height=400)
window.config(padx=150, pady=150)


def calculate():
    miles = int(miles_entry.get())
    kilometers = miles * 1.609
    print(kilometers)


miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

mainloop()
