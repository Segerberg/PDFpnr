#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import argparse
import glob
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import csv
import time
import datetime
import fnmatch

#Skapar argument som används i terminal/kommandoprompt 
parser = argparse.ArgumentParser(description='Ett program som extraherar personnummer ur pdf-filer')
parser.add_argument('-p')
parser.add_argument('-o')
parser.add_argument('-n', nargs='?', const = 11, default = 11)
args = parser.parse_args()

#Funktion som används för att kontrollera giltiga tecken 
def match(strg, search=re.compile(r'[^0-9-]').search):
    return not bool(search(strg))
    
#Funktion som används för att skapa tidsstämplar 
def timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H%M%S')
    return st

#Öppna filer som information ska skrivas till 
utfil = open(args.o, 'a')
logfil = open('log.txt', 'a')

#Skapar headerinformation för CSV-filen 
header = "filnamn,personnummer"+"\n" 

#Skriver headerinformation till CSV-filen
utfil.write(header) 

###Globala variabler för att hålla antal filer, antal processade metadata samt antal fel###
count = 0
itemcount = 0
errorcount = 0

###Söker igenom samtliga kataloger efter alla filer med ändelse .pdf###
matches = []
for root, dirnames, filenames in os.walk(args.p):
    for file in fnmatch.filter(filenames, '*.pdf'):
        matches.append(os.path.join(root, file))
        
for file in matches:        
    count = count + 1
    a = PdfFileReader(open(file, "rb"))
    b = a.getXmpMetadata()
    c = b.dc_subject
    file = file.split(args.p, 1)[1]
    
    #Kontrollera om metadata saknas 
    if c == []:
        stamp = timestamp()
        text = '  1: '
        logtext = stamp + text + file +'\n'
        errorcount = errorcount + 1
        logfil.write(logtext)
        
    #Kontrollera att antalet tecken överensstämmer med det satta kriteriet i -n flaggan
    else:
        for item in c:
            if len(item) != args.n:
                stamp = timestamp()
                text = '  2: '+ item 
                logtext = stamp + text + file +'\n'
                logfil.write(logtext)

                errorcount = errorcount + 1
            #Kontrollerar att personnummer innehåller giltiga tecken 
            elif match(item) is False:
                stamp = timestamp()
                text = '  3: '+ item 
                logtext = stamp + text + file +'\n'
                logfil.write(logtext)
                
            #Skriver till utfilen
            else:
                itemcount = itemcount + 1
                item2 = file +","+item+'\n'
        
                utfil.write(item2)        
#Stäng alla filer
utfil.close
logfil.close

#Skriver ut meddelanden i terminalen 
print count, 'filer bearbetade'
print itemcount, 'personnummer extraherade'
print errorcount, 'fel.'

