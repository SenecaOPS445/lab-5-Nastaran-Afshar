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
    list = [line.strip() for line in list]
    return list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))