import customtkinter as ctk
import random
word = ['rock' , ' paper' , 'scissor']

def get_winner(player):

    result = ''

    com_choice = random.choice(word)

    if player == com_choice :
        result = 'IT IS A TIE '
    elif (player== 'rock' and com_choice =='paper') or (player =='paper' and com_choice=='scissor' ) or  (player=='scissor' and com_choice=='rock'): 
        result = 'YOU LOSE'
    else:
        result='YOU WIN '
    label_pl.configure(text=f'you chose {player}')
    label_comp.configure(text=f'computer chose {com_choice}')
    label.configure( text=result)


window = ctk.CTk()
window.title('ROCK PAPER SCISSOR GAME')
window.geometry("500x500")
window._set_appearance_mode("Dark")
window.resizable(True , True)


buttom_1 = ctk.CTkButton(window , text='🪨' ,font=ctk.CTkFont(size=50), command=lambda: get_winner('rock') , width=100 , height=100 , fg_color='black')
buttom_2 = ctk.CTkButton(window , text='📄' ,font=ctk.CTkFont(size=50), command=lambda: get_winner('paper' ) , width=100 ,height=100, fg_color='black')
buttom_3 = ctk.CTkButton(window , text='✂️' ,font=ctk.CTkFont(size=50), command=lambda: get_winner('scissor') , width=100 , height=100 , fg_color='black')

buttom_1.grid( row=1 , column=2 , padx= 40)
buttom_3.grid( row=1 , column=4 , padx= 40)
buttom_2.grid( row=1 , column=3 , padx= 40)

label_pl = ctk.CTkLabel(window , text='' ,font=ctk.CTkFont(size=15))
label_comp = ctk.CTkLabel(window ,text='',font=ctk.CTkFont(size=15))
label = ctk.CTkLabel(window , text='' , font=ctk.CTkFont( family='arial' , size= 20) , text_color='yellow'  )


label_comp.grid(row=2 , column=3 , padx=10)
label_pl.grid(row=3 , column=3 , padx=10)
label.grid(row=4 , column=3 , padx=10)

window.mainloop()