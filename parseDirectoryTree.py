import os
import shutil


def create_directories_files(file_path):
    try:
        os.makedirs(file_path + '/res')
        os.makedirs(file_path + '/res/files')
        os.makedirs(file_path + '/res/dirs')
        os.makedirs(file_path + '/res/alphabetical_index')
    except:
        shutil.rmtree(file_path + '/res')
        os.makedirs(file_path + '/res')
        os.makedirs(file_path + '/res/files')
        os.makedirs(file_path + '/res/dirs')
        os.makedirs(file_path + '/res/alphabetical_index')
    file_path_linux = file_path.replace('/', '\\')
    for root, dirs, files in os.walk(file_path):
        if root.split('/')[-1].startswith('.'):
            continue
        s = root[root.find(file_path) + len(file_path):].replace('\\', '&')
        k = file_path + '/res/dirs/' + file_path_linux.split('\\')[-1] + root[len(file_path) + root.find(file_path):].replace('\\', '&') + '.html'
        f = open(file_path + '/res/dirs/' + file_path_linux.split('\\')[-1] + root[len(file_path) + root.find(file_path):].replace('/', '&') + '.html', 'w')
        for file in files:
            if file.endswith('.java'):
                f = open(file_path + '/res/files/' + file_path_linux.split('\\')[-1] + root[len(file_path) + root.find(file_path):].replace('/', '&') + '&' + file[:-5] + '.html', "w")
            if file.endswith('.md'):
                f = open(file_path + '/res/files/' + file_path_linux.split('\\')[-1] + root[len(file_path) + root.find(file_path):].replace('/', '&') + '&' + file[:-3] + 'MD' + '.html', "w")
                md_file = open(root + '/' + file, 'r')
                md_file_read = md_file.read()
                f.write(md_file_read)
                f.close()
                md_file.close()
