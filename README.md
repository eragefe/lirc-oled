/boot/firmware/config.txt
dtoverlay=gpio-ir,gpio_pin=17

/etc/rc.local
irexec > /dev/null &
