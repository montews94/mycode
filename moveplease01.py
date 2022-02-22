#!/usr/bin/env python3
import shutil
import os


# move into this working directory
os.chdir('/home/student/mycode/')

#move from source to destination
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

#
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


