import re

java_file = ''
classname = ''
constructor = []
last_constructor = []


def read_file(path_to_file):
    global java_file
    global java_array
    java_file = open(path_to_file, 'r').read()
    java_file = re.sub(r'//[^\n]+\n', '', java_file)
    java_file = java_file.replace('\n', ' ')


def find_class_interface_enum(class_interface):
    class_arrays = []
    class_comments = ''
    class_array = re.findall(r'[;{}][^;{}]+ ' + class_interface + r' [^{]+[{]', java_file)
    for i in range(0, len(class_array)):
        class_array[i] = class_array[i][1:-1].strip()
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
                annotation += class_array[i][index]
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
        while index< len(class_first) and class_first[index] not in {' ', '<'}:
            k = len(class_first)
            classname += class_first[index]
            index += 1
    return class_arrays


def find_variables():
    variables_arr = []
    try:
        first_variables = re.findall(r'[{][^;]*[;]', java_file)[0][1:]
        if first_variables.count('(') == 0 and java_file[:java_file.index(first_variables)].count('{') - java_file[
                                                                                                         :java_file.index(
                                                                                                             first_variables)].count(
            '}') == 1 and java_file[:java_file.index(first_variables)].count('"') % 2 == 0:
            p = first_variables.split(' ')
            for j in p:
                if '@' in j:
                    first_variables = first_variables.replace(j, '')
            comments = re.findall(r'/\*\*[^`]+\*/', first_variables)
            comment = ''
            for j in comments:
                first_variables = first_variables.replace(j, '')
                comment += j
            variables_arr.append(
                [first_variables.replace('>', '&gt;').replace('<', '&lt;').replace(';', '').strip(), comment])
    except:
        print('no variables')
    s = java_file[java_file.index('{'):]
    a = re.findall(r'[;][^;]+[;]', java_file.replace(';', ';;')[java_file.replace(';', ';;').index('{'):])
    for i in re.findall(r'[;][^;]+[;]', java_file.replace(';', ';;')[java_file.replace(';', ';;').index('{'):]):

        p = i.split(' ')
        t = i
        for j in p:
            if '@' in j:
                i = i.replace(j, '')
        comments = re.findall(r'/\*\*[^`]+\*/', i)
        comment = ''
        for j in comments:
            i = i.replace(j, '')
            comment += j
        if i != '' and t != ';;' and (('"' not in i and "/" not in i) or '=' in i):
            if ')' not in i and java_file[:java_file.index(t)].count('{') - java_file[:java_file.index(t)].count(
                    '}') == 1:
                variables_arr.append([i.replace('>', '&gt;').replace('<', '&lt;').replace(';', '').strip(),
                                      comment.replace('>', '&gt;').replace('<', '&lt;').replace(';', '').strip()])

    return variables_arr


def find_methods():
    global java_file
    global java_array
    global constructor
    ################
    while java_file.count('@') != 0:

        index = java_file.find('@')
        left = 0
        right = 0
        annotation = java_file[index]
        while (java_file[index] != ' ' and right == 0) or (left == 1 and right == 0):
            index += 1
            annotation += java_file[index]
            if java_file[index] == '(':
                left += 1
            elif java_file[index] == ')':
                right += 1
        java_file = java_file.replace(annotation, '')

    ############
    methods_arr = []
    start_index = -1
    for i in re.findall(r'[(][^)]*[)]', java_file):
        method_comments = ''
        method_modifier_arr = []
        start_index += 1
        start_index = start_index + java_file[start_index:].find(i)
        min_index = start_index - 1
        max_index = start_index + len(i)
        while java_file[min_index] not in ('{', '}', ')', ')', ';', '/'):
            if min_index == 0:
                break
            min_index -= 1
            a = java_file[min_index:max_index]

        while java_file[max_index] not in ('{', '}', ')', ')', ';' '/'):
            if java_file[min_index: max_index].endswith(';') or java_file[min_index: max_index].endswith('{'):
                break
            if max_index == len(java_file) - 1:
                break
            max_index += 1
            a = java_file[min_index:max_index]

        min_index += 1
        method_str = java_file[min_index: max_index].strip()
        if (method_str.endswith('{') or method_str.endswith(';') or java_file[max_index] == '{') and method_str.count(
                '(') == 1 and method_str.count(
            ')') == 1 and '.' not in method_str and '*' not in method_str:
            arr_method = method_str.split(' ')
            if 'for' not in arr_method and 'if' not in arr_method and 'catch' not in arr_method and '=' not in arr_method:
                left_bracket = method_str.find('(')
                right_bracket = method_str.find(')')
                in_brackets = method_str[left_bracket: right_bracket + 1]
                throws = method_str[right_bracket + 1:]
                method_str = method_str[:left_bracket]
                method_str = re.sub(r'[ ]+', ' ', method_str)
                method_arr = method_str.split(' ')
                if len(method_arr) < 2:
                    continue
                method_name = method_arr[-1]
                method_str = method_str[:method_str.rfind(' ')]
                if method_str.endswith(' '):
                    method_str = method_str[:-1]
                if method_str.endswith('>'):
                    left_index = method_str.find('<')
                    type_brackets = method_str[left_index:]
                    method_str = method_str[:left_index]
                    method_arr = method_str.split(' ')
                    method_return_type = method_arr[-1] + type_brackets
                    method_arr.append('')
                else:
                    method_return_type = method_arr[-2]
                modifiers = ''
                if len(method_arr) >= 2:
                    index = 3
                    while len(method_arr) >= index:
                        if method_arr[-index] in (
                                'abstract', 'final', 'static', 'native', 'synchronized', 'public', 'protected',
                                'private'):
                            method_modifier_arr.append(method_arr[-index])
                        index += 1
                    method_modifier_arr.reverse()
                    modifiers = ' '.join(method_modifier_arr)
                throws = throws.strip()
                is_comment = False
                for j in range(min_index, -1, -1):
                    if len(method_comments) == 2 and method_comments[1] != '*':
                        is_comment = False
                        method_comments = ''
                    if java_file[j] == '/':
                        is_comment = True
                    if is_comment:
                        method_comments += java_file[j]
                    if method_comments.endswith('**/'):
                        break
                    if not is_comment and (java_file[j] == '{' or java_file[j] == '}' or java_file == ';'):
                        break
                method_comments = method_comments[::-1]
                modifiers = modifiers.replace('>', '&gt;').replace('<', '&lt;').strip()
                method_return_type = method_return_type.replace('>', '&gt;').replace('<', '&lt;').strip()
                method_name = method_name.replace('>', '&gt;').replace('<', '&lt;').strip()
                in_brackets = in_brackets.replace('>', '&gt;').replace('<', '&lt;').strip()
                throws = throws.replace('>', '&gt;').replace('<', '&lt;').strip()
                method_comments = method_comments.replace('>', '&gt;').replace('<', '&lt;').strip()

                try:
                    if re.sub(r'&lt;[^1]+&gt;', '', method_name) == classname:
                        global constructor
                        constructor.append(
                            [modifiers, method_return_type, method_name, in_brackets, throws, method_comments])
                    else:
                        methods_arr.append(
                            [modifiers, method_return_type, method_name, in_brackets, throws, method_comments])

                except:
                    methods_arr.append(
                        [modifiers, method_return_type, method_name, in_brackets, throws, method_comments])

    java_file = ''
    java_array = []
    global last_constructor
    last_constructor = constructor
    constructor = []

    return methods_arr


def find_constructors():
    return last_constructor


if __name__ == '__main__':
    read_file("src/com/pubnub/api/models/consumer/pubsub/MessageResult.java")
    find_class_interface_enum('class')
    find_class_interface_enum('interface')
    find_variables()
    find_methods()
    find_constructors()
