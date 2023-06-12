import customtkinter
import PIL
import modules.search_path as m_path

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.APP_WIDTH = 400
        self.APP_HEIGHT = 500
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.SCREEN_WIDTH}+{self.SCREEN_HEIGHT - self.APP_WIDTH}")
        self.resizable(False, False)
        
        self.IMAGE = customtkinter.CTkImage(
            dark_image = PIL.Image.open(m_path.create_path("img/1.png")),
            size = (self.APP_WIDTH, self.APP_HEIGHT)
        )
        self.IMAGE_LABEL = customtkinter.CTkLabel(master = self, text = "моя перша практична робота з customtkinter", image = self.IMAGE, text_color = "red")
        self.IMAGE_LABEL.grid(row = 10, column = 10)
        self.title("Практична робота")
        
app = App()