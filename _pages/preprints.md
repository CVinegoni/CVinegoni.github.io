---
layout: page
permalink: /preprints/
title: Preprints
description: List of publications in preprint. 


years: [ 2022, 2021]

nav: false
---

## Notes

This is a  complete list of my papers in preprint or at biorxiv <a href="https://www.biorxiv.org" title="Biorxiv"><i class="ai ai-biorxiv" aria-hidden="true"></i></a> and <a href="https://www.arxiv.org" title="Arxiv"><i class="ai ai-arxiv" aria-hidden="true"></i></a>.   
Total number of papers in preprint <i class="fas fa-print" aria-hidden="true"></i>: [{% bibliography_count -f preprint %}]

These electronic articles are posted for individual, non-commercial use to ensure timely dissemination of scholarly work. They are intended for teaching and training purposes only. Articles may not be reposted or disseminated without permission by the copyright holder. Copyright holders retain all rights as indicated within each article.

<!-- [[Books](#books)] | [[Conference papers](#conference-papers)] | [[Journal papers](#journal-papers)] -->

> ### Preprints
  

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f preprint -q @*[year={{y}}]* %}
{% endfor %}

</div>
