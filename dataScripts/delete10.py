import os

cwd = os.getcwd()
data = os.path.join(cwd, "assets\\train")

for filename in os.listdir(data):
    data_dir = data + "\\" + filename
    for i in range(0,10):
        top10 = data_dir + "\\" + str(i) + ".jpg"
        os.remove(top10)    
    print("Removed top 10 for " + filename)
