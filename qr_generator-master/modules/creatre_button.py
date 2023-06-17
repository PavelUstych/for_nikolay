import customtkinter as ctk
import modules.app_screen as m_app
import modules.create_qr as m_qr
import modules.create_frame as m_frame
import modules.function as fun

font = ctk.CTkFont(family="Papyrus",
                   size=14,
                   weight="bold"
                   )

url_code = ctk.CTkButton(master=m_frame.frame_main,
                         width=100,
                         height=40,
                         text="Створити QR-code",
                         command=m_qr.bg,
                         fg_color="#64ac8f",
                         bg_color = '#4b6154',
                         font=font,
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

# url_code.place(x=430,y=25, anchor = ctk.CENTER)


logo_button = ctk.CTkButton(master=m_frame.frame_main,
                         width=360,
                         height=40,
                         text="Підібрати логотип до qr-code",
                         fg_color="#64ac8f",
                         command=m_qr.add_logo,
                         font=font,
                         bg_color = '#4b6154',
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

# logo_button.place(x=10,y=170)

# 

autorisation_button = ctk.CTkButton(master=m_frame.frame2,
                         width=110,
                         height=30,
                         text="Регістрація",
                         fg_color="#64ac8f",
                         command=fun.register,
                         font=font,
                        #  bg_color="#64ac8f",
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

autorisation_button.place(x=10,y=35)

# 

come_button = ctk.CTkButton(master=m_frame.frame2,
                         width=110,
                         height=30,
                         text="Вхід",
                         fg_color="#64ac8f",
                         command=fun.bye,
                         font=font,
                        #  bg_color="#64ac8f",
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

come_button.place(x=140,y=35)

# 

register_button = ctk.CTkButton(master=m_frame.frame_register,
                         width=110,
                         height=30,
                         text="Підтвердити",
                         fg_color="#64ac8f",
                         command=fun.registrate,
                         font=font,
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

register_button.place(x=100,y=310)

come_button_2 = ctk.CTkButton(master=m_frame.frame_come,
                         width=110,
                         height=30,
                         text="Увійти",
                         fg_color="#64ac8f",
                         command=fun.come,
                         font=font,
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

come_button_2.place(x=95,y=180)










bg_color_button = ctk.CTkButton(master=m_frame.frame_main,
                         width=360,
                         height=40,
                         text="Обрати задній фон qr-code",
                         fg_color="#64ac8f",
                         command=m_qr.select_bg_color,
                         font=font,
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

# bg_color_button.place(x=95,y=180)

fg_color_button = ctk.CTkButton(master=m_frame.frame_main,
                         width=360,
                         height=40,
                         text="Обрати колір qr-code",
                         fg_color="#64ac8f",
                         command=m_qr.select_fg_color,
                         font=font,
                         text_color="black",
                         hover_color= '#c0dfc2'
                         )

# fg_color_button.place(x=95,y=180)

profile_button = ctk.CTkButton(master=m_frame.frame_main,
                         width=100,
                         height=100,
                         text="",
                         command=fun.profile,
                         font=font,
                         text_color="black",
                         hover_color= '#c0dfc2',
                         fg_color="#94d6ba",
                        bg_color='#4b6154'
                         )

bye_profile_button = ctk.CTkButton(master=m_frame.frame_1,
                         width=100,
                         height=30,
                         text="НАЗАД",
                         command=fun.back,
                         font=font,
                        #text="Назад",
                         text_color="black",
                         hover_color= '#c0dfc2',
                         fg_color="#64ac8f",
                        bg_color='#94d6ba'
                         )

bye_profile_button.place(x=580,y=10)

select_button = ctk.CTkButton(master=m_frame.frame_1,
                        width=100,
                        height=30,
                        text="ВЫБРАТЬ",
                        command=m_qr.history,
                        font=font,
                        text_color="black",
                        hover_color= '#c0dfc2',
                        fg_color="#64ac8f",
                        bg_color='#94d6ba'
                         )
select_button.place(x=10,y=280)











png_button = ctk.CTkButton(master=m_frame.frame_main,
                        width=100,
                        height=30,
                        command=m_qr.png,
                        font=font,
                        text="save in png",
                        text_color="black",
                        hover_color= '#c0dfc2',
                        fg_color="#64ac8f",
                        bg_color="#4b6154"
                         )
# png_button.place(x=10,y=260)

jpg_button = ctk.CTkButton(master=m_frame.frame_main,
                        width=100,
                        height=30,
                        command=m_qr.jpg,
                        font=font,
                        text="save in jpg",
                        text_color="black",
                        hover_color= '#c0dfc2',
                        fg_color="#64ac8f",
                        bg_color="#4b6154"
                         )
# jpg_button.place(x=137,y=260)

svg_button = ctk.CTkButton(master=m_frame.frame_main,
                        width=100,
                        height=30,
                        command=m_qr.svg,
                        font=font,
                        text="save in svg",
                        text_color="black",
                        hover_color= '#c0dfc2',
                        fg_color="#64ac8f",
                        bg_color="#4b6154"
                         )
# svg_button.place(x=265,y=260)


style_qrc_button = ctk.CTkButton(master=m_frame.frame_main,
                        width=170,
                        height=30,
                        command=m_qr.style_qrc_code,
                        font=font,
                        text="⬤",
                        text_color="black",
                        hover_color= '#c0dfc2',
                        fg_color="#64ac8f",
                        bg_color="#4b6154"
                         )
style_qrc_button.place(x=10,y=300)

#  ▲

font2 = ctk.CTkFont(family="Papyrus",
                   size=20,
                   weight="bold"
                   )

style_qrt_button = ctk.CTkButton(master=m_frame.frame_main,
                        width=170,
                        height=30,
                        command=m_qr.style_qrt_code,
                        font=font2,
                        text="▲",
                        text_color="black",
                        hover_color= '#c0dfc2',
                        fg_color="#64ac8f",
                        bg_color="#4b6154"
                         )
style_qrt_button.place(x=200,y=300)


