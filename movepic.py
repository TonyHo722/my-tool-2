

import glob
import os
from os import makedirs
from os.path import exists


jpg_dir_path= "jpg" + os.sep
cr2_dir_path= "CR2" + os.sep

if not exists(jpg_dir_path):
    makedirs(jpg_dir_path)

if not exists(cr2_dir_path):
    makedirs(cr2_dir_path)

filenames = glob.glob('*.jpg')
for filename in filenames:
#    print filename
    jpg_path = jpg_dir_path+filename
    move_command = "move {0}  {1}".format(filename,
                                          jpg_path)

    print("Move command is:")
    print(move_command)
    print("Running:")
    if os.system(move_command) == 0:
        print('Successful move to', jpg_path)
    else:
        print('move FAILED')

filenames = glob.glob('*.CR2')
for filename in filenames:
#    print filename
    cr2_path = cr2_dir_path+filename
    move_command = "move {0}  {1}".format(filename,
                                          cr2_path)

    print("Move command is:")
    print(move_command)
    print("Running:")
    if os.system(move_command) == 0:
        print('Successful move to', cr2_path)
    else:
        print('move FAILED')

