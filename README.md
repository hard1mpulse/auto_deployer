# Router OS autodeployer
To install this script:
```
git clone git@github.com:hard1mpulse/auto_deployer.git
chmod +x install.sh
./install.sh
```
Script pushes commands from file from "data/commands" (reads line by line) to all devices in "data/devices.csv" using file "data/credentials.csv" as credentials list
.csv tabs description in commented first line in files.

All files path can be changed with editing config.py

Script writes logs of executed commands to logfile
