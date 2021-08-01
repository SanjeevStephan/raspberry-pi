# Download VNC Server for Raspberry Pi | VNC® Connect | <a href="https://www.tomshardware.com/how-to/install-vnc-raspberry-pi-os">source</a>

## How to Install VNC on Raspberry Pi OS (64 bit) 
1. Open a terminal window either directly on the Raspberry Pi or by connecting remotely via SSH.
2. Update the list of available software for the Raspberry Pi by typing:

        sudo apt update

3. Install tightvncserver by typing:

        sudo apt install tightvncserver
4. Start the TightVNC server at 720p by typing:

        tightvncserver -geometry 1280x720
5. Create a password to use the VNC session, set this to be the same as your pi login. There is no need to set a view only password.         
        
The Raspberry Pi has now started a VNC server session at raspberrypi.local:1 remember this address as it is needed later.

       

6. Download and install the RealVNC viewer for your operating system from RealVNC.com.
