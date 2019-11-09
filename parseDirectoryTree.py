import os
import shutil


def create_directories_files():
    try:
        os.makedirs('res')
        os.makedirs('res\\files')
        os.makedirs('res\\dirs')
    except:
        shutil.rmtree('res')
        os.makedirs('res')
        os.makedirs('res\\files')
        os.makedirs('res\\dirs')
    for root, dirs, files in os.walk('src'):
        f = open('res/dirs/' + root.replace('\\', '_') + '.html', 'w')
        for file in files:
            if file.endswith('.java'):
                f = open('res/files/' + root.replace('\\', "_") + '_' + file[:-5] + '.html', "w")


if __name__ == '__main__':
    create_directories_files()
