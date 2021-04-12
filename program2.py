# 8:59 am

from tkinter import *
from tkinter.messagebox import showerror


class CreateEntry:
    def __init__(self, window, row, col, introtext):
        self.var = IntVar()
        self.var.set("")

        self.info = Label(window, text=introtext, bg='black', fg='white')
        self.info.grid(row=row, column=col, sticky=E)

        self.entry = Entry(window, textvar=self.var)
        self.entry.grid(row=row, column=col + 1, sticky=E)


class CreateLabel:
    def __init__(self, window, row, col):
        self.var = StringVar()

        self.label = Label(window, textvar=self.var, bg='black', fg='white')
        self.label.grid(row=row, column=col)


def calc():
    try:
        if 1 <= hourly_rate.var.get() <= 5:
            total_made = (((hourly_rate.var.get() - 1) * 2.5) + 10) * hours_worked.var.get()
            total.var.set(f"Total Made: ${total_made}")
            tax.var.set(f"Tax: -{0.1 * total_made}")
            insurance.var.set(f"Insurance: -{0.05 * total_made}")

            if hours_worked.var.get() > 40:
                overtime.var.set(f"Overtime Hours Worked: {hours_worked.var.get() - 40}")
            else:
                overtime.var.set(f"Overtime Hours Worked: 0")

            take_home.var.set(f"Take Home Pay: {0.85 * total_made}")
        else:
            showerror("Oops!", "Please type a valid hourly rate code.")
    except TclError:
        showerror("Oops!", "Please fill out the form correctly.")


def main_page():
    global main_frame
    global total, tax, insurance, overtime, take_home
    global name, social, hourly_rate, hours_worked, shift_works

    main_frame.destroy()

    main_frame = Frame(root, bg='black')
    main_frame.place(relx=.5, rely=.5, anchor='center')

    input_frame = Frame(main_frame, bg='black')
    input_frame.grid(row=0, column=0)

    output_frame = Frame(main_frame, bg='black')
    output_frame.grid(row=1, column=0, pady=20)

    name = CreateEntry(input_frame, row=0, col=0, introtext="First and Last Name")
    social = CreateEntry(input_frame, row=1, col=0, introtext="Social Security Number")
    hourly_rate = CreateEntry(input_frame, row=2, col=0, introtext="Hourly Rate Code")
    hours_worked = CreateEntry(input_frame, row=3, col=0, introtext="Hours Worked This Week")
    shift_works = CreateEntry(input_frame, row=4, col=0, introtext="Shift Worked")

    calculate_button = Button(input_frame, text="Calculate", command=calc)
    calculate_button.grid(row=5, column=1)

    calculate_button = Button(input_frame, text="Clear", command=main_page)
    calculate_button.grid(row=6, column=1)

    total = CreateLabel(output_frame, row=0, col=0)
    tax = CreateLabel(output_frame, row=1, col=0)
    insurance = CreateLabel(output_frame, row=2, col=0)
    overtime = CreateLabel(output_frame, row=3, col=0)
    take_home = CreateLabel(output_frame, row=4, col=0)


root = Tk()
root.geometry("500x500")
root.configure(bg='black')
root.title("Payroll Program")

main_frame = Frame()

main_page()

root.mainloop()

# 9:39 am
