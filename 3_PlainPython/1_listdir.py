# Resources:
# http://www.google.com/search?q=how+to+open+all+files+in+folder+python
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

# Method 1: os.listdir()
import os

data_dir = "./data/"

for file in os.listdir(data_dir):
    if file.endswith(".txt"):
        print(file)
        file_location = os.path.join(data_dir, file)
        print(file_location)


# Method 2: glob
# import glob

# for file in glob.glob("./data/*.txt"):
#     print(file)
