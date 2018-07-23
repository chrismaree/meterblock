## Basic Implementation
This version runs using HTTP to communicate with a Sonoff POW and uses a simple smart contract to act as the accounting mechanism to store energy consumed (tokens left in wallet).

To run this software, you require a number of packages that can be installed using a virtual environment: 

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python blockchainConnectedHTTP.py
    
Additionally, you need to run a local ethereum node on `http:localhost:8575`. For this, Ganache or Ganache-cli is recommended.

Lastly, the IP address of the Sonoff POW has been hard coded to be `10.0.0.5`. this would need to be changed to the local IP of your device.