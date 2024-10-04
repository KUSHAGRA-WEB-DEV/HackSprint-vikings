mport tkinter as tk
import time
from datetime import datetime

class DigitalClock:
    def _init_(self, master):
        self.master = master
        master.title("Digital Clock")

        self.is_24_hour = True

        # Create the display label
        self.label = tk.Label(master, font=("Helvetica", 48), fg="white", bg="black")
        self.label.pack(padx=20, pady=20)

        # Create a date label
        self.date_label = tk.Label(master, font=("Helvetica", 24), fg="white", bg="black")
        self.date_label.pack(padx=20, pady=5)

        # Create buttons for format and color
        self.toggle_button = tk.Button(master, text="Toggle 12/24 Hour", command=self.toggle_format)
        self.toggle_button.pack(pady=5)

        self.color_button = tk.Button(master, text="Change Background Color", command=self.change_color)
        self.color_button.pack(pady=5)

        self.update_clock()

    def update_clock(self):
        if self.is_24_hour:
            current_time = datetime.now().strftime("%H:%M:%S")
        else:
            current_time = datetime.now().strftime("%I:%M:%S %p")

        current_date = datetime.now().strftime("%A, %B %d, %Y")

        self.label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.label.after(1000, self.update_clock)

    def toggle_format(self):
        self.is_24_hour = not self.is_24_hour

    def change_color(self):
        color = tk.colorchooser.askcolor()[1]
        if color:
            self.label.config(bg=color)
            self.date_label.config(bg=color)

if _name_ == "_main_":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
    

