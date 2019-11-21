import os
import shutil


def create_directories_files(file_path, path_to_res):
    try:
        os.makedirs(path_to_res + '/res')
        os.makedirs(path_to_res + '/res/files')
        os.makedirs(path_to_res + '/res/dirs')
        os.makedirs(path_to_res + '/res/alphabetical_index')
    except:
        shutil.rmtree(path_to_res + '/res')
        os.makedirs(path_to_res + '/res')
        os.makedirs(path_to_res + '/res/files')
        os.makedirs(path_to_res + '/res/dirs')
        os.makedirs(path_to_res + '/res/alphabetical_index')
    for root, dirs, files in os.walk(file_path):
        s = path_to_res + '/res/dirs/' + file_path.split('/')[-1] + root[len(file_path) + root.find(file_path):].replace('/', '&') + '.html'
        s = s.replace('//', '/')
        f = open(s, 'w')
        for file in files:
            if file.endswith('.java'):
                f = open(path_to_res + '/res/files/' + file_path.split('/')[-1] + root[len(file_path) + root.find(file_path):].replace('/', '&') + '&' + file[:-5] + '.html', "w")
            if file.endswith('.md'):
                f = open(path_to_res + '/res/files/' + file_path.split('/')[-1] + root[len(file_path) + root.find(file_path):].replace('/', '&') + '&' + file[:-3] + 'MD' + '.html', "w")
                md_file = open(root + '/' + file, 'r')
                md_file_read = md_file.read()
                f.write(md_file_read)
                f.close()
                md_file.close()
