import tkinter as tk

class CorruptedShadows:
    def __init__(self): 
        self.master = tk.Tk()
        self.master.title("Corrupted Shadows Reforged")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

    def run(self):
        self.master.mainloop()