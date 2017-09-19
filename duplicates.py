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
        list_of_lists_file_size = [[file_item, file_item] for file_item in data_check_result[file_size]]
        same_name__file_dict = [item[1] for item in list_of_lists_file_size if
                                Counter([item_inner[0] for item_inner in list_of_lists_file_size])[item[0]] > 1]
        data_check_result[file_size] = same_name__file_dict
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
