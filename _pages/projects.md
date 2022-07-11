---
layout: page
title: Projects
permalink: /projects/
description: Research areas and selected projects. 


order: 1
nav: true
display_categories: [ optical imaging, ai, biomedical, image processing, cardiovascular, systems biology, fiber optics, solid state physics ]
#horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <h2>{%- for category in page.display_categories %}
  {%- assign category_link = category | remove: " " -%}
  <a href='#{{ category_link }}'>{{ category }} - </a>
  {%- endfor %}</h2>
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  {%- assign category_link = category | remove: " " -%}
  <h2 class="category" id={{category_link}}>{{ category }}<a class="anchor" href='#{{ category_link }}'></a></h2>
<!-- >  <h2 class="category" id={{category}}>{{ category }}<a class="anchor" href='#{{ category }}{{ tag | url_encode }}'></a></h2> -->
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
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
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
