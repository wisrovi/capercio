contadorNoInstalados= 0
contadorNoEncontrados = 0
contadorTotalArchivos = 0

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from properties import *                                                 
except ImportError:
    contadorNoEncontrados = contadorNoEncontrados + 1
    print("falta un archivo de ejecucion (properties), por favor vuelva a descargar el repositorio de github")  
           
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from descargarImagen import *                                                
except ImportError:
    contadorNoEncontrados = contadorNoEncontrados + 1
    print("falta un archivo de ejecucion (descargarImagen), por favor vuelva a descargar el repositorio de github")
    
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from servidorPI import *                                                
except ImportError:
    contadorNoEncontrados = contadorNoEncontrados + 1
    print("falta un archivo de ejecucion (servidorPI), por favor vuelva a descargar el repositorio de github")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                         
    import os.path
    if os.path.exists("ejecutarNavegador.sh"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (ejecutarNavegador), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("ca.crt"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (certificado), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("icono.ico"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (icono), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("detectors/haarcascade_frontalface_alt2.xml"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (haarcascade), por favor vuelva a descargar el repositorio de github")
        
    if os.path.exists("index.py"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (index), por favor vuelva a descargar el repositorio de github")
    
    if os.path.exists("indexM.py"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (indexM), por favor vuelva a descargar el repositorio de github")
    
    if os.path.exists("indexCV.py"):
        print(".")
    else:
        contadorNoEncontrados = contadorNoEncontrados + 1
        print("falta un archivo de ejecucion (indexCV), por favor vuelva a descargar el repositorio de github")
        
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1#
    print("No se encontro la libreria os")   


contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from tkinter import *                                                 
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria tkinter *")                              
      
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from tkinter.ttk import Progressbar                                   
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria tkinter - Progressbar")                  
       
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    from tkinter import ttk                                               
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria tkinter - ttk")                    




                                    
contadorTotalArchivos = contadorTotalArchivos + 1                                                                    
try:                                                                      
    from threading import Thread                                          
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria threading")                              
           
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import time                                                           
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria time")                              
                                                                          
            
contadorTotalArchivos = contadorTotalArchivos + 1        
try:                                                                      
    import cv2                                                
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria cv2")               

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import picamera                                               
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria picamera")
    
contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import picamera.array                                              
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria picamera.array")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import numpy as np                                             
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria numpy")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import requests                                            
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria requests")   

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import os                                           
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria os")  

contadorTotalArchivos = contadorTotalArchivos + 1
try:                                                                      
    import webbrowser                                           
except ImportError:
    contadorNoInstalados = contadorNoInstalados + 1
    print("No se encontro la libreria webbrowser")  

print(".")
print(".")
print(".")
print(".")
print("Archivos no instalados: %s" %(contadorNoInstalados))
print("Archivos no encontrados: %s" %(contadorNoEncontrados))
print("Total instalados: %s" %(contadorTotalArchivos))

