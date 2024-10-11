Install lirc

/boot/firmware/config.txt
add  dtoverlay=gpio-ir,gpio_pin=17

/etc/rc.local  
add  irexec > /dev/null &
