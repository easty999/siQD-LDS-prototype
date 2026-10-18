# what changed in the model

## why the old result needed checking

the supplied methodology and flowchart describe a simulation pipeline, not a fabrication protocol. the notebook contains two substantial code cells and an empty cell. both substantial cells mix `wavelength` and `λ`; neither is independently reproducible in a fresh kernel without repair. saved output text and traceback variable names differ from visible source. cell 0 retains a positive 0.03 mA/cm2 output; cell 2 retains -1.96 mA/cm2. so the saved output alone doesn't tell us which version of the code produced it.

the separately supplied `iris graphs.pdf`, visually inspected, shows negative values throughout graph 3 and graph 4. the line goes up, but it stays below zero. the loss gets smaller; it doesn't turn into a gain. the final paper and right panel instead claim +2.3 to +3.8 mA/cm2. the clean reconstruction reproduces the negative notebook value, not that claim.

the actual workbook headers are wavelength, **etr**, **global tilt**, and **direct+circumsolar**. the notebook's `usecols=[0,1]` selects extraterrestrial irradiance. the corrected reconstruction selects column c, global tilt. it also uses one float wavelength array consistently, normalized emission and the notebook's constants. the parameters weren't adjusted to force a better-looking result.

| run | integrated input W/m2 | baseline jsc | lds jsc | delta jsc |
|---|---:|---:|---:|---:|
| historical spectrum selection, reconstructed | 1347.9343 | 42.6564 | 40.6977 | -1.9588 |
| corrected global tilt | 1000.3707 | 35.4728 | 34.0859 | -1.3868 |

current densities are mA/cm2. qy=0.6, capture=0.7; absorption is a gaussian of amplitude 0.6, center 400 nm, sigma 70 nm. emission is normalized per nm, center 750 nm, sigma 80 nm. eqe is the notebook's assumed piecewise curve, not a measured device response. the extra digits help check the rerun. they don't mean the model is that accurate in real life.

## why it loses current

with emission s normalized so its wavelength integral is one:

`Delta J = 0.1 q N_abs [QY * capture * <EQE>_emission - <EQE>_absorbed]`.

for the corrected input this becomes `Delta J = 2.914668*(QY*capture) - 2.611006` mA/cm2. break-even requires qy*capture > 0.895816 under these assumptions. the chosen product is 0.42. across the paper's qy=0.3–0.8 and capture=0.4–0.9 ranges, the corrected delta ranges from -2.2612 to -0.5124 mA/cm2. that settles the sign: the written gain isn't supported by this model. we still don't know exactly where the old positive saved output came from.

absorbing a photon removes its original chance of generating current. the emitted light has to make up for that, after accounting for light that isn't emitted or doesn't reach the cell. ordinary one-photon lds does not recover thermalization energy as extra electron-hole pairs. its opportunity is poor short-wavelength eqe. a modern high-eqe silicon cell may benefit little or lose power. the broad gaussian model even permits a small unphysical anti-stokes tail; measured excitation/emission and energy-consistent redistribution should replace it before predictive work.

## what to fix before sharing the older work

- replace the positive-gain statement with the reconstructed loss and explicit assumptions. do not call calculated jsc a measured efficiency. pce needs maximum-power and incident-power measurements.
- change the middle-panel claim that lds shifts photons to shorter wavelengths: down-shifting emission has a longer wavelength.
- replace “three trials account for numerical variance.” this deterministic calculation has no independent experimental replication or random uncertainty model. use convergence checks and measured-input uncertainty instead.
- remove “validated by matching a published gain.” the supplied project does not reproduce that paper's measured eqe, reflectance, film or cell, and its spectral input was wrong.
- correct the cdse/cds reference to lopez-delgado et al., scientific reports **7, 14104 (2017)**, doi 10.1038/s41598-017-14269-0. that paper reports 32.5 to 37.0 mA/cm2 and includes antireflection effects; it does not validate this si-qd-only model. the separate si-qd study is doi 10.1007/s00542-017-3405-x, published online 2017, journal volume 2018. do not merge the two.
- avoid blanket “non-toxic,” “long-term stable,” “easy to manufacture,” or novel-first-si-qd claims. surface ligands, solvents, particle exposure and film aging matter. si-qd lds has prior art.
- existing `qd animation.py` uses red for higher frequency and blue for lower frequency. relabel or swap colors before reuse so they do not imply the opposite spectral shift.

## the other files that were checked

read: final paper draft, iris graphs, left/middle/right panel pdfs, local astm workbook and `programs/siQD research/qd animation.py`. relevant assets inventoried but not fully reviewed: `iris_draft_fixed.docx`, presentation decks, `iris poster.png`, `baselineLDsvsPhotonFlux.png`, `jsc-comparison-chart.svg`, panel subfolders, and `iris video draft - Made with Clipchamp.mp4`. the video filename is evidence of an existing draft only; its footage and claims were not verified, so it is not used as proof of a build. `generate_figure5.py` concerns land-cover classes and is unrelated. personal recommendation/travel documents were excluded.

hashes of the principal analyzed files are in `source_manifest.json`. original files were left unchanged. the original files haven't been changed. the old slides and video still need these corrections before reuse.
