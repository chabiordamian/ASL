# zad3a   ###########################################
# sparsowac przygotowanego XML (parserem SAX)
####################################################

import xml.sax
import sys
from xml.sax import saxutils


class Data(object):
    def __init__(self):
        self.date = ""
        self.price = 0

    def __str__(self):
        return "Data: {}\t\tCena: {}".format(self.date, self.price)


class DataHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.current_data = ""
        self.current_rate = None
        self.storage = []

    def startElement(self, tag, attr):
        self.current_data = tag
        if self.current_data == "CenaZlota":
            self.current_rate = Data()

    def endElement(self, tag):
        if self.current_data != "Data" and self.current_data != "Cena":
            if self.current_rate != None:
                self.storage.append(self.current_rate)
                self.current_rate = None
        self.current_data = ""

    def characters(self, content):
        if self.current_data == "Data":
            self.current_rate.date = content
        elif self.current_data == "Cena":
            self.current_rate.price = content

    def return_data(self):
        return self.storage


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = DataHandler()
parser.setContentHandler(handler)
parser.parse("test.xml")
data_tables = handler.return_data()
print("Table below shows how GOLD price changed in times from {} to {}".format(data_tables[0].date, data_tables[-1].date))
for table in data_tables:
    print(table)
