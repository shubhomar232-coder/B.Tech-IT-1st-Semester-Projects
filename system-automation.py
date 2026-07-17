import sys
import os
import shutil
def leave():
    sys.exit("You are leaving Simple Text Editor")


def read():
    try:
        file_name = input("Enter your file name: ")
        target = open(file_name, "r")
        readfile = target.read()
        print(readfile)
    except Exception as e:
        print("There was a problem: %s" % (e))


def delete():
    file_name = input("Enter your file name: ")
    try:
        os.unlink(file_name)
    except Exception as e:
        print("There was a problem: %s" % (e))


def write():
    try:
        print("it will first prompt file name,type the file name to create new file,then type the text for file,on next line type menu to save the file and return to the main menu")
        file_name = input("Enter your file name: ")
        target = open(file_name, "a")
        while True:
            append = input()
            target.write(append)
            target.write("\n")
            if append.lower() == "menu":
                break
    except Exception as e:
        print("There was a problem: %s" % (e))


def cwd():
    try:
        print(os.getcwd())
        change = input("Change Y/N: ")
        if change.startswith("y"):
            path = input("New CWD: ")
            os.chdir(path)
    except Exception as e:
        print("There was a problem: %s" % (e))


def rename():
    try:
        file_name = input("Enter current file name: ")
        new = input("Enter new file name: ")
        shutil.move(file_name, new)
    except Exception as e:
        print("There was a problem: %s" % (e))


while True:
    print("===================================================")
    print("                 SIMPLE TEXT EDITOR")
    print("===================================================")
    print("Options: \n write\n read\n cwd\n exit\n delete\n rename")
    do = input("So, what are you wishing for today: ")
    if do.lower() == "write":
        write()
    elif do.lower() == "read":
        read()
    elif do.lower() == "delete":
        delete()
    elif do.lower() == "exit":
        leave()
    elif do.lower() == "cwd":
        cwd()
    elif do.lower() == "rename":
        rename()
