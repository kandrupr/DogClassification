import os

cwd = os.getcwd()
cwd += r"\assets"

breed_dir = ""

for filename in os.listdir("./assets"):
    breed_dir += cwd + "\\" + filename
    counter = 0
    for image in os.listdir("./assets/"+filename):
        ext = os.path.splitext(image)[1]
        old = os.path.join(breed_dir, image)
        new = os.path.join(breed_dir, str(counter) + ext)
        if(old != new):
            os.rename(old, new)
        counter += 1
    print("Completed " + breed_dir)
    breed_dir = ""

