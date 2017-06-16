# Automatic wallpaper changer
## Instructions
1. In terminal, type ```gsettings```,take a note of the output and in changewallpaper.py paste that path in place of ```/usr/bin/gsettings```, if it is same then leave it as is.
2. In terminal, type ```whoami``` and paste the output in place of username in  ```/home/""username""/Pictures/script_images/%d.jpg``` (make sure you remove quotes of username)
3. Create a folder "script_images" in Pictures directory and inside it place all the images which will be used as wallpapers.Rename them in numbers like 1.jpg, 2.jpg or whatever the extension is but all images should be of same extension.
4. Change the extension in script accordingly for the images,```%d.jpg```
5. Change the if condition accordingly with the no. of images. ```if number > 4:```
6. Change time interval according to your need, currently it is set to 4 seconds.```time.sleep(4)```
