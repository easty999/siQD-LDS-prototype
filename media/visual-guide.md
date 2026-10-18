# visuals for the video

these are computer renders of the proposed fixture. the tray, spacers, and masks use the actual stl files in this repo. the slide and cell are explanatory placeholders. there isn't a fabricated prototype or measured film appearance behind these images.

## files you can drop into an editor

| file | use it for |
|---|---|
| [tray hero](renders/tray-hero.png) | introduce the object; 1920 x 1080 |
| [assembled setup](renders/assembly-labeled.png) | show where the slide and cell would go; 1920 x 1080 |
| [exploded view](renders/exploded-labeled.png) | explain the individual parts; 1920 x 1080 |
| [how the test works](renders/how-the-test-works.png) | explain the controls and what stays fixed; 1920 x 1080 |
| [corrected result](renders/model-result.png) | show the model's negative change without implying a measurement; 1920 x 1080 |
| [assembled to separated](renders/assembled-to-exploded.mp4) | an eight-second assembly-to-exploded animation; 1920 x 1080, 24 fps, no audio |
| [turntable](renders/tray-turntable.mp4) | a six-second rotating view of the tray; 1920 x 1080, 24 fps, no audio |

keep the “unbuilt design” or “simulation” label visible when using these. the turntable has an on-screen design label too. the source renders ending in `-raw.png` are clean versions for reframing; add an equivalent label if you use those.

## a short object description

this is a removable-slide holder for a solar-cell experiment. a coated glass slide sits in the tray, and the cell stays separately mounted underneath. the central opening is 20 x 20 mm. swapping slides should make it easier to compare plain glass, plain polymer, and quantum-dot films without changing the wiring each time. it's a test fixture, and it hasn't been printed yet.

## what each part does

- teal tray: locates the glass slide. outer size: 90 x 38 x 4 mm.
- slide pocket: 75.4 x 25.4 mm, intended for a measured 75 x 25 mm slide.
- orange spacers: four 8 mm blocks that lift the tray above the support.
- dark masks: keep the nominated illuminated area the same. their material still needs opacity and fluorescence checks.
- blue slide: shows the glass envelope. its tint is just for visibility; it isn't the predicted colour of a si-qd film.
- cell and base: show the arrangement only. the cell mount, contacts, clips, and leads need to match the real parts.

the gaps in the exploded view are enlarged to separate the parts. don't use that image to measure the working optical gap. the holder isn't a way to direct every emitted photon into the cell, and the render doesn't establish any efficiency improvement.

## editing the scenes

open `fixture-scene.blend` in blender for the exploded setup. open `turntable-scene.blend` for the animated tray. the materials and camera are editable. `render_scene.py` rebuilds the renders from the stl files. `make_video_graphics.py` adds the still-image labels and makes the explanatory cards (it needs pillow). run `label_video.py` in blender after that to add the video label. `video-edit.blend` keeps that labeled edit ready to reopen. the clean clip is saved separately as `renders/tray-turntable-clean.mp4`; add a design label if you use it.

the stills were rendered with cycles. the animation uses blender's studio renderer for a clean technical view. the shapes come from the model, not an ai-generated product image. none of these files is experimental footage.

## the moving layers

the new clip starts assembled for 1.5 seconds, eases apart over four seconds, then holds the separated view for 2.5 seconds. the masks, slide, tray, and cell separate vertically. the spacers move outward so they are easier to see. those enlarged gaps are for the explanation, not assembly dimensions.

open `layers-animation.blend` to edit the motion or `layers-video-edit.blend` to edit the labels and framing. `animate_layers.py` rebuilds the clip in blender 2.93. the glass and cell are still illustrative placeholders, and the design has not been built.
