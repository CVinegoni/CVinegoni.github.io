---
layout: page
title: Scientific contributions
permalink: /diffpubs/
description: ""
nav: false
social: true

#horizontal: false
---



Complete list of my publications through {{ site.time | date: '%Y' }}.  
An up-to-date list is also available on:
[Google Scholar](https://scholar.google.com/citations?user={{site.scholar_userid}}), 
[Semantic Scholar](https://www.semanticscholar.org/author/{{site.semantic_scholar_id}}), 
[Scopus profile](https://www.scopus.com/authid/detail.uri?authorId={{site.scopus_authorid}}), 
[ResearcherID](https://www.researcherid.com/rid/{{site.researcher_id}}), 
[Orcid](https://orcid.org/{{site.orcid_id}}),
[Publons](https://publons.com/a/{{site.publons_id}}), or
[PubMed](https://pubmed.ncbi.nlm.nih.gov/?term={{site.pubmed_authorid}}%5BAuthor%5D&sort=), or 
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




Total number of journal publications <i class="fas fa-file-invoice" aria-hidden="true"></i>: [{% bibliography_count -f papers %}] | preprints <i class="fas fa-print" aria-hidden="true"></i>: [{% bibliography_count -f preprint %}] | conferences and proceedings  <i class="fas fa-globe-americas" aria-hidden="true"></i>: [{% bibliography_count -f conferences %}, {% bibliography_count -f proceedings %}] | books <i class="fas fa-book" aria-hidden="true"></i>: [{% bibliography_count -f books %}] | patents <i class="fas fa-file-signature" aria-hidden="true"></i>: [{% bibliography_count -f patents %}] | thesis <i class="fa fa-graduation-cap" aria-hidden="true"></i> : [2]
<br>
<br>

<!-- pages/projects.md -->
<div class="diffpubs">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.diffpubs | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

<br><br>

---