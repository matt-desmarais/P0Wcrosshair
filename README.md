# P0Wcrosshair

[Background Info](http://hackaday.com/2017/07/10/building-a-smart-airsoft-gun-with-open-source-hardware/)


Pi Zero W crosshair system

![wiring](https://github.com/matt-desmarais/P0Wcrosshair/raw/master/wiringDiagram.png)


![prototype](https://github.com/matt-desmarais/P0Wcrosshair/blob/master/complete.jpeg)


![display](https://github.com/matt-desmarais/P0Wcrosshair/blob/master/crosshair.png)


install instructions:
1. sudo raspi-config enable camera and i2c under interfacing options
2. git clone https://github.com/matt-desmarais/P0Wcrosshair.git
3. sudo apt-get install python-opencv
4. run ./RunBoth.sh
