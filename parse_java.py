import re

java_file = ''
comments = []
classname = ''
constructor = []
last_constructor = []
imports = []


def read_file(path_to_file):
    global comments
    global java_file
    try:
        java_file = open(path_to_file, 'r').read()
    except:
        java_file = ''
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
            new_java+=java_file[i]
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
        comments.append(s)
        java_file = java_file.replace(s, '~comment' + str(len(comments) - 1) + '~')

    c=False
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
    class_arrays = []
    class_comments = ''
    class_array = re.findall(r'[;{}][^;{}]+ ' + class_interface + r' [^{]+[{]', java_file)
    for i in range(0, len(class_array)):
        class_array[i] = class_array[i][1:-1].strip()
        if '*/' in class_array[i]:
            index = java_file.find(class_array[i])
            while '/**' not in class_array[i]:
                index -= 1
                try:
                    class_array[i] = java_file[index] + class_array[i]
                except:
                    break
        comment = re.findall(r'/\*\*[^`]+\*/', class_array[i])
        for j in comment:
            class_comments += j
            class_array[i] = class_array[i].replace(j, '')
        while class_array[i].count('@') != 0:

            index = class_array[i].find('@')
            left = 0
            right = 0
            annotation = class_array[i][index]
            while (class_array[i][index] != ' ' and right == 0) or (left == 1 and right == 0):
                index += 1
                try:
                    annotation += class_array[i][index]
                except:
                    break
                if class_array[i][index] == '(':
                    left += 1
                elif class_array[i][index] == ')':
                    right += 1
            class_array[i] = class_array[i].replace(annotation, '')
        class_array[i] = class_array[i].replace('  ', ' ')
        class_array[i] = re.sub(r'/\*[^*]+\*/', '', class_array[i]).replace('>', '&gt;').replace('<', '&lt;').strip()
        class_arrays.append([class_array[i], class_comments.replace('>', '&gt;').replace('<', '&lt;')])
    if len(class_array) > 0:
        class_first = class_array[0]
        index = class_first.find(class_interface)
        index += len(class_interface) + 1
        global classname
        classname = ''
        t = class_first[index]
        while index < len(class_first) and class_first[index] not in {' ', '<'}:
            k = len(class_first)
            classname += class_first[index]
            if classname.endswith('&lt;'):
                classname = classname[:-4]
                break
            index += 1
    return class_arrays


def find_variables():
    variables_arr = []
    variables = re.findall(r'[^;{}]*[;=]', java_file)
    for i in variables:
        if '=' in i:
            i = i[:i.find('=')]
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
                variables_arr.append([i.strip(), comment])
    return variables_arr


def find_methods():
    methods_arr = []
    methods = re.findall(r'[^;{}]*[;{]', java_file)
    for i in methods:
        i = i[:-1]
        if java_file[:java_file.find(i)].count('{') - java_file[:java_file.find(i)].count('}') == 1 and '=' not in i:
            if ')' in i:
                comments_v = re.findall(r'~comment\d+~', i)
                for j in comments_v:
                    i = i.replace(j, '')
                comment = ''
                if len(comments_v) > 0:
                    comment = comments[int(comments_v[-1][8:-1])]
                methods_arr.append([i.strip(), comment])
    return methods_arr


def find_constructors():
    return last_constructor


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


if __name__ == '__main__':
    read_file("src/guava-master/android/guava/src/com/google/common/base/Absent.java")
    print(find_class_interface_enum('class'))
    print(find_class_interface_enum('interface'))
    print(find_class_interface_enum('enum'))
    print(find_variables_enum())
    print(find_variables())
    print(find_imports())
    print(find_methods())
