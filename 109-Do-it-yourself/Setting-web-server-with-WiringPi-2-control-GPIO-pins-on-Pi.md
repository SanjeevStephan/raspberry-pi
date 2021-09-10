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
    
