import customtkinter as ctk

screen_width = 700
screen_height = 380

class App(ctk.CTk):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        
        self.SCREEN_WIDTH = screen_width,
        self.SCREEN_HEIGHT = screen_height,
        self.geometry("700x380"),
        self.resizable(False, False),
        
        self.fg = ctk.CTkLabel(master=self, 
                    text="", 
                    fg_color="#4b6154",
                    width=700,
                    height=380)
        self.fg.place(x = 0, y = 0)
        self.title("Qr-Code")
        
screen = App(screen_width, screen_height)
# screen.