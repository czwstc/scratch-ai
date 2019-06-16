# scratch-ai

Required Python packages
-------------------------
 - tensorflow 1.12
 - opencv 3.4
 - pygame 
 - flask 
 - Pillow

if you use Raspberry Pi, you can follow the instructions in [install/raspberry_pi.sh](https://github.com/augustye/scratch-ai/blob/master/install/raspberry_pi.sh)

Start python server
-------------------
Run this in console:
```Bash
git clone https://github.com/augustye/scratch-ai
cd scratch-ai
sudo python3 server.py
```

Run Scratch 3.0 in Browser:
---------------------------
1. open scratch: http://scratch.augustye.net/?url=http://192.168.3.107/extension/mnist
   - replace 192.168.3.107 with the ip address of your python server
2. you will find the "MINST" block on the left side
