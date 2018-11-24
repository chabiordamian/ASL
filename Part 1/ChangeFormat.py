# zad6    #########################################
# Napisz skrypt konwersji rozszerzen plikow *.jpg na *.png (uprzednio stworz
# zestaw 4 plików z rozszerzeniem *.jpg)
####################################################
import os

current_script_path = os.path.dirname(os.path.abspath(__file__))
os.sys.path.insert(0, os.path.dirname(os.path.dirname(current_script_path)))

file_name_list = ["Damian.jpg", "Piotrek.jpg", "Kon.jpg", "Piesek.jpg"]
os.chdir(current_script_path)
for file in file_name_list:
    with open(file, "a+") as f:
        base = os.path.splitext(file)[0]
        f.close()
    try:
        os.rename(file, base + ".png")
    except FileExistsError:
        print ("Files already exist!")