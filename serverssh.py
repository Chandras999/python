#!/usr/bin/python

import paramiko
import smtplib , os ,sys

server_list = ['aws-terra', 'linux-practice']
mount_point ='/dev/mapper/VolGroup00-LogVol00'
thresh = 90
server = smtplib.SMTP('smtp.gmail.com' , 587)

def check_disk(server,mount_point):
    sr = paramiko.SSHClient()
    sr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sr.connect('aws-terra', username='root', password='css909',
          allow_agent=False,look_for_keys=True)
    sr.connect('linux-practice', username='root', password='css989',
          allow_agent=False,look_for_keys=True)
    err, out, ins = sr.exec_command("uname -a")
    print("uname is")
    ss=out.read()
    err, out, ins = sr.exec_command("df -h")
    ss=out.read()
    for line in ss.split('\n'):
        #print(line.split()[0])
        if len(line.split()) > 0:
           if line.split()[0] == mount_point:
            return int(line.split()[4].split('%')[0]) 
 


for serverr in server_list:
    print(serverr)
    disk_usage=check_disk(server,mount_point)
    if disk_usage < thresh:
        server.sendmail('root@example.com', 'chandrasekharlsetty@gmail.com', 'Daily Server Report')

        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()
        print('Sending email')
    else:
        print("Server is good")
