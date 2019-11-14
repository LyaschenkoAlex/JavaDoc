import re

java_file = ''
comments = []
classname = ''
constructor = []
last_constructor = []
imports = []
about_file = ''


def read_file(path_to_file):
    global comments
    global constructor
    global java_file
    global about_file
    constructor = []
    try:
        java_file = open(path_to_file, 'r').read()
    except:
        java_file = ''
    if java_file.startswith('/**'):
        index = java_file.find('*/') + 2
        about_file = java_file[:index].replace('\n', '<br>')
        java_file = java_file[index:]
    ans = ''
    while java_file.count('/*\n') != 0:
        index = java_file.find('/*\n')
        ans = ''
        while not ans.endswith('*/'):
            ans += java_file[index]
            index += 1
        java_file = java_file.replace(ans, '')
    new_java = ''
    right = 0
    left = 0
    for i in range(len(java_file)):

        if java_file[i] == '}' and java_file[:i].count('/**') == java_file[:i].count('*/'):
            left += 1
        if right - left < 2:
            new_java += java_file[i]
        if java_file[i] == '{' and java_file[:i].count('/**') == java_file[:i].count('*/'):
            right += 1
    java_file = new_java
    java_file = re.sub(r'[\n ]//[^\n]+', '\n', java_file)
    java_file = java_file.replace('\n', ' ')
    while '/**' in java_file:
        s = ''
        index = java_file.find('/**')
        while not s.endswith('*/'):
            s += java_file[index]
            index += 1
        s = s.replace('\n', '<br>')
        comments.append(s)
        java_file = java_file.replace(s, '~comment' + str(len(comments) - 1) + '~')

    c = False
    new_java_file = ''
    left = 0
    right = 0
    for i in range(len(java_file)):
        if not ((java_file[i] != ' ' and right == 0) or (left == 1 and right == 0)) and c == True:
            c = False
            left = 0
            right = 0
        s = ''
        if java_file[i] == '@' and java_file[:i].count('/**') == java_file[:i].count('*/'):
            c = True
        if c and java_file[i] == '(':
            left += 1
        if c and java_file[i] == ')':
            right += 1
        if not c:
            new_java_file += java_file[i]
    java_file = new_java_file


def find_class_interface_enum(class_interface):
    global classname

    class_arrays = []

    classes = re.findall(r'[^;{}]+ ' + class_interface + ' [^{]+', java_file)
    for i in classes:
        if ';' not in i:

            if java_file[:java_file.find(i)].count('{') - java_file[:java_file.find(i)].count('}') == 0:
                comments_c = re.findall(r'~comment\d+~', i)
                for j in comments_c:
                    i = i.replace(j, '')
                classname = i
                comment = ''
                i = i + '{'
                i = i[:-1]
                if len(comments_c) > 0:
                    comment = comments[int(comments_c[-1][8:-1])]
                    i = i.replace('<', '&lt;').replace('>', '&gt;')
                    comment = comment.replace('<', '&lt;').replace('>', '&gt;')
                class_arrays.append([i.strip(), comment])
    return class_arrays


def find_variables():
    variables_arr = []
    variables = re.findall(r'[^;{}]*[;=]', java_file)
    for i in variables:

        if '=' not in i:
            if '(' not in i:
                if java_file[:java_file.find(i)].count('{') - java_file[:java_file.find(i)].count('}') == 1:
                    if i.endswith('='):
                        i = i[:-1] + ';'
                    comments_v = re.findall(r'~comment\d+~', i)
                    for j in comments_v:
                        i = i.replace(j, '')
                    comment = ''
                    if len(comments_v) > 0:
                        comment = comments[int(comments_v[-1][8:-1])]
                    i = i.replace('<', '&lt;').replace('>', '&gt;')
                    comment = comment.replace('<', '&lt;').replace('>', '&gt;')
                    variables_arr.append([i.strip(), comment])
        else:
            if '(' not in i[:i.find('=')]:
                if java_file[:java_file.find(i)].count('{') - java_file[:java_file.find(i)].count('}') == 1:
                    index = java_file.find(i) + len(i) - 1
                    while (java_file[index]) not in {';', '{'}:
                        index += 1
                        i += java_file[index]
                    comments_v = re.findall(r'~comment\d+~', i)
                    for j in comments_v:
                        i = i.replace(j, '')
                    comment = ''
                    if len(comments_v) > 0:
                        comment = comments[int(comments_v[-1][8:-1])]
                    i = i.replace('<', '&lt;').replace('>', '&gt;')
                    comment = comment.replace('<', '&lt;').replace('>', '&gt;')
                    variables_arr.append([i.strip(), comment])
            i = i[:i.find('=')]
    return variables_arr


def find_methods():
    methods_arr = []
    methods = re.findall(r'[^;{}]*[;{]', java_file)
    for i in methods:
        i = i[:-1]
        if java_file[:java_file.find(i)].count('{') - java_file[:java_file.find(i)].count('}') == 1 and '=' not in i:
            if ')' in i and '(' in i:

                comments_v = re.findall(r'~comment\d+~', i)
                for j in comments_v:
                    i = i.replace(j, '')
                comment = ''
                if len(comments_v) > 0:
                    comment = comments[int(comments_v[-1][8:-1])]
                index = i.find('(')
                index -= 1
                method_name = ''
                if i[index] != ' ':
                    while i[index] != ' ':
                        method_name += i[index]
                        index -= 1
                else:
                    while i[index] == ' ':
                        index -= 1
                    while i[index] != ' ':
                        method_name += i[index]
                        index -= 1
                i = i.replace('<', '&lt;').replace('>', '&gt;')
                comment = comment.replace('<', '&lt;').replace('>', '&gt;')
                if method_name[::-1] not in classname:
                    methods_arr.append([i.strip(), comment])
                else:
                    global constructor
                    constructor.append([i.strip(), comment])

    return methods_arr


def find_constructors():
    global java_file
    global comments
    global classname
    global last_constructor
    global imports
    java_file = ''
    comments = []
    classname = ''
    last_constructor = []
    imports = []
    global constructor
    return constructor


def find_imports():
    ret_imports_arr = []
    imports_arr = re.findall(r'[^;]+import[^;]+', java_file)
    for i in imports_arr:
        comment = ''
        comments = re.findall(r'/\*\*[^`]+\*/', i)
        for j in comments:
            comment += j
            i = i.replace(j, '')
        ret_imports_arr.append([i.replace('>', '&gt;').replace('<', '&lt;').strip(),
                                comment.replace('>', '&gt;').replace('<', '&lt;').strip()])
    return ret_imports_arr


def find_variables_enum():
    variables_arr = []
    if len(find_class_interface_enum('enum')) != 0:
        string_variables = ''
        index = java_file.find('{')
        index += 1
        while java_file[index] not in {'}', ';'}:
            string_variables += java_file[index]
            index += 1
        if ',' in string_variables:
            arr_variables = string_variables.split(',')
            for i in arr_variables:
                variables_arr.append(i)
    return variables_arr


def about_java_file():
    global about_file
    s = about_file
    about_file = ''
    return s


# if __name__ == '__main__':
#     read_file("src/StdAudio.java")
#     print(find_class_interface_enum('class'))
#     print(about_java_file())
#     print(len(about_file))
#     print(find_class_interface_enum('interface'))
#     print(find_class_interface_enum('enum'))
#     print(find_variables_enum())
#     print(find_variables())
#     print(find_imports())
#     print(find_methods())
#     print(find_constructors())
