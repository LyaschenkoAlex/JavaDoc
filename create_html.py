import os

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
            left_block += '<a href="dirs/' + file + '" style="width:auto; font-size:12px">' + file.replace('_', '/')[
                                                                                         :-5] + '</a>'
            f.write('<a href="dirs/'+file+'" style="width:auto; font-size:12px">' + file.replace('_', '/')[:-5] + '</a>')
    f.write('''          
        </div>
        <div class="col-sm-5 list-group" style="overflow:auto;">
        <h4>All classes</h4>''')
    for root, dirs, files in os.walk(directory_files):
        for file in files:
            f.write('<a href="files/' + file + '" style="width:auto; font-size:12px"> ' + file.replace('_', '/')[:-5] + '.java</a>')
    f.write('''
        </div>
    </div>
</div>

</body>
</html>''')
    f.close()


def show_classes_in_package(directory_dirs):
    for root, dirs, files in os.walk(directory_dirs):
        print(root)
        print(files)


if __name__ == '__main__':
    create_index('res/dirs', 'res/files')
    show_classes_in_package('src')