#!/bin/bash
export DISPLAY=:0.0
xset s off
xset -dpms
xset s noblank
#chromium-browser --noerrdialogs --disable-session-crashed-bubble --disable-infobars --kiosk --incognito https://paul.fcv.org:8443/capercio/
cd /home/pi/capercio
sudo sh start.sh
