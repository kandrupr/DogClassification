import os

cwd = os.getcwd()
cwd += r"\assets"

for filename in os.listdir("./assets"):
    breed = filename.split('-')[1]
    breed = breed.lower()
    breed = breed.replace("_", " ")
    os.rename(os.path.join(cwd, filename),os.path.join(cwd, breed))
    print("Rename of " + breed + " succesful")