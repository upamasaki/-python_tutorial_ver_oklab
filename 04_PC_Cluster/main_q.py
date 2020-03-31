import paramiko

if __name__ == '__main__':

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect('172.31.19.192', username='hashimoto', password='0gur11a6')
    #client.connect('172.31.19.150', username='tani', password='0gur11a6')

    stdin, stdout, stderr = client.exec_command('echo %USERNAME%')
    username = ''
    for line in stdout:
        username = line
        
    print("username : {}".format(username))

    client.close()

    