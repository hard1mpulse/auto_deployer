import csv
from routeros_ssh_connector import MikrotikDevice
#### Функция читает данные из файла по пути path и отдаёт словарь, в котором первый столбец является ключом, а остальные данные записываются списком в значение этого ключа
def read_data_from_csv(path):
    with open(path) as datafile:
        data={}
        data_csv=csv.reader(datafile,delimiter=',')
        for row in data_csv:
            if row[0].startswith('#'):
                pass
            else:
                data.update({row.pop(0): row})
    return data

#### Функция принимает на вход ip,креды в формате списка [login,password],и комадны.
#### Возвращает строку с ответом устройства
def push_cmd_on_mikrotik(ip,creds,cmd):
    mikrotik=MikrotikDevice()
    mikrotik.connect(ip,creds[0],creds[1])
    output=mikrotik.send_command(cmd)
    return output