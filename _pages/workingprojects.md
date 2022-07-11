---
layout: page
title: OpenProjects
permalink: /workingprojects/
description: Current running open source projects.
nav: true
order: 8
display_categories: [L1, L2, L3, M1]
---
<div class="workingprojects">
  {% if site.enable_workingprojects_categories and page.display_categories %}
  <!-- Display categorized workingproject -->
    {% for category in page.display_categories %}
      <h2 class="category">{{category}}</h2>
      {% assign categorized_workingproject = site.workingproject | where: "category", category %}
      {% assign sorted_workingproject = categorized_workingproject | sort: "importance" %}
      <!-- Generate cards for each workingproject -->
      
      <div class="grid">
        {% for workingproject in sorted_workingproject %}
          {% include workingprojects.html %}
        {% endfor %}
      </div>
      
    {% endfor %}

  {% else %}
  <!-- Display workingprojects without categories -->
    {% assign sorted_workingproject = site.workingprojects | sort: "importance" %}
    <!-- Generate cards for each workingproject -->
      <div class="grid">
        {% for workingproject in sorted_workingproject %}
          {% include workingprojects.html %}
        {% endfor %}
      </div>
  {% endif %}

</div>