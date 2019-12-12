import os

try:
    dirname = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(dirname, 'headshot'))
except:
    print("There is an issue with navigating to the headshot folder. Please make sure the folder exists in the main directory.")

for file in os.listdir():


    end = file.find(' - ')


    netid = file[:end]

    if '.jpeg' in file:
        new = netid + '.jpg'
        os.rename(file,new)
    if '.png' in file:
        new = netid + '.png'
        os.rename(file,new)
    if '.jpg' in file:
        new = netid + '.jpg'
        os.rename(file,new)
    if '.JPG' in file:
        new = netid + '.jpg'
        os.rename(file,new)
