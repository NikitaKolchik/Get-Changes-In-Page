# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:36:10 2020

@author: admin
"""

from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf8'     
    return r.text   

 
url1 = open("origin.txt", "r").read() 
url2 = open("another.txt", "r").read() 


html1 = get_html(url1)
html2 = get_html(url2)

       
soup1 = BeautifulSoup(html1, 'lxml')
soup2 = BeautifulSoup(html2, 'lxml')
while True:
    button1 = str(soup1.find_all('a', id='make-everything-ok-button'))
    button1 = button1[1:-1]
    button2 = str(soup2.find_all('a', id='make-everything-ok-button'))
    
    if len(button2) ==2:
        print('----------------------------------------------------------------\n') 
        print('make-everything-ok-button IN NEW FILE NOT FOUND\n')
        
    
    mydivs = soup2.findAll("div", {"class": "col-lg-8"})
    mydivs = str(mydivs)
    divA=str(mydivs).split('<a')
    
    for split in divA:
        if 'btn-success' in split:
            button2 = split
            button2 = '<a' + button2
            button2 = button2.split('</a>')
            button2 = button2[0] + '</a>'
            
            if len(button2)==2:
                print(2)
                break
            
    print('----------------------------------------------------------------\n')       
    
    if button1 == button2:
        print('BUTTONS ARE EQUAL')
        break
    print('make-everything-ok-button changed from:\n')       
    print(button1) 
    print('to:\n')  
    print(button2) 
    break
