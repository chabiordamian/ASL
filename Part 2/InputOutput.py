#zad1    ###########################################
# Operacje wejscia/wyjscia (zapisac i odczytac dane)
####################################################
import sys
import shutil

if (len(sys.argv)) < 1:
    print("Usage: script.py filename [ write | read ]\n")
else:
    if sys.argv[2] == "write":
        with open(sys.argv[1], 'w') as file:
            file.write("Hello Everyone!!")
        file.close()
    if sys.argv[2] == "read":
        with open(sys.argv[1], 'r') as file:
            shutil.copyfileobj(file, sys.stdout)
        file.close()
