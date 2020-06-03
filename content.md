<!-- .slide: class="slide-title" data-background-image="img/title-slide-background.jpg" data-background-opacity="0.25" data-background-color="#000000" -->

<div class="centered">
<div>

# Geophysical research powered by open-source

## [Leonardo Uieda](https://www.leouieda.com)

[leouieda.com](https://www.leouieda.com)
<span style="margin: 0 20px"></span>
[<i class="fab fa-twitter fa-small"></i> @leouieda](https://twitter.com/leouieda)

Institute of Geophysics and Geoinformatics, Technische Universität Bergakademie Freiberg

4 June 2020

<div class="container">
<div class="col-left">

[<img src="img/compgeolab.svg" style="width: 40%">](https://www.compgeolab.org)

</div>
<div class="col-right">

[<img src="img/university-of-liverpool-white.png" style="width: 40%">](https://www.liverpool.ac.uk/earth-ocean-and-ecological-sciences/)

</div>
</div>

<div class="title-license">

[<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i> CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
<span style="margin: 0 20px">|</span>
<i class="fa fa-camera"></i> Feel free to share/photograph this presentation

</div>

</div>
</div>

---

<div class="centered">
<div class="huge">

1. Why software **best practices** are important
2. How investing in software can benefit **science**
3. What **you** can do about it today

</div>
</div>

---

<!-- .slide: class="slide-transition" data-background-color="rgb(25, 34, 55)" -->

<div class="centered">
<div>

# My Background

*A tale of three projects*

</div>
</div>

---

<!-- .slide: data-background-video="video/brasil-sao-paulo-rio.mp4" data-background-size="cover" -->

<div class="r-stretch bottom-left">

BSc in Geophysics from Universidade de São Paulo |
MSc + PhD in Geophysics from Observatório Nacional in Rio

</div>

---

<!-- .slide: data-background-image="img/first-contact-with-c.jpg" data-background-size="cover" -->

<div class="r-stretch bottom-right">

16 years later and the code actually compiled on my first try!

</div>

---

<!-- .slide: data-background-image="img/paleomagnetism-field-work.jpg" data-background-size="cover" -->

<div class="r-stretch bottom-left">

Brief stint as a paleomagnetist getting stung by hornets.
Don't judge the hair, I was 19.

</div>

---

<div class="centered">
<div>

## Project #1

<img src="img/tesseroids.svg" style="width: 80%; margin: 0 0 5% 0;">

*C command-line programs for gravity modelling*

[`tesseroids.leouieda.com`](https://tesseroids.leouieda.com)

</div>
</div>

---

<div class="container">
<div class="col-left">


## Support for future GOCE data

<br>

Collaboration between
<br>
Naomi Ussami (USP),
<br>
Carla Braitenberg (Trieste),
<br>
and  Valéria Barbosa (ON).

</div>
<div class="col-right">

<img src="img/tesseroid-modelling.svg">

</div>
</div>

<div class="bottom-left">

Uieda, Barbosa, Braitenberg (2016) |
doi:[10.1190/geo2015-0204.1](https://doi.org/10.1190/geo2015-0204.1)

</div>

---

<div class="centered">
<div>

## Project #2

<img src="img/fatiando.svg" style="width: 80%; margin: 0 0 3% 0;">

*Libraries for modelling, inversion, data processing, etc.*

[`www.fatiando.org`](https://www.fatiando.org)

</div>
</div>

---

<!-- .slide: data-background-image="img/fatiando-first-gallery.jpg" data-background-size="cover" -->

<div class="r-stretch bottom-right bottom-dark">

Started in 2010 as a mixed bag of geophysics in Python.
<br>
First website and example gallery from 2011. (Google+ &#x1f602;)

</div>

---

<!-- .slide: data-background-video="video/seismic-waves-demo.mp4" data-background-size="cover" -->

<div class="r-stretch bottom-right bottom-dark">

Used extensively in **teaching** at [UERJ](https://www.uerj.br/) and
**research** at the [PINGA Lab](https://www.pinga-lab.org/)

</div>

---

<!-- .slide: data-background-image="img/fatiando-tools.svg" data-background-size="cover" -->

<div class="r-stretch bottom-right">

In 2018 started a complete rewrite of Fatiando a Terra,
<br>
breaking into separate tools.

</div>

---

<div class="container">
<div class="col-left">

<img src="img/santisoler.jpg" style="margin-top: 5%; border-radius: 50%; width: 70%;">
<p style="text-align: center;">
<a href="https://santisoler.github.io/">Santiago Soler<br>@santisoler</a>
</p>

</div>
<div class="col-right">

## Breath of fresh air

* PhD student from Argentina
* Collaborating since 2015
* Inspired writing down my process
* Leading some of our new packages (Harmonica and RockHound)
* Main force behind many new developments

</div>
</div>

---

<!-- .slide: data-background-video="video/run-away-to-hawaii.mp4" data-background-size="cover" -->

<div class="r-stretch bottom-left">

Postdoct at University of Hawai'i working on the Generic Mapping Tools (GMT)

</div>

---

<div class="centered">
<div>

## Project #3

<img src="img/gmt.png" style="width: 50%; margin: 0 0 3% 0;">

*Command-line tool for mapping/processing geophysical data*

[`www.generic-mapping-tools.org`](https://www.generic-mapping-tools.org)

</div>
</div>

---

## PyGMT: Bringing GMT to Python

<div class="container">
<div class="col-large">

```python
import pygmt

# Load built-in topography data
grid = pygmt.datasets.load_earth_relief()

fig = pygmt.Figure()
# Pseudo-color map of topography
fig.basemap(
    region=[-150, -30, -60, 60],
    projection="I-90/6i",
    frame=True,
)
fig.grdimage(grid=grid, cmap="viridis")
# Mask continents in dark grey
fig.coast(land="#333333")
# Display in Jupyter or pop-up window
fig.show()
```

</div>
<div class="col-small">

<img src="img/pygmt-example.png" style="width: 100%;">

<div class="r-stretch bottom-center">

My [initial role in Hawai'i](https://www.leouieda.com/blog/hawaii-gmt-postdoc.html)
was creating [PyGMT](https://www.pygmt.org/).

</div>

</div>
</div>

---

<div class="container">
<div class="col-large">

<img src="img/pygmt-release.jpg" style="width: 95%">

<div class="r-stretch bottom-left">

The [first official release of PyGMT](https://www.pygmt.org/latest/changes.html#release-v0-1-0-2020-05-03)
was managed by Wei Ji and Dongdong.

</div>

</div>
<div class="col-small">

### A community developed project

Contributors to v0.1.0:

<div class="container" style="margin-top: 5%">
<div class="col-left tiny">

* Dongdong Tian
* Wei Ji Leong
* Leonardo Uieda
* Liam Toney
* Brook Tozer

</div>
<div class="col-right tiny">

* Claudio Satriano
* Cody Woodson
* Mark Wieczorek
* Philipp Loose
* Kathryn Materna

</div>
</div>

</div>
</div>

---

<!-- .slide: data-background-image="img/gmt-summit-2019-names.jpg" data-background-size="cover" data-background-position="top" -->

<div class="r-stretch bottom-left">

GMT started in the 80s by Paul Wessel and Walter Smith.
Photo from the 2019 GMT Summit at Scripps.

</div>

---

<!-- .slide: data-background-image="img/hawaii-sunset.jpg" data-background-opacity="0.25" data-background-color="#000000" -->

### How Paul can retire in peace &#x1F3DD;

<ul class="fa-ul">
<li>
  <i class="fa-li fab fa-github fa-fw"></i>
  Lower barriers to contribution
</li>
<li>
  <i class="fa-li fas fa-robot fa-fw"></i>
  Automate as much as possible
</li>
<li>
  <i class="fa-li fa fa-users fa-fw"></i>
  Nurture a community of users/developers
</li>
<li>
  <i class="fa-li fas fa-university fa-fw"></i>
  Formalize project governance
</li>
<li>
  <i class="fa-li fas fa-code fa-fw"></i>
  General house cleaning of the code
</li>
<li class="fragment">
  <i class="fa-li fa fa-dollar-sign fa-fw"></i>
  new NSF grant to fund this
  &#x1F389;
  (ID: <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1948602">1948602</a>)
<div class="bottom-left bottom-dark" style="margin-top: 3%;">

Proposal is public at
[doi.org/10.6084/m9.figshare.12235727](https://doi.org/10.6084/m9.figshare.12235727)

</div>
</li>
</ul>

---

<!-- .slide: data-background-video="video/hawaii-to-liverpool.mp4" data-background-size="cover" -->

<div class="r-stretch bottom-left">

Lecturer of Geophysics at the University of Liverpool from 2019

</div>

---

<!-- .slide: data-background-image="img/title-slide-background.jpg" data-background-opacity="0.35" data-background-color="#000000" -->

<div class="centered">
<div>

<a href="https://www.compgeolab.org">
<img src="img/compgeolab.svg" style="width: 50%; margin-bottom: 5%;">
</a>

## Geophysics + Open-source

Building **methods and software** foundations to power

**scalable**
gravity and magnetics **processing and inversion**

</div>
</div>

---

<!-- .slide: data-background-image="img/Wikimedia_Foundation_Servers-8055_35.jpg" data-background-opacity="0.2" data-background-color="#000000" -->

## Code is essential to research

<div class="container">
<div class="col-left">

Data processing, analysis, visualization, inference, etc.

<br>

**Computers are always involved somehow.**

</div>
<div class="col-right">

Machine learning is <br> open-source:

* [scikit-learn](https://scikit-learn.org/)
* [TensorFlow](https://www.tensorflow.org/) (Google)
* [PyTorch](https://pytorch.org/) (Facebook)
* [RAPIDS](https://rapids.ai/) (NVIDIA)

</div>
</div>

<div class="r-stretch bottom-left bottom-dark">

Image by
Victor Grigas
([CC-BY-SA](https://commons.wikimedia.org/wiki/File:Wikimedia_Foundation_Servers-8055_35.jpg))

</div>

---

<!-- .slide: class="slide-transition" data-background-color="rgb(25, 34, 55)" -->

<div class="centered">
<div>

# Why best practices <br> are important

*Horror stories of public embarassment and backlash*

</div>
</div>

---

Something about the spreadsheet bug.

A bit about the recent covid C code.

Your quick hack can end up becoming the foundations of a field.
By the time you realize it it could be too late.

But also positive sides. Good software gets used. Used software generates
citations and collaborations.

---

<!-- .slide: class="slide-transition" data-background-color="rgb(25, 34, 55)" -->

<div class="centered">
<div>

# Good software <br> benefits science

*Success stories of past, present, and future*

</div>
</div>

---

past:

Tesseroids usage for GOCE grids.

Building on top of previous work.
No hunting for bugs in already tested code.
Design for reuse.
Rapid prototyping for Moho inversion (idea to results in couple of days).
Even moderately documented generated use.

Present

Our recent work on building scalable equivalent layers.
What do we need to make this work?
Based on Verde so talk a bit about it.
Software + ML + distributed.
Santi's work on block eql.
Work on cross-validation.

Future

Next steps with Dask and Santi's work on iterative EQL.

---

## Scaling processing to large datasets

EQL is costly.
Figure from Santi's talk.
ML approach.
Working towards automatic pipelines and faster execution.
Santi's work on reducing number of sources.
My work on CV (include animation of Dask running in parallel).
Future plans.
Parallel fitting and prediction.
Reduce memory usage.
CV with data from ground + satellite?
Integrate large collections in the cloud.

---

<!-- .slide: class="slide-transition" data-background-color="rgb(25, 34, 55)" -->

<div class="centered">
<div>

# What you <br> can do now

*(with limited time and money)*

</div>
</div>

---

What PIs, postdocs and students can do to make a difference.

Invest in software from the start.

Encourage training.

Value software work in evaluations.

Software Carpentry and the SSI.

Get involved in existing projects (learn by helping).

---

You can get credit for this work. JOSS.

---

<!-- .slide: class="slide-conclusions" -->

## Main takeaways

<ol>
<li class="fragment">

**Treat code as you would data** <br> *be skeptical, diligent, careful*

</li>
<li class="fragment">

**Learn "good-enough" practices** <br> *to safely handle code*

</li>
<li class="fragment">

**One step at a time** <br> *do what can be done right now*

</li>
<li class="fragment">

**Value good software** <br> *with credit, money, and time*

</li>
</ol>

---

<!-- CONTACT -->
<!-- ====================================================================== -->

<!-- .slide: class="slide-contact" data-background-image="img/liverpool.jpg" data-background-position="top" data-background-opacity="0.25" data-background-color="#000000" -->

<div class="centered">
<div>

# Contact

<ul class="fa-ul" style="">
<li><i class="fa-li fa fa-envelope"></i>

[Leonardo.Uieda@liverpool.ac.uk](mailto:Leonardo.Uieda@liverpool.ac.uk)

</li>
<li><i class="fa-li fab fa-twitter"></i>

[@leouieda](https://twitter.com/leouieda)

</li>
<li><i class="fa-li fa fa-desktop"></i>

[www.leouieda.com](https://www.leouieda.com)

</li>
<li><i class="fa-li fa fa-flask"></i>

[www.compgeolab.org](https://www.compgeolab.org)

</li>
</ul>

</div>
</div>

---

<!-- LICENSE -->
<!-- ====================================================================== -->

<!-- .slide: class="slide-license" -->

<div class="centered">
<div>

<p class="license-icons">
<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i>
</p>

This presentation is licensed under

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

</div>
</div>
