import tkinter as tk
from tkinter import ttk




#ventana de inicio
ventana = tk.Tk()
ventana2 = ttk.Entry()
ventana.title("Formulario")
ventana.geometry("600x500")
#ventana.resizable(False,False)

#titulo a la ventana:
vacio = tk.Label(ventana, text='')
titulo = tk.Label(ventana, text='Nombre:',width=30)
titulo1 = tk.Label(ventana, text='Es peruano?:')

#entrada de datos:
nombre_variable = tk.StringVar(ventana)
nombre = tk.Entry(ventana, textvariable=nombre_variable,width=50)

#checkbutton
check_peruano = tk.BooleanVar()
es_peruano = tk.Checkbutton(ventana,variable=check_peruano)

#radiobutton
radio_vacuna = tk.BooleanVar()
vacuna1 = tk.Radiobutton(ventana, variable=radio_vacuna, text="Vacuna1", value="True")
vacuna2 = tk.Radiobutton(ventana, variable=radio_vacuna, text="Vacuna2",value="False")
#vacuna3 = tk.Radiobutton(ventana, variable=radio_vacuna, text="Vacuna3", value="False")



#lista
lista = tk.Listbox(ventana,width=80)
lista.insert(0,"vacunado1")
lista.insert(1,"vacunado2")
lista.insert(2,"vacunado3")

#menu
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

menu_inicio = tk.Menu(menu_principal)

menu_inicio.add_command(label="Inicio")
menu_inicio.add_command(label="¿Quienes somos?")
menu_inicio.add_command(label="Salir")

menu_vacunas = tk.Menu(menu_principal)
menu_pacientes = tk.Menu(menu_principal)

menu_principal.add_cascade(label="Inicio",menu=menu_inicio)
menu_principal.add_cascade(label="Vacunas",menu=menu_vacunas)
menu_principal.add_cascade(label="Pacientes",menu=menu_pacientes)

#Mensaje
mensaje = tk.Message(ventana, text="Bienvenidos al sistema de registro de vacunas", width=300)

#Sistema de grillas
vacio.grid(row=0,column=0,pady=10)
titulo.grid(row=3,column=0,pady=10)
nombre.grid(row=3,column=1,pady=10)
titulo1.grid(row=4,column=0,pady=10)
es_peruano.grid(row=4,column=1,pady=10)
vacuna1.grid(row=5,column=0,pady=10)
vacuna2.grid(row=5,column=1,pady=10)
#vacuna3.grid(row=3,column=2)


#Ubicaciones estática
mensaje.place(x=180,y=10)
lista.place(x=70,y=250)


def captura_dato():
    nombre1 = nombre.get()
    es_peruano1 = check_peruano.get()
    v1 = radio_vacuna.get()

    #Imprimir valores en consola
    print(nombre1,es_peruano1,v1)

#boton
enviar = tk.Button(ventana, text="Enviar formulario", command=captura_dato)
enviar.grid(row=6,column=0,pady=10)

ventana.mainloop()