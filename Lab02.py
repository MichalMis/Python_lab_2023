import os
import sys

def replace_word(file_path,new_file_path,word):
    with open(file_path, 'r') as file:  
        filedata = file.read()  
    filedata = filedata.replace(word, 'not so random')  
    with open(new_file_path, 'w') as new_file:  
        new_file.write(filedata)  

def remove_words(file_path,new_file_path,word):
    with open(file_path, 'r') as file:  
        filedata = file.read()  
    filedata = filedata.replace(word, '')  
    with open(new_file_path, 'w') as new_file:  
        new_file.write(filedata)  

def main():
    file_path = r'D:\Lab_Python\plik_testowy.txt'
    new_file_path = r'D:\Lab_Python\nowy_plik_testowy.txt'
    replace_word(file_path,new_file_path,"random")  
    remove_words(new_file_path,new_file_path,"text")
    print("Words has been replaced")

if __name__ == '__main__':
    sys.exit(main())