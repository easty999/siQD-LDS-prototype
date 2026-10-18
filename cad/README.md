# the slide holder

this is the small tray that keeps a coated slide in the same place above the solar cell. you can change the slide without moving the cell or pulling on its wires. that's the whole job of this part.

![the holder](../media/renders/tray-hero.png)

## what the parts are

- `tray.stl`: one tray with a slide pocket and a square hole in the middle.
- `spacer.stl`: print four. they raise the tray above the board.
- `mask.stl`: two aperture templates. they help keep the illuminated area consistent.
- `slide-tray.scad`: the editable design. choose `tray`, `spacer`, `mask`, or `assembly` using the `part` setting.
- `export_mesh.py`: makes the default stl files and checks their geometry.

the [exploded render](../media/renders/exploded-labeled.png) shows how the parts sit together. the glass and cell in that image are placeholders. their colour and the cell grid are just there to make the explanation easier.

## dimensions

| feature | size |
|---|---|
| tray | 90 x 38 x 4 mm |
| slide pocket | 75.4 x 25.4 mm, 2 mm deep |
| intended slide | 75 x 25 x 1 mm |
| central opening | 20 x 20 mm |
| each spacer | 8 x 8 x 8 mm |
| each mask | 30 x 30 x 1 mm, with a 20 x 20 mm opening |

the pocket gives 0.2 mm of clearance on each side. that may need adjusting for the printer and actual slide. a 1 mm slide sits with its top 1 mm below the tray rim. measure the glass before printing.

## printing and putting it together

start with the tray flat and the pocket facing up. a 0.2 mm layer height and at least three perimeters are reasonable first settings, but they haven't been tested. there isn't a roof over the opening, so the tray doesn't need a long bridge there.

print the spacers separately and fix them under the four outer corners on an insulating board. check that they're the same height and that the tray can't slide around. mount the cell separately underneath. the tray mustn't press on it. clips can hold the slide at its ends; keep them away from the light path and don't stress the glass.

the slide underside sits 10 mm above the board with these spacers. the actual gap to the cell depends on the cell, its mount, and which way the coated slide faces. measure that gap and keep it the same between tests. this air gap makes swapping easier, but it can lose emitted light. it doesn't justify assuming the model's capture value of 0.7.

put one mask above the film and one at the cell plane. the upper mask rests across the tray rim. check alignment, shadows, opacity, and whether the material itself glows under the test light. if the printed material lets light through or fluoresces, use an opaque, nonluminescent sheet mask instead. keep conductive masks away from contacts.

## what has actually been checked

the three meshes passed closed-edge, face-direction, and volume checks. the new renders use those meshes directly. the design hasn't been sliced, printed, or fit-tested. the renders don't show every clip, lead, or mounting detail you'll need in the real setup.

before taking readings, test-fit a plain slide, check both apertures, secure the cell and leads, and repeat the same blank-slide measurement after several removals and insertions. that will show how much the positioning changes the result.

keep the printed parts away from wet solvent work. choose a lab-approved opaque material that can handle the measured test temperature.

## changing the design

all dimensions are in mm. if you change the scad parameters, export those new parts from openscad. the python exporter has its own default dimensions, so it won't pick up scad edits automatically. update both if you want to keep using that exporter. the cell mount still needs to suit the real cell; it isn't included as a fitted part.
