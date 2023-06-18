import customtkinter as ctk
import modules.app_screen as m_app

frame = ctk.CTkFrame(master = m_app.screen,
                     width=700,
                     height=380,
                     fg_color='#94d6ba',
                     bg_color='#4b6154'
                     )

# frame.place(x=0,y=0)

frame2 = ctk.CTkFrame(master = m_app.screen,
                     width=260,
                     height=100,
                     fg_color="#94d6ba",
                     bg_color='#4b6154'
                     )

frame2.place(x=230,y=130) #?

frame_register = ctk.CTkFrame(master = m_app.screen,
                     width=300,
                     height=350,
                     fg_color="#94d6ba",
                     bg_color='#4b6154'
                     )

# frame_register.place(x=230,y=130)

frame_come = ctk.CTkFrame(master = m_app.screen,
                     width=300,
                     height=230,
                     fg_color="#94d6ba",
                     bg_color='#4b6154'
                     )
# frame_come.place(x=230,y=130)

frame_1 = ctk.CTkFrame(master = m_app.screen,
                     width=700,
                     height=380,
                     fg_color="#94d6ba",
                     bg_color='#4b6154'
                     )

frame_main = ctk.CTkFrame(master = m_app.screen,
                     width=700,
                     height=380,
                     fg_color="#4b6154",
                     bg_color='#4b6154'
                     )
