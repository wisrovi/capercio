sudo cp /home/pi/capercio/config/splash.png /usr/share/plymouth/themes/pix/splash.png

sleep 5

echo cargando configuracion en el root
sudo cp /home/pi/capercio/config/config.txt /boot/config.txt

sleep 5

echo cargando binarios
mkdir -p /home/pi/bin
sudo cp -r /home/pi/capercio/config/kiosk.sh /home/pi/bin/kiosk.sh
sudo chmod +x /home/pi/bin/kiosk.sh

sleep 5

echo cargando autoarranque
mkdir -p /home/pi/.config/autostart/
sudo cp /home/pi/capercio/config/kiosk.desktop /home/pi/.config/autostart/kiosk.desktop

sleep 5

echo colocando imagen de fondo en la carpeta de fondos de escritorio
cd /home/pi/capercio/
chmod +x /home/pi/capercio/config/capercioWallpaper.jpg
sudo cp /home/pi/capercio/config/capercioWallpaper.jpg /usr/share/rpd-wallpaper/capercioWallPaper.jpg

sleep 5

echo configurando el funcionamiento de la pantalla y el modo ahorro de energía
sudo cp /home/pi/capercio/config/lightdm.conf /etc/lightdm/lightdm.conf

touch 3.bin

sleep 5

echo Configuracion terminada.

sudo python3 /home/pi/capercio/check.py

touch 4.bin