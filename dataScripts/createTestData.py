from shutil import copy
import os

cwd = os.getcwd()
data = os.path.join(cwd, "assets")
test = os.path.join(cwd, "testdata")
print data, test
for filename in os.listdir(data):
    directory = test + "\\" + filename
    data_dir = data + "\\" + filename
    counter = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(0,10):
        testFile = data_dir + "\\" + str(i) + ".jpg"
        copy(testFile, directory)    
    print("Created test data for " + filename)