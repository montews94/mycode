#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os


## where to connect to
where = input("enter ip: ")
t = paramiko.Transport(where, 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
username1 = input("username: ")
password1 = input("password: ")
t.connect(username= username1, password= password1)

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connections
sftp.close() # close the connection
t.close()

