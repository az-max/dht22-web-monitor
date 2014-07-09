dht22-web-monitor
=================
This is a project combining the work of PrivateeyePi and PyPlate. It makes use of an Adafruit DHT22 temperature and humidity sensor and writes data to SQLite. It then fetech info from the DB on demand using Python scripts behind an Apache server. I've written down the basic commands to install on Wheezy and have included modules I have changed from the originals.

From a bash prompt, type the next 5 commands in one line at a time:

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install apache2

sudo apt-get install python-dev

sudo apt-get install sqlite3


change directory to /home. this was the default in one of the projects. you can keep things here or change the code to point to a user's sub directory

git clone git://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git

cd /home/
 /home/Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver_Python 
python setup.py build


more to come.....
