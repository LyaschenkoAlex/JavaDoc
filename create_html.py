import os
from sys import argv
from parse_java import *
from parseDirectoryTree import *
from datetime import datetime

path = ''
left_block = ''


def create_index(directory_dirs, directory_files, directory_path, path_to_res):
    f = open(path_to_res + '/res/index.html', "w")
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container-fluid">
    <h1>JavaDoc</h1>
    <div><p>''')
    f.write('Date of generation - ' + str(datetime.utcnow()) + '<br>Version of generator - 2.1')
    f.write('''</p></div>
    <div class="row">
        <div class="col-sm-4 list-group" style="overflow: auto; margin: 10px;"> <h4>All packages</h4>
            ''')
    for root, dirs, files in os.walk(directory_dirs):
        global left_block

        for file in files:
            left_block += '<a href="'+path_to_res+'/res/dirs/' + file + '" style="width:auto; font-size:12px">' + file.replace('&', '/')[
                                                                                              :-5] + '</a>'
            f.write('<a href="'+path_to_res+'/res/dirs/' + file + '" style="width:auto; font-size:12px">' + file.replace('&', '/')[
                                                                                        :-5] + '</a>')
    f.write('''          
        </div>
        <div class="col-sm-5 list-group" style="overflow:auto;">
        <h4>All classes</h4>''')
    for root, dirs, files in os.walk(directory_files):
        for file in files:
            if 'READMEMD' not in file and not file[:-5].endswith('MD'):
                f.write('<a href="'+path_to_res+'/res/files/' + file + '" style="width:auto; font-size:12px"> ' + file.replace('&', '/')[
                                                                                              :-5] + '.java</a>')
    f.write('''
        </div>
        <div class="col-sm-2 list-group" style="overflow:auto;">
        <h4>Alphabetical index</h4>''')
    alphabet_set = set()
    alphabet_dict = {}
    for root, dirs, files in os.walk(directory_files):
        for file in files:
            if 'READMEMD' not in file:
                alphabet_set.add(str(file.split('&')[-1][0]))

                try:
                    alphabet_dict[str(file.split('&')[-1][0])] += ' ' + str(file.split('/')[-1])
                except:
                    alphabet_dict[str(file.split('&')[-1][0])] = '' + str(file.split('/')[-1])
    alphabet_set = sorted(alphabet_set)
    for key in alphabet_dict:
        f1 = open(path_to_res + '/res/alphabetical_index/' + key + '.html', "w")
        f1.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>''')
        f1.write('<a href="' +path_to_res+'/res/'+ 'index.html">All packages</a>')
        href_arr = alphabet_dict[key].split(' ')
        f1.write('<ul class="list-group">')
        for i in href_arr:
            print(i)
            f1.write(
                '<li class="list-group-item"><a href="../files/' + i + '"class="btn btn-default">' + i.replace('&',
                                                                                                               '/')[
                                                                                                     :-5] + '</a></li>')
        f1.write('</ul>')
        f1.write('</body>')
        f1.close()

    for i in alphabet_set:
        f.write(
            '<a href="'+path_to_res+'/res/alphabetical_index/' + i.upper() + '.html' + '" style="width:auto; font-size:12px">' + i.upper() + '</a>')
    f.write('''</div>
    </div>
</div>

</body>
</html>''')
    f.close()


def show_classes_in_package(directory_dirs, path_to_res):
    for root, dirs, files in os.walk(path_to_res + '/res/dirs'):
        for f_d in files:
            f = open(path_to_res + '/res/dirs/' + f_d, "w")
            f.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Bootstrap Example</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    </head>
    <body>
                    <div class="container-fluid">
        <h1>JavaDoc</h1>
        <div class="row">
        <div" style="overflow: auto; margin: 10px;"> 
        ''')
            f.write(
                '<a href="../index.html"> All packages</a></div>' + '<br><br><h4>Directory -&gt; ' + f_d.replace('&',
                                                                                                                 '/')[
                                                                                                     :-5] + '</h4>')
            t = path_to_res + '/'.join(f_d.split('&')[1:])[:-5]
            for root_p, dirs_p, files_p in os.walk(directory_path + '/' + '/'.join(f_d.split('&')[1:])[:-5]):
                if len(dirs_p) > 0:
                    f.write('<p>Folders in this directory -&gt;</p>')
                for dir_p in dirs_p:
                    if root_p[len(directory_dirs):].replace('/', '&') != '&':
                        f.write(
                            '<a href="' + path_to_res + '/res/dirs/' + directory_dirs.split('/')[-1] + root_p[len(directory_dirs):].replace(
                                '/', '&') + '&' + dir_p + '.html">' + root_p + '/' + dir_p + '</a>' + '<br>')
                    else:
                        f.write('<a href="' + path_to_res + '/res/dirs/' + directory_dirs.split('/')[
                            -1] + '&' + dir_p + '.html">' + root_p + dir_p + '</a>' + '<br>')

                f.write('<br>')
                #############################################3
                for file_p in files_p:
                    if file_p.endswith('.md'):
                        f.write('<p>Readme -&gt; </p>')
                        if root_p[len(directory_dirs):][1:] != '':
                            f.write('<a href="'+ path_to_res + '/res/files/' + (f_d[:-5] + '&' + file_p[:-3]).replace('/',
                                                                                                            '&') + 'MD' + '.html">' + root_p + '/' + file_p + '</a>' + '<br>')
                        else:
                            f.write('<a href="'+ path_to_res + '/res/files/' + ( f_d[:-5] + '&' + file_p[:-3]).replace('/',
                                                                                                      '&') + 'MD' + '.html">' + root_p + file_p + '</a>' + '<br>')

                f.write('<br>')
                f.write('<ul>')
                root_p = root[:-1]

                for file_p in files_p:

                    s = '<li><a href="' + path_to_res + '/res/files/' + f_d[:-5] + '&' + file_p[:-5] + '.html">'
                    s = s.replace('//', '/')
                    s = s.replace('//', '/')

                    if file_p.endswith('.java'):
                        if root_p[len(directory_dirs):].replace('/', '&') != '&':
                            f.write(s + file_p + '</a></li>')
                        else:
                            f.write('<li><a href="' + path_to_res + '/res/files/' + file_p[:-5] + '.html">' + file_p + '</a></li>')

                break
            f.write('''</ul>
        </div>
    </div>
    
    </body>
    </html>''')
            f.close()


def write_files(directory_src, path_to_res):
    for root, dirs, files in os.walk(directory_src):
        for file in files:
            if file.endswith('.java'):
                s = path_to_res + '/res/files/' + root[len(directory_src):].replace('/', '&') + \
                    directory_src.split('/')[-1] + '&' + file[:-5] + '.html'
                f = open(
                    path_to_res + '/res/files/' + directory_src.split('/')[-1] + root[len(directory_src):].replace(
                        '/', '&') + '&' + file[:-5] + '.html', 'w')
                read_file(root + '/' + file)
                f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>''')
                f.write('<body>')
                f.write('<a href="../index.html"> All packages</a>')

                f.write('&nbsp;<a href="#variable">variables</a>')
                f.write('&nbsp;<a href="#method">methods</a>')
                f.write('&nbsp;<a href="#constructor">constructors</a>')
                f.write('<br>')
                if len(find_package()) != 0:
                    f.write('<table class="table table-striped">')

                    f.write('''<thead>
                <tr>
                  <th scope="col">Package</th>
                </tr>
              </thead>''')
                    f.write('<tr><td>')
                    f.write(find_package()[0])
                    f.write('</tr></td>')
                    f.write('</tbody></table>')

                s = about_java_file()
                if s != '':
                    f.write('<br>')
                    f.write('<div><h2>About this class</h2><br>')
                    f.write('<tbody>')
                    f.write(s)
                    f.write('</div>')
                if len(find_imports()) != 0:
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
            <tr>
              <th scope="col">Imports</th>
              <th scope="col">Documentation</th>
            </tr>
          </thead>''')
                    f.write('<tbody>')
                    for i in find_imports():
                        s = ' '.join(i[:-1])
                        f.write('<tr>')
                        f.write('<td>')
                        f.write(s)
                        f.write('</td>')
                        f.write('<td>')

                        if i[-1] == '':
                            f.write('NONE')
                        else:
                            i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                    f.write('</tbody></table>')
                if len(find_class_interface_enum('class')) != 0:
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">Class</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
                    f.write('<tbody>')
                    for i in find_class_interface_enum('class'):
                        s = ' '.join(i[0:-1])
                        f.write('<tr>')
                        f.write('<td>')
                        f.write(s)
                        f.write('</td>')
                        f.write('<td>')
                        if i[-1] == '':
                            f.write('NONE')
                        else:
                            i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                    f.write('</tbody></table>')
                    f.write('<br>')
                if len(find_class_interface_enum('enum')) > 0:
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">Enum</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
                    f.write('<tbody>')
                    for i in find_class_interface_enum('enum'):
                        s = ' '.join(i[:-1])
                        f.write('<tr>')
                        f.write('<td>')
                        f.write(s)
                        f.write('</td>')
                        f.write('<td>')
                        if i[-1] == '':
                            f.write('NONE')
                        else:
                            i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                        f.write('</tbody></table>')
                        f.write('<br>')
                if len(find_class_interface_enum('interface')) != 0:
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">Interface</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
                    f.write('<tbody>')
                    for i in find_class_interface_enum('interface'):
                        s = ' '.join(i[:-1])
                        f.write('<tr>')
                        f.write('<td>')
                        f.write(s)
                        f.write('</td>')
                        f.write('<td>')
                        if i[-1] == '':
                            f.write('NONE')
                        else:

                            i[-1] = re.sub(r'\*[*]+', '*', i[-1])

                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                    f.write('</tbody></table>')
                    f.write('<br>')

                f.write('<br>')

                f.write('<table class="table table-striped"><a name="variable"></a>')
                f.write('''<thead>
    <tr>
      <th scope="col">Variable</th>
      <th scope="col">Documentation</th>
    </tr>
  </thead>''')
                f.write('<tbody>')
                for i in find_variables():
                    f.write('<tr>')
                    f.write('<td>')
                    f.write(i[0])
                    f.write('</td>')
                    f.write('<td>')
                    if i[-1] == '':
                        f.write('NONE')
                    else:
                        i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                        f.write(i[-1][4:-2].replace('*', '<br>'))
                    f.write('</td>')
                    f.write('</tr>')
                f.write('</tbody></table>')

                # f.write('VARIABLES - ' + str(find_variables()))
                f.write('<br>')
                if find_variables_enum():
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">Variable enum</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
                    f.write('<tbody>')
                    for i in find_variables_enum():
                        if i.strip() != '':
                            i = i.strip()
                            f.write('<tr>')
                            f.write('<td>')
                            f.write(i)
                            f.write('</td>')
                            f.write('<td>')
                            f.write('NONE')
                            f.write('</td>')
                            f.write('</tr>')
                    f.write('</tbody></table>')
                    f.write('<br>')

                f.write('<table class="table table-striped"><a name="method"></a>')
                f.write('''<thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Documentation</th>
    </tr>
  </thead>''')
                f.write('<tbody>')
                for i in find_methods():
                    f.write('<tr>')
                    f.write('<td>')
                    f.write(i[0])
                    f.write('</td>')
                    f.write('<td>')
                    if i[-1] == '':
                        f.write('NONE')
                    else:
                        i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                        f.write(i[-1][4:-2].replace('*', '<br>'))
                    f.write('</td>')
                    f.write('</tr>')
                f.write('</tbody></table>')
                f.write('<br>')
                f.write('<br>')
                f.write('<table class="table table-striped"><a name="constructor"></a>')
                f.write('''<thead>
    <tr>
      <th scope="col">Constructor</th>
      <th scope="col">Documentation</th>
    </tr>
  </thead>''')
                f.write('<tbody>')
                for i in find_constructors():
                    f.write('<tr>')
                    f.write('<td>')
                    f.write(i[0])
                    f.write('</td>')
                    f.write('<td>')
                    if i[-1] == '':
                        f.write('NONE')
                    else:
                        i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                        f.write(i[-1][4:-2].replace('*', '<br>'))
                    f.write('</td>')
                    f.write('</tr>')
                f.write('</tbody></table>')
                f.write('<br>')

                f.write('</body>')
                f.close()


def create_java_doc_for_one_class(classpath, path_to_res):
    read_file(classpath)
    f = open(path_to_res+ classpath[classpath.rfind('/'):][:-5] + '.html', "w")
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>''')
    f.write('<body>')
    f.write('<h1>JavaDoc</h1>')
    f.write('<div><p>')
    f.write('Date of Generation - ' + str(datetime.utcnow()) + '<br>Version of generator - 2.1')
    f.write('</p></div>')
    s = about_java_file()
    if s != '':
        f.write('<br>')
        f.write('<div><h2>About this class</h2>')
        f.write(s)
        f.write('</div>')
    if len(find_package()) != 0:
        f.write('<table class="table table-striped">')

        f.write('''<thead>
                <tr>
                  <th scope="col">Package</th>
                </tr>
              </thead>''')
        f.write('<tr><td>')
        f.write(find_package()[0])
        f.write('</tr></td>')
        f.write('</tbody></table>')



    if len(find_imports()) != 0:
        f.write('<table class="table table-striped">')
        f.write('''<thead>
            <tr>
              <th scope="col">Imports</th>
              <th scope="col">Documentation</th>
            </tr>
          </thead>''')
        f.write('<tbody>')
        for i in find_imports():
            s = ' '.join(i[:-1])
            f.write('<tr>')
            f.write('<td>')
            f.write(s)
            f.write('</td>')
            f.write('<td>')
            if i[-1] == '':
                f.write('NONE')
            else:
                i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                f.write(i[-1][4:-2].replace('*', '<br>'))
            f.write('</td>')
            f.write('</tr>')
        f.write('</tbody></table>')
        f.write('<br>')


    if len(find_class_interface_enum('class')) != 0:
        f.write('<table class="table table-striped">')
        f.write('''<thead>
        <tr>
          <th scope="col">Class</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
        f.write('<tbody>')
        for i in find_class_interface_enum('class'):
            s = ' '.join(i[0:-1])
            f.write('<tr>')
            f.write('<td>')
            f.write(s)
            f.write('</td>')
            f.write('<td>')
            if i[-1] == '':
                f.write('NONE')
            else:
                i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                f.write(i[-1][4:-2].replace('*', '<br>'))
            f.write('</td>')
            f.write('</tr>')
        f.write('</tbody></table>')
        f.write('<br>')
    if len(find_class_interface_enum('enum')) != 0:
        print(find_class_interface_enum('enum'))
        f.write('<table class="table table-striped">')
        f.write('''<thead>
        <tr>
          <th scope="col">Enum</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
        f.write('<tbody>')
        for i in find_class_interface_enum('enum'):
            s = ' '.join(i[:-1])
            f.write('<tr>')
            f.write('<td>')
            f.write(s)
            f.write('</td>')
            f.write('<td>')
            if i[-1] == '':
                f.write('NONE')
            else:
                i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                f.write(i[-1][4:-2].replace('*', '<br>'))
            f.write('</td>')
            f.write('</tr>')
            f.write('</tbody></table>')
            f.write('<br>')

    if len(find_class_interface_enum('interface')) != 0:
        f.write('<table class="table table-striped">')
        f.write('''<thead>
        <tr>
          <th scope="col">Interface</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
        f.write('<tbody>')
        for i in find_class_interface_enum('interface'):
            s = ' '.join(i[:-1])
            f.write('<tr>')
            f.write('<td>')
            f.write(s)
            f.write('</td>')
            f.write('<td>')
            if i[-1] == '':
                f.write('NONE')
            else:

                i[-1] = re.sub(r'\*[*]+', '*', i[-1])

                f.write(i[-1][4:-2].replace('*', '<br>'))
            f.write('</td>')
            f.write('</tr>')
        f.write('</tbody></table>')
        f.write('<br>')

    if len(find_variables()) != 0:
        f.write('<table class="table table-striped"><a name="variable"></a>')
        f.write('''<thead>
        <tr>
          <th scope="col">Variable</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
        f.write('<tbody>')
        for i in find_variables():
            f.write('<tr>')
            f.write('<td>')
            f.write(i[0])
            f.write('</td>')
            f.write('<td>')
            if i[-1] == '':
                f.write('NONE')
            else:
                i[-1] = re.sub(r'\*[*]+', '*', i[-1])
                f.write(i[-1][4:-2].replace('*', '<br>'))
            f.write('</td>')
            f.write('</tr>')
        f.write('</tbody></table>')

        # f.write('VARIABLES - ' + str(find_variables()))
        f.write('<br>')
    if find_variables_enum():
        f.write('<table class="table table-striped">')
        f.write('''<thead>
        <tr>
          <th scope="col">Variable enum</th>
          <th scope="col">Documentation</th>
        </tr>
      </thead>''')
        f.write('<tbody>')
        for i in find_variables_enum():
            if i.strip() != '':
                i = i.strip()
                f.write('<tr>')
                f.write('<td>')
                f.write(i)
                f.write('</td>')
                f.write('<td>')
                f.write('NONE')
                f.write('</td>')
                f.write('</tr>')
        f.write('</tbody></table>')
        f.write('<br>')

    f.write('<table class="table table-striped"><a name="method"></a>')
    f.write('''<thead>
    <tr>
      <th scope="col">Method</th>
      <th scope="col">Documentation</th>
    </tr>
  </thead>''')
    f.write('<tbody>')
    for i in find_methods():
        f.write('<tr>')
        f.write('<td>')
        f.write(i[0])
        f.write('</td>')
        f.write('<td>')
        if i[-1] == '':
            f.write('NONE')
        else:
            i[-1] = re.sub(r'\*[*]+', '*', i[-1])
            f.write(i[-1][4:-2].replace('*', '<br>'))
        f.write('</td>')
        f.write('</tr>')
    f.write('</tbody></table>')
    f.write('<br>')
    f.write('<br>')
    f.write('<table class="table table-striped"><a name="constructor"></a>')
    f.write('''<thead>
    <tr>
      <th scope="col">Constructor</th>
      <th scope="col">Documentation</th>
    </tr>
  </thead>''')
    f.write('<tbody>')
    for i in find_constructors():
        f.write('<tr>')
        f.write('<td>')
        f.write(i[0])
        f.write('</td>')
        f.write('<td>')
        if i[-1] == '':
            f.write('NONE')
        else:
            i[-1] = re.sub(r'\*[*]+', '*', i[-1])
            f.write(i[-1][4:-2].replace('*', '<br>'))
        f.write('</td>')
        f.write('</tr>')
    f.write('</tbody></table>')
    f.write('<br>')

    f.write('</body>')
    f.close()


if __name__ == '__main__':
    key = ''
    directory_path = ''
    path_to_res = ''
    try:
        program_path, directory_path, path_to_res, key = argv
        print(key)
    except:
        print('Error, wrong key')
        exit(-1)
    if key == '-p':
        create_directories_files(directory_path, path_to_res)
        create_index(path_to_res + '/res/dirs', path_to_res + '/res/files', directory_path, path_to_res)
        show_classes_in_package(directory_path, path_to_res)
        write_files(directory_path, path_to_res)
    elif key == '-c':
        create_java_doc_for_one_class(directory_path, path_to_res)
