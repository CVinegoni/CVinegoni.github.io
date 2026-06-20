#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: p1.py
# Project: parser
# File Created: Wednesday, 27th April 2022 9:34:35 pm
# Author: C.V (vinegoni@yahoo.com)
# -----
# Last Modified: Wednesday, 27th April 2022 9:34:35 pm
# Modified By: C.V (vinegoni@yahoo.com)
# -----
# Copyright 2022 - C.V
###

import bibtexparser

with open('papers.txt') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

print(bib_database.entries)

for i in range(0,130):
    print(bib_database.entries[i]['ID'])


for idx in range(0,200):
    s1 = s2 = s3 = s4 = s5 = s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=""
    title = "\""+ bib_database.entries[idx]['title']+"\""
    description = bib_database.entries[idx]['journal']
    short_title = bib_database.entries[idx]['ID']
    imgcover_small = bib_database.entries[idx]['ID']+'.jpg'
    if "category" in bib_database.entries[idx].keys():
        category = bib_database.entries[idx]['category']
    else:
        category = "Various"
    year = bib_database.entries[idx]['year']+"""-03-15 16:40:16"""
    reference = bib_database.entries[idx]['ID']
    abstract = "\""+bib_database.entries[idx]['abstract']+"\""
    imgcover = bib_database.entries[idx]['ID']+'.png'
    title_image = imgcover
    importance = year

    s1 = """---\nlayout: papersgallerypage\ntitle: """  
    s1 = s1 + title +"""\n"""
    s2 = s1+"""shorttitle: """+short_title+"""\n"""
    s3 = s2+"""date: """ + year  +"""\n"""
    s4 = s3+"""description: """ + description+"""\n"""
    s5 = s4+"""img: /assets/img/papers/extract/""" + imgcover_small+"""\n"""
    s6= s5+"""tags: formatting links"""+"""\n"""
    s7= s6+ """category: """ + category +"""\n"""
    s7 = s7 + """importance: """ + year +"""\n"""
    s7 = s7 + """social: true""" + """\n"""
    s8 = s7 +  """---""" +"""\n"""
    s9 = s8+"""<div class="publications">\n   {% bibliography -f papers -q @*[key="""+reference
    s11 = s9+"""] %}\n</div>\n\n\n<i class="fa fa-sticky-note" aria-hidden="true"></i> Abstract\n<p>  <div style="font-size:0.85em; text-align: justify;">"""+abstract+"""\n"""
    s12 = s11+"""</div> </p>\n<div class="cv">\n   <div class="card mt-3 p-3">\n      <h3 class="card-title font-weight-light " style='color:purple'>Full citation</h3>\n      <h6 >  For attribution in academic contexts, please cite this work as: </h6>      \n      <div>\n         <table class="table table-sm table-borderless">\n            <tr>\n               <td class="p-0 pr-2 font-weight-light text-justify font-italic"><span style="color:purple">{% reference """
    s12 = s12+reference+"""%}</span></td>"""
    s13 = s12+"""\n              </tr>\n         </table>\n      </div>\n   </div>\n</div>\n\n<br>\n\n---\n<br>\n<div class="row">\n   <div class="col-sm mt-3 mt-md-0">\n      {% include figure.html path="assets/img/papers/cover/"""
    s13=s13+imgcover
    s14 = s13+ """\" title=\"""" + title_image
    s15 = s14+ """\" class="img-fluid rounded z-depth-1" %}\n   </div>\n</div>\n<div class="caption">\n   <div style="text-align: justify"> {% reference """
    s15 = s15+reference
    s16 = s15+""" %}\n   </div>\n</div>\n"""

    f_name = reference+'.md'
    with open('/home/claudio/Downloads/parser/'+f_name, 'w') as f:
        _= f.write(s16)
        f.close()





s1 = s2 = s3 = s4 = s5 = s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=""
title = "\""+ bib_database.entries[idx]['title']+"\""
description = bib_database.entries[idx]['journal']
short_title = bib_database.entries[idx]['ID']
imgcover_small = bib_database.entries[idx]['ID']+'.jpg'
if "category" in bib_database.entries[idx].keys():
    category = bib_database.entries[idx]['category']
else:
    category = "Various"
year = bib_database.entries[idx]['year']+"""-03-15 16:40:16"""
reference = bib_database.entries[idx]['ID']
abstract = "\""+bib_database.entries[idx]['abstract']+"\""
imgcover = bib_database.entries[idx]['ID']+'.png'
title_image = imgcover
importance = year
s1 = """---\nlayout: papersgallerypage\ntitle: """  
s1 = s1 + title +"""\n"""
s2 = s1+"""shorttitle: """+short_title+"""\n"""
s3 = s2+"""date: """ + year  +"""\n"""
s4 = s3+"""description: """ + description+"""\n"""
s5 = s4+"""img: /assets/img/papers/extract/""" + imgcover_small+"""\n"""
s6= s5+"""tags: formatting links"""+"""\n"""
s7= s6+ """category: """ + category +"""\n"""
s7 = s7 + """importance: """ + year +"""\n"""
s7 = s7 + """social: true""" + """\n"""
s8 = s7 +  """---""" +"""\n"""
s9 = s8+"""<div class="publications">\n   {% bibliography -f papers -q @*[key="""+reference
s11 = s9+"""] %}\n</div>\n\n\n<i class="fa fa-sticky-note" aria-hidden="true"></i> Abstract\n<p>  <div style="font-size:0.85em; text-align: justify;">"""+abstract+"""\n"""
s12 = s11+"""</div> </p>\n<div class="cv">\n   <div class="card mt-3 p-3">\n      <h3 class="card-title font-weight-light " style='color:purple'>Full citation</h3>\n      <h6 >  For attribution in academic contexts, please cite this work as: </h6>      \n      <div>\n         <table class="table table-sm table-borderless">\n            <tr>\n               <td class="p-0 pr-2 font-weight-light text-justify font-italic"><span style="color:purple">{% reference """
s12 = s12+reference+"""%}</span></td>"""
s13 = s12+"""\n              </tr>\n         </table>\n      </div>\n   </div>\n</div>\n\n<br>\n\n---\n<br>\n<div class="row">\n   <div class="col-sm mt-3 mt-md-0">\n      {% include figure.html path="assets/img/papers/cover/"""
s13=s13+imgcover
s14 = s13+ """\" title=\"""" + title_image
s15 = s14+ """\" class="img-fluid rounded z-depth-1" %}\n   </div>\n</div>\n<div class="caption">\n   <div style="text-align: justify"> {% reference """
s15 = s15+reference
s16 = s15+""" %}\n   </div>\n</div>\n"""

f_name = reference+'.md'
with open('/home/claudio/Downloads/parser/'+f_name, 'w') as f:
    _= f.write(s16)
    f.close()