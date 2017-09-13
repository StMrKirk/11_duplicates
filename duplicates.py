import os
import sys
import hashlib


def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def data_check(directory):
    same_hash_files = {}
    os.chdir(directory)
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath,filename)
            filename_hash = hashfile(path)
            if filename_hash in same_hash_files:
                same_hash_files[filename_hash].append(path)
            else:
                same_hash_files[filename_hash] = [path]
    return same_hash_files


def look_for_duplicates(directory):
    duplicates_counter = 0
    for file_hash in data_check(directory).keys():
        if len(data_check(directory)[file_hash]) > 1:
            duplicates_counter += 1
            print('Дубликаты {}. Пути и имена к файлам:'.format(duplicates_counter))
            for file in data_check(directory)[file_hash]:
                print(file)
        elif len(data_check(directory)[file_hash]) == 1:
            pass


if __name__ == '__main__':
    look_for_duplicates(sys.argv[1])
