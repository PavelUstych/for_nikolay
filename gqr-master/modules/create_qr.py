import qrcode
import os
import modules.create_frame as m_frame
import modules.app_screen as m_app
import tkinter.colorchooser as colorchooser
import modules.create_entry as m_entry
import customtkinter as ctk 
# from qrcode import getmat
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import *    
from qrcode.image.styledpil import StyledPilImage
import PIL                             




font_andrey = ctk.CTkFont(
    family= "Papyrus",
    size=15,
)

box = tk.Listbox(
    m_frame.frame_1,
    font=font_andrey,
    bg= "#e7f5dc",
    fg = "#4b6154",
    width= 20,
    height= 14
)
box.place(x=10,y=10)
list_history = []

def history():
    select_index = box.curselection()
    if select_index:
        select_item = list_history[select_index[0]]
        image_path = ctk.CTkImage(dark_image=PIL.Image.open(select_item), size=(250,250))
        qr_label = ctk.CTkLabel(m_frame.frame_1, image=image_path, text="")
        qr_label.place(x = 220, y = 14)
    else:
        print("Тут нечого немає")

#       qr_label.place(x = 420, y = 120)
        


    

bg_color = "white"
fg_color = "black"
# bg_color = "black"
# fg_color = "white"


def select_bg_color():
    global bg_color
    color = colorchooser.askcolor(title= "xxx")
    if color[1]:
        bg_color = color[1]

def select_fg_color():
    global fg_color
    color = colorchooser.askcolor(title= "xxxx")
    if color[1]:
        fg_color = color[1]


def path_search(file_name):
    abs_path = __file__.split("/")
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, file_name)
    return file_name

# 

count = 1



def bg():
    global qrr_style
    global count
    global fg_color
    global bg_color
    global qrsave
    global qr
    
    style_qrr = style_var.get()  
    if style_qrr == "1":
        qrr_style = "1"

    if style_qrr == "2":
        qrr_style = "2"

    if style_qrr == "3":
        qrr_style = "3"

    if style_qrr == "4":
        qrr_style = "4"

    if style_qrr == "5":
        qrr_style = "5"

    if style_qrr == "6":
        qrr_style = "6"

    if style_qrr == "7":
        qrr_style = "7"

    if style_qrr == "8":
        qrr_style = "8"

    if style_qrr == "9":
        qrr_style = "9"

    if style_qrr == "10":
        qrr_style = "10"
    
    qr = qrcode.QRCode(
        version= qrr_style,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border= 4,
        mask_pattern= 7
    )        
    count += 1
    email = m_entry.text_email2.get()
    folder_name = (f"{email}")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join( desktop_path, folder_name)
    
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        print("папка вже створена")
        
    qr.add_data(m_entry.text.get())
    qr.make(fit=True)
    


   
    save_qr = save_var.get()   
    
    if save_qr == "png":
        qrsave = "png"
    elif save_qr == "svg":
        qrsave = "svg"
    elif save_qr == "jpeg":
        qrsave = "jpeg"
        
    


    qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
    qr_image.save(f'C:/Users/Дом/Desktop/{email}/{count}.png')
    
    qr_file_name = f"{count}.png"
    qr_path = os.path.join(folder_path, qr_file_name)
    file_path1 = os.path.splitext(os.path.basename(qr_path))[0]
    list_history.append(qr_path)
    
    image_path = ctk.CTkImage(dark_image=PIL.Image.open(f'C:/Users/Дом/Desktop/{email}/{count}.png'), size=(235,235))
    qr_label = ctk.CTkLabel(m_frame.frame_main, image=image_path, text="")
    qr_label.place(x = 420, y = 120)
    
    box.insert(END, file_path1)




    

style_var = ctk.StringVar()
style_var.set("1")
style_qr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
  

qr_style= ctk.CTkOptionMenu(master = m_frame.frame_main,
                                  width=360,
                                  height=40,
                                  fg_color="#e7f5dc",
                                  button_color="#64ac8f",
                                  bg_color = '#4b6154',
                                  button_hover_color = "#c0dfc2",
                                  dropdown_fg_color="white",
                                  values=style_qr,
                                  text_color="black",
                                  variable= style_var)

# qr_style.place(x=10,y=210)



#

save_var = ctk.StringVar()
save_var.set("png")
savee_qr = ["png", "svg", "jpeg"]

qr_savee= ctk.CTkOptionMenu(master = m_frame.frame_main,
                                  width=360,
                                  height=40,
                                  fg_color="#e7f5dc",
                                  button_color="#64ac8f",
                                  dropdown_fg_color="white",
                                  bg_color = '#4b6154',
                                  button_hover_color = "#c0dfc2",
                                  values=savee_qr,
                                  text_color="black",
                                  variable=save_var
                                  )

# qr_savee.place(x=10,y=250)

#


def add_logo():
    global fg_color
    global bg_color
    global qrsave
    global count
    global qr     
    # qr = qrcode.QRCode(
    #     version= qrr_style,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border= 4,
    #     mask_pattern= 7
    # )        
    email = m_entry.text_email2.get()
    url = m_entry.text.get()
    file_path = ctk.filedialog.askopenfilename(initialdir="Desktop/", filetypes=(("PNG files", "*.png;"),))
    bg_image = PIL.Image.open(file_path)
    
    width = 100
    
    width_img = (width / float(bg_image.size[0]))
    
    h_size = int((float(bg_image.size[1])*float(width_img)))
    bg_image = bg_image.resize((width, h_size))
    
    qr.add_data(url)
    qr.make()


    qr_image = qr.make_image(fill_color = fg_color, back_color = bg_color).convert("RGB")
    pos = ((qr_image.size[0] - bg_image.size[0]) // 2, (qr_image.size[1] - bg_image.size[1]) // 2)
    qr_image.paste(bg_image, pos)
    qr_image.save(path_search(f'C:/Users/Дом/Desktop/{email}/{count}.png'))
    
    # result_image = PIL.Image.new("RGBA", qr_image.size, (0, 0, 0, 0))
    # result_image.paste(bg_image, (180, 180))
    # qr_logo =  PIL.Image.alpha_composite(qr_image.convert("RGBA"), result_image)
    # qr_logo.save(path_search(f'C:/Users/Дом/Desktop/{email}/{count}.{qrsave}'))
    
    image_path = ctk.CTkImage(dark_image=PIL.Image.open(f'C:/Users/Дом/Desktop/{email}/{count}.png'), size=(235,235))
    qr_label = ctk.CTkLabel(m_frame.frame_main, image=image_path, text="")
    qr_label.place(x = 420, y = 120)






def png():
    global count
    global qr 
    # qr = qrcode.QRCode(
        # version= qrr_style,
        # error_correction=qrcode.constants.ERROR_CORRECT_L,
        # box_size=10,
        # border= 4,
        # mask_pattern= 7
    # )        
    email = m_entry.text_email2.get()
    qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
    qr_image.save(f'C:/Users/Дом/Desktop/{email}/{count}.png')


def jpg():
    global count
    global qr 
    # qr = qrcode.QRCode(
        # version= qrr_style,
        # error_correction=qrcode.constants.ERROR_CORRECT_L,
        # box_size=10,
        # border= 4,
        # mask_pattern= 7
    # )        
    email = m_entry.text_email2.get()
    qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
    qr_image.save(f'C:/Users/Дом/Desktop/{email}/{count}.jpg')


def svg():
    global count
    global qr 
    # qr = qrcode.QRCode(
    #     version= qrr_style,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border= 4,
    #     mask_pattern= 7
    # )        
    email = m_entry.text_email2.get()
    qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
    qr_image.save(f'C:/Users/Дом/Desktop/{email}/{count}.svg')


def style_qrc_code():
    global qr
    # qr = qrcode.QRCode(
    #     version= qrr_style,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border= 4,
    #     mask_pattern= 7
    # )        
    global count
    url = m_entry.text.get()
    email = m_entry.text_email2.get()
    qr.add_data(url)
    qr.make()
    # qr_image = qr.make_image(fill_color = fg_color, back_color = bg_color).convert("RGB")
    matrix = qr.get_matrix()
    size = 10
    color = fg_color
    image_size = len(matrix) * size
    image = PIL.Image.new("RGB", (image_size, image_size), bg_color)
    draw = ImageDraw.Draw(image)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                x = size * col
                y = row * size
                draw.ellipse((x, y, x + size, y + size), fill = color)
            else:
                 print("Новый yt ujl!")
    image = image.resize((200, 200))
    image.save(f'C:/Users/Дом/Desktop/{email}/{count}.png')
    image_path = ctk.CTkImage(dark_image=PIL.Image.open(f'C:/Users/Дом/Desktop/{email}/{count}.png'), size=(235,235))
    qr_label = ctk.CTkLabel(m_frame.frame_main, image=image_path, text="")
    qr_label.place(x = 420, y = 120)
    
    





def style_qrt_code():
    global qr
    # qr = qrcode.QRCode(
    #     version= qrr_style,
    #     error_correction=qrcode.constants.ERROR_CORRECT_L,
    #     box_size=10,
    #     border= 4,
    #     mask_pattern= 7
    # )        
    global count
    url = m_entry.text.get()
    email = m_entry.text_email2.get()
    qr.add_data(url)
    qr.make()
    # qr_image = qr.make_image(fill_color = fg_color, back_color = bg_color).convert("RGB")
    matrix = qr.get_matrix()
    size = 10
    color = fg_color
    image_size = len(matrix) * size
    image = PIL.Image.new("RGB", (image_size, image_size), bg_color)
    draw = ImageDraw.Draw(image)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                x = size * col
                y = row * size
                triangle_coords = [(x, y), (x + size, y), (x + size // 2, y + size)]
                draw.polygon(triangle_coords, fill=color)
            else:
                 print("Новый yt ujl!")
    image = image.resize((200, 200))
    image.save(f'C:/Users/Дом/Desktop/{email}/{count}.png')
    image_path = ctk.CTkImage(dark_image=PIL.Image.open(f'C:/Users/Дом/Desktop/{email}/{count}.png'), size=(235,235))
    qr_label = ctk.CTkLabel(m_frame.frame_main, image=image_path, text="")
    qr_label.place(x = 420, y = 120)
    
    