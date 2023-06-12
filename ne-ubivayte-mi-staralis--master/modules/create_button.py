from customtkinter import *
import random
import modules.main_app as m_app
import modules.json as m_json  

dict1 = {
    "login":"",
    "password":""
} 

def registration():
    text = CTkLabel(master = m_app.main_app, text = "Зареєструйтесь")
    text_log = CTkLabel(master = m_app.main_app, text = "Введіть ваш логін:")
    register_login = CTkEntry(master = m_app.main_app)
    text_password1 = CTkLabel(master = m_app.main_app,text = "Введіть пароль")
    register_password1 = CTkEntry(master = m_app.main_app)
    text_password2 = CTkLabel(master = m_app.main_app,text = "Підтвердіть ваш пароль")
    register_password2 = CTkEntry(master = m_app.main_app, show = "*")
    button_register = CTkButton(master = m_app.main_app, text = "Зареєструватися")
    dict1["login"] = str(register_login)
    dict1["password"] = str(register_password1)
    m_json.create_json(dict1)
    text.pack()
    text_log.pack()
    register_login.pack()
    text_password1.pack()
    register_password1.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()
    button1.place(
        x=100000000000,
        y=100000000000,
        anchor = CENTER
    ) 
    button2.place(
        x=100000000000,
        y=100000000000,
        anchor = CENTER
    ) 

def login():
    text = CTkLabel(master = m_app.main_app, text = "Авторизуйтесь")
    text_log = CTkLabel(master = m_app.main_app, text = "Введіть ваш логін:")
    login = CTkEntry(master = m_app.main_app)
    text_password1 = CTkLabel(master = m_app.main_app, text = "Введіть пароль")
    login_password = CTkEntry(master = m_app.main_app) 
    button_login = CTkButton(master = m_app.main_app, text = "Авторизуватися")
    text.pack()
    text_log.pack()
    login.pack()
    text_password1.pack()
    login_password.pack()
    button_login.pack()
    button1.place(
        x=100000000000,
        y=100000000000,
        anchor = CENTER
    ) 
    button2.place(
        x=100000000000,
        y=100000000000,
        anchor = CENTER
    ) 
    
    
button1lambda = lambda:registration()
button2lambda = lambda:login()

def create_button2(master, text, width=100, height=50, fg="black"):
    button = CTkButton(
        master = master,
        width = width,
        height = height,
        text = text,
        command = button1lambda
)
    return button

def create_button1(master, text, width=100, height=50, fg="black"):
    button = CTkButton(
        master = master,
        width = width,
        height = height,
        text = text,
        command = button2lambda
)
    return button



button1 = create_button1(master=m_app.main_app,
    text = "Авторізація"
    # command = button1lambda
)
button1.place(
    x= m_app.app_width // 2, 
    y= m_app.app_height // 2,
    anchor = CENTER
)

button2 = create_button2(master = m_app.main_app,
    text = "Реєстрація"
    # command = button2lambda
    
)

button2.place(
    x = m_app.app_width // 2 ,
    y = m_app.app_height // 2 - 50,
    anchor = CENTER
)