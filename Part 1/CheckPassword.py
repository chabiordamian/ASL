# zad4    #########################################
# Napisz skrypt realizujacy funkcj¦ zamka szyfrowego. Prosi o podanie kodu
# i nastepnie sprawdza czy jest on zgodny z wczesniej wprowadzonym kodem
####################################################
password = input("Set password: ")
try:
    int(password)
except ValueError:
    print("Wrong format!")
if password == input("Please provide your password\n"):
    print("Password matched")
else:
    print("Wrong -\(o.o)/-")