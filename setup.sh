cd /home/pi/capercio/
sudo cp config/splash.png /usr/share/plymouth/themes/pix/splash.png

sleep 5

echo cargando configuracion en el root
sudo cp config/config.txt /boot/config.txt

sleep 5

echo cargando binarios
mkdir -p /home/pi/bin
sudo cp -r config/kiosk.sh /home/pi/bin/kiosk.sh
sudo chmod +x /home/pi/bin/kiosk.sh

sleep 5

echo cargando autoarranque
mkdir -p /home/pi/.config/autostart/
sudo cp config/kiosk.desktop /home/pi/.config/autostart/kiosk.desktop

sleep 5

echo colocando imagen de fondo en la carpeta de fondos de escritorio
cd /home/pi/capercio/
chmod +x config/capercioWallpaper.jpg
sudo cp config/capercioWallpaper.jpg /usr/share/rpd-wallpaper/capercioWallPaper.jpg

sleep 5

echo configurando el funcionamiento de la pantalla y el modo ahorro de energía
sudo cp /home/pi/capercio/config/lightdm.conf /etc/lightdm/lightdm.conf

sleep 5

echo Configuracion terminada, reiniciando el dispositivo.

sudo reboot