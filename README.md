# pynq-scratch
PYNQ-Z2 board + Scratch 3.0

Start python server on PYNQ-Z2 board:
----------------------------------
```Bash
sudo pip3 install git+https://github.com/Xilinx/BNN-PYNQ.git
sudo pip3 install flask
git clone https://github.com/augustye/pynq-scratch
cd pynq-scratch
#release port 80
sudo pkill -f redirect_server
sudo python3 server.py
```

Run Scratch 3.0 in Browser:
---------------------------
1. open scratch: http://scratch.augustye.net/?url=http://192.168.3.107/extension/led
   - replace 192.168.3.107 with the ip address of your pynq board
2. you will find the "led on/off" block in "LED" section
