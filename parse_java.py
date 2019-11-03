import re

java_file = ''
java_array = []
constructor = []


def read_file(path_to_file):
    global java_file
    global java_array
    java_file = open(path_to_file, 'r').read()
    java_file = java_file.replace('\n', ' ')
    java_array_without_comments = re.split(r'[/][*][*][^/]+[/]', java_file)
    java_array_comments = re.findall(r'[/][*][*][^/]+[/]', java_file)
    index = 0
    if java_array_without_comments[0] == '':
        index += 1
        java_array.append(java_array_comments[0])
    for i in range(0, len(java_array_without_comments)):
        java_array_without_comments[i] = re.sub(r'[ ]+', ' ', java_array_without_comments[i])
        arr = java_array_without_comments[i].split(' ')
        for j in arr:
            if j != '':
                java_array.append(j)
        if len(java_array_comments) > i + index:
            java_array.append(java_array_comments[i + index])


def find_class_interface_enum(class_interface):
    class_array = []
    classname = ''
    class_modifier = ''
    comments = ''
    start_index = -1
    for i in range(0, java_array.count(class_interface)):
        class_modifier = ''
        implements_extends = []
        comments = ''
        class_modifier_arr = []
        start_index += 1
        start_index = start_index + java_array[start_index:].index(class_interface)
        classname = java_array[start_index + 1]
        indx = 2
        while '{' not in java_array[start_index + indx]:
            implements_extends.append(java_array[start_index + indx])
            indx += 1
        if classname.endswith('}'):
            classname = classname[:-1]
        index = 1
        while java_array[start_index - index] in (
                'static', 'final', 'private', 'protected', 'public', 'abstract', 'strictfp'):
            class_modifier_arr.append(java_array[start_index - index])
            index += 1
        class_modifier_arr.reverse()
        class_modifier = ' '.join(class_modifier_arr)
        for j in range(start_index - 1, -1, -1):
            if ';' in java_array[j] or '}' in java_array[j] or '{' in java_array[j]:
                break
            if '/**' in java_array[j]:
                comments = java_array[j]
                break
        class_array.append([class_modifier, class_interface, classname, comments, ' '.join(implements_extends)])
    return class_array


def find_variables():
    variables_arr = []
    left_brace = 0
    right_brace = 0
    left = 0 # {
    right = 0 # }
    for i in range(0, len(java_array)):
        variable_name = ''
        variable_modifier = []
        variable_type = ''
        left_brace += java_array[i].count('(')
        right_brace += java_array[i].count(')')
        left += java_array[i].count('{')
        right += java_array[i].count('}')
        if java_array[i] in ('byte', 'short', 'int', 'long', 'char', 'float', 'double', 'boolean', 'String'):
            if left_brace == right_brace and '(' not in java_array[i + 1] and '(' not in java_array[i + 2] and left - right == 1:
                variable_type = java_array[i]
                variable_name = java_array[i + 1]
                index = 1
                while java_array[i - index] in (
                        'static', 'final', 'transient', 'volatile', 'protected', 'public', 'private'):
                    variable_modifier.append(java_array[i - index])
                    index += 1
                comments = ''
                variable_modifier.reverse()
                variable_modifier = ' '.join(variable_modifier)
                for j in range(i - 1, -1, -1):
                    if ';' in java_array[j] or '}' in java_array[j] or '{' in java_array[j]:
                        break
                    if '/**' in java_array[j]:
                        comments = java_array[j]
                        break
                variables_arr.append([variable_modifier, variable_type, variable_name, comments])
    print(variables_arr)
    return variables_arr


def find_methods():
    methods_arr = []
    start_index = -1
    for i in re.findall(r'[(][^)]*[)]', java_file):
        in_brackets = ''
        throws = ''
        method_name = ''
        method_return_type = ''
        method_modifier = ''
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
        while java_file[max_index] not in ('{', '}', ')', ')', ';' '/'):
            if max_index == len(java_file) - 1:
                break
            max_index += 1
        min_index += 1
        method_str = java_file[min_index: max_index].strip()
        if java_file[max_index] == '{' and method_str.count('(') == 1 and method_str.count(
                ')') == 1 and '.' not in method_str and '*' not in method_str:
            arr_method = method_str.split(' ')
            if 'for' not in arr_method and 'if' not in arr_method and 'catch' not in arr_method and '=' not in arr_method:
                left_bracket = method_str.find('(')
                right_bracket = method_str.find(')')
                in_brackets = method_str[left_bracket: right_bracket + 1]
                throws = method_str[right_bracket + 1:]
                method_str = method_str[:left_bracket]
                method_str = re.sub(r'[ ]+', ' ', method_str)
                ###############################
                # method_arr = method_str.split(' ')
                # method_name = method_arr[-1]
                # method_return_type = method_arr[-2]
                ############################
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
                if len(method_arr) > 2:
                    index = 3
                    while len(method_arr) >= index:
                        if method_arr[-index] in (
                        'abstract', 'final', 'static', 'native', 'synchronized', 'public', 'protected', 'private'):
                            method_modifier_arr.append(method_arr[-index])
                        index += 1
                    method_modifier_arr.reverse()
                    modifiers = ' '.join(method_modifier_arr)
                throws = throws.strip()
                ###########
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
                try:
                    if method_name == find_class_interface_enum('class')[0][2]:
                        global constructor
                        constructor.append([modifiers, method_return_type, method_name, in_brackets, throws, method_comments])
                    else:
                        methods_arr.append([modifiers, method_return_type, method_name, in_brackets, throws, method_comments])

                except:
                    methods_arr.append([modifiers, method_return_type, method_name, in_brackets, throws, method_comments])

                   # methods_arr.append([modifiers, method_return_type, method_name, in_brackets, throws, method_comments])

    for i in methods_arr:
        print(i)
    return methods_arr


if __name__ == '__main__':
    read_file("src/main/java/com/pubnub/api/PubNub.java")
    # find_class_interface_enum('class')
    # find_class_interface_enum('interface')
    # find_variables()
    find_methods()
    print(len(constructor))