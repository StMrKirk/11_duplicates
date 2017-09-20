import os
import sys
from collections import Counter


def data_check(directory):
    same_size_files = {}
    os.chdir(directory)
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            filename_size = os.stat(path).st_size
            if filename_size in same_size_files:
                same_size_files[filename_size].append(filename)
            else:
                same_size_files[filename_size] = [filename]
    return same_size_files


def check_for_same_name(directory):
    data_check_result = data_check(directory)
    for file_size in data_check_result.keys():
        same_name_files = [file_item for file_item in data_check_result[file_size]
                           if Counter([file_item_in for file_item_in in data_check_result[file_size]])[file_item] > 1]
        data_check_result[file_size] = same_name_files
    return data_check_result


def look_for_duplicates(directory):
    data_check_result = check_for_same_name(directory)
    for file_size in data_check_result.keys():
        if len(data_check_result[file_size]) > 1:
            file_set = set(data_check_result[file_size])
            for file in file_set:
                print(file)
        elif len(data_check_result[file_size]) == 1:
            pass


if __name__ == '__main__':
    look_for_duplicates(sys.argv[1])
