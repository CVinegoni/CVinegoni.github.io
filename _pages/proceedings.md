---
layout: page
permalink: /proceedings/
title: Proceedings and Conferences
description: List of conferences and proceedings in reversed chronological order. 


yearsconf: [  2019, 2017, 2016, 2015, 2014, 2013, 2011,  2007, 2006, 2004, 2003, 2001, 2000, 1999, 1998, 1997 ]
yearsproc: [ 2020, 2011, 2010, 2009, 2008, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1998 ]

nav: false
---

## Notes

This is a  complete list of my conferences and proceedings through {{ site.time | date: '%Y' }}.   
Total number of conferences and proceedings <i class="fas fa-globe-americas" aria-hidden="true"></i>: [{% bibliography_count -f conferences %}, {% bibliography_count -f proceedings %}]


These electronic articles are posted for individual, non-commercial use to ensure timely dissemination of scholarly work. They are intended for teaching and training purposes only. Articles may not be reposted or disseminated without permission by the copyright holder. Copyright holders retain all rights as indicated within each article.

[[Proceedings papers](#proceedings-papers)] | [[Conferences](#conferences)]

---

> #### Proceedings papers

<div class="publications">

{% for y in page.yearsproc %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f proceedings -q @*[year={{y}}]* %}
{% endfor %}

</div>

---

> #### Conferences 

<div class="publications">

{% for y in page.yearsconf %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f conferences -q @*[year={{y}}]* %}
{% endfor %}

</div>

