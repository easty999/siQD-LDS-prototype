import unittest,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'analysis'))
from model import calculate
class Physics(unittest.TestCase):
    def setUp(self):
        self.w=np.linspace(280,1200,921); self.i=np.ones(len(self.w))
    def test_no_layer(self):
        r=calculate(self.w,self.i,amplitude=0);self.assertAlmostEqual(r['delta_mA_cm2'],0)
    def test_zero_yield_loss(self):
        r=calculate(self.w,self.i,qy=0);self.assertAlmostEqual(r['delta_mA_cm2'],-r['loss_mA_cm2'])
    def test_gain_monotonic(self):
        self.assertGreater(calculate(self.w,self.i,qy=.9)['delta_mA_cm2'],calculate(self.w,self.i,qy=.1)['delta_mA_cm2'])
    def test_invalid(self):
        with self.assertRaises(ValueError): calculate(self.w[::-1],self.i)
    def test_reference_sign(self):
        a=np.loadtxt(Path(__file__).resolve().parents[1]/'data/processed/reference_spectra.csv',delimiter=',',skiprows=1)
        r=calculate(a[:,0],a[:,2]);self.assertAlmostEqual(r['delta_mA_cm2'],-1.3868450418,places=8)
if __name__=='__main__':unittest.main()
