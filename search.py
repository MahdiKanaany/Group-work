import os

drive = 'c:/'
namefilee = 'python.exe'
for root,dirs,files in os.walk(drive):
    for file in files :
        if file.endswith(namefilee):
            print(os.path.join(root , file))

