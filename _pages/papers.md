---
layout: page
permalink: /papers/
title: Journal Articles
description: List of publications in reversed chronological order. 
start_year: 2013


years: [ 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997 ]

nav: false
---



## Notes




For a complete list of my publications through {{ site.time | date: '%Y' }} see [below](#published).  
An up-to-date list is also available on:
[Google Scholar](https://scholar.google.com/citations?user={{site.scholar_userid}}), 
[Semantic Scholar](https://www.semanticscholar.org/author/{{site.semantic_scholar_id}}), 
[Scopus profile](https://www.scopus.com/authid/detail.uri?authorId={{site.scopus_authorid}}), 
[ResearcherID](https://www.researcherid.com/rid/{{site.researcher_id}}), 
[Orcid](https://orcid.org/{{site.orcid_id}}),
[Publons](https://publons.com/a/{{site.publons_id}}),
[PubMed](https://pubmed.ncbi.nlm.nih.gov/?term={{site.pubmed_authorid}}%5BAuthor%5D&sort=), and
[ResearchGate](https://www.researchgate.net/profile/{{site.research_gate_profile}})
(
{% if site.scholar_userid %}<a href="https://scholar.google.com/citations?user={{site.scholar_userid}}" target="_blank" title="Google Scholar"><i class="ai ai-google-scholar" aria-hidden="true"></i></a>{% endif %}
{% if site.semantic_scholar_id %} <a href="https://www.semanticscholar.org/author/{{site.semantic_scholar_id}}" target="_blank" title="Semantic Scholar"><i class="ai ai-semantic-scholar" aria-hidden="true"></i></a>{% endif %}
{% if site.scopus_authorid %}<a href="https://www.scopus.com/authid/detail.uri?authorId={{ site.scopus_authorid }}" target="_blank" title="Scopus"><i class="ai ai-scopus" aria-hidden="true"></i></a>{% endif %}
{% if site.researcher_id %}<a href="https://www.researcherid.com/rid/{{site.researcher_id}}" target="_blank" title="ResearcherID"><i class="ai ai-researcherid" aria-hidden="true"></i></a>{% endif %}
{% if site.orcid_id %}<a href="https://orcid.org/{{ site.orcid_id }}" target="_blank" title="ORCID"><i class="ai ai-orcid" aria-hidden="true"></i></a>{% endif %}
{%- if site.publons_id %}<a href="https://publons.com/a/{{ site.publons_id }}/" title="Publons"><i class="ai ai-publons" aria-hidden="true"></i></a>{% endif %}
{% if site.pubmed_authorid %}<a href="https://pubmed.ncbi.nlm.nih.gov/?term={{ site.pubmed_authorid }}%5BAuthor%5D&sort=" target="_blank" title="PubMed"><i class="ai ai-pubmed" aria-hidden="true"></i></a>{% endif %}
{%- if site.research_gate_profile -%} <a href="https://www.researchgate.net/profile/{{site.research_gate_profile}}/" title="ResearchGate"><i class="ai ai-researchgate" aria-hidden="true"></i></a>{% endif %}
)




Total number of journal publications <i class="fas fa-file-invoice" aria-hidden="true"></i>: [{% bibliography_count -f papers %}]


These electronic articles are posted for individual, non-commercial use to ensure timely dissemination of scholarly work. They are intended for teaching and training purposes only. Articles may not be reposted or disseminated without permission by the copyright holder. Copyright holders retain all rights as indicated within each article.



`†`: denotes equal contribution  
`#`: corresponding author.  

<!-- [[Books](#books)] | [[Conference papers](#conference-papers)] | [[Journal papers](#journal-papers)] -->

> ### Published
  

<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
<script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>



<div class="publications">


{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  <br><br>

  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}
</div>


