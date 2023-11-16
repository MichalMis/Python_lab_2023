import sys
import os

def counting_files(dir_path):
     count = 0
     for path in os.listdir(dir_path):
         if os.path.isfile(os.path.join(dir_path, path)):
             count += 1
     print('Files Number: ', count)

def directory_list(dir):
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            print("Pliki w katalogu ",dir ,":", path)
        elif os.path.isdir(os.path.join(dir, path)):
            print(os.path.join(dir, path))
            directory_list(os.path.join(dir, path))
            


def main():
    dir_path = r'D:\Lab_Python'
    counting_files(dir_path)
    directory_list(dir_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
