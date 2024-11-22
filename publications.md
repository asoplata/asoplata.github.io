---
layout: page
title: Publications
description: "List of all publications"
---

### Table of Contents:
- [Papers](#papers)
- [Posters](#posters)
- [Talks](#talks)
- [Resources](#resources)
- [Software](#software)

### Papers

- [Soplata, Austin E., Michelle M. McCarthy, Elie M. Adam, Patrick L. Purdon,
Emery N. Brown, and Nancy Kopell. Neuromodulation Due to Propofol Affects
Anesthetic Oscillatory Coupling. bioRxiv, February
20, 2022. https://doi.org/10.1101/2022.02.17.480766](https://doi.org/10.1101/2022.02.17.480766)
    - [Local PDF download here.](/publications/papers/Soplata-2022-neuromodulation.pdf)
    - Code: The reproducible code for this paper's simulations are available
      [in this GitHub
      repo.](https://github.com/asoplata/soplata-2022-thalcort-code)
    - Code: If you only want the model equation code, that is available [in this GitHub repo.](https://github.com/asoplata/dynasim-extended-benita-model)
      
- [Sherfey JS, Soplata AE, Ardid S, Roberts EA, Stanley DA, Pittman-Polletta BR, et al. DynaSim: A MATLAB Toolbox for Neural Modeling and Simulation. Front Neuroinform. 2018;12. doi:10.3389/fninf.2018.00010
](https://www.frontiersin.org/articles/10.3389/fninf.2018.00010/full)
    - [Local PDF download here.](/publications/papers/Sherfey-2018-DynaSim.pdf)
    - Code: The reproducible code for this paper's DynaSim and Brian2 benchmarks
      is available [here in this
      repo.](https://github.com/asoplata/dynasim-benchmark-brette-2007)

- [Soplata AE, McCarthy MM, Sherfey J, Lee S, Purdon PL, Brown EN, et al.
  Thalamocortical control of propofol phase-amplitude coupling. PLOS
  Computational Biology. 2017;13: e1005879.
  doi:10.1371/journal.pcbi.1005879](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005879)
    - [Local PDF download
      here.](/publications/papers/Soplata-2017-thalamocortical-control.pdf)
    - Code: The reproducible code for this paper is available both [here as a
      standalone
      repo](https://github.com/asoplata/propofol-coupling-2017-full) or
      [here in "plugin" form](https://github.com/asoplata/propofol-coupling-2017-mechanisms) for use with [DynaSim, available here.](https://github.com/dynasim/dynasim/)

### Posters
- SFN 2019: [A. SOPLATA; M. MCCARTHY; E. ROBERTS; E. BROWN; P. PURDON; N. KOPELL. Cortical UP DOWN state synchrony drives propofol phase amplitude coupling in slow waves. Program No. 289.18. Neuroscience 2019 Abstracts. Chicago, IL: Society for Neuroscience, 2019. Online.](/publications/posters/ASoplata-SFN2019-poster.pdf)

- SFN 2016: [A. SOPLATA; J. SHERFEY; E. BROWN; P. PURDON; N. KOPELL.
  Thalamic generation of propofol phase amplitude coupling. Program No.
  507.13. Neuroscience 2016 Abstracts. San Diego, CA: Society for
  Neuroscience, 2016.
  Online.](/publications/posters/ASoplata-SFN2016-poster.pdf)
    - To see the actual source code for this poster, [go to the GitHub
      repo
      here.](https://github.com/asoplata/asoplata.github.io/tree/master/publications/posters)

### Talks
To see the actual source code for these talks, [go to the GitHub repo
here.](https://github.com/asoplata/asoplata.github.io/tree/master/publications/talks/)
- [2021-03-10 "Dynamics of propofol anesthesia in the thalamocortical loop"
  Thalamus Trainees Meeting Group](/publications/talks/20210310-thalamus-trainees.pdf)
- [2018-04-23 Monday, "Thalamic Control of Propofol Phase-amplitude Coupling"
  Cognitive Rhythms Collaborative Retreat, MIT
  ](/publications/talks/20180423-crc-retreat/20180423-crc-retreat.html)
- [2017-11-17 Friday, Git Introduction for BU CNSO, Boston University,
  ](/publications/talks/20171117-git-intro/slides.html) going over both the basics of
  Git and how to contribute for the Computational Neuroscience Students Organization
- [2016-10-13 Thursday, NaK Group talk, Boston University,
  ](/publications/talks/20161013-nak-talk/slides.html) reviewing this paper:
>   Niethard, N., Hasegawa, M., Itokazu, T., Oyanedel, C. N., Born, J., & Sato,
>   T. R. (2016). Sleep-Stage-Specific Regulation of Cortical Excitation and
>   Inhibition. Current Biology.
>   [https://doi.org/10.1016/j.cub.2016.08.035](https://doi.org/10.1016/j.cub.2016.08.035)


### Resources
- I maintain collaborative, public lists of:
    - [Open Computational Neuroscience
      Resources](https://github.com/asoplata/open-computational-neuroscience-resources)
    - [Open Science
      Resources](https://github.com/asoplata/open-science-resources)

### Software
- I try to make all the code/data for my publications as reproducible as
  possible. For code specific to each paper, see above.
- I've contributed to [DynaSim, a very powerful ODE solver
  system written in MATLAB](https://github.com/dynasim/dynasim/) with built-in
  parallelization, cluster support, grid-search parameter sweeping, and plug-and-play
  mechanism functionality. The primary author is [Dr. Jason
  Sherfey](https://github.com/jsherfey), and other contributors include Drs. [Erik
  Roberts](https://github.com/erik-roberts), [Dave
  Stanley](https://github.com/davestanley), [Salva
  Ardid](https://github.com/kupiqu), and [Ben
  Polletta](https://github.com/benpolletta).
- [Here is a working DynaSim
  implementation](https://github.com/asoplata/dynasim-extended-benita-model)
  for a connected combination of the cortical model of the first paper and thalamic
  model of the second paper here:
> Benita, Jose M., Antoni Guillamon, Gustavo Deco, and Maria V. Sanchez-Vives.
> “Synaptic Depression and Slow Oscillatory Activity in a Biophysical Network
> Model of the Cerebral Cortex.” Frontiers in Computational Neuroscience 6
> (2012). [https://doi.org/10.3389/fncom.2012.00064](https://doi.org/10.3389/fncom.2012.00064)
> 
> Destexhe, Alain, Thierry Bal, David A. McCormick, and Terrence J. Sejnowski.
> “Ionic Mechanisms Underlying Synchronized Oscillations and Propagating Waves
> in a Model of Ferret Thalamic Slices.” Journal of Neurophysiology 76, no. 3
> (1996): 2049–70. [https://doi.org/10.1152/jn.1996.76.3.2049](https://doi.org/10.1152/jn.1996.76.3.2049)
- [Here is a working DynaSim
  implementation](https://github.com/asoplata/dynasim-krishnan-2016-model) for
  the thalamocortical model of the following paper:
> Krishnan GP, Chauvette S, Shamie I, Soltani S, Timofeev I, Cash SS, et al.
> Cellular and neurochemical basis of sleep stages in the thalamocortical
> network. eLife. 2016;5: e18607.
> [https://doi.org/10.7554/eLife.18607](https://doi.org/10.7554/eLife.18607)
- [ya-pandoc-template](https://github.com/asoplata/ya-pandoc-template), a simple
  system (wrapper) combining a Makefile with Pandoc templates that lets you
  effortlessly turn Markdown content into HTML presentations, LaTeX documents,
  etc. using personally-stylized templates.
- [poorquery](https://github.com/asoplata/poorquery), a program for quickly
  visualizing a large number of PNG picture files. This finds all PNG files
  with filenames that match a sed regular expression and then builds a single HTML file
  with references to the PNGs, allowing for quick, controllable, and "sliceable" viewing of very many PNGs in
  your browser.
- [evernote-to-markdown](https://github.com/asoplata/evernote-to-markdown), a
  very preliminary, possibly out of date program to convert Evernote XML files
  into Markdown files. In the future I'll probably make something like this
  for Evernote -> Emacs' Org mode.
- [A collection of simple bash scripts](https://github.com/asoplata/bin) I find
  to be particularly helpful when searching across code and
  interacting/synchronizing files between my local computer and a cluster.
