# how to try the experiment

this is the plan, not a record of a completed experiment. first, make films that can be compared fairly. then check whether they glow and whether they help the cell. a loss or no clear change is worth recording too.

## 1. get the lab and material sorted

start with a supervising materials or solar-cell lab. the easiest route may be getting si-qd/polymer slides from a collaborator who has already characterized them. if you're making the films, use a characterized dispersion and a process the lab has checked. this plan doesn't involve making the quantum dots, hf etching, silane, or cadmium chemistry. handle nanomaterial dispersions and toluene in the laboratory hood with ppe and waste arrangements specified by the lot sds. use an enclosed uv source; camera brightness is not an optical-safety measure.

verify cell active region, contacts, front window, eqe availability and cell rating. a 20 x 20 mm aperture requires a cell active region larger than 20 x 20 mm. keep the same cell, mask, wiring, source angle and optical gap for all paired comparisons. use an independent reference cell to monitor source drift.

## 2. make samples you can actually compare

| condition | independent coupons | purpose |
|---|---:|---|
| bare cell, no slide | repeated bracket measurements | overall device baseline, including all added interface losses |
| uncoated slide | g1–g3 | substrate, mounting and air-gap effect |
| host-only slide | h1–h3 | polymer and solvent-processing effects |
| low si-qd loading | l1–l3 | matched host plus qds |
| high si-qd loading | d1–d3 | loading dependence, quenching/scattering risk |

make three separate samples for each film condition. taking five readings from the same sample helps check repeatability, but it still counts as one film. compare the quantum-dot film with plain polymer first. also compare it with the bare cell, so any loss from adding glass and polymer stays visible. use a nonluminescent absorption-matched control if a suitable independently characterized material is available, but do not claim host-only isolates luminescence from every refractive/scattering effect.

## 3. try a small coating batch first

this is a starting recipe to test, using the listed 200 uM silicon-core stock in toluene. the supplier and lab still need to confirm it works with pmma. these amounts haven't been established as an optimum. prepare pmma stock at 4% w/v (40 mg/mL) in the compatible solvent using the lab's dissolution sop. finish dissolution before adding qds; do not heat the qds without lot guidance.

mix each 300 uL batch separately:

| batch | 200 uM qd stock | 4% w/v pmma stock | matching solvent | final nominal core concentration |
|---|---:|---:|---:|---:|
| host | 0 uL | 75 uL | 225 uL | 0 |
| low | 75 uL | 75 uL | 150 uL | 50 uM |
| high | 150 uL | 75 uL | 75 uL | 100 uM |

each mixture has 1% w/v pmma. make three batches of each condition, then coat one sample from each batch. these nine batches consume 675 uL qd stock; the remainder of a 2 mL lot permits optical pilots and repeats. volumes assume additive mixing. the supplier's concentration is based on silicon cores; it must not be reported as particle molarity or converted to coated-dot weight percent without characterization. the film may absorb too little light at these concentrations. that's something to check in the pilot before making more.

1. label slide margins and photograph clean substrates. clean using the substrate/vendor and lab sop; match cleaning across conditions. dry completely. measure slide dimensions and thickness.
2. first coat one host-only pilot. use a 100 um wet gap and approximately 100 uL starting dispense across a roughly 22 x 30 mm central patch. maintain a constant documented drawdown speed (start at 5 mm/s). ensure full 20 x 20 mm aperture coverage; edge beads stay outside it. adjust dispense only to achieve continuous coverage and log the change.
3. mix each batch gently; reject obvious precipitate and record it. coat in the same manner as host. photograph under fixed illumination. use the same gap, drawdown direction, substrate batch and polymer content. randomize coating order where practical.
4. dry covered against dust in the hood at ambient conditions, using the supplier/lab endpoint. record elapsed time, temperature and humidity. don't assume one drying time works for every formulation; the solvent and surface ligands matter. verify stable mass where instrument resolution permits, and obtain lab clearance before removing the sample from the hood. store dark in labeled containers.
5. measure dry thickness on a masked-step witness using profilometry if available. the wet gap doesn't tell you the final dry thickness. do not infer thickness from a micrometer reading dominated by 1 mm glass. reject cracks, visible aggregates or incomplete aperture coverage under a predeclared rule; keep rejected samples in the record.
6. measure transmission and reflectance across the cell-response range, and pl spectrum at a documented excitation wavelength. measure film plqy with a calibrated integrating sphere if available. solution plqy is not film plqy. use dark, substrate and host references. correct instrument spectra before normalizing photon emission; an energy spectrum requires a wavelength/hc conversion.
7. proceed to electrical attribution only if pl exceeds the host background reproducibly. if absorption is below instrument resolution or pl is quenched, ask the supplier/lab for a higher-concentration compatible stock or finished film. do not blindly concentrate the dispersion or invent a new mass loading. record this as a failed feasibility pilot if unresolved.

## 4. put the holder and cell in place

use the slide tray on four equal spacers over an independently secured cell on an insulating board. measure the actual film-to-cell gap. record film facing up/down and keep it fixed. fix contacts before inserting films. clip only the slide ends, avoiding glass stress and the optical area. the cell needs its own secure, insulated mount. the tray doesn't provide that.

place a characterized opaque 20 x 20 mm aperture upstream of the film, centered over a matching cell-plane aperture. this limits light collected from outside the nominated area. use the same masks for all states, with empty support for the bare-cell state. printed mask stl is a positioning template; check opacity and dimensions or cut an opaque thin mask from appropriate sheet stock. do not allow conductive mask stock to touch cell contacts.

confirm dark offset, polarity and current range. prefer smu near-zero-voltage isc and full i-v sweeps. if using a dmm, verify burden voltage; a meter with appreciable voltage drop does not measure true isc. start with a resistor/load sweep only after estimating maximum current/power from the cell specification. a single load point or voc alone cannot establish efficiency.

## 5. take the readings

use a calibrated am1.5g simulator and controlled cell temperature for quantitative solar claims. record source spectrum, irradiance, reference calibration, instrument settings, aperture area and uncertainty, settling/sweep time, spatial uniformity and cell temperature. measure spectral mismatch for every optical configuration when reporting corrected standard-condition results; a reference cell alone cannot correct the modified spectrum.

for a screening session, proposed acceptance limits are reference-current drift <=1% within a bracket and test temperature change <=1 degree c. these are starting limits for this project. if the effect you're looking for is smaller, the setup needs to be more stable too. warm the source until stable; determine settling time empirically. record five repeat sweeps per state, from near isc through voc with at least 40 points and extra sampling around the maximum-power knee; check reversed sweep for settling artifacts.

randomize the nine coated coupons using a saved random seed. for each qd coupon, use a matching host replicate in the sequence h–qd–h, with reference current logged throughout. for substrate coupons use bare–glass–bare. bracket host states with glass and include repeated bare-cell runs at the beginning/end of each block. re-seat each tested coupon at least three times to estimate positioning repeatability. return the cell to the same temperature before paired comparisons. keep negative results too. if a run is rejected, save it with the reason.

for each scan calculate isc, voc, max(v*i), fill factor and (only with calibrated incident power) pce. set the sign convention so delivered current and power are positive. jsc = isc_ma / aperture_area_cm2; nominal 20 x 20 mm area is 4 cm2, but use measured dimensions and stated uncertainty. with e in W/m2, incident watts = e * area_cm2 * 1e-4.

for source-specific screening, normalize isc to simultaneous reference current and interpolate between bracketing host readings at the qd acquisition time. compute paired relative change `(QD_normalized / host_interpolated - 1)*100`. report raw as well as normalized results. this helps with changes in brightness. it doesn't fix a changing spectrum. do not treat lamp results or uncalibrated outdoor readings as am1.5g efficiency.

average repeat scans within a seating, then seatings within each independent coupon. report the three independent coupon effects, mean, standard deviation and 95% t interval (df=2, t=4.303). separately estimate systematic contributions from instrument calibration, area, source spectrum, temperature and mismatch. the confidence interval across three samples doesn't include all of those systematic errors. a positive claim requires a positive effect beyond repeatability and the applicable combined uncertainty; otherwise report inconclusive or loss. repeat on another day and preferably a second cell before generalization.

## 6. check what is causing the change

measure pl plus transmission/reflectance; electrical gain alone does not prove lds. compare eqe before/after with the same aperture and geometry. optional uv-blocked illumination can probe excitation dependence, but its changed spectrum needs its own reference/control measurements. enclosed narrowband uv tests demonstrate source-specific response, not solar benefit.

record an initial and post-exposure optical/electrical set after a planned, logged exposure interval (for example 1 h and 10 h under the chosen lamp), including irradiance, temperature, elapsed time and cumulative dose where known. keep a dark-stored matched coupon. these checks only tell us about that short exposure. they don't establish a long service life.

## 7. what still needs hands-on work

secure lab/supplier access and sds; obtain characterized material and instruments; measure parts; print and fit-test the holder; fabricate or receive coupons; perform optical and electrical measurements; film actual work. the files can't do those steps. before coating anything, the lab still needs the full method details and compatibility advice for the actual material.
