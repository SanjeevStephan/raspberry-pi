# Controlling LED using Raspberry Pi Webserver

![pi-image](https://iotdesignpro.com/sites/default/files/main-image/Controlling-an-LED-with-Raspberry-Pi-Webserver-using-Apache.jpg)

### Step 2: Installing WiringPi Library
_WiringPi is a PIN-based GPIO access library written in C for the BCM2835, BCM2836, and BCM2837 SoC devices used in all Raspberry Pi versions_

1 First we will update our Pi with the latest versions of Raspbian using the command

    sudo apt-get update
    
2 Now we will install git by using this command:    
    
    sudo apt-get install git-core
    
3 Now obtain WiringPi using git by this command:

    git clone https://github.com/wiringpi/wiringpi
    
4 Then install WiringPi library using:

    cd wiringP./build
    sudo ./build
    
### Step 3: Installing a Web Server
_Apache is a very popular webserver, designed to create web servers that have the ability to host one or more HTTP-based websites. Apache Web Server can be enhanced by manipulating the code base or adding multiple extensions/add-ons. In our project, we are using an HTTP server and its PHP extension_

Now, install the apache2 package by using this command in the terminal:

    sudo apt-get install apache2 -y
    
To find the Pi's IP address, type ifconfig at the command line.    
Browse to the default web page either on the Pi or from another computer on the network and you will see the following

![apache2 index page ](https://iotdesignpro.com/sites/default/files/inline-images/Webserver-using-Apache-for-Controlling-an-LED-with-Raspberry-Pi.png)
This means the Apache web server is working.


