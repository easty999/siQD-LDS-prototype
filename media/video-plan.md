# the video plan

working title: **my solar-cell simulation showed a loss. here's what i'm testing next.**

aim for about 4–6 minutes once there's real build footage. for now, there's enough material for a shorter design update: the model correction, the holder, and the test plan. don't fill the missing experiment section with staged results.

## the order

| section | what to say | what to show |
|---|---|---|
| 0:00–0:20 | the write-up said the current improved, but the graph was negative | the old graph beside the corrected result; hide private paths |
| 0:20–0:55 | the film absorbs shorter-wavelength light and emits longer-wavelength light; it still has to overcome its own losses | `renders/how-the-test-works.png`, labeled as a schematic |
| 0:55–1:35 | the code used the extraterrestrial spectrum; correcting it still gives a loss | a real screen recording of the model, plus `renders/model-result.png` |
| 1:35–2:15 | this holder keeps the slide in place while the cell stays put | `renders/tray-turntable.mp4`, `renders/tray-hero.png`, then `renders/exploded-labeled.png` |
| 2:15–3:10 | explain what was actually made, after it has been made | real clips of sample labels, coating, drying, and anything that went wrong |
| 3:10–4:20 | explain the host–sample–host comparison | real masks, reference cell, temperature reading, and instrument export |
| 4:20–5:00 | show the result and what remains uncertain | all independent samples, error bars, and the next step |

the last three sections are waiting for physical work. the [voiceover draft](voiceover.md) only speaks about what is supported now.

## getting the footage

get one wide shot of the whole setup before closeups. show the sample id so each clip can be matched to a lab record. keep the original files, and log the date, sample, filename, and useful timecodes. film a complete measurement too, even if only a few seconds go into the edit.

keep camera exposure fixed when comparing glowing films. a bright-looking clip isn't a quantum-yield measurement. don't show someone's face, lab paperwork, or private details without permission. use your own audio and cleared music.

the old clipchamp draft was found, but its contents weren't reviewed for this package. check its claims and footage before reusing it. the old animation also has the wavelength colours reversed; shorter wavelengths should not be explained as red and longer wavelengths as blue.

## how to end it

- if it helps: state the light source, setup, sample count, and uncertainty. compare against both plain polymer and the bare cell.
- if it hurts: show the loss. absorption, scattering, and escaped light are things to investigate, not causes to claim without evidence.
- if it's too close to tell: show the uncertainty and explain what needs a better measurement.
- if material or lab access holds it up: end with the corrected simulation and proposed fixture. that's the actual progress so far.

## description draft

“this is my plan for testing a silicon quantum-dot film above a solar cell. the original simulation had a spectrum-selection problem, and the corrected model shows a loss under its current assumptions. i've included the design renders and the planned controls here. the holder hasn't been printed yet, and there's no measured efficiency improvement to report.”

add a github link only after the repo is published. link the source papers too. these are draft words written with ai help; read them aloud and change anything you wouldn't normally say.
