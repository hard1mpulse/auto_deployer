#!/usr/bin/env python3
from time import strftime,gmtime
import os
from functions import read_data_from_csv,push_cmd_on_mikrotik
from config import devices_path,credentials_path,log_path,commands_list_path

devices=read_data_from_csv(devices_path)
credentials=read_data_from_csv(credentials_path)

#### Получение списка команд из файла
f=open(commands_list_path)
commands_list=f.read().rstrip().split('\n')
f.close()

#### Проверка существования файла логов
if os.path.isfile(log_path):
    pass
else:
    f=open(log_path,'w')
    f.close()


with open(log_path,'a') as f:
    for device in devices.keys():
        for command in commands_list:
            output=push_cmd_on_mikrotik(devices[device][2],credentials[devices[device][3]][1:3],command)
            if output.startswith('['+credentials[devices[device][3]][1]):
                f.write('{}   autodeployer.py   {}({}) Deploying command:\"{}\" was successful!\n'.format(strftime("%D %B %Y %H:%M:%S", gmtime()),device,devices[device][2],command))
            else:
                f.write('{}   autodeployer.py   {}({}) Deploying command:\"{}\" was failed with error: \"{}\"!\n'.format(strftime("%D %B %Y %H:%M:%S", gmtime()),device,devices[device][2],command,output.split('\n')[0].rstrip()))
