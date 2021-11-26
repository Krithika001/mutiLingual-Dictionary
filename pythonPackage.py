# -*- coding: utf-8 -*-
"""
            PYTHON-PACKAGE
             SEMESTER-II

        PSG COLLEGE OF TECHNOLOGY
                AMCS

@author: ALAGU PRAKALY-19PD05
         KRITHIKA-19PD19
"""


import json
import csv 
import pandas as pd 
from difflib import get_close_matches
from googletrans import Translator

data=json.load(open("data.json"))
p=[]
def definition(word):
    if word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data,n=6,cutoff=0.8))>0:
        print("DID YOU MEAN ANY OF THE FOLLOWING?/n")
        for i in range(0,len(get_close_matches(word,data,n=6,cutoff=0.8))):
            print(get_close_matches(word,data,n=6,cutoff=0.8)[i])
        dec=input("[y/n]")
        if dec=="y":
            fin=input("Enter the word.")
        elif dec=='n':
            print("THE WORD DOESN'T EXIST.DO TRY AGAIN!!!!")
            return 0
            if fin!="none" :
                return(definition(fin))
    else:
        print("THE WORD DOESN'T EXIST.DO TRY AGAIN!!!!")
        return 0
        
r=1
print("\n***********************************************************\n")
print("               WELCOME TO THE S%A DICTIONARY                   ")
print("\n***********************************************************\n")
print("HERE YOU COULD FIND THE DEFINITONS AND THE ANTONYMS OF WORDS...\n")
print("Dear User,this is Non-Case Sensitive and you could find the best matches\nwhen you are stuck with what you want to search\n")

ip=input("Enter the word:\t")

print("\n**DEFINITON**\n")
val=definition(ip)

if val!=0:
    for j in val:
        print(r,".",j)
        r+=1
    print("\n**PART OF SPEECH AND IT'S RESPECTIVE ANTONYM**\n")
    with open("antonyms.csv") as csv_file:  
      
    # read the csv file 
        csv_reader = csv.reader(csv_file, delimiter=',') 
       
    # now we can use this csv files into the pandas 
        df = pd.DataFrame([csv_reader], index=None) 
        df.head() 
    
    # iterating values of first column 
    count=7
    for i in range(1,11244):
        v=list(df[i])
        if v[0][0]==ip.lower():
            print("Part of speech: {0:20} Antonym: {1:30}".format(v[0][1],v[0][2]))
            count=2
    if count==7:
        print("\n*****NO ANTONYM FOUND FOR THIS WORD******\n")
    print("\n**SYNONYM**\n")
    with open("synonyms.csv") as csv_file:  
      
    # read the csv file 
        csv_reader = csv.reader(csv_file, delimiter=',') 
       
    # now we can use this csv files into the pandas 
        df = pd.DataFrame([csv_reader], index=None) 
        df.head() 
    
    # iterating values of first column 
    count_2=7
    for i in range(1,127000):
        v=list(df[i])
        if v[0][0]==ip.lower():
            print("Synonym:  ",v[0][2])
            count_2=2
    if count_2==7:
        print("\n*****NO SYNONYM FOUND FOR THIS WORD******\n")
  
    print("\n****MULTILINGUAL DICTIONARY****\n")
    a=0
    while True :
        gs=Translator()
        print("\nEnter \n1-Tamil\n2-Hindi\n3-Malayalam\n4-French\n5-Chinese\n6-German\n7-Telugu\n8-Russian\n9-Greek\n10-Kannada\n11-Exit")
        a=int(input())
        if a==1 :
            print("\n****TAMIL****\n")
            text=gs.translate(ip,dest='ta')
            print(text.text)
        elif a==2 :
            print("\n****HINDI****\n")
            text=gs.translate(ip,dest='hi')
            print(text.text)
        elif a==3 :
            print("\n****MALAYALAM****\n")
            text=gs.translate(ip,dest='ml')
            print(text.text)
        elif a==4 :
            print("\n****FRENCH****\n")
            text=gs.translate(ip,dest='fr')
            print(text.text)
        elif a==5 :
            print("\n****CHINESE****\n")
            text=gs.translate(ip,dest='zh-cn')
            print(text.text)
        elif a==6 :
            print("\n****GERMAN****\n")
            text=gs.translate(ip,dest='de')
            print(text.text)
        elif a==7 :
            print("\n****TELUGU****\n")
            text=gs.translate(ip,'te')
            print(text.text)
        elif a==8 :
            print("\n****RUSSIAN****\n")
            text=gs.translate(ip,'ru')
            print(text.text)
        elif a==9 :
            print("\n****GREEK****\n")
            text=gs.translate(ip,'el')
            print(text.text)
        elif a==10 :
            print("\n****KANADA****\n")
            text=gs.translate(ip,'kn')
            print(text.text)
        else :
            break   
        print("\n**************")
print("\n**********THANKS FOR USING OUR DICTIONARY**********\n")