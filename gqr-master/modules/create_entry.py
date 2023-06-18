import customtkinter as ctk
import modules.app_screen as m_app
import modules.create_frame as m_frame

font = ctk.CTkFont(family="Papyrus",
                   size=18,
                   weight="bold"
                   )

t_c="black"

text = ctk.StringVar()

entry_url = ctk.CTkEntry(master=m_frame.frame_main,
                     height=40,
                     width=360,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     bg_color = '#4b6154',
                     textvariable=text)

# entry_url.place(x=10,y=10)

text_name = ctk.StringVar()
entry_name = ctk.CTkEntry(master=m_frame.frame_register,
                     height=30,
                     width=250,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     textvariable=text_name)
entry_name.place(x=10,y=40)
#

text_email = ctk.StringVar()
entry_mail= ctk.CTkEntry(master=m_frame.frame_register,
                     height=30,
                     width=250,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     textvariable=text_email)
entry_mail.place(x=10,y=110)
# 

text_password = ctk.StringVar()
entry_password = ctk.CTkEntry(master=m_frame.frame_register,
                     height=30,
                     width=250,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     textvariable=text_password)
entry_password.place(x=10,y=180)
# 

text_passwordre = ctk.StringVar()
entry_passwordre = ctk.CTkEntry(master=m_frame.frame_register,
                     height=30,
                     width=250,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     textvariable=text_passwordre)
entry_passwordre.place(x=10,y=250)

# 




# 




# 

text_email2 = ctk.StringVar()
entry_email2 = ctk.CTkEntry(master=m_frame.frame_come,
                     height=30,
                     width=250,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     textvariable=text_email2)
entry_email2.place(x=25,y=40)

# 

text_password_2 = ctk.StringVar()
entry_password_2 = ctk.CTkEntry(master=m_frame.frame_come,
                     height=30,
                     width=250,
                     text_color=t_c,
                     font=font,
                     fg_color="#e7f5dc",
                     textvariable=text_password_2)
entry_password_2.place(x=25,y=120)


