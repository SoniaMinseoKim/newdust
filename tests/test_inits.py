
from newdust import graindist
from newdust import grainpop

ALLOWED_SIZES = ['Grain','Powerlaw','ExpCutoff']
ALLOWED_COMPS = ['Drude','Silicate','Graphite']
ALLOWED_SCATM = ['RG','Mie']

custom_sdist = graindist.sizedist.ExpCutoff(acut=0.5, nfold=12)
custom_comp  = graindist.composition.CmDrude(rho=2.2)

def test_graindist_init():
    for size in ALLOWED_SIZES:
        for comp in ALLOWED_COMPS:
            test = graindist.GrainDist(size, comp)
            assert isinstance(test, graindist.GrainDist)
            assert test.size.dtype  == size
            assert test.comp.cmtype == comp

def test_custom_graindist():
    test = graindist.GrainDist(custom_sdist, custom_comp, custom=True)
    assert isinstance(test, graindist.GrainDist)
    assert test.size.dtype == custom_sdist.dtype
    assert test.comp.cmtype == custom_comp.cmtype

def test_grainpop_inits():
    for size in ALLOWED_SIZES:
        for comp in ALLOWED_COMPS:
            for scat in ALLOWED_SCATM:
                test = grainpop.SingleGrainPop(size, comp, scat)
                assert isinstance(test, grainpop.SingleGrainPop)
