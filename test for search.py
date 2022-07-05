import os

nameapp = input("pleas enter name app:")

drive = 'c:/Program Files/' + nameapp
namefilee = (nameapp,'.exe')
for root,dirs,files in os.walk(drive):
    for file in files :
        if file.endswith(namefilee):
            n = print(os.path.join(root , file))


# os.startfile()


