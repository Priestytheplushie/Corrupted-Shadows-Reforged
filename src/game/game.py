import tkinter as tk
from tkinter import ttk

class CorruptedShadows:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Corrupted Shadows Reforged")
        self.master.geometry("800x600")
        self.master.resizable(True, True)

        self._define_styles() # Set up basic styling

        # Initialize current_frame to None. This will hold the active state's frame.
        self.current_frame = None

        # Call the initial state setup method directly from __init__
        self._show_title_screen()

    def _define_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.BG_DARK = "#1a1a1a"
        self.BG_MEDIUM = "#333333"
        self.FG_LIGHT = "white"
        self.BORDER_COLOR = "#555555"

        self.master.configure(bg=self.BG_MEDIUM)

        self.style.configure("TFrame", background=self.BG_MEDIUM)
        # We'll create a new style for the Title Label to make it stand out
        self.style.configure("Title.TLabel",
                             background=self.BG_MEDIUM,
                             foreground=self.FG_LIGHT,
                             font=("Consolas", 24, "bold")) # Larger, bold font
        self.style.configure("TLabel", background=self.BG_MEDIUM, foreground=self.FG_LIGHT, font=("Consolas", 10))
        self.style.configure("TButton", background="#555555", foreground=self.FG_LIGHT, font=("Consolas", 12)) # Slightly larger button font
        self.style.map("TButton", background=[('active', '#777777')])
        self.style.configure("TScrollbar", troughcolor=self.BG_MEDIUM, bordercolor=self.BORDER_COLOR,
                             background="#777777", arrowcolor=self.FG_LIGHT)

    def _clear_frame(self):
        """Destroys all widgets in the current_frame, if one exists."""
        if self.current_frame:
            for widget in self.current_frame.winfo_children():
                widget.destroy()
            self.current_frame.destroy()
        self.current_frame = None # Reset the reference

    def _show_title_screen(self):
        """Configures and displays the Title Screen UI."""
        self._clear_frame() # Clear any existing widgets

        # Create a new frame for the Title Screen, filling the entire window
        self.title_frame = ttk.Frame(self.master, style="TFrame")
        self.title_frame.pack(fill="both", expand=True)
        self.current_frame = self.title_frame # Set this as the current active frame

        # Center content using grid configuration
        self.title_frame.grid_rowconfigure(0, weight=1) # Spacer row above title
        self.title_frame.grid_rowconfigure(1, weight=0) # Title row
        self.title_frame.grid_rowconfigure(2, weight=0) # Button row
        self.title_frame.grid_rowconfigure(3, weight=1) # Spacer row below button
        self.title_frame.grid_columnconfigure(0, weight=1) # Spacer column left
        self.title_frame.grid_columnconfigure(1, weight=0) # Content column
        self.title_frame.grid_columnconfigure(2, weight=1) # Spacer column right


        # Title Label
        self.title_label = ttk.Label(self.title_frame, text="CORRUPTED SHADOWS", style="Title.TLabel")
        self.title_label.grid(row=1, column=1, pady=20, sticky="nsew")

        # Play Button
        self.play_button = ttk.Button(self.title_frame, text="PLAY", command=self._show_character_creation)
        self.play_button.grid(row=2, column=1, pady=10, ipadx=20, ipady=10, sticky="nsew")

        print("Game State: Title Screen displayed.") # For dev console/internal log


    def _show_character_creation(self):
        """Placeholder method to switch to the Character Creation screen."""
        self._clear_frame()

        # Create a new frame for the Character Creation Screen
        self.char_creation_frame = ttk.Frame(self.master, style="TFrame")
        self.char_creation_frame.pack(fill="both", expand=True)
        self.current_frame = self.char_creation_frame

        temp_label = ttk.Label(self.char_creation_frame, text="CHARACTER CREATION SCREEN (Under Construction)", font=("Consolas", 16, "bold"))
        temp_label.pack(pady=50)

        back_button = ttk.Button(self.char_creation_frame, text="Back to Title", command=self._show_title_screen)
        back_button.pack(pady=20)


    def run(self):
        self.master.mainloop()