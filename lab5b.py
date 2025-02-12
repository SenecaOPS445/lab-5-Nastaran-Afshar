#!/usr/bin/env python3
# Author ID: [nmohammadiafshar]

def read_file_string(file_name):
    f = open(file_name, 'r')
    string = f.read()
    f.close()
    return string

def read_file_list(file_name):
    f = open(file_name, 'r')
    list = f.readlines()
    f.close()
    list2 = [line.strip() for line in list]
    return list2

def append_file_string(file_name, string_of_lines):
    f = open(str(file_name), 'a')
    added = f.write(str(string_of_lines))
    f.close()
    return added

def write_file_list(file_name, list_of_lines):
    f = open(str(file_name), 'w')
    for line in list_of_lines:
        f.write(line + '\n')  
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    read = open(str(file_name_read), 'r')
    lines = read.readlines()
    read.close()
    write = open(str(file_name_write), 'w')
    for i in range(len(lines)):
        write.write(f"{i + 1}:{lines[i]}")  
    write.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))