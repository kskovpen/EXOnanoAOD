# EXOnanoAOD
Development of custom cms EXO PAG nanoAOD format


## Setup in CMSSW
```
cmsrel CMSSW_15_0_0_pre3
cd CMSSW_15_0_0_pre3/src
cmsenv
git cms-init
mkdir PhysicsTools
cd PhysicsTools
git clone git@github.com:kerstinlovisa/EXOnanoAOD.git
scram b -j
```

# Template
You find a very simple template with a producer in ´plugins´ and python customization script in ´python´, in the branch `EXOnanoAOD_template`. 

Or you can use the producers already implemented in main for reference.

# Test run AOD -> EXOnanoAOD for Run 3
In `test` there is a test config file for Run 3 2023 which runs over one MC file (from TTto2L2Nu dataset). It will run AOD to NanoAOD format directly. 

Add your customization functions at the end of the script under `EXOnanoAOD customisation`. If you included everything you need (also updating your `BuildFile.xml` if needed) you should be able to run your customizations with:
```
cmsRun Run3_2023_PAT_EXONANO_template.py
```

# Event size of customized NanoAOD
Check the event size of your custom EXOnanoAOD implementations in your nanoAOD root file (replace `nanoAOD.root`) by running:
```
git cms-add
$CMSSW_BASE/src/PhysicsTools/NanoAOD/test/inspectNanoFile.py nanoAOD.root --size size.html
```

