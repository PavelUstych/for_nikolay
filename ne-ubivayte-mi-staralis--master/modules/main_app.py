import customtkinter as ctk

app_width = 600
app_height = 700

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_HEIGHT}x{self.APP_WIDTH}+{0}+{0}")
        self.title("просто")
        self.resizable(False, False)
        
        


main_app = App(app_width, app_height)