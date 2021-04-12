# Conversion Code 8:00 am

# Imports
from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import showerror


# Class to create button
class CreateButton:
    def __init__(self, text, font, window, command):
        self.button = Button(window, text=text, command=command)
        self.button["font"] = font


# Function to show main page
def main_page():
    global frame
    frame.destroy()
    frame = Frame(root, bg='black')
    frame.place(relx=.5, rely=.5, anchor="center")

    # Intro labels
    intro_label = Label(frame, text="Currency Conversion", font=intro_font, bg='black', fg='white')
    explanation_label = Label(frame, text="Choose which currency you'd like to convert from USD to.",
                              font=buttons_font, bg='black', fg='white')

    # Buttons and Canvas for main page
    buttons_canvas = Canvas(frame)

    pounds_button = CreateButton(text="Pounds", font=buttons_font, window=buttons_canvas,
                                 command=lambda: switch_page(0.64, "British Pound"))
    francs = CreateButton(text="French Francs", font=buttons_font, window=buttons_canvas,
                          command=lambda: switch_page(6.07426, "French Francs"))
    lire = CreateButton(text="Italian Lire", font=buttons_font, window=buttons_canvas,
                        command=lambda: switch_page(1793.62, "Italian Lire"))
    deutsche = CreateButton(text="German Deutsche Mark", font=buttons_font, window=buttons_canvas,
                            command=lambda: switch_page(1.811, "German Deutsche Mark"))
    pesetas = CreateButton(text="Spanish Pesetas", font=buttons_font, window=buttons_canvas,
                           command=lambda: switch_page(154.076, "Spanish Pesetas"))
    # Gridding everything
    intro_label.grid()
    explanation_label.grid(row=1)

    buttons_canvas.grid(row=2)

    pounds_button.button.grid()
    francs.button.grid(row=0, column=1)
    lire.button.grid(row=0, column=2)
    deutsche.button.grid(row=0, column=3)
    pesetas.button.grid(row=0, column=4)

    # Exit button creating and gridding
    exit_button = CreateButton(text="Exit", font=buttons_font, window=frame, command=exit)
    exit_button.button.grid(row=3)


# Function to show conversion page
def conversion_page():
    global frame
    frame.destroy()
    frame = Frame(root, bg='black')
    frame.place(relx=.5, rely=.5, anchor="center")

    # Conversion intro label
    conversion_intro = Label(frame, text="Type the amount of USD you'd like to convert from.", font=buttons_font,
                             bg='black', fg='white')
    conversion_intro.grid()

    conversion_canvas = Canvas(frame, bg='black', highlightthickness=0)
    conversion_canvas.grid(row=1)

    conversion_int = IntVar()

    # Entry for original amount to convert
    convert_from = Entry(conversion_canvas, width=4, font=conversion_entry_font, textvariable=conversion_int)
    convert_from.grid(row=0)

    conversion_string = StringVar()

    # Calculating button
    convert_button = CreateButton(text="Calculate", font=buttons_font, window=conversion_canvas,
                                  command=lambda: convert(conversion_string, conversion_int))
    convert_button.button.grid(row=0, column=2, padx=2)

    # Go back button
    convert_button = CreateButton(text="Go Back", font=buttons_font, window=conversion_canvas,
                                  command=main_page)
    convert_button.button.grid(row=0, column=3, padx=1)

    # Label that shows conversion
    conversion_end = Label(frame, textvariable=conversion_string, bg='black', fg='white', font=buttons_font)
    conversion_end.grid(row=2)


def switch_page(convert_number, text):
    global conversion
    global conversion_text
    conversion = convert_number
    conversion_text = text
    conversion_page()


def convert(stringvar, conversion_int):
    try:
        stringvar.set(f"{int(conversion_int.get() * conversion)} {conversion_text}")
    except TclError:
        showerror("Oops!", "Looks like you typed an invalid character.")
        conversion_int.set(0)


# Creating window and widgets
root = Tk()
root.geometry("600x300")
root.configure(bg='black')
root.title("Conversion Program")

frame = Frame(root)
conversion = 1
conversion_text = "USD"

# Fonts
intro_font = Font(family="Lucida Grande", size=18)
buttons_font = Font(family="Lucida Grande", size=12)
conversion_entry_font = Font(family="Lucida Grande", size=30)

# Shows main page originally
main_page()

root.mainloop()

# 8:59 am
