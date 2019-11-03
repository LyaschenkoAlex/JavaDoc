import os

for root, dirs, files in os.walk('src'):

    print(root, dirs, files)
    # print(root)
    # print(dirs)
    # print(files)
