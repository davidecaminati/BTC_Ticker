# BTC_Ticker
Simple ticker for BTC on C.H.I.P.


--instal requrements

	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install python
	sudo apt-get install git

--install GPIO
	sudo apt-get install git build-essential python-dev python-pip flex bison chip-dt-overlays -y
	git clone git://github.com/xtacocorex/CHIP_IO.git
	cd CHIP_IO
	sudo python setup.py install
	cd ..
  
  --clone repo
  	git clone https://github.com/davidecaminati/BTC_Ticker.git
  
  --launch
  	cd BTC_Ticker
  	sudo python chip_btc_market.py
  
  --wait btc to the moon
  
