import re

java_file = ''
java_array = []


def read_file():
    global java_file
    global java_array
    java_file = open("src/main/java/com/pubnub/api/PubNubError.java", 'r').read()
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


def find_class():
    class_array = []
    classname = ''
    class_modifier = ''
    start_index = -1
    for i in range(0, java_array.count('class')):
        class_modifier = ''
        class_modifier_arr = []
        start_index += 1
        start_index = start_index + java_array[start_index:].index('class')
        classname = java_array[start_index + 1]
        if classname.endswith('}'):
            classname = classname[:-1]
        index = 1
        while java_array[start_index - index] == 'static' or java_array[start_index - index] == 'final' or\
                java_array[start_index - index] == 'protected' or java_array[start_index - index] == 'private' or \
                java_array[start_index - index] == 'public':
            class_modifier_arr.append(java_array[start_index - index])
            index += 1
        class_modifier_arr.reverse()
        class_modifier = ' '.join(class_modifier_arr)
    class_array.append([class_modifier, 'class', classname])
    return class_array


if __name__ == '__main__':
    read_file()
    find_class()
