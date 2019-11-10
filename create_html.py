import os
from parse_java import *
from parseDirectoryTree import *

left_block = ''


def create_index(directory_dirs, directory_files):
    f = open('res\\index' + '.html', "w")
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
        <div class="col-sm-4 list-group" style="overflow: auto; margin: 10px;"> <h4>All packages</h4>
            ''')
    for root, dirs, files in os.walk(directory_dirs):
        global left_block

        for file in files:
            left_block += '<a href="dirs/' + file + '" style="width:auto; font-size:12px">' + file.replace('-', '/')[
                                                                                              :-5] + '</a>'
            f.write('<a href="dirs/' + file + '" style="width:auto; font-size:12px">' + file.replace('-', '/')[
                                                                                        :-5] + '</a>')
    f.write('''          
        </div>
        <div class="col-sm-5 list-group" style="overflow:auto;">
        <h4>All classes</h4>''')
    for root, dirs, files in os.walk(directory_files):
        for file in files:
            f.write('<a href="files/' + file + '" style="width:auto; font-size:12px"> ' + file.replace('-', '/')[
                                                                                          :-5] + '.java</a>')
    f.write('''
        </div>
        <div class="col-sm-2 list-group" style="overflow:auto;">
        <h4>Alphabetical index</h4>''')
    alphabet_set = set()
    alphabet_dict = {}
    for root, dirs, files in os.walk(directory_files):
        for file in files:
            alphabet_set.add(str(file.split('-')[-1][0]))

            try:
                alphabet_dict[str(file.split('-')[-1][0])] += ' ' + str(file.split('/')[-1])
            except:
                alphabet_dict[str(file.split('-')[-1][0])] = '' + str(file.split('/')[-1])
    alphabet_set = sorted(alphabet_set)
    for key in alphabet_dict:
        f1 = open('res/alphabetical_index/' + key + '.html', "w")
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
        f1.write('<a href="../index.html">All packages</a>')
        href_arr = alphabet_dict[key].split(' ')
        f1.write('<ul class="list-group">')
        for i in href_arr:
            f1.write(
                '<li class="list-group-item"><a href="../files/' + i + '"class="btn btn-default">' + i.replace('-','/')[:-5] + '.java</a></li>')
        f1.write('</ul>')
        f1.write('</body>')
        f1.close()

    for i in alphabet_set:
        f.write(
            '<a href="alphabetical_index/' + i.upper() + '.html' + '" style="width:auto; font-size:12px">' + i.upper() + '</a>')
    f.write('''</div>
    </div>
</div>

</body>
</html>''')
    f.close()


def show_classes_in_package(directory_dirs):
    for root, dirs, files in os.walk(directory_dirs):
        f = open('res/dirs/' + root.replace('\\', '-') + '.html', "w")
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
        f.write('<a href="../index.html"> All packages</a></div>' + '<br><br><h4>Directory -> ' + root + '</h4><ul>')
        for file in files:
            f.write('<li><a href="../files/' + root.replace('\\', '-') + '-' + file.replace('\\', '-')[
                                                                               :-5] + '.html">' + file + '</a></li>')
        f.write('''</ul>
    </div>
</div>

</body>
</html>''')
        f.close()


def write_files(directory_src):
    for root, dirs, files in os.walk(directory_src):
        for file in files:
            if file.endswith('.java'):
                f = open('res/files/' + root.replace('\\', '-') + '-' + file[:-5] + '.html', 'w')
                read_file(root + '\\' + file)
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
                f.write('<br>')
                if find_class_interface_enum('class'):
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">Class</th>
          <th scope="col">Comments</th>
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
                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                    f.write('</tbody></table>')
                    f.write('<br>')

                if find_class_interface_enum('enum'):
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">enum</th>
          <th scope="col">Comments</th>
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
                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                    f.write('</tbody></table>')
                    f.write('<br>')

                if find_class_interface_enum('interface'):
                    f.write('<table class="table table-striped">')
                    f.write('''<thead>
        <tr>
          <th scope="col">Interface</th>
          <th scope="col">Comments</th>
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
                            f.write(i[-1][4:-2].replace('*', '<br>'))
                        f.write('</td>')
                        f.write('</tr>')
                    f.write('</tbody></table>')
                    f.write('<br>')
                f.write('<table class="table table-striped">')
                f.write('''<thead>
        <tr>
          <th scope="col">Imports</th>
          <th scope="col">Comments</th>
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
                        f.write(i[-1][4:-2].replace('*', '<br>'))
                    f.write('</td>')
                    f.write('</tr>')
                f.write('</tbody></table>')
                f.write('<br>')

                f.write('<table class="table table-striped"><a name="variable"></a>')
                f.write('''<thead>
    <tr>
      <th scope="col">Variable</th>
      <th scope="col">Comments</th>
    </tr>
  </thead>''')
                f.write('<tbody>')
                for i in find_variables():
                    s = ' '.join(i[:-1])
                    f.write('<tr>')
                    f.write('<td>')
                    f.write(s)
                    f.write('</td>')
                    f.write('<td>')
                    if i[-1] == '':
                        f.write('NONE')
                    else:
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
          <th scope="col">Comments</th>
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
      <th scope="col">Comments</th>
    </tr>
  </thead>''')
                f.write('<tbody>')
                for i in find_methods():
                    s = ' '.join(i[:-1])
                    f.write('<tr>')
                    f.write('<td>')
                    f.write(s)
                    f.write('</td>')
                    f.write('<td>')
                    if i[-1] == '':
                        f.write('NONE')
                    else:
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
      <th scope="col">Comments</th>
    </tr>
  </thead>''')
                f.write('<tbody>')
                for i in find_constructors():
                    s = ' '.join(i[:-1])
                    f.write('<tr>')
                    f.write('<td>')
                    f.write(s)
                    f.write('</td>')
                    f.write('<td>')
                    if i[-1] == '':
                        f.write('NONE')
                    else:
                        f.write(i[-1][4:-2].replace('*', '<br>'))
                    f.write('</td>')
                    f.write('</tr>')
                f.write('</tbody></table>')
                f.write('<br>')

                f.write('</body>')
                f.close()


if __name__ == '__main__':
    create_directories_files()
    create_index('res/dirs', 'res/files')
    show_classes_in_package('src')
    write_files('src')
