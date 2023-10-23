from flask import Flask, flash, render_template, request, redirect
import subprocess
import os
import time

app = Flask(__name__)
app.debug = True


@app.route('/', methods = ['GET', 'POST'])
def index():
    with open("/root/web/vol", "r") as f:
         vol = f.read()
    with open("/root/web/input", "r") as f:
         input = f.read()
    return render_template('app.html', vol=vol, input=input)

@app.route("/volume", methods = ['GET', 'POST'])
def volume():
    if request.method == 'POST':
       a = request.form.get('a', type=int)
       with open("/root/web/vol", "w") as f:
            f.write(str(a))
       os.system('i2cset -y 1 0x48 15 $(cat /root/web/vol)')
       os.system('i2cset -y 1 0x48 16 $(cat /root/web/vol)')
       return redirect('/')

@app.route('/input', methods = ['GET', 'POST'])
def input():
    input = request.form["input"]
    if input == "S1":
         os.system('systemctl stop autospdif')
         os.system('i2cset -y 1 0x48 1 0xc1')
         os.system('echo 0 >/sys/class/gpio/gpio65/value')
         os.system('echo "(optical)" > /root/web/input')
    if input == "S2":
         os.system('systemctl stop autospdif')
         os.system('i2cset -y 1 0x48 1 0xc1')
         os.system('echo 1 >/sys/class/gpio/gpio65/value')
         os.system('echo "(coaxial)" > /root/web/input')
    if input == "i2s":
         os.system('systemctl stop autospdif')
         os.system('i2cset -y 1 0x48 1 0xc0')
         os.system('echo "(streamer)" > /root/web/input')
    if input == "auto":
         os.system('systemctl start autospdif')
         os.system('echo "(auto select)" > /root/web/input')
    return redirect('/')

@app.route('/power')
def power():
    return render_template('power.html')

@app.route('/reboot', methods = ['GET', 'POST'])
def reboot():
    os.system('amixer cset numid=3 1 >/dev/nul')
    os.system('aplay -D plughw:0 /root/reboot.wav')
    os.system('systemctl restart volume')
    os.system('bash -c "sleep 1; reboot"&')
    return redirect('/')

@app.route('/poweroff', methods = ['GET', 'POST'])
def poweroff():
    os.system('bash -c "sleep 1; poweroff"&')
    return redirect('/')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
