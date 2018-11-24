# zad5    #########################################
# Napisz rekurencyjne przejscie drzewa katalogow i wypisanie plików, które
# znajduje sie w eksplorowanej strukturze
####################################################
import os

current_script_path = os.path.dirname(os.path.abspath(__file__))
os.sys.path.insert(0, os.path.dirname(os.path.dirname(current_script_path)))


def scan_dir(path):
    dir_list = os.scandir(path)
    for file in dir_list:
        if file.is_file():
            print(file.name)
        else:
            scan_dir(file.path)

scan_dir(current_script_path)