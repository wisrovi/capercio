#descargar imagen fondo
nohup python3 descargarImagen.py &  >> log.log

sleep 5

#abrir aplicacion nativa de python
nohup python3 index.py &  >> log.log

sleep 5

#abrir servidor POST para PI
nohup python3 servidorPI.py & >> log.log

date >> log.log