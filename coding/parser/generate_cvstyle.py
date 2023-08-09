#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: generate_cvstyle.py
# Project: parser
# File Created: Monday, 6th June 2022 2:01:25 pm
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Monday, 6th June 2022 2:01:26 pm
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2022 - C.V
###


import bibtexparser

with open('papers.txt') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)

counter = {}
for idx in range(0,130):
    print(bib_database.entries[idx]['ID'])
    counter[(int((bib_database.entries[idx]['artnumber'])))] = idx

for key in sorted(counter, reverse=True):
    print(key, counter[key])

f_name = 'name_transformed_papers.tex'
f = open('/home/claudio/Downloads/parser/'+f_name, 'a')
for key in sorted(counter, reverse=True):
    idx = counter[key]
    s1 = s2 = s3 = s4 = s5 = s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=""
    title = bib_database.entries[idx]['title']
    authors = bib_database.entries[idx]['author']
    journal = bib_database.entries[idx]['journal']
    link = "https://cvinegoni.github.io/assets/pdf/papers/"+bib_database.entries[idx]['pdf']
    if "pmid" in bib_database.entries[idx].keys():
        pmid = bib_database.entries[idx]['pmid']
    else:
        pmid = "N/A"
    if "pmcid" in bib_database.entries[idx].keys():
        pmcid = bib_database.entries[idx]['pmcid']
    else:
        pmcid = "N/A"
    if "doi" in bib_database.entries[idx].keys():
        doi = bib_database.entries[idx]['doi']
    else:
        doi = "N/A"    
    if "volume" in bib_database.entries[idx].keys():
        volume = bib_database.entries[idx]['volume']
    else:
        volume = "N/A"

    year = bib_database.entries[idx]['year']
    pages = bib_database.entries[idx]['pages']

    s1 = """\item \htmladdnormallink{\\it  """
    s1 = s1 + title +"""}{"""
    s2 = s1 + link + """} \\\ """
    s3 = s2 + authors + """ \\\ ``""" + journal
    s4 = s3+"""'' Vol. """
    s5 = s4+volume+""" ("""
    s6 = s5+year+""") pp. """+pages+""". \\\ """
    s7 = s6+ """DOI: """ + doi + """ PMID: """ + pmid + """ PMCID: """ + pmcid
    s8 = s7.replace('<sup>#</sup>','$^\\#$')
    s9 = s8.replace('<sup>†</sup>','$^\dag$')
    s10 = s9.replace('<sup>†#</sup>','$^{\dag \\#}$')
    s11 = s10.replace('<sup>#†</sup>','$^{\dag \\#}$')
    s12 = s11.replace('Vinegoni$^\\#$, C.','{\\bf Vinegoni$^\\#$, C.}')
    s13 = s12.replace('Vinegoni$^\dag$, C.','{\\bf Vinegoni$^\dag$, C.}')
    s14 = s13.replace('Vinegoni$^{\dag \\#}$, C.','{\\bf Vinegoni$^{\dag \\#}$, C.}')
    s15 = s14.replace('Vinegoni, C.','{\\bf Vinegoni, C.}')

    f.write(s15)
f.close()


##

with open('proceedings.txt') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)


counter = {}
for idx in range(0,130):
    print(bib_database.entries[idx]['ID'])
    counter[(int((bib_database.entries[idx]['artnumber'])))] = idx

for key in sorted(counter, reverse=True):
    print(key, counter[key])


for i in range(0,130):
    print(bib_database.entries[i]['ID'])


f_name = 'name_transformed_proceedings.tex'
f = open('/home/claudio/Downloads/parser/'+f_name, 'a')
for key in sorted(counter, reverse=True):
    idx = counter[key]
    s1 = s2 = s3 = s4 = s5 = s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=""
    title = bib_database.entries[idx]['title']
    authors = bib_database.entries[idx]['author']
    link = "https://cvinegoni.github.io/assets/pdf/proceedings/"+bib_database.entries[idx]['pdf']
    year = bib_database.entries[idx]['year']
    book = bib_database.entries[idx]['booktitle']

    s1 = """\item \htmladdnormallink{\\it """   
    s1 = s1 + title +"""}{"""
    s2 = s1 + link + """} \\\ """
    s3 = s2 + authors + """ \\\ ``"""
    s4 = s3+book + """'' """
    s5 = s4+""" ("""
    s6 = s5+year+"""). """
    s7 = s6.replace('Vinegoni, C.','{\\bf Vinegoni, C.}')

    f.write(s7)
f.close()




with open('conferences.txt') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)



counter = {}
for idx in range(0,130):
    print(bib_database.entries[idx]['ID'])
    counter[(int((bib_database.entries[idx]['artnumber'])))] = idx

for key in sorted(counter, reverse=True):
    print(key, counter[key])


for i in range(0,130):
    print(bib_database.entries[i]['ID'])



f_name = 'name_transformed_conferences.tex'
f = open('/home/claudio/Downloads/parser/'+f_name, 'a')
for key in sorted(counter, reverse=True):
    idx = counter[key]
    s1 = s2 = s3 = s4 = s5 = s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=""
    title = bib_database.entries[idx]['title']
    authors = bib_database.entries[idx]['author']
    year = bib_database.entries[idx]['year']
    book = bib_database.entries[idx]['booktitle']

    s1 = """\item \\it """   
    s2 = s1 + title +""" \\\ """
    s3 = s2 + authors + """ \\\ ``"""
    s4 = s3+book + """'' """
    s5 = s4+""" ("""
    s6 = s5+year+"""). """
    s7 = s6.replace('Vinegoni, C.','{\\bf Vinegoni, C.}')

    f.write(s7)
f.close()