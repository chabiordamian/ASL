# zad3b   ###########################################
# sparsowac przygotowanego XML (parserem DOM) i go zmody-
# fkowac np. zmieni¢ wartosc ktoregos tag'a,
#####################################################
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("test.xml")
collection = DOMTree.documentElement
content = collection.getElementsByTagName('CenaZlota')
print("*****Table of gold price changes*****")

for data in content:
    date = data.getElementsByTagName('Data')[0].childNodes[0].data
    price = data.getElementsByTagName('Cena')[0].childNodes[0].data
    print("Data: {} Cena: {}".format(date, price))

doc = xml.dom.minidom.parse("dom.xml")
new_change = doc.createElement("Zmiana")
new_change.setAttribute("Zmiana","-3%")
doc.firstChild.appendChild(new_change)
change = doc.getElementsByTagName("Zmiana")
for data in change:
    print("Zmiana: {}".format(data.getAttribute("Zmiana")))
