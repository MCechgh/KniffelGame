import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from .backend import Kniffel, wuerfelauge_1, wuerfelauge_2, wuerfelauge_3, wuerfelauge_4, wuerfelauge_5, wuerfelauge_6
images = [wuerfelauge_1, wuerfelauge_2, wuerfelauge_3, wuerfelauge_4, wuerfelauge_5, wuerfelauge_6]

class KniffelGame(tk.Tk):
    def __init__(self):
        # init-call to superclass
        super().__init__()

        self.K = Kniffel()
        self.images = [tk.PhotoImage(data=images[i]) for i in
                       range(6)]

        self.current_dices = [self.images[i - 1] for i in self.K.see_all_dices()]
        self.old_dices = [self.images[i - 1] for i in self.K.see_all_dices()]
        self.keeps = [tk.BooleanVar() for _ in range(5)]
        self.throws_left = 3 - self.K.times_thrown

        # name and size it as wished
        self.title("Kniffel")
        self.rowconfigure(0, minsize=400, weight=1)
        self.columnconfigure(1, minsize=400, weight=1)

        self.frame1 = tk.Frame(self)
        self.frame1.pack(side=tk.TOP, fill=tk.X)

        frame12 = tk.Frame(self)
        frame12.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        frame3 = tk.Frame(self)
        frame3.pack()

        self.frame4 = tk.Frame(self)
        self.frame4.pack()

        frame5 = tk.Frame(self)
        frame5.pack()

        frame56 = tk.Frame(self)
        frame56.pack()

        self.frame6 = tk.Frame(self)
        self.frame6.pack()

        # start from the top
        title = tk.Label(self.frame1, text="Welcome to Kniffel")
        title.config(font=("Courier", 44))
        title.grid(column=0)

        credit = tk.Button(self.frame1, text="Credits", fg="blue", command=self.credit_box)
        credit.config(font=("Courier", 10))
        credit.grid(column=1, padx=10)

        message1 = tk.Label(frame12, text="Your current throw involves:")
        message1.config(font=("Courier", 20))
        message1.pack()

        self.update_pictures()

        message2 = tk.Label(frame3, text="Those which are ticked, won't be thrown again.")
        message2.config(font=("Courier", 18))
        message2.pack()

        next_round = tk.Button(frame5, text="Next round.", padx=100, command=self.new_round)
        next_round.config(font=("Courier", 18))
        next_round.grid(row=3, column=0)

        empty3 = tk.Label(frame56, text="")
        empty3.config(font=("Courier", 40))
        empty3.pack()

        message1 = tk.Label(frame56, text="The last throw ended with:")
        message1.config(font=("Courier", 18))
        message1.pack()

        try:
            self.iconbitmap("M:\Python Scripts\KniffelGame\Kniffel\media/logo/Kniffel.ico")
        except:
            pass

    def new_round(self):
        self.K.start_new_round()
        self.current_dices = [self.images[i - 1] for i in self.K.see_all_dices()]
        self.old_dices = [self.images[i - 1] for i in self.K.see_all_old_dices()]
        for i in range(5):
            self.keeps[i].set(value=False)
        self.throws_left = 3 - self.K.times_thrown
        self.update_pictures()

    def roll_dices(self):
        keep_transfer = [i for i in range(5) if self.keeps[i].get() is True]
        self.K.keep(keep_transfer)
        self.K.roll()
        self.throws_left = 3 - self.K.times_thrown
        self.current_dices = [self.images[i - 1] for i in self.K.see_all_dices()]
        for i in range(len(keep_transfer)):
            self.keeps[i].set(value=True)
        for i in range(len(keep_transfer), 5):
            self.keeps[i].set(value=False)
        self.update_pictures()

    i = 0

    def update_pictures(self):
        # clear windows for update:
        for frame in [self.frame2, self.frame4, self.frame6]:
            for widget in frame.winfo_children():
                widget.destroy()

        # and fill them again
        for x in range(5):
            tk.Label(self.frame2, image=self.current_dices[x]).grid(row=0, column=x, padx=30)
            tk.Label(self.frame6, image=self.old_dices[x]).grid(row=0, column=x, padx=30)
            tk.Checkbutton(self.frame2, variable=self.keeps[x], onvalue=True, offvalue=False).grid(row=1, column=x)

        empty1 = tk.Label(self.frame4, text="")
        empty1.config(font=("Courier", 10))
        empty1.grid(row=0, column=0)

        throws_left_panel = tk.Label(self.frame4, text="Throws left {}".format(self.throws_left), padx=30)
        throws_left_panel.config(font=("Courier", 18))
        throws_left_panel.grid(row=1, column=0)

        throw_button = tk.Button(self.frame4, text="Throw the remaining dices.", command=self.roll_dices)
        throw_button.config(font=("Courier", 18))
        throw_button.grid(row=1, column=1)

        empty2 = tk.Label(self.frame4, text="")
        empty2.config(font=("Courier", 20))
        empty2.grid(row=2, column=0)

    @staticmethod
    def credit_box():
        messagebox.showinfo("Credits to:", "Marcel Cech\n marcel.cech@t-online.de")

def run_KniffelGame():
    window = KniffelGame()
    window.mainloop()