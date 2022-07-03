This is mikrotik autodeployer
To install this script:
    git clone git@github.com:hard1mpulse/auto_deployer.git
    chmod +x install.sh
    ./install.sh
Script pushes commands from file to all devices in "data/devices.csv"
.csv tabs description in commented first line in files.
All files path can be changed with editing config.py
Script writes logs of executed commands to logfile