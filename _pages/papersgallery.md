---
layout: page
title: Gallery
permalink: /papersgallery/
description: A gallery of published papers 
order: 4
nav: true
# display_categories: [a1, a2]
#horizontal: false
---



<!-- pages/papersgallery.md -->
<div class="papersgallery">
{%- if site.enable_papersgallery_categories and page.display_categories %}
  <!-- Display categorized papersgallery -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_papersgallery = site.papersgallery | where: "category", category -%}
  {%- assign sorted_papersgallery = categorized_papersgallery | sort: "importance" | reverse -%} <!-- perhaps put reverse -->
  <!-- Generate cards for each papersgallery -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for papersgallery in sorted_papersgallery -%}
      {% include papersgallery_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for papersgallery in sorted_papersgallery -%}
      {% include papersgallery.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display papersgallery without categories -->
  {%- assign sorted_papersgallery = site.papersgallery | sort: "importance" | reverse -%}
  <!-- Generate cards for each papersgallery -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for papersgallery in sorted_papersgallery -%}
      {% include papersgallery_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for papersgallery in sorted_papersgallery -%}
      {% include papersgallery.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>



