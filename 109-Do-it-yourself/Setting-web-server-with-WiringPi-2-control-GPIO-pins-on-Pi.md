# Controlling LED using Raspberry Pi Webserver | <a href="https://iotdesignpro.com/projects/control-led-with-raspberry-pi-webserver-using-apache">src : iotdesignpro.com</a>

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

To change the default web page with your own HTML page
Navigate to this directory in a terminal window

    cd var/www/html
    ls -al
    This will show you:
    total 12
    drwxr-xr-x  2 root root 4096 Jan  8 01:29 .
    drwxr-xr-x 12 root root 4096 Jan  8 01:28 ..
    -rw-r--r--  1 root root  177 Jan  8 01:29 index.html
    
This shows that by default there is one file in /var/www/html/ called index.html and it is owned by the root user. To edit the file, you need to change its ownership to your own username. Change the owner of the file using:   
    
     Sudo chown pi: index.html   

### 3 Install PHP in Raspberry Pi  
_Now if we want to use PHP code along with HTML, then we have to further install the PHP extension in Raspberry pi. Using PHP code, we can create shell commands to control the LED from the PHP script._

To allow the Apache server to edit PHP files, we will install the latest version of PHP and the PHP module for Apache. 
Use the following command in terminal to install these:

    sudo apt-get install php libapache2-mod-php -y

Now remove or remane the default index.html file:

    sudo rm index.html or
    sudo mv index.html index-backup.html
 
And create your own index.php file:

    sudo nano index.php
 
Now enter the below code in index.php to test the PHP installation.

    <?php phpinfo(); ?>
 

Save it by pressing CTRL + X and the ‘y’ and enter. Now refresh the webpage in your browser, you will see a long page with lots of information about PHP. This shows that the PHP extension is installed properly. 
If you have any problem with the pages or if the pages do not appear, try reinstalling the apache server and its PHP extension.

### Step 5: Start Coding for controlling GPIO pin using this Raspberry Pi Webserver 
_Now delete the previous code in index.php (<?php phpinfo(); ?>) file and insert below PHP code to control GPIO pins inside body of HTML code.

Below is the complete code for creating two buttons to turn on and off the LED connected to Raspberry Pi.

<code>
    
  ````<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Raspberry Pi WiFi Controlled LED</title>
</head>
       <body>
       <center><h1>Control LED using Raspberry Pi Webserver</h1>      
         <form method="get" action="index.php">                
            <input type="submit" style = "font-size: 14 pt" value="OFF" name="off">
            <input type="submit" style = "font-size: 14 pt" value="ON" name="on">
         </form>\u200b\u200b\u200b
                         </center>
<?php

// shell_exec('sudo echo "6" > /sys/class/gpio/export');
// shell_exec('sudo echo "out" > /sys/class/gpio/gpio6/direction');

//  shell_exec("/usr/local/bin/gpio -g mode 27 out"); 


system("gpio export 6");
system("gpio -g mode 6 out");
//system("gpio -g write 6 1");

    if(isset($_GET['off']))
        {
                        echo "LED is off";
//			 shell_exec("sudo echo '0' > /sys/class/gpio/gpio6/value");
//           shell_exec("/usr/local/bin/gpio -g write 27 0");
			system("gpio -g write 6 0");


        }
            else if(isset($_GET['on']))
            {
                        echo "LED is on";
//			 shell_exec('sudo echo "1" > /sys/class/gpio/gpio6/value');
//           shell_exec("/usr/local/bin/gpio -g write 27 1");
			 system("gpio -g write 6 1");


            }
?>
   </body>
</html> ````

</code>
    
![pi_web_page](https://iotdesignpro.com/sites/default/files/inline-images/Raspberry-Pi-Webserver.png)    
