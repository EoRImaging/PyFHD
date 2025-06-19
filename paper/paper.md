---
title: 'PyFHD: Python Fast Holographic Deconvolution, a translation of FHD from IDL to Python'
tags:
  - Python
  - astronomy
  - epoch of reionisation
  - radio astronomy
  - IDL
authors:
  - name: Joel Dunstan
    orcid: 0000-0000-0000-0000
    equal-contrib: true
    affiliation: "1, 2"
  - name: Nichole Barry
    orcid: 0000-0000-0000-0000
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    affiliation: 2
  - name: Jack Line
    orcid: 0000-0000-0000-0000
    equal-contrib: true # (This is how to denote the corresponding author)
    affiliation: 2
affiliations:
 - name: Curtin Institute for Data Science, Curtin University, Australia
   index: 1
   ror: 02n415q13
 - name: Astronomy Data and Computing Services, Curtin University Node, Australia
   index: 2
 - name: University of New South Wales, Australia
   index: 3
   ror: 03r8z3t63
date: 19 June 2025
bibliography: paper.bib

---

# Summary
Python Fast Holographic Deconvolution (PyFHD), is an open source, a python translation of the open source package Fast Holographic Deconvolution (FHD). FHD and therefore, PyFHD has been built for fast mode Epoch of Reionisation (EoR) analysis, serving as a testbed for new ideas, supporting new instruments, supporting both evolutionary and revolutionary cutting edge Epoch of Reionisation, while also giving researchers a package to train the next generation of Epoch of Reionisation astronomers. PyFHD has been primarily tested with analysing Murchison Widefield Array (MWA) observations, reading UVFITS and METAFITS files, importing both FHD [@Sullivan_2012; @Barry_2019] or WODEN [@Line2022] skymodels and importing beams produced by FHD to perform calibration, gridding and HEALPIX file generation required for the error propogated power spectrum with interleaved observed noise ($\epsilon$ppsilon) package [@Barry_2019]. PyFHD also supports beamforming in a similar format to FHD, utilising puvdata [@Hazelton2017; @Keating2025] where possible and translation of FHD where pyuvdata couldn't achieve the same result, though this part of the package is in alpha, and has problems that need to be solved through additional research and/or translation of the FHD package.


# Statement of need
The most successful open-source Epoch of Reionisation (EoR) pipeline, Fast Holographic Deconvolution (FHD) [@Sullivan_2012; @Barry_2019] was built using the Interactive Data Language (IDL), a proprietary
language which has significant limitations in regards to it's cost, terms of use, and licensing thereby preventing those in the EoR community from using and/or contributing to FHD, while also preventing the EoR community from growing. 
The use of IDL for FHD has also made it difficult to utilise FHD results in other packages and in other languages as the resulting save files that IDL produces can be difficult to read, while also being very slow to read into languages like Python when utilising using SciPy's `readsav` function [@2020SciPy-NMeth]. To remove the limitations of IDL, attaining better integration with other packages, and to best support the training of a new generation of EoR astronomers, FHD has been translated to Python, 


# Testing of the Translation



# Citations

<!-- Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% } -->

# Acknowledgements

We acknowledge contributions the from Bryna Hazelton, who provided code examples from pyuvdata [@Hazelton2017; @Keating2025] of which a part of it has made it into the alpha state of the beam forming part of the PyFHD package.
We also acknowledge Paul Hancock, who has provided advice and knowledge throughout the project as a member of the Astronomy Data and Computing Services, Curtin University Node.

# References