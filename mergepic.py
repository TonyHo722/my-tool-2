

import glob
import os
from os import makedirs
from os.path import exists


jpg_dir_path= "jpg" + os.sep
cr2_dir_path= "CR2" + os.sep

filenames = glob.glob(jpg_dir_path+'*.jpg')
for filename in filenames:

    basename = os.path.basename(filename)
    print filename
    print basename
    move_command = "move {0}  {1}".format(filename,
                                          basename)

    print("Move command is:")
    print(move_command)
    print("Running:")
    if os.system(move_command) == 0:
        print('Successful merge jpg file to current DIR')
    else:
        print('jpg file merge FAILED')

filenames = glob.glob(cr2_dir_path+'*.CR2')
for filename in filenames:

    basename = os.path.basename(filename)
    print filename
    print basename
    move_command = "move {0}  {1}".format(filename,
                                          basename)

    print("Move command is:")
    print(move_command)
    print("Running:")
    if os.system(move_command) == 0:
        print('Successful merge CR2 file to current DIR')
    else:
        print('CR2 file merge FAILED')


'''
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

'''