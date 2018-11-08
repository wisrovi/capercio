#! /usr/bin/env python3
from tkinter import *
import time
import os
import os.path as path
from tkinter.ttk import Progressbar
from tkinter import ttk
from threading import Thread

fileDesinstalacion = "1.bin"
fileInstalacion = "2.bin"
fileConfiguracion = "3.bin"

class util:                                                                                                   #
    def __init__(self, parent):                                                                               #
        self.parent = parent                                                                                  #
                                                                                                              #
    def mensajeAutoDestroid(self, texto="Probando..."):                                                       #
        self.top = Toplevel()                                                                                 #
        self.top.title('Capercio')                                                                            #
        self.top.geometry("800" + "x" + "480")                                                                 #
        Message(self.top, text=texto, padx=20, pady=20, font=("Helvetica", 16), width=600).pack()             #
        centrarVentana(self.top)                                                                              #
        self.top.after(30000, self.top.destroy)                                                                #
                                                                                                              #
    def progressbarAutoDestroid(self, texto="Probando...", tiempo=10000):                                     #
        self.topProgressbar = Toplevel()                                                                      #
        self.topProgressbar.title('Capercio')                                                                 #
        # top.wm_attributes('-alpha', 0.3)                                                                    #
        self.topProgressbar.geometry("620" + "x" + "50")                                                      #
        pbar_ind = ttk.Progressbar(self.topProgressbar, orient="horizontal", length=620, mode="indeterminate")#
        pbar_ind.grid(row=1, column=0, pady=2, padx=2, sticky=E + W + N + S)                                  #
        pbar_ind.start()                                                                                      #
        Label(self.topProgressbar, text=texto, font="Helvetica 16 bold italic").grid(row=0, column=0)         #
        centrarVentana(self.topProgressbar)                                                                   #
        self.topProgressbar.after(tiempo, self.topProgressbar.destroy)

class centrarVentana:
    def __init__(self, parent):
        self.parent = parent
        self.parent.update_idletasks()
        w = self.parent.winfo_screenwidth()
        h = self.parent.winfo_screenheight()
        size = tuple(int(_) for _ in self.parent.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        self.parent.geometry("%dx%d+%d+%d" % (size + (x, y)))

class MyDialog:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.parent = parent
        self.top.title("Salir")
        Label(self.top, text="¿Está seguro?", font = "Helvetica 12 bold").grid(row=0, column=0, columnspan=2)
        self.button1 = Button(self.top, text="Si, salir de la app.", font = "Helvetica 12 bold", command=self.salir)
        self.button2 = Button(self.top, text="No, solo minimizar.", font = "Helvetica 12 bold", command=self.minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=1, padx=5, pady=5)
        centrarVentana(self.top)

    def salir(self):
        self.top.destroy()
        self.parent.destroy()

    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()
        time.sleep(3)
        self.parent.deiconify()


class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        d = MyDialog(raiz)
        self.parent.wait_window(d.top)

def cancelar():
    raiz.destroy()

def procesarInstalacion():
    while True:
        time.sleep(3)
        if path.exists(fileDesinstalacion):
            time.sleep(1)
            os.remove(fileDesinstalacion)
            utilidades.mensajeAutoDestroid("Paquetes desinstalados.")
            time.sleep(3)
        if path.exists(fileInstalacion):
            time.sleep(1)
            os.remove(fileInstalacion)
            utilidades.mensajeAutoDestroid("Repositorios Instalados.")
            time.sleep(3)
        if path.exists(fileConfiguracion):
            time.sleep(1)
            os.remove(fileConfiguracion)
            utilidades.mensajeAutoDestroid("Repositorios Configurados.")
            time.sleep(3)
            raiz.destroy()


def iniciarInstalador():
    os.system("sudo sh /home/pi/capercio/execute.sh ")

def instalar():    
    Thread(target=iniciarInstalador).start()
    utilidades.progressbarAutoDestroid("Cargando...", 2400000)
    Thread(target=procesarInstalacion).start()

raiz = Tk()#inicializo la raiz
app = MyApp(raiz)
raiz.title("Capercio")
raiz.resizable(False,False)
raiz.geometry("800" + "x" + "480") #ancho x alto
raiz.attributes('-fullscreen', True) #maximizar ventana
centrarVentana(raiz)

utilidades = util(raiz)

frame = Frame(raiz)
button1 = Button(frame, text="Instalar", font = "Helvetica 12 bold", bg = "green", command=instalar)
button2 = Button(frame, text="Cancelar", font = "Helvetica 12 bold", bg = "red", command=cancelar)

Label(frame, text="¿Desea instalar CAPERCIO?", font = "Helvetica 12 bold").grid(  row=0, column=0, columnspan=2, padx=10)
Label(frame, text="",                          font = "Helvetica 12 bold").grid(  row=1, column=0, columnspan=2)
Label(frame, text="Archivos a eliminar",          font = "Helvetica 12 bold").grid(  row=2, column=0, padx=10)
Label(frame, text="scratch",                   font = "Helvetica 12 italic").grid(row=3, column=0)
Label(frame, text="minecraft",                 font = "Helvetica 12 italic").grid(row=4, column=0)
Label(frame, text="geany",                     font = "Helvetica 12 italic").grid(row=5, column=0)
Label(frame, text="sonic",                     font = "Helvetica 12 italic").grid(row=6, column=0)
Label(frame, text="python2",                   font = "Helvetica 12 italic").grid(row=7, column=0)
Label(frame, text="libreoffice",               font = "Helvetica 12 italic").grid(row=8, column=0)
Label(frame, text="bluej",                     font = "Helvetica 12 italic").grid(row=9, column=0)
Label(frame, text="dillo",                     font = "Helvetica 12 italic").grid(row=10, column=0)
Label(frame, text="epiphany",                  font = "Helvetica 12 italic").grid(row=11, column=0)
Label(frame, text="netsurf",                   font = "Helvetica 12 italic").grid(row=12, column=0, padx=10)

Label(frame, text="Archivos a instalar",          font = "Helvetica 12 bold").grid(  row=2, column=1, padx=10)
Label(frame, text="libavformat",                   font = "Helvetica 12 italic").grid(row=3, column=1)
Label(frame, text="libjpeg",                 font = "Helvetica 12 italic").grid(row=4, column=1)
Label(frame, text="build-essential",                     font = "Helvetica 12 italic").grid(row=5, column=1)
Label(frame, text="python3",                     font = "Helvetica 12 italic").grid(row=6, column=1)
Label(frame, text="libhdf5",                   font = "Helvetica 12 italic").grid(row=7, column=1)
Label(frame, text="libqtgui4",               font = "Helvetica 12 italic").grid(row=8, column=1)
Label(frame, text="opencv",                     font = "Helvetica 12 italic").grid(row=9, column=1)
Label(frame, text="opencv-contrib",                     font = "Helvetica 12 italic").grid(row=10, column=1)
Label(frame, text="request",                  font = "Helvetica 12 italic").grid(row=11, column=1)
Label(frame, text="numpy",                     font = "Helvetica 12 italic").grid(row=12, column=1, padx=10)

Label(frame, text="",                          font = "Helvetica 12 bold").grid(  row=13, column=1, columnspan=2)
Label(frame, text="Para mas información visita www.fcv.org",                          font = "Helvetica 12 bold").grid(  row=14, column=0, columnspan=2)
Label(frame, text="",                          font = "Helvetica 12 bold").grid(  row=15, column=1, columnspan=2)
button2.grid(                                                                     row=16, column=0, padx=5, pady=5)
button1.grid(                                                                     row=16, column=1, padx=5, pady=5)

frame.pack(expand=True)

raiz.mainloop()


