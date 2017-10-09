'''
Copyright Davide Caminati 2017
Licence WTFPL   http://www.wtfpl.net/


LCD-D4 U13_19
LCD-D5 U13_22
LCD-D6 U13_21
LCD-D7 U13_24	

LCD-D10	U13_23
LCD-D11	U13_26
LCD-D12	U13_25
LCD-D13	U13_28
LCD-D14	U13_27	
LCD-D15	U13_30
LCD-D18	U13_29
LCD-D20	U13_31	


#bittrex 
https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-btc
 ------- configuration ------
 
 
wifi connection
	nmcli device wifi list

	sudo nmcli device wifi connect 'NETGEAR2' password '123456789' ifname wlan0
	
update OS
	sudo apt-get update
	sudo apt-get upgrade

	
instal requrements
	sudo apt-get install python
	sudo apt-get install git

install GPIO
	sudo apt-get update
	sudo apt-get install git build-essential python-dev python-pip flex bison chip-dt-overlays -y
	git clone git://github.com/xtacocorex/CHIP_IO.git
	cd CHIP_IO
	sudo python setup.py install
	cd ..
	

'''
import CHIP_IO.GPIO as GPIO
import time
import urllib2
import json

gnd_1 = "U13_19" #LCD-D4
gnd_2 = "U13_22" #LCD-D5
gnd_3 = "U13_21" #LCD-D6
gnd_4 = "U13_24" #LCD-D7
a = "U13_23"     #LCD-D10	
b = "U13_26"     #LCD-D11	
c = "U13_25"     #LCD-D12	
d = "U13_28"     #LCD-D13
e = "U13_27"     #LCD-D14
f = "U13_30"     #LCD-D15
g = "U13_29"     #LCD-D18
punto = "U13_31" # LCD-D20

GPIO.setup(gnd_1, GPIO.OUT)
GPIO.setup(gnd_2, GPIO.OUT)
GPIO.setup(gnd_3, GPIO.OUT)
GPIO.setup(gnd_4, GPIO.OUT)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(punto, GPIO.OUT)

GPIO.output(gnd_1, GPIO.LOW)
GPIO.output(gnd_2, GPIO.LOW)
GPIO.output(gnd_3, GPIO.LOW)
GPIO.output(gnd_4, GPIO.LOW)
GPIO.output(a, GPIO.HIGH)
GPIO.output(b, GPIO.HIGH)
GPIO.output(c, GPIO.HIGH)
GPIO.output(d, GPIO.HIGH)
GPIO.output(e, GPIO.HIGH)
GPIO.output(f, GPIO.HIGH)
GPIO.output(g, GPIO.HIGH)
GPIO.output(punto, GPIO.HIGH)

def get_price():
	response = urllib2.urlopen('https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-btc')
	data = json.loads(response.read())

	d = data['result']
	valore =  int(d[0]['Last'])
	return valore
	
def scrivi(input_number):
	ritardo = 0.005
	ones = (input_number%10)
	tens = ((input_number/10)%10)
	hundreds = ((input_number/100)%10)
	thousands = (input_number/1000)
	conversione (ones,gnd_4,False)
	time.sleep(ritardo)
	conversione (tens,gnd_3,False)
	time.sleep(ritardo)
	conversione (hundreds,gnd_2,False)
	time.sleep(ritardo)
	conversione (thousands,gnd_1,True)
	time.sleep(ritardo)
	print input_number

def conversione( valore, digit, dot):
	if (valore == 0): 
		zero(digit,dot)
	if (valore == 1):
		one(digit,dot)
	if (valore == 2):
		two(digit,dot)
	if (valore == 3):
		three(digit,dot)
	if (valore == 4):
		four(digit,dot)
	if (valore == 5):
		five(digit,dot)
	if (valore == 6):
		six(digit,dot)
	if (valore == 7):
		seven(digit,dot)
	if (valore == 8):
		eight(digit,dot)
	if (valore == 9):
		nine(digit,dot)

def zero( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)  
	GPIO.output(d, GPIO.HIGH)  
	GPIO.output(e, GPIO.HIGH)   
	GPIO.output(f, GPIO.HIGH)  
	GPIO.output(g, GPIO.LOW)     
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def one( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.LOW)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.LOW)   
	GPIO.output(e, GPIO.LOW)   
	GPIO.output(f, GPIO.LOW)   
	GPIO.output(g, GPIO.LOW)     
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def two( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.LOW)   
	GPIO.output(d, GPIO.HIGH)   
	GPIO.output(e, GPIO.HIGH)   
	GPIO.output(f, GPIO.LOW)   
	GPIO.output(g, GPIO.HIGH)     
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def three( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.HIGH)   
	GPIO.output(e, GPIO.LOW)   
	GPIO.output(f, GPIO.LOW)   
	GPIO.output(g, GPIO.HIGH)     
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def four( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.LOW)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.LOW)   
	GPIO.output(e, GPIO.LOW)   
	GPIO.output(f, GPIO.HIGH)   
	GPIO.output(g, GPIO.HIGH)    
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def five( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.LOW)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.HIGH)   
	GPIO.output(e, GPIO.LOW)   
	GPIO.output(f, GPIO.HIGH)   
	GPIO.output(g, GPIO.HIGH)    
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def six( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.LOW)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.HIGH)   
	GPIO.output(e, GPIO.HIGH)   
	GPIO.output(f, GPIO.HIGH)   
	GPIO.output(g, GPIO.HIGH)    
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def seven( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.LOW)   
	GPIO.output(e, GPIO.LOW)   
	GPIO.output(f, GPIO.LOW)   
	GPIO.output(g, GPIO.LOW)    
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

def eight( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.HIGH)   
	GPIO.output(e, GPIO.HIGH)   
	GPIO.output(f, GPIO.HIGH)   
	GPIO.output(g, GPIO.HIGH)    
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)


def nine( digit, dot):
	GPIO.output(gnd_1, GPIO.HIGH)
	GPIO.output(gnd_2, GPIO.HIGH)
	GPIO.output(gnd_3, GPIO.HIGH)
	GPIO.output(gnd_4, GPIO.HIGH)
	GPIO.output(a, GPIO.HIGH)   
	GPIO.output(b, GPIO.HIGH)  
	GPIO.output(c, GPIO.HIGH)   
	GPIO.output(d, GPIO.HIGH)   
	GPIO.output(e, GPIO.LOW)   
	GPIO.output(f, GPIO.HIGH)   
	GPIO.output(g, GPIO.HIGH)    
	if (dot == True):
		GPIO.output(punto,GPIO.HIGH)
	else:
		GPIO.output(punto,GPIO.LOW)
	GPIO.output(digit,GPIO.LOW)

i = 1
valore = 1000
while True:
	i += 1
	if (i == 1000):
		i = 0
		valore = get_price()
	scrivi(valore)
	

