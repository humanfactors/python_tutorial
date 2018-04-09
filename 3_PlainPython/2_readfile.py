# http://www.google.com/search?q=how+to+get+filename+python
# https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python

import glob
import os

for file in glob.glob("./data/*.txt"):

        print(os.path.basename(file))

        opened_file = open(file, 'r')
        read_file = opened_file.readlines()

        for line in read_file:
            print(line)
