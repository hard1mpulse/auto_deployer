#!/bin/bash
chmod +x auto_deployer.py
mkdir data
touch data/credentials.csv
touch data/devices.csv
touch data/commands
echo "#### credential_name,protocol,login,password" >> data/credentials.csv
echo "#### name,vendor,type,ip,credential_name" >> data/devices.csv
echo "Script auto_deployer was succefully installed! Have fun!"