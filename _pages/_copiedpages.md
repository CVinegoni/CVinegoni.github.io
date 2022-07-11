---
layout: page
title: copiedpages
permalink: /copiedpages/
description: 
nav: true
display_categories:
horizontal: false
---
<div class="copiedpages">
<p align="justify">The degree to which species diversify taxonomically and functionally varies dramatically across time, space, and the tree of life.
    This ultimately has resulted in the vast diversity and disparity that we see on Earth today. Numerous physiological, ecological, and environmental conditions have been implicated as the causes for this variation.
    I integrate tools and theory from paleontology, geology, ecology, and physiology to study how these components collectively drive and constrain diversity and disparity across time, space, and life.
    Beyond understanding how and why life diversified the way it did in the past, my research provides insights into how modern anthropogenic environmental shifts may ultimately influence the ecology and evolution of today’s biosphere.
</p>

<p><i>Click any of the tiles below to learn more about my various research projects:</i></p>

<center>
{% assign copiedpages = site.copiedpages | sort: 'importance' %}
{% for copiedpages in copiedpages %}

{% unless copiedpages.hidden %}

{% if copiedpages.redirect %}
<div class="copiedpages">
    <div class="thumbnail">
        <a href="{{ copiedpages.redirect }}" target="_blank">
        {% if copiedpages.img %}
        <img class="thumbnail" src="{{ copiedpages.img | prepend: site.baseurl | prepend: site.url }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <div>
            <span>
                <h1>{{ copiedpages.title }}</h1>
                {% if copiedpages.description %}
                <br/>
                <p>{{ copiedpages.description }}</p>
                {% endif %}
            </span>
        </div>
        </a>
    </div>
</div>
{% else %}

<div class="copiedpages ">
    <div class="thumbnail">
        <a href="{{ copiedpages.url | prepend: site.baseurl | prepend: site.url }}">
        {% if copiedpages.img %}
        <img class="thumbnail" src="{{ copiedpages.img | prepend: site.baseurl | prepend: site.url }}"/>
        {% else %}
        <div class="thumbnail blankbox"></div>
        {% endif %}    
        <div>
            <span>
                <h1>{{ copiedpages.title }}</h1>
                {% if copiedpages.description %}
                <br/>
                <p>{{ copiedpages.description }}</p>
                {% endif %}
            </span>
        </div>
        </a>
    </div>
</div>

{% endif %}

{% endunless %}

{% endfor %}
</center>
</div>