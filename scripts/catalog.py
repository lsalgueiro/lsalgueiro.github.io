import datetime
import operator
import re

cat = {
    1: {
        "title": "Três poemas de David Mourão-Ferreira",
        "year": 2012,
        "dur": 6,
        "dates": "2012",
        "inst": "voice and piano",
        "perf": {
            1: {
                "date": datetime.datetime(2013, 5, 18),
                "venue": "Palácio Nacional da Ajuda, Lisboa",
                "ensemble": "Carolina Sá (sop), Bárbara Santos (pf)"
            },
            2: {
                "date": datetime.datetime(2013, 5, 3),
                "venue":
                "Grande Auditório da Escola Superior de Música de Lisboa",
                "ensemble": "Carolina Sá (sop), Fernando Loura (pf)"
            },
        }
    },
    2: {
        "title": "Anatomia de um suspiro",
        "year": 2013,
        "dur": 6,
        "dates": "Abril 2013",
        "inst": "violoncello",
        "perf": {
            1: {
                "date": datetime.datetime(2013, 6, 5),
                "venue": "Escola Superior de Música de Lisboa",
                "solo": "Raquel Merrelho"
            },
            2: {
                "date": datetime.datetime(2013, 6, 7),
                "venue": "Escola Superior de Música de Lisboa",
                "solo": "Paulo Cepêda"
            },
            3: {
                "date": datetime.datetime(2013, 6, 28),
                "venue": "Escola Superior de Música de Lisboa",
                "solo": "Raquel Merrelho"
            },
            4: {
                "date": datetime.datetime(2015, 5, 19),
                "venue":
                "Grande Auditório da Escola Superior de Música de Lisboa",
                "solo": "Raquel Merrelho"
            },
        }
    },
    3: {
        "title": "Trust/Tryst",
        "year": 2013,
        "dur": 5,
        "dates": "Julho 2013",
        "inst": "percussion duo",
        "perf": {
            1: {
                "date": datetime.datetime(2014, 3, 15),
                "venue":
                "Grande Auditório da Escola Superior de Música de Lisboa",
                "ensemble": "Sforzanduo",
            }
        }
    },
    4: {
        "title": "Mar violento",
        "year": 2018,
        "dur": 11,
        "dates": "2014, Verão; 2018, Janeiro",
        "award":
        "Honorable mention, Banda Sinfónica Portuguesa Prize for Composition.",
        "inst": "wind orchestra",
        "perf": {
            1: {
                "date": datetime.datetime(2018, 3, 18),
                "venue": "Sala Suggia, Casa da Música, Porto",
                "ensemble": "Banda Sinfónica Portuguesa",
                "cond": "Pedro Neves"
            }
        }
    },
    5: {
        "title": "Gentes",
        "year": 2015,
        "dur": 5,
        "dates": "Maio 2016",
        "comm": " Setúbal Music Festival, for the Setúbal Youth Ensemble",
        "note":
        "encomenda do Festival de Música de Setúbal, dedicado ao Ensemble Juvenil de Setúbal",
        "inst": "ensemble and live electronics",
        "perf": {
            1: {
                "date": datetime.datetime(2015, 5, 30),
                "venue": "Fórum Luísa Todi, Setúbal",
                "ensemble": "Setúbal Youth Ensemble",
                "cond": "Rui Borges Maia"
            },
            2: {
                "date": datetime.datetime(2015, 6, 7),
                "venue": "Cine-Teatro S. João, Palmela",
                "ensemble": "Setúbal Youth Ensemble",
                "cond": "Rui Borges Maia"
            },
            3: {
                "date": datetime.datetime(2015, 10, 1),
                "venue": "Auditório 2 da Fundação Calouste Gulbenkian, Lisboa",
                "ensemble": "Setúbal Youth Ensemble",
                "cond": "Rui Borges Maia"
            },
        }
    },
    6: {
        "title": "tu julgas que amas",
        "year": 2016,
        "dur": 3,
        "dates": "Janeiro 2016",
        "comm": "Antena 2/RTP, for Prémio Jovens Músicos 2016.",
        "note":
        "encomenda do Prémio Jovens Músicos; peça obrigatório para Piano (nível superior)",
        "inst": "piano",
        "perf": {
            1: {
                "date":
                datetime.datetime(2016, 6, 28),
                "venue":
                "Salão Nobre do Conservatório Nacional, Lisboa",
                "PJM":
                'Isabel Romero, Pedro Patrocínio Borges, Rodrigo Ayala, Alexandru Stratila, Luís Cardoso Arede, Vasco Dantas Rocha, Diogo da Costa Simões, Tiago Rosário'
            },
            2: {
                "date": datetime.datetime(2019, 12, 7),
                "venue":
                "Kammermusiksaal, Hochschule für Musik, Theater und Medien Hannover",
                "solo": 'Leonie Kruppa'
            },
        },
        "soundcloud": 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/348574893&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"'
    },
    7: {
        "title": "prelúdio, coral e fuga",
        "year": 2017,
        "dur": 12,
        "dates": "Julho–Outubro 2017",
        "note": "originalmente escrito para o VI concurso Lopes-Graça",
        "inst": "piano four hands",
        "perf": {
            1: {
                "date": datetime.datetime(2018, 3, 25),
                "venue": "Escola Superior de Música de Lisboa",
                "ensemble": "Duarte Pereira Martins and Philippe Marques, pf"
            }
        },
        "soundcloud": '"https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/538870590&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"'
    },
    8: {
        "title": "bokeh",
        "year": 2018,
        "dur": 10,
        "dates": "Maio–Junho 2018",
        "award": "Honorable mention, SPA/Antena 2 Prize for Composition 2018.",
        "inst": "orchestra",
    },
    9: {
        "title": "chaser (dbs#0)",
        "year": 2018,
        "dur": 2,
        "dates": "Agosto–Setembro 2018",
        "comm":
        "Arte no Tempo for the project Nova Música para Novos Músicos 2019.",
        "note":
        "encomenda da Arte no Tempo para o projecto Nova Música para Novos Músicos 2019.",
        "inst": "trumpet and electronics",
        "perf": {
            1: {
                "date": datetime.datetime(2019, 3, 15),
                "venue": "Sala Estúdio, Teatro Aveirense, Aveiro",
            }
        }
    },
    10: {
        "title": "hoje é dia de coisas simples",
        "year": 2019,
        "dur": 8,
        "dates": "Outubro 2018 – Janeiro 2019",
        "note":
        "composto no contexto do Laboratório de Criação de Ópera da Inestética Companhia Teatral, com Luís Soldado e Alexandre Lyra Leite.",
        "inst": "soprano, baritone and chamber ensemble",
        "perf": {
            1: {
                "date": datetime.datetime(2019, 1, 26),
                "venue": "Palácio do Sobralinho, Vila Franca de Xira",
            }
        }
    },
    11: {
        "title": "L'envie de rire",
        "year": 2019,
        "dur": 9,
        "dates": "Fev + Maio–Jun",
        "note":
        "enoa workshop Composing for voices, dirigido por Luís Tinoco. Sobre texto de Georges Bataille.",
        "inst": "soprano and orchestra",
        "perf": {
            1: {
                "date": datetime.datetime(2019, 7, 13),
                "venue":
                "Grande Auditório da Fundação Calouste Gulbenkian, Lisboa",
                "ensemble": "Orquestra Gulbenkian",
                "cond": "Pedro Neves",
                "solo": "Lara Martins, sop"
            }
        }
    },
    12: {
        "title": "Fuzzy Concepts",
        "year": 2019,
        "dur": 2,
        "dates": "Agosto–Setembro",
        "comm":
        "Arte no Tempo for the project Nova Música para Novos Músicos 2020.",
        "note":
        "encomenda da Arte no Tempo para o projecto Nova Música para Novos Músicos 2020.",
        "inst": "viola and fixed media"
    },
    13: {
        "title": "Wolf Town",
        "year": 2020,
        "dur": 10,
        "dates": "Outubro 2019 – Março 2020",
        "inst": "saxophone quartet"
    },
    14: {
        "title": "A Princeza dos sapatos de ferro",
        "year": 2020,
        "dur": 11,
        "dates": "Agosto 2019 – Junho 2020",
        "inst": "piano four hands",
        "comm": "Duarte Pereira Martins and Philippe Marques"
    },
    15: {
        "title": "Early Eckensee",
        "year": 2020,
        "dur": 13,
        "dates": "rec. February 2020, ed. June 2020",
        "inst": "2 ch. audio",
        "perf": {
            1: {
                "date": datetime.datetime(2020, 6, 23),
                "venue": "5:4",
            }
        }
    }
}


def site_index():
    #generate works.html file for the site, overwriting
    f = open(
        "/Users/LSalgueiro/Documents/GitHub/lsalgueiro.github.io/works.html",
        "w")
    jekyllheader = '''---\nlayout: notitle\ntitle: works\nimage: /assets/images/DSCF4031.jpg\n---\n<div class="grid">'''
    f.write(jekyllheader)

    oldyear = 0
    index = len(cat)

    # sort by year
    order = {}
    for key in cat:
        order[key] = cat[key]['year']
    byYear = reversed(sorted(order.items(), key=lambda kv: (kv[1], kv[0])))

    for i in byYear:
        index = i[0]

        if cat[index]["year"] != oldyear:
            year = '<h1>' + str(cat[index]["year"]) + '</h1>'
            f.write(year)
            oldyear = cat[index]["year"]
        else:
            pass

        piece = ('<div class="piece"><works>'
                 '<h6>' + cat[index]["title"] + '</h6>'
                 '<p>for ' + cat[index]["inst"] + '</p>'
                 '<p>dur. ca. ' + str(cat[index]["dur"]) + "\'</p>")
        f.write(piece)

        if 'comm' in cat[index]:
            f.write('<p>Commissioned by ' + cat[index]["comm"] + '</p>')
        else:
            pass

        if 'award' in cat[index]:
            f.write('<p>' + cat[index]["award"] + '<p>')
        else:
            pass

        if 'perf' in cat[index]:
            f.write(('<p>Premiered ' +
                     (cat[index]["perf"][1]["date"].strftime("%d/%m/%Y")) +
                     ', ' + cat[index]["perf"][1]["venue"] + '</p>'))
            if 'ensemble' in cat[index]["perf"][1]:
                f.write('<p>' + cat[index]["perf"][1]["ensemble"])
                if 'cond' in cat[index]["perf"][1]:
                    f.write(', cond. ' + cat[index]["perf"][1]["cond"])
                f.write('</p>')
            if 'solo' in cat[index]["perf"][1]:
                f.write('<p>' + cat[index]["perf"][1]["solo"] + '</p>')
        else:
            pass

        close = ('</works>' '</div>')
        f.write(close)

    f.write('</div>')
    f.close()

    pass

def work_page(key):
    title = cat[key]['title']
    to_lowercase = title.lower()
    strip_special_chars = re.sub('[^a-zA-Z.\d\s]', '', to_lowercase)
    strip_spaces = strip_special_chars.replace(' ', '-')
    filename = strip_spaces
    
    with open(f'./_works/{filename}.md', 'w') as new_file:
        title = cat[key]['title']
        inst = cat[key]['inst']
        dur = cat[key]['dur']
        soundcloud = cat[key]['soundcloud']
        
        opt = ''
        if 'comm' in cat[key]:
            opt += 'comm: ' + cat[key]['comm']
        else:
            pass
        
        if 'perf' in cat[key]:
            opt += '\nprem: ' + cat[key]['perf'][1]['date'].strftime("%d/%m/%Y") + ', ' + cat[key]['perf'][1]['venue']
            if 'ensemble' in cat[key]["perf"][1]:
                opt += cat[key]["perf"][1]["ensemble"]
                if 'cond' in cat[key]["perf"][1]:
                    opt += ', cond. ' + cat[key]["perf"][1]["cond"]
            if 'solo' in cat[key]["perf"][1]:
                opt += cat[key]["perf"][1]["solo"]
        else:
            pass
        
        work_header = f'''---\nlayout: work\ntitle: {title}\ninst: {inst}\ndur: {dur}\n#image: /assets/images/placeholder-2.jpg\nsoundcloud: {soundcloud}\n{opt}\n---'''
        print(work_header)
        new_file.write(work_header)


site_index()
#work_page(6)