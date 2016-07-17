

import glob
import os.path


argv = '*.jpg'

path = argv

#filenames = glob.glob('F:\\Code\\samples\*.jpg')
filenames = glob.glob(path)

for filename in filenames:
    print filename
    print os.path.abspath(filename)

'''

    with gzip.open(filename) as f:
        data = f.read()
        number_of_characters = len(data)
        # the last line usually has no '\n' so add 1 to count
        number_of_lines = data.count('\n') + 1
        number_of_words = len(data.split())
        print "%d %d %d %s" % (number_of_lines, number_of_words,
                               number_of_characters, filename)
'''