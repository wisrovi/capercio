
echo cargando configuracion en el root
sudo cp /home/pi/capercio/config/config.txt /boot/config.txt

sleep 5

echo cargando binarios
sudo cp -r /home/pi/capercio/config/bin /home/pi/bin/

sleep 5

echo cargando autoarranque
mkdir -p /home/pi/.config/autostart/
cd config/autostart/
sudo cp kiosk.desktop /home/pi/.config/autostart/kiosk.desktop

sleep 5

cd /home/pi/capercio/
sudo cp config/splash.png /usr/share/plymouth/themes/pix/splash.png

sleep 5

echo colocando imagen de fondo en la carpeta de fondos de escritorio
cd /home/pi/capercio/
chmod +x config/capercioWallpaper.jpg
sudo cp config/capercioWallpaper.jpg /usr/share/rpd-wallpaper/capercioWallPaper.jpg

sleep 5

echo quitando el icono en el arranque de dispositivo
sudo cp /home/pi/capercio/config/cmdline.txt /boot/cmdline.txt

sleep 5

python3 check.py