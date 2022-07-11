---
layout: page
permalink: /photos/
title: photos
description: <br>some places I've been, things I've seen. <br>
images:
  - image_path: /assets/img/gallery/1.jpg
    title: Uummannaq, Greenland (circa May 2015)
  - image_path: /assets/img/gallery/2.jpg
    title: Flam, Norway (circa May 2018)
  
nav: false
social: true
---

***

<div class="row justify-content-sm-center">

{% for image in page.images %}

  <div class="col-sm-6 mt-4 mt-md-4">
      <a href="{{ image.image_path }}"><img class="img-fluid rounded z-depth-2" src="{{ image.image_path }}"  alt="{{ image.title }}" title="{{ image.title }}"/></a>
  </div>

{% endfor %}
</div>