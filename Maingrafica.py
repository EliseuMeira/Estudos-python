import customtkinter as aplicativo

janela = aplicativo.CTk() #Criando a nossa janela

janela._set_appearance_mode ('dark')

Btn = aplicativo.CTkButton (janela, text=("calcular"))
Btn.pack()

janela.mainloop() # janela
