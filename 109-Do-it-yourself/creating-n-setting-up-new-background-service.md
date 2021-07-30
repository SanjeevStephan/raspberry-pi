## Creating and setting up new service to run in the background (as a service) as follows:

1. Create a new service file in `/lib/systemd/system/` called `rpi-netmonitor.service`:
```commandline
nano /lib/systemd/system/rpi-netmonitor.service
```
2. Copy and paste the following in the new service file:
```
[Unit]
Description=A RPi network monitor for a 16x2 LCD

[Service]
Type=simple
User=pi

ExecStart=/usr/bin/python /home/pi/rpi-lcd/demo_netmonit.py

Restart=always
RestartSec=5

KillMode=process
KillSignal=SIGINT

[Install]
WantedBy=multi-user.target
```
3. Enable the service and start it:
```commandline
sudo systemctl enable rpi-netmonitor.service
sudo systemctl start rpi-netmonitor.service
```
4. Check that the LCD is displaying the correct information; otherwise, check the service status
```commandline
sudo systemctl status rpi-netmonitor.service
```
