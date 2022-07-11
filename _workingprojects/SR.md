---
layout: page
title: Superresolution Imaging
description: Deep learning based super resolution for optical imaging microscopy.
img: /assets/img/workingprojects/sr.jpg
importance: 1
category: L1
website: https://github.com/cvinegoni
github: https://github.com/cvinegoni
---


<script type="text/javascript">
 function showhide(id) {
    var e = document.getElementById(id);
    e.style.display = (e.style.display == 'block') ? 'none' : 'block';
 }
</script> 
   
> How to better reconstruct image data obtained in fast (video-rate)
acquisition modalities and mitigate the accompanying noise
and distortion effects intrinsically present in the images.

<i class="fa fa-download fa-ld" aria-hidden="true"></i> PDF: <a  href="{{ '/assets/pdf/proceedings/2020-BIBE.pdf' | prepend: site.baseurl | prepend: site.url }}">Video-rate acquisition fluorescence microscopy via generative adversarial networks
</a> _(extended abstract)_

<i class="fa fa-sticky-note" aria-hidden="true"></i> <a href="javascript:showhide('absdl')">_Abstract_</a>
<div id="absdl" style="display:none;">
<p>  <div style="font-size:0.85em; text-align: justify;"> Laser scanning microscopy is a powerful imaging
modality ideal for monitoring spatial and temporal dynamics
in both in vitro and in vivo models. To accurately resolve
dynamic changes, particular to the neuroimaging field, fast
acquisition rates are in great need. Unfortunately, the videorate acquisition required to capture these changes comes with
a trade-off between resolution, high spatial distortion, and low
signal-to-noise ratio due to the electronics and Poisson noise. By
combining microscopy fast acquisition methods with a Generative
Adversarial Network (GAN), we show here, for the first time, that
video-rate image acquisition, up to 20x the speed of equivalent
standard high resolution acquisition, can be obtained without
significant reduction in image quality. Specifically, we present
a GAN based training approach that is able to simultaneously
1) super-resolve, 2) denoise and 3) correct distortion on fast
scanning acquisition microscopy images. In addition, we show
that our method generalizes on unseen data, requires minimal
ground truth images for traini. </div> </p>
</div>

Code: <a class="github-button" href="https://github.com/cvinegoni" data-size="large" aria-label="Follow @cvinegoni on GitHub">Follow @cvinegoni</a> 
