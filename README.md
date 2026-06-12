# EXOnanoAOD

Development of custom cms EXO PAG nanoAOD format for HNL displaced search (LRSM)

## Setup in CMSSW

source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_15_1_0_pre2
cd CMSSW_15_1_0_pre2/src
cmsenv
git cms-init
git cms-addpkg PhysicsTools/NanoAOD
cd PhysicsTools
git clone https://github.com/kskovpen/EXOnanoAOD
cd EXOnanoAOD
git checkout LRSM_HNL
cd ../../
scram b -j10

# Submission

(modify the list of needed datasets, user name, output directory, etc.)

./createConfig.py
./submitCrab.py
