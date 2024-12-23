from tkinter import *
import os

wn = Tk() # Declaracion de objeto wn
wn.title("App-Agado") # Nombre de App
wn.geometry("400x550") # Dimension de la aplicaion


#Funciones - Serviran para dar comandos a los botones creados
def restarttime():
    '''Reinicia el sistema en 30 segundos'''
    os.system("shutdown /r /t 30")

def restart():
    '''Reinicia el sistema al instante (1 seg)'''
    os.system("shutdown /r /t 1")

def shutdown():
    '''Apaga el sistema al instante (1 seg)'''
    os.system("shutdown /s /t 1")

def logout():
    '''Cierra sesion'''
    os.system("shutdown -l")


#Boton Restart Time
restime_ph = PhotoImage(file="images/restime.png")

restime_btn = Button(wn, image=restime_ph, border=0, cursor="hand2", command=restarttime) #Imagen y comando del 1° btn
restime_btn.place(x = 10, y = 10) # Posicion primer btn

#Boton de Close
close_ph = PhotoImage(file="images/close.png")

close_btn = Button(wn, image = close_ph, border=0, cursor="hand2", command=wn.destroy) #Imagen y comando del 2° btn
close_btn.place(x = 230, y = 10) # Posicion de segundo btn

#Boton de Restart
restart_ph = PhotoImage(file="images/restart.png")

restart_btn = Button(wn, image=restart_ph, border=0, cursor="hand2", command=restart) #Imagen y comando del 3° btn
restart_btn.place(x = 10, y = 200) # Posicion de tercer btn

#Boton de Shutdown
shtdwn_ph = PhotoImage(file="images/shutdown.png")

shtdwn_btn = Button(wn, image=shtdwn_ph, border=0, cursor="hand2", command=shutdown) #Imagen y comando del 4° btn
shtdwn_btn.place(x = 230, y = 200) # Posicion de cuarto btn

#Boton de Logout
logout_ph = PhotoImage(file="images/logout.png")

logout_btn = Button(wn, image=logout_ph, border=0, cursor="hand2", command=logout) #Imagen y comando del 5° btn
logout_btn.place(x = 130, y = 380) # Posicion de quinto btn


wn.mainloop()
