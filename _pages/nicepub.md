---
title: "Highlights"
layout: gridlay
description: publications highlights 
permalink: /nicepub/
order: 3
nav: true
horizontal: false
---


# Publications highlights

<br>


## Notes

These electronic articles are posted for individual, non-commercial use to ensure timely dissemination of scholarly work. They are intended for teaching and training purposes only. Articles may not be reposted or disseminated without permission by the copyright holder. Copyright holders retain all rights as indicated within each article.

------

<br>
{% assign number_printed = 0 %}
{% for publi in site.data. publisthighlight %}
{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
    <div class="cardnicepub">
        <h6 class="card-title"   style="font-weight: bold">{{ publi.title }}</h6>
        <img src="{{ site.url }}{{ site.baseurl }}/assets/img/highlights/{{ publi.image }}" class="img-fluid rounded"  style="float: left; padding-right:10px" />                    
        <p>{{ publi.description }}</p>
        <p><em>{{ publi.authors }}</em></p>
        <p><strong><a href="/papersgallery/{{ publi.link.url }}" target="_blank">{{ publi.link.display }}</a></strong></p>
    </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}
{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


