import os
import time
number = 1
while True:
    if number > 4:
        number = 1;
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/""username""/Pictures/script_images/%d.jpg"%number)
    print "wallpaper changed to %d.jpg"%number
    number += 1
    time.sleep(4)
