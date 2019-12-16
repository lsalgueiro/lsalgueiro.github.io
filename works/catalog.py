#!/usr/bin/python
# coding=latin-1
import datetime
import operator

#generate works.html file for the site, overwriting
f = open("/Users/LSalgueiro/Documents/GitHub/lsalgueiro.github.io/works.html", "w")
jekyllheader = '''---
layout: notitle
title: works
image: /assets/images/placeholder-22.jpg
---
'''
f.write(jekyllheader)


cat = {
    12: {
        "title": "L'envie de rire",
        "year": 2019,
        "dur": 9,
        "dates": "Fev + Maio–Jun",
        "note": "enoa workshop Composing for voices, dirigido por Luís Tinoco. Sobre texto de Georges Bataille.",
        "inst": "soprano and orchestra",
        "perf": {
              1: {
                 "date": datetime.datetime(2019, 7, 13),
                 "venue": "Grande Auditório da Fundação Calouste Gulbenkian, Lisboa",
                  }
             }
        },
    13: {
        "title": "Fuzzy Concepts",
        "year": 2019,
        "dur": 2,
        "dates": "Agosto–Setembro",
        "comm": "Arte no Tempo for the project Nova Música para Novos Músicos 2020.",
        "note": "encomenda da Arte no Tempo para o projecto Nova Música para Novos Músicos 2020.",
        "inst": "viola and fixed media",
        "perf": {
              1: {
                 "date": datetime.datetime(2020, 3, 1),
                 "venue": "Festival Aveiro_Síntese, Teatro Aveirense, Aveiro",
                  }
             }
        }
    }


year = "<h1>2019</h1>"
f.write(year)


index = 13
while index > 0:
    piece = (
    '<div class="piece"><works>'
    '<h6>' + cat[index]["title"] + '</h6>'
    '<p>for ' + cat[index]["inst"] + '</p>'
    '<p>dur. ca. ' + str(cat[index]["dur"]) + "\'</p>"
    )
    f.write(piece)
    
    if 'comm' in cat[index]:
        f.write('<p>Commissioned by ' + cat[index]["comm"] + '</p>')
    else:
        print "boo"


    prem = (
    '<p>Premiered ' + (cat[index]["perf"][1]["date"].strftime("%d/%m/%Y")) + ', ' + cat[index]["perf"][1]["venue"] + '</p>'
    )
    f.write(prem)
    
    
    close = (
    '</works>' 
    '</div>'
    )
    f.write(close)
    
    index -= 1

#im running this from the shell, which doesn't have python 3.x installed, so using concatenation instead of fstrings…




#print(cat[1]['name'])
# print(cat[12]["perf"][1]["date"].strftime("%B"))
# print(cat[12]["perf"][1]["date"].year)
# print(cat[12]["perf"][1]["venue"])


#how to iterate
# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
    
#     for key in p_info:
#         print(key + ':', p_info[key])






f.close()