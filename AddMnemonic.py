
import glob
from os.path import exists


path = '*.jpg'
MnemonicFile = 'Mnemonic.txt'

MnemonicList = []
MnemonicListAppend = []
filenames = glob.glob(path)

if not exists(MnemonicFile):
    f=open(MnemonicFile,'w')
else:
    f=open(MnemonicFile, 'a+' )
    MnemonicList = f.readlines()


for filename in filenames:
    print filename
    filename_with_newline = filename+'\n'
    for Mnemonic in MnemonicList :
        if filename_with_newline == Mnemonic:
            break
    else:
        MnemonicListAppend.append(filename_with_newline)




f.writelines(MnemonicListAppend)

f.close()

f=open(MnemonicFile,'r')
newList = f.readlines()
print newList
f.close()

