---
title: |
    Thalamic Control of Propofol Phase-amplitude Coupling
author: |
    Austin Soplata, Boston University

    Access this presentation live at: [asoplata.com/talk](http://asoplata.com/talk)

layout: null

---

Background / Methods
==============================================================================

## Propofol Alpha and Slow Wave

![From Fig 1 of 
@mukamel_transition_2014](figures/fig01-propofol-basic-phenom.png){ width=100% 
}

## Why do we care?

- Better understanding of propofol mechanisms could lead to more targeted 
  anesthetics

- Clarify mechanistic differences between between anesthesia and sleep, 
  including rhythms

- Propofol coupling correlates with depth of anesthesia, as can be used in the 
  Operating Room
    - Coupling mechanisms may tie to specific aspects of loss of consciousness

## Sleep Spindles vs Propofol Alpha

![From Fig 1 of @astori_manipulating_2013](figures/fig02-spindles.png){ 
width=100% }

## Propofol Mechanisms of Action

1. **Increases** $GABA_A$ **inhibition**:
    - Increases max synaptic conductance (**$\uparrow \bar g_{GABA_A}$**  )
    - Increases decay time constant (**$\uparrow \tau_{GABA_A}$**  )

2. **Decreases thalamocortical (TC) cell H-current conductance ($\downarrow \bar g_H$  )**

3. **Decreases Excitation from brainstem** ($\downarrow I_{applied}$)

## Our Model Thalamus

![From Fig 2 of 
@soplata_thalamocortical_2017](figures/fig03-thalamic-model.png){ width=80% }



Overview
==============================================================================

## Overview

1. **Increase of $GABA_A$ and decrease of TC cell H-current are required for 
   thalamic Alpha oscillations**

2. Thalamic Alpha oscillations are sustained spindles

3. Interaction between thalamic Alpha and Slow Wave Activity can produce 
   propofol phase-amplitude coupling regimes




$GABA_A$ and H-current changes are required for thalamic Alpha oscillations
==============================================================================

## Native hyperpolarized thalamus cannot produce Alpha oscillations

![From Fig 3 of 
@soplata_thalamocortical_2017](figures/fig04-baseline-space.png){ width=75% }

## Simulating $GABA_A$ increase enables thalamic Alpha oscillations

![From Fig 2 of 
@soplata_thalamocortical_2017](figures/fig05-initial-alpha.png){ width=55% }

## Alpha requires H-current decrease

![From Fig 4 of @soplata_thalamocortical_2017](figures/fig06-ncf-planes.png){ 
width=65% }

## Summary So Far

- Sustained Alpha does *not* occur normally

- **$GABA_A$ increase** is a necessary factor for sustained Alpha

- **TC cell H-current decrease** is also a necessary factor for sustained Alpha



## Overview So Far

1. Increase of $GABA_A$ and decrease of TC cell H-current are required for 
thalamic Alpha oscillations

2. **Thalamic Alpha oscillations are sustained spindles**

3. Interaction between thalamic Alpha and Slow Wave Activity can produce 
propofol phase-amplitude coupling regimes

Thalamic Alpha oscillations are sustained spindles
==============================================================================

## Sustained alpha emerges from Baseline spindles

![From Fig 5 of 
@soplata_thalamocortical_2017](figures/fig07-from-spindles.png){ width=90% }

## Summary So Far

- Propofol thalamic alpha takes advantage of thalamic spindle dynamics (e.g. 
  $T_{window}$)

- Enhanced *inhibition* enables *more* spiking/oscillating due to T-current and 
  H-current interplay



## Overview So Far

1. Increase of $GABA_A$ and decrease of TC cell H-current are required for 
thalamic Alpha oscillations

2. Thalamic Alpha oscillations are sustained spindles

3. **Interaction between thalamic Alpha and Slow Wave Activity can produce 
propofol phase-amplitude coupling regimes**

Alpha-SWO Coupling
==============================================================================

## Slow Wave Oscillations

![From Fig 1 of @crunelli_slow_2010](figures/fig08-swo-overview.png){ 
width=100% }

## Phase-amplitude Coupling Switches

![From Fig 1 of 
@mukamel_transition_2014](figures/fig09-coupling-phenom.png){ width=70% 
}

## Our Full Model Network

![From Fig 9 of @soplata_thalamocortical_2017](figures/fig10-full-model.png){ 
width=60% }

## Simulating UP vs DOWN states

![From Fig 7 of @soplata_thalamocortical_2017](figures/fig11-cf-ncf-part1.png){ 
width=70% }

## Simulating UP vs DOWN states

![From Fig 7 of @soplata_thalamocortical_2017](figures/fig12-cf-ncf-part2.png){ 
width=70% }

## Trough-max thalamic alpha

![From Fig 7 of @soplata_thalamocortical_2017](figures/fig13-cf-ncf-part3.png){ 
width=70% }

## Trough-max comparison
![From Fig1 and 7 of @soplata_thalamocortical_2017](figures/fig14-tmax-comparison.png){ 
width=70% }

## Peak-max thalamic alpha

![From Fig1 and 7 of @soplata_thalamocortical_2017](figures/fig15-pmax.png){ width=70% }

## Peak-max comparison

![From Fig1 and 7 of @soplata_thalamocortical_2017](figures/fig16-pmax-comparison.png){ 
width=70% }

## Coupling Summary So Far

- Given SWO UP/DOWN transitions coming from cortex to thalamus,

    1. **"trough-max" Alpha can be generated during DOWNs by the thalamus**

    2. **"peak-max" Alpha can be generated during UPs by the thalamus**

- **Overall thalamic hyperpolarization** is the critical factor for switching
  the thalamus between trough-max and peak-max

Conclusions
==============================================================================

## Conclusions 1

1. Propofol sustained alpha may come from its **$GABA_A$ increase** and 
  **H-current decrease** in the thalamus.

2. This propofol alpha is dependent on the **spindling dynamics** of the 
   thalamus.

## Conclusions 2

3. During **"trough-max"** propofol coupling, the thalamus may cause 
   the sustained Alpha in the DOWN/trough phase. Similarly, in **"peak-max"**
   coupling, the thalamus may cause the sustained Alpha seen during 
   the UP/peak phase.

4. **Increased hyperpolarization** of the thalamus is sufficient to switch 
   from trough-max thalamic firing to peak-max thalamic firing, and vice versa.

## Implications

- Propofol alpha may arise from the thalamus.

- Hyperpolarization level of the thalamus may determine which coupling regime 
  is present (trough-max or peak-max), and may be controlled by specific 
  brainstem nuclei.

- Since propofol alpha is not present during trough-max UP states, there may 
  still be corticothalamic *communication* during trough-max.

## Acknowledgements

- Kopell Lab @ BU: Nancy Kopell, Michelle McCarthy, Jason Sherfey, Erik 
  Roberts, alums Shane Lee, ShiNung Ching, Sujith Vijayan
- CRC community
- BU Graduate Program for Neuroscience, especially Shelley Russek and Sandi 
  Grasso
- Anesthesia research @ MIT: Emery Brown lab, Patrick Purdon lab, Christa van 
  Dort lab, Ken Solt lab
- NIH, NSF, and HHS for funding including training

## Simulation Code

Our lab uses and develops the [DynaSim 
Simulator](https://www.github.com/dynasim/dynasim) originally created by Jason 
Sherfey. All the code necessary to run these simulations [is available on 
GitHub here](https://github.com/asoplata/propofol-coupling-2017-mechanisms)!

![](figures/fig17-dynasim-paper.png){ width=100% }


Appendix
==============================================================================

## Detail: $T_{window}$ is critical

![](figures/fig18-t-window.png){ width=85% }

## Detail: Propofol Alpha mechanism

![](figures/fig19-full-propofol-mechanism.png){ width=75% }

References
==============================================================================

## CSS

<style>
.reveal h1,
.reveal h2,
.reveal h3,
.reveal h4,
.reveal h5,
.reveal h6 {
  text-transform: none;
}

.reveal section img { background:none; border:none; box-shadow:none; }
</style>

## 
