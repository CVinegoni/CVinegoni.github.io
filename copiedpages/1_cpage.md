---
layout: page
title:  title
description: 
img: /assets/img/1998-APL.svg
---
<!-- 
{% reference razansky2009multispectral %}

hh

<div class="publications">
{% reference razansky2009multispectral %}
</div>
-->
<div class="publications">
     {% bibliography -f papers -q @*[key=razansky2009multispectral] %} 
</div>



<i class="fa fa-sticky-note" aria-hidden="true"></i> Abstract
<p>  <div style="font-size:0.85em; text-align: justify;">Background: Combining biomechanical modelling of left ventricular (LV) function and dysfunction with cardiac magnetic resonance (CMR) imaging has the potential to improve the prognosis of patient-specific cardiovascular disease risks. Biomechanical studies of LV function in three dimensions usually rely on a computerized representation of the LV geometry based on finite element discretization, which is essential for numerically simulating in vivo cardiac dynamics. Detailed knowledge of the LV geometry is also relevant for various other clinical applications, such as assessing the LV cavity volume and wall thickness. Accurately and automatically reconstructing personalized LV geometries from conventional CMR images with minimal manual intervention is still a challenging task, which is a pre-requisite for any subsequent automated biomechanical analysis. I this talk I will present a deep learning-based automatic pipeline for predicting the three-dimensional LV geometry directly from routinely-available CMR cine images, without the need to manually annotate the ventricular wall. The framework takes advantage of a low-dimensional representation of the high-dimensional LV geometry based on principal component analysis. I will discuss how the inference of myocardial passive stiffness is affected by using our automatically generated LV geometries instead of manually generated ones. These insights can be used to inform the development of statistical emulators of LV dynamics to avoid computationally expensive biomechanical simulations. The proposed framework enables accurate LV geometry reconstruction, outperforming previous approaches by delivering a reconstruction error 50% lower than reported in the literature. I will further demonstrate that for a nonlinear cardiac mechanics model, using our reconstructed LV geometries instead of manually extracted ones only moderately affects the inference of passive myocardial stiffness described by an anisotropic hyperelastic constitutive law. The developed methodological framework has the potential to make an important step towards personalized medicine by eliminating the need for time consuming and costly manual operations. In addition, the proposed method automatically maps the CMR scan into a low-dimensional representation of the LV geometry, which constitutes an important stepping stone towards the development of an LV geometry-heterogeneous emulator.
</div> </p>
</div>

<div class="cv">
		<div class="card mt-3 p-3">
			<h3 class="card-title font-weight-light ">Full citation</h3>
			<div>
				<table class="table table-sm table-borderless">
						<tr>
							<td class="p-0 pr-2 font-weight-light text-justify font-italic"><span style="color:purple">{% reference razansky2009multispectral %}</span></td>
							<td class="p-0 pl-2 font-weight-light text-left">Claudio</td>
						</tr>
				</table>
            </div>
        </div>
</div>

<br>

---

<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html ref="pdf/papers/1998-APL.pdf" path="assets/img/1998-APL.svg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
<div style="text-align: justify"> {% reference razansky2009multispectral %}
 </div>
</div>
