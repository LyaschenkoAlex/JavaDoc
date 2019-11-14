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
        f = open('res/dirs/' + root.replace('\\', '&') + '.html', 'w')
        for file in files:
            if file.endswith('.java'):
                f = open('res/files/' + root.replace('\\', "&") + '&' + file[:-5] + '.html', "w")
            if file.endswith('.md'):
                f = open('res/files/' + root.replace('\\', "&") + '&' + file[:-3] + 'MD' + '.html', "w")
                md_file = open(root + '\\' + file, 'r')
                md_file_read = md_file.read()
                f.write(md_file_read)
                f.close()
                md_file.close()
