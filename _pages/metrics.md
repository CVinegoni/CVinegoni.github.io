---
layout: page
title: Bibliometrics
permalink: /metrics/
description: Personal bibliometrics and scientific production
news: false
social: true
nav: false
---

[[By Field](#by-field)] | [[By Journal](#by-journal)] | [[By Year](#by-year)] | [[Citations](#citations)] 


<br>  
<div class="cv">
	{% for entry in site.data.metrics %}
		<div class="card mt-3 p-3">
			<h3 class="card-title">{{ entry.title }}</h3>
			<div>
			{% if entry.type == "list" %}
				<ul class="card-text font-weight-light  list-group list-group-flush"> 
				{% for content in entry.contents %}
					<li class="list-group-item">{{ content }}</li>
				{% endfor %}
				</ul>
            {% endif %}
			</div>
		</div>
	{% endfor %}
</div>


<br>

***

<br>

<h3 style="color:purple" class="category" id="by-field">By Field<a class="anchor" href='#by-field'></a></h3>
<p>
<img src="/assets/img/metrics/metrics-fields.jpg" style="width:100%;"/>
    <div class="caption">
    </div>
</p>

<h3 style="color:purple" class="category" id="by-journal">By Journal<a class="anchor" href='#by-journal'></a></h3>
<p>
<img src="/assets/img/metrics/metrics-journals.jpg" style="width:100%;"/>
    <div class="caption">
    </div>
</p>

<h3 style="color:purple" class="category" id="by-year">By Year<a class="anchor" href='#by-year'></a></h3>
<p>
<img src="/assets/img/metrics/metrics-pubsyear.jpg" style="width:100%;"/>
    <div class="caption">
    </div>
</p>


<h3 style="color:purple" class="category" id="citations">Citations<a class="anchor" href='#citations'></a></h3>
<p>
<img src="/assets/img/metrics/metrics-yearcitations.jpg" style="width:100%;"/>
    <div class="caption">
    </div>
</p>