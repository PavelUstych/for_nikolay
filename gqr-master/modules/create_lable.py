import customtkinter as ctk
import modules.create_frame as m_frame
import modules.app_screen as m_app


font = ctk.CTkFont(family="Papyrus",
                   size=14,
                   weight="bold",
                   
                   )

name = ctk.CTkLabel(m_frame.frame_register, 
                    text="Ім'я:", 
                    text_color="black",
                    font=font)
name.place(x = 10, y = 10)

email = ctk.CTkLabel(m_frame.frame_register, 
                     text="E-mail:", 
                     text_color="black",
                     font=font)
email.place(x = 10, y = 81)

password = ctk.CTkLabel(m_frame.frame_register, 
                        text="Пароль:", 
                        text_color="black",
                        font=font)
password.place(x = 10, y = 150)

passwordre = ctk.CTkLabel(m_frame.frame_register, 
                          text="Підтвердіть пароль:", 
                          text_color="black",
                          font=font)
passwordre.place(x = 10, y = 220)



# 



email1 = ctk.CTkLabel(m_frame.frame_come, 
                     text="E-mail:", 
                     text_color="black",
                     font=font)
email1.place(x = 10, y = 10)

password1 = ctk.CTkLabel(m_frame.frame_come, 
                        text="Пароль:", 
                        text_color="black",
                        font=font)
password1.place(x = 10, y = 90)

