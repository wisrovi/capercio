contadorNoInstalados= 0
contadorNoEncontrados = 0
contadorTotalArchivos = 0

def iniciarArchivo():
    infoGuardar = 'date >> install.log '
    os.system(infoGuardar)

def MostrarLogConsola(datos):
    infoGuardar = 'echo "%s" >> install.log ' %(datos)
    os.system(infoGuardar)
    print(datos)

def terminarArchivo():
    infoGuardar = 'echo " " >> install.log '
    os.system(infoGuardar)


contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import os
    iniciarArchivo()
    MostrarLogConsola("os se instalo correctamente")
except ImportError:
    iniciarArchivo()
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria os")  

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from properties import *      
    MostrarLogConsola("properties se instalo correctamente")                                           
except ImportError:
    contadorNoEncontrados = contadorNoEncontrados + 1
    MostrarLogConsola("falta un archivo de ejecucion (properties), por favor vuelva a descargar el repositorio de github")  
           
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from descargarImagen import *     
    MostrarLogConsola("descargarImagen se instalo correctamente")                                            
except ImportError:
    contadorNoEncontrados = contadorNoEncontrados + 1
    MostrarLogConsola("falta un archivo de ejecucion (descargarImagen), por favor vuelva a descargar el repositorio de github")
    
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from servidorPI import *     
    MostrarLogConsola("servidorPI se instalo correctamente")                                               
except ImportError:
    contadorNoEncontrados = contadorNoEncontrados + 1
    MostrarLogConsola("falta un archivo de ejecucion (servidorPI), por favor vuelva a descargar el repositorio de github")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                         
    import os.path
    if os.path.exists("ejecutarNavegador.sh"):
        MostrarLogConsola("ejecutarNavegador se instalo correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (ejecutarNavegador), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("ca.crt"):
        MostrarLogConsola("certificados se instalaron correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (certificado), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("icono.ico"):
        MostrarLogConsola("icono se instalo correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (icono), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("detectors/haarcascade_frontalface_alt2.xml"):
        MostrarLogConsola("haarcascade se instalo correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (haarcascade), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("index.py"):
        MostrarLogConsola("index se instalo correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (index), por favor vuelva a descargar el repositorio de github")
    
    if os.path.exists("indexM.py"):
        MostrarLogConsola("indexM se instalo correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (indexM), por favor vuelva a descargar el repositorio de github")
    
    if os.path.exists("indexCV.py"):
        MostrarLogConsola("indexCV se instalo correctamente")  
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        MostrarLogConsola("falta un archivo de ejecucion (indexCV), por favor vuelva a descargar el repositorio de github")
        
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1#
    MostrarLogConsola("No se encontro la libreria os")   


contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from tkinter import *
    MostrarLogConsola("tkinter * se instalo correctamente")  
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria tkinter *")                              
      
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from tkinter.ttk import Progressbar
    MostrarLogConsola("tkinter.ttk se instalo correctamente") 
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria tkinter - Progressbar")                  
       
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from tkinter import ttk            
    MostrarLogConsola("tkinter ttk se instalo correctamente")                                    
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria tkinter - ttk")                    




                                    
contadorTotalArchivos = contadorTotalArchivos + 1                                                                    
try:                                                                      
    from threading import Thread     
    MostrarLogConsola("threading-Thread se instalo correctamente")                                      
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria threading")                              
           
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import time     
    MostrarLogConsola("time se instalo correctamente")                                                        
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria time")                              
                                                                          
            
contadorTotalArchivos = contadorTotalArchivos + 1        
try:                                                                      
    import cv2             
    MostrarLogConsola("cv2-OpenCV se instalo correctamente")                                     
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria cv2")               

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import picamera     
    MostrarLogConsola("picamera se instalo correctamente")                                           
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria picamera")
    
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import picamera.array             
    MostrarLogConsola("picamera.array se instalo correctamente")                                    
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria picamera.array")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import numpy as np              
    MostrarLogConsola("numpy se instalo correctamente")                                 
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria numpy")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import requests        
    MostrarLogConsola("requests se instalo correctamente")                                      
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria requests")   



contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import webbrowser         
    MostrarLogConsola("webbrowser se instalo  correctamente")                                     
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    MostrarLogConsola("No se encontro la libreria webbrowser")  

terminarArchivo()

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



noInstalados = contadorNoInstalados
noEncontrados = contadorNoEncontrados
instalados = contadorTotalArchivos


def minimizar():
    raiz.iconify()
    time.sleep(3)
    raiz.deiconify()

def reiniciar():
    os.system("sudo reboot ")

raiz = Tk()#inicializo la raiz
app = MyApp(raiz)
centrarVentana(raiz)
raiz.title("Capercio")
raiz.resizable(False,False)
raiz.geometry("400" + "x" + "220") #ancho x alto

texto1 = "Archivos no instalados: %s " %(noInstalados)
texto2 = "Archivos no encontrados: %s" %(noEncontrados)
texto3 = "Total instalados: %s " %(instalados)

frame = Frame(raiz)
button1 = Button(frame, text="Reiniciar Ahora", font = "Helvetica 12 bold", bg = "green", command=reiniciar)
button2 = Button(frame, text="Reiniciar mas tarde", font = "Helvetica 12 bold", bg = "red", command=minimizar)

Label(frame, text="La instalación se ha completado.", font = "Helvetica 12 bold").grid(row=0, column=0, columnspan=2, padx=10)
Label(frame, text="", font = "Helvetica 12 bold").grid(row=1, column=0, columnspan=2)
Label(frame, text="Resumen de instalación", font = "Helvetica 12 bold").grid(row=2, column=0, columnspan=2, padx=10)
Label(frame, text=texto1, font = "Helvetica 12 italic").grid(row=3, column=0, columnspan=2)
Label(frame, text=texto2, font = "Helvetica 12 italic").grid(row=4, column=0, columnspan=2)
Label(frame, text=texto3, font = "Helvetica 12 italic").grid(row=5, column=0, columnspan=2, padx=10)

button1.grid(row=6, column=0, padx=5, pady=5)
button2.grid(row=6, column=1, padx=5, pady=5)

frame.pack(expand=True)

raiz.mainloop()





