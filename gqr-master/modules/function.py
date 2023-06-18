import customtkinter as ctk
import modules.create_frame as m_frame
import sqlite3 as sql
import modules.create_entry as m_entry
import modules.creatre_button as m_button
import modules.create_qr as m_qr
import modules.create_lable as m_lable
import PIL
import modules.app_screen as m_app

def profile():
    m_frame.frame_main.place_forget()
    # image = PIL.Image.open('C:/Users/Дом/Desktop/qrcodes/1.png')
    m_frame.frame_1.place(x = 0, y = 0)
    # image_path = ctk.CTkImage(dark_image=PIL.Image.open(f'C:/Users/Дом/Desktop/qrcodes/1.png'), size=(200,200))
    qr_label = ctk.CTkLabel(m_frame.frame_1,  text="")
    qr_label.place(x = 100, y = 14)

def register():
    m_frame.frame2.place_forget()
    m_frame.frame_register.place(x=200,y=10)
    
def registrate():
    con = sql.connect('newdatabase.db')
    name = m_entry.text_name.get()
    email = m_entry.text_email.get()
    password = m_entry.text_password.get()
    passwordre = m_entry.text_passwordre.get()
    cur = con.cursor()

    if password == passwordre:
        cur.execute("CREATE TABLE IF NOT EXISTS Register (ID INTEGER PRIMARY KEY)")
        # cur.execute("ALTER TABLE Register ADD COLUMN Name TEXT")
        # cur.execute("ALTER TABLE Register ADD COLUMN Email TEXT")
        # cur.execute("ALTER TABLE Register ADD COLUMN Password TEXT")
        # cur.execute("ALTER TABLE Register ADD COLUMN Passwordagain TEXT")
        cur.execute("INSERT INTO Register (Name, Email, Password, Passwordagain) VALUES (?,?,?,?)", (name, email, password, passwordre))
        con.commit()

        if cur.fetchone() is None:
            con.commit()
            print('You have registered')

        else:
            print('Такая запись уже существует')
            for i in cur.execute('SELECT * FROM users'):
                print(i)
# 
        m_frame.frame_register.place_forget()
        m_frame.frame2.place(x=230,y=130)

    else:
        print("Паролі не схожі")
    con.commit()

def bye():
    m_frame.frame2.place_forget()
    m_frame.frame_come.place(x=200,y=80)
    # m_frame.frame_register.place(x=200,y=10)
    
def come():
    con = sql.connect('newdatabase.db')
    cur = con.cursor()
    email = m_entry.text_email2.get()
    password = m_entry.text_password_2.get()
    cur.execute("SELECT * FROM Register WHERE Email=? AND Password=?", (email, password))
    result = cur.fetchone()
    # con.commit()
    if result:
        m_frame.frame_come.place_forget()
        m_button.url_code.place(x=450,y=30, anchor = ctk.CENTER)
        m_button.logo_button.place(x=10,y=160)
        m_button.bg_color_button.place(x=10,y=60)
        m_button.fg_color_button.place(x=10,y=110)
        m_qr.qr_style.place(x=10,y=210)
        
        m_button.svg_button.place(x=270,y=260)
        m_button.jpg_button.place(x=140,y=260)
        m_button.png_button.place(x=10,y=260)

        # m_qr.qr_savee.place(x=10,y=260)
        m_entry.entry_url.place(x=10,y=10)
        m_button.profile_button.place(x=590,y=10)
        m_frame.frame_main.place(x=0,y=0)
        con.commit()
        
        # m_frame.frame_come.place_forget()
        # m_frame.frame_register.pack_forget()
        # register()
    else:
        print("Нет такой записи")
        for i in cur.execute("SELECT * FROM Register"):
            print(i)
    # con.close()

def back():
    m_frame.frame_1.place_forget()
    m_frame.frame_main.place(x = 0, y = 0)
    # m_qr.place(x = 380, y = 80)
    
    # m_button.url_code.place(x=450,y=30, anchor = ctk.CENTER)
    # m_button.logo_button.place(x=10,y=160)
    # m_button.bg_color_button.place(x=10,y=60)
    # m_button.fg_color_button.place(x=10,y=110)
    # m_qr.qr_style.place(x=10,y=210)
    # m_qr.qr_savee.place(x=10,y=260)
    # m_entry.entry_url.place(x=10,y=10)
    # m_button.profile_button.place(x=590,y=10)
