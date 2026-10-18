"""an illustrative lds model. the outputs are simulations, not measurements."""
from pathlib import Path
import json
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def calculate(w, irradiance, qy=.6, capture=.7, amplitude=.6):
    w=np.asarray(w,dtype=float); irradiance=np.asarray(irradiance,dtype=float)
    if w.shape!=irradiance.shape or len(w)<2 or not np.all(np.isfinite(w)) or not np.all(np.diff(w)>0):
        raise ValueError('Wavelengths must be finite, increasing and match irradiance')
    if not np.all(np.isfinite(irradiance)) or np.any(irradiance<0): raise ValueError('Invalid irradiance')
    if not all(0<=x<=1 for x in (qy,capture,amplitude)): raise ValueError('Fractions outside [0,1]')
    eqe=np.where((w>=300)&(w<=1100),.9-.4*np.abs(w-700)/800,0)
    photons=irradiance*w*1e-9/(6.626e-34*3e8)
    absorption=amplitude*np.exp(-.5*((w-400)/70)**2)
    emission=np.exp(-.5*((w-750)/80)**2)
    emission/=np.trapezoid(emission,w)
    nabs=np.trapezoid(absorption*photons,w)
    # a/m2 -> mA/cm2 is multiplication by 0.1.
    k=1.602e-19*.1
    base=k*np.trapezoid(eqe*photons,w)
    loss=k*np.trapezoid(eqe*absorption*photons,w)
    coeff=k*nabs*np.trapezoid(eqe*emission,w)
    final=(1-absorption)*photons+qy*capture*nabs*emission
    lds=k*np.trapezoid(eqe*final,w)
    assert np.isclose(lds-base,qy*capture*coeff-loss)
    assert np.isclose(np.trapezoid(final,w),np.trapezoid(photons,w)-(1-qy*capture)*nabs)
    return dict(baseline_mA_cm2=float(base),lds_mA_cm2=float(lds),delta_mA_cm2=float(lds-base),loss_mA_cm2=float(loss),emission_coefficient_mA_cm2=float(coeff),break_even_qy_times_capture=float(loss/coeff) if coeff else None,irradiance_W_m2=float(np.trapezoid(irradiance,w)))

def main():
    a=np.loadtxt(ROOT/'data/processed/reference_spectra.csv',delimiter=',',skiprows=1)
    results={name:calculate(a[:,0],a[:,col]) for col,name in [(1,'historical_extraterrestrial'),(2,'corrected_global_tilt')]}
    q=np.linspace(.2,.9,20); e=np.linspace(.3,.9,20)
    sweep=np.array([(x,y,calculate(a[:,0],a[:,2],x,y)['delta_mA_cm2']) for x in q for y in e])
    np.savetxt(ROOT/'data/processed/sweep.csv',sweep,delimiter=',',header='QY,capture,delta_mA_cm2',comments='')
    (ROOT/'data/processed/results.json').write_text(json.dumps(results,indent=2)+'\n')
    # dependency-light svg for a reproducible figure with a visible zero reference.
    r=results['corrected_global_tilt']; pts=[(x,.7*x*r['emission_coefficient_mA_cm2']-r['loss_mA_cm2']) for x in np.linspace(.2,.9,8)]
    x=lambda v:90+(v-.2)/.7*610
    y=lambda v:100-v/3*330
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="800" height="540" viewBox="0 0 800 540"><rect width="800" height="540" fill="white"/><g font-family="Arial" fill="#142331"><text x="40" y="35" font-size="22">corrected global-tilt model: current decreases</text><text x="40" y="62" font-size="15">assumed cell response and spectra; capture = 0.7. no measured data.</text>']
    for v in [0,-1,-2,-3]:parts.append(f'<path d="M90 {y(v)}H700" stroke="#c9ced4"/><text x="45" y="{y(v)+5}">{v}</text>')
    for v in [.2,.3,.4,.5,.6,.7,.8,.9]:parts.append(f'<text x="{x(v)-10}" y="460">{v}</text>')
    parts.append('<polyline fill="none" stroke="#086a83" stroke-width="3" points="'+' '.join(f'{x(u)},{y(v)}' for u,v in pts)+'"/>')
    parts.append('<text x="270" y="500">quantum yield (photons out / absorbed)</text><text transform="translate(20,370) rotate(-90)">change in current density (mA/cm2)</text></g></svg>')
    (ROOT/'analysis/corrected-sweep.svg').write_text(''.join(parts))
    print(json.dumps(results,indent=2))
if __name__=='__main__':main()
