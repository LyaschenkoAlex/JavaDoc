import os
import shutil


def create_directories_files():
    try:
        os.makedirs('res')
        os.makedirs('res\\files')
        os.makedirs('res\\dirs')
        os.makedirs('res\\alphabetical_index')
    except:
        shutil.rmtree('res')
        os.makedirs('res')
        os.makedirs('res\\files')
        os.makedirs('res\\dirs')
        os.makedirs('res\\alphabetical_index')
    for root, dirs, files in os.walk('src'):
        f = open('res/dirs/' + root.replace('\\', '-') + '.html', 'w')
        for file in files:
            if file.endswith('.java'):
                f = open('res/files/' + root.replace('\\', "-") + '-' + file[:-5] + '.html', "w")
