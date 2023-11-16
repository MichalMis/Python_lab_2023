import re
import os
import sys

def replace_words_with_regex(file_path, new_file_path, word_to_replace, replacement):
    with open(file_path, 'r') as file:
        filedata = file.read()
    filedata = re.sub(word_to_replace, replacement, filedata)
    with open(new_file_path, 'w') as new_file:
        new_file.write(filedata)

def remove_words_with_regex(file_path, new_file_path, words_to_remove):
    with open(file_path, 'r') as file:
        filedata = file.read()
    for word in words_to_remove:
        filedata = re.sub(word, '', filedata)
    with open(new_file_path, 'w') as new_file:
        new_file.write(filedata)

def main():
    file_path = r'D:\Lab_Python\plik_testowy.txt'
    new_file_path = r'D:\Lab_Python\nowy_plik_testowy_2.txt'
    replace_words_with_regex(file_path, new_file_path, 'random', 'not so random')
    remove_words_with_regex(new_file_path, new_file_path, ['text'])

    print("Words have been replaced and removed")

if __name__ == '__main__':
    sys.exit(main())
