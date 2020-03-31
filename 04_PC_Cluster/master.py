#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko


if __name__ == '__main__':

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect('172.31.19.192', username='hashimoto', password='0gur11a6')
    #client.connect('172.31.19.150', username='tani', password='0gur11a6')



    stdin, stdout, stderr = client.exec_command('pwd')
    for line in stdout:
        print("PWD : {}".format(line))


    stdin, stdout, stderr = client.exec_command('net use Y: /delete')
    stdin, stdout, stderr = client.exec_command('net use Y: \\\\172.31.19.150\\Users 0gur11a6 /user:tani')
    stdin, stdout, stderr = client.exec_command('net use')
    for line in stdout:
        print(line)

    
    #cmd = 'net use Y: /delete & net use Y: \\\\172.31.19.150\\Users 0gur11a6 /user:tani & cd /d Y:\\tani\\Documents\\GitRepo\\-python_tutorial_ver_oklab\\04_PC_Cluster ; python slave.py'
    cmd = 'cd test & pwd'
    cmd = 'cd /d Y:\\tani\\Documents\\GitRepo\\-python_tutorial_ver_oklab\\04_PC_Cluster & pwd & .\\venv\\Scripts\\activate.bat & .\\venv\\Scripts\\python.exe -V'
    print(cmd)
    stdin, stdout, stderr = client.exec_command(cmd)
    for line in stdout:
        print(line)

    for line in stderr:
        print(line)
    



    
    client.close()

    