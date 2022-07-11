---
layout: page
title: Code&Data
permalink: /projectscards/
description: A select collection of research code and open datasets.
order: 5
nav: true
display_categories: [research code, open datasets]
horizontal: false
---

<div style="float: left; width: 70%;">
Code from different projects is available at <a href="https://github.com/cvinegoni" title="GitHub">GitHub repositories <i class="fab fa-github gh-icon"></i></a>. 
</div>
<br>
[[Research code](#research code)] | [[Open datasets](#open datasets)]

---
<br>
<br><br>
<!-- pages/projectscards.md -->
<div class="projectscards">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projectscards -->
  {%- for category in page.display_categories %}
<!-- <h2 class="category">{{ category }}<a href='/projectscards#{{ category }}'><i class="anchor"></i></a></h2> -->

<!-- <h2 id='{{ category }}'>{{ category }}<a href="/projectscards#{{category}}"><i class="anchor"></i></a>
</h2> -->
<!-- <h1>{{ category }}</h1><a href='/projectscards#{{ category }}'><div class="anchor"></div></a> -->

<!-- <h1 id="{{ category }}">{{ category }}<a href='/projectscards#{{ category }}'><div class="anchor"></div></a></h1> -->

<!-- <h2 id="{{category}}">{{ category }}<a class="anchor" href="#{{category}}"> </a></h2> -->

<h2 class="category" id="{{category}}">{{ category }}<a class="anchor" href='#{{ category }}'></a></h2>


  {%- assign categorized_projectscards = site.projectscards | where: "category", category -%}
  {%- assign sorted_projectscards = categorized_projectscards | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projectscards -%}
      {% include projectscards_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projectscards -%}
      {% include projectscards.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projectscards without categories -->
  {%- assign sorted_projectscards = site.projectscards | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projectscards -%}
      {% include projectscards_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projectscards -%}
      {% include projectscards.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}

</div>
