
import tkinter as tk
from tkinter import ttk

class PantallaHola(tk.Frame):

    def __init__(self, parents, *args, **kwargs):
        super().__init__(parents, *args, **kwargs)

        self.nombre = tk.StringVar()
        self.hola_texto = tk.StringVar()
        self.hola_texto.set("Hola UPAL")

        #Variables:
        nombre_label = ttk.Label(self, text="Nombre:")
        entrada_nombre = ttk.Entry(self, textvariable=self.nombre)
        boton = ttk.Button(self, text="Cambiar", command=self.cuando_cambie)
        hola_label = ttk.Label(self, textvariable=self.hola_texto,
            font=("TkDefaultFont", 30), wraplength=600)

        # Formulario:
        nombre_label.grid(row=0, column=0, sticky=tk.W)
        entrada_nombre.grid(row=0, column=1, sticky=(tk.W+ tk.E))
        boton.grid(row=0, column=2, sticky=tk.W)
        hola_label.grid(row=1, column=0, columnspan=3)
        self.columnconfigure(1, weight=1)

    def cuando_cambie(self):
        """Maneja click del boton cambiar"""
        if self.nombre.get().strip():
            self.hola_texto.set("Hola " + self.nombre.get())
        else:
            self.hola_texto.set("Hola UPAL")


class MiAplicacion(tk.Tk):
    """Hola Mundo"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Setear propiedades de la ventana
        
        self.title("UPAL Sesion13")
        self.geometry("500x500")
        self.resizable(width=False, height=False)

        # Define UI
        PantallaHola(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MiAplicacion()
    app.mainloop()