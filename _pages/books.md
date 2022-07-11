---
layout: page
permalink: /books/
title: Books
description: List of books (contributed chapter). 

years: [ 2015, 2013,2001]

nav: false
---

## Notes

This is a  complete list of contributed books' chapters through {{ site.time | date: '%Y' }}.  
Total number of chapters <i class="fas fa-book" aria-hidden="true"></i>: [{% bibliography_count -f books %}]

> ### Books

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f books -q @*[year={{y}}]* %}
{% endfor %}

</div>

