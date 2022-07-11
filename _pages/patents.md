---
layout: page
permalink: /patents/
title: Patents
description: List of patents.


years: [ 2017]

nav: false
---

## Notes

This is a  complete list of my patents.   
Total number of patents <i class="fas fa-file-signature" aria-hidden="true"></i>: [{% bibliography_count -f patents %}]

These electronic articles are posted for individual, non-commercial use to ensure timely dissemination of scholarly work. They are intended for teaching and training purposes only. Articles may not be reposted or disseminated without permission by the copyright holder. Copyright holders retain all rights as indicated within each article.

<!-- [[Books](#books)] | [[Conference papers](#conference-papers)] | [[Journal papers](#journal-papers)] -->

> ### Patents
  

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f patents -q @*[year={{y}}]* %}
{% endfor %}

</div>
