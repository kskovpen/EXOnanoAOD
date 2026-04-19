#!/bin/env python3

import os

date = '20260418'
tag = 'NanoAODv15_LRSM_'+date
run = 'run3_2022_mc'
user = 'kskovpen'

samples = {
    'run3_2022': [
        '/EGamma/Run2022A-22Sep2023-v1/MINIAOD',
        '/EGamma/Run2022B-22Sep2023-v2/MINIAOD',
        '/EGamma/Run2022C-22Sep2023-v1/MINIAOD',
        '/EGamma/Run2022D-22Sep2023-v1/MINIAOD',
        '/EGamma/Run2022E-22Sep2023-v1/MINIAOD',
        '/EGamma/Run2022F-19Dec2023-v1/MINIAOD',
        '/EGamma/Run2022G-19Dec2023-v1/MINIAOD',
        '/EGamma/Run2022F-19Dec2023-v1/MINIAOD',
        '/EGamma/Run2022G-19Dec2023-v1/MINIAOD',
        '/SingleMuon/Run2022A-22Sep2023-v1/MINIAOD',
        '/SingleMuon/Run2022B-22Sep2023-v2/MINIAOD',
        '/SingleMuon/Run2022C-22Sep2023-v1/MINIAOD',
        '/SingleMuon/Run2022D-22Sep2023-v1/MINIAOD',
        '/SingleMuon/Run2022E-22Sep2023-v1/MINIAOD',
        '/SingleMuon/Run2022F-19Dec2023-v1/MINIAOD',
        '/SingleMuon/Run2022G-19Dec2023-v1/MINIAOD',
        '/SingleMuon/Run2022F-19Dec2023-v1/MINIAOD',
        '/SingleMuon/Run2022G-19Dec2023-v1/MINIAOD'
    ],
    'run3_2023': [
        '/EGamma0/Run2023B-22Sep2023-v1/MINIAOD',
        '/EGamma0/Run2023C-22Sep2023_v1-v1/MINIAOD',
        '/EGamma0/Run2023C-22Sep2023_v2-v1/MINIAOD',
        '/EGamma0/Run2023C-22Sep2023_v3-v1/MINIAOD',
        '/EGamma0/Run2023C-22Sep2023_v4-v1/MINIAOD',
        '/EGamma0/Run2023D-22Sep2023_v1-v1/MINIAOD',
        '/EGamma0/Run2023D-22Sep2023_v2-v1/MINIAOD',
        '/EGamma1/Run2023B-22Sep2023-v1/MINIAOD',
        '/EGamma1/Run2023C-22Sep2023_v1-v1/MINIAOD',
        '/EGamma1/Run2023C-22Sep2023_v2-v1/MINIAOD',
        '/EGamma1/Run2023C-22Sep2023_v3-v1/MINIAOD',
        '/EGamma1/Run2023C-22Sep2023_v4-v1/MINIAOD',
        '/EGamma1/Run2023D-22Sep2023_v1-v1/MINIAOD',
        '/EGamma1/Run2023D-22Sep2023_v2-v1/MINIAOD',
        '/Muon/Run2023E-PromptReco-v1/MINIAOD',
        '/Muon0/Run2023B-22Sep2023-v1/MINIAOD',
        '/Muon0/Run2023C-22Sep2023_v1-v1/MINIAOD',
        '/Muon0/Run2023C-22Sep2023_v2-v1/MINIAOD',
        '/Muon0/Run2023C-22Sep2023_v3-v1/MINIAOD',
        '/Muon0/Run2023C-22Sep2023_v4-v1/MINIAOD',
        '/Muon0/Run2023D-22Sep2023_v1-v1/MINIAOD',
        '/Muon0/Run2023D-22Sep2023_v2-v1/MINIAOD',
        '/Muon1/Run2023B-22Sep2023-v1/MINIAOD',
        '/Muon1/Run2023C-22Sep2023_v1-v1/MINIAOD',
        '/Muon1/Run2023C-22Sep2023_v2-v1/MINIAOD',
        '/Muon1/Run2023C-22Sep2023_v3-v1/MINIAOD',
        '/Muon1/Run2023C-22Sep2023_v4-v2/MINIAOD',
        '/Muon1/Run2023D-22Sep2023_v1-v1/MINIAOD',
        '/Muon1/Run2023D-22Sep2023_v2-v1/MINIAOD',
        '/MuonEG/Run2023B-22Sep2023-v1/MINIAOD',
        '/MuonEG/Run2023C-22Sep2023_v1-v1/MINIAOD',
        '/MuonEG/Run2023C-22Sep2023_v2-v1/MINIAOD',
        '/MuonEG/Run2023C-22Sep2023_v3-v1/MINIAOD',
        '/MuonEG/Run2023C-22Sep2023_v4-v1/MINIAOD',
        '/MuonEG/Run2023D-22Sep2023_v1-v1/MINIAOD',
        '/MuonEG/Run2023D-22Sep2023_v2-v1/MINIAOD'
    ],
    'run3_2024': [
        '/EGamma0/Run2024C-2024CDEReprocessing-v1/MINIAOD',
        '/EGamma0/Run2024C-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma0/Run2024D-2024CDEReprocessing-v1/MINIAOD',
        '/EGamma0/Run2024D-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma0/Run2024E-2024CDEReprocessing-v1/MINIAOD',
        '/EGamma0/Run2024E-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma0/Run2024F-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma0/Run2024G-MINIv6NANOv15-v2/MINIAOD',
        '/EGamma0/Run2024H-MINIv6NANOv15-v2/MINIAOD',
        '/EGamma0/Run2024I-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/MINIAOD',
        '/EGamma1/Run2024C-2024CDEReprocessing-v1/MINIAOD',
        '/EGamma1/Run2024C-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma1/Run2024D-2024CDEReprocessing-v1/MINIAOD',
        '/EGamma1/Run2024D-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma1/Run2024E-2024CDEReprocessing-v1/MINIAOD',
        '/EGamma1/Run2024E-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma1/Run2024F-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma1/Run2024G-MINIv6NANOv15-v2/MINIAOD',
        '/EGamma1/Run2024H-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma1/Run2024I-MINIv6NANOv15-v1/MINIAOD',
        '/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/MINIAOD',
        '/Muon0/Run2024C-2024CDEReprocessing-v1/MINIAOD',
        '/Muon0/Run2024C-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024D-2024CDEReprocessing-v1/MINIAOD',
        '/Muon0/Run2024D-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024E-2024CDEReprocessing-v1/MINIAOD',
        '/Muon0/Run2024E-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024F-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024G-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024H-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024I-MINIv6NANOv15-v1/MINIAOD',
        '/Muon0/Run2024I-MINIv6NANOv15_v2-v1/MINIAOD',
        '/Muon1/Run2024C-2024CDEReprocessing-v1/MINIAOD',
        '/Muon1/Run2024C-MINIv6NANOv15-v1/MINIAOD',
        '/Muon1/Run2024D-2024CDEReprocessing-v1/MINIAOD',
        '/Muon1/Run2024D-MINIv6NANOv15-v1/MINIAOD',
        '/Muon1/Run2024E-2024CDEReprocessing-v1/MINIAOD',
        '/Muon1/Run2024E-MINIv6NANOv15-v1/MINIAOD',
        '/Muon1/Run2024F-MINIv6NANOv15-v1/MINIAOD',
        '/Muon1/Run2024G-MINIv6NANOv15-v2/MINIAOD',
        '/Muon1/Run2024H-MINIv6NANOv15-v2/MINIAOD',
        '/Muon1/Run2024I-MINIv6NANOv15-v1/MINIAOD',
        '/Muon1/Run2024I-MINIv6NANOv15_v2-v1/MINIAOD'
    ],
    'run3_2022_mc': [
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
        '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5_ext1-v2/MINIAODSIM',
        '/TTtoLminusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1/MINIAODSIM',
        '/TTtoLminusNu2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TTtoLplusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1/MINIAODSIM',
        '/TTtoLplusNu2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TTto4Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1/MINIAODSIM',
        '/TTto4Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
        '/TTto2L2Nu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1/MINIAODSIM',
        '/TTto2L2Nu-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM',
    ],
    'run3_2022EE_mc': [
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/MINIAODSIM',
        '/TTtoLminusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v3/MINIAODSIM',
        '/TTtoLminusNu2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
        '/TTtoLplusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v3/MINIAODSIM',
        '/TTtoLplusNu2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
        '/TTto4Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v3/MINIAODSIM',
        '/TTto4Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
        '/TTto2L2Nu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v3/MINIAODSIM',
        '/TTto2L2Nu-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM',
    ],
    'run3_2023_mc': [
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
        '/TTtoLminusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v3/MINIAODSIM',
        '/TTtoLplusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v3/MINIAODSIM',
        '/TTto4Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v3/MINIAODSIM',
        '/TTto2L2Nu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v2/MINIAODSIM',
    ],
    'run3_2023BPix_mc': [
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v3/MINIAODSIM',
        '/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v3/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v3/MINIAODSIM',
        '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v2/MINIAODSIM',
        '/TTtoLminusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v3/MINIAODSIM',
        '/TTtoLplusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v3/MINIAODSIM',
        '/TTto4Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v2/MINIAODSIM',
        '/TTto2L2Nu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4-130X_mcRun3_2023_realistic_postBPix_v2-v2/MINIAODSIM',
    ],
    'run3_2024_mc': [
        '/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v10-v2/MINIAODSIM',
        '/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v10-v2/MINIAODSIM',
        '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter24MiniAOD-133X_mcRun3_2024_realistic_v8-v2/MINIAODSIM',
    ]
}

for d in samples[run]:
    dname = d.split('/')[1]
    isext = True if 'ext' in d.split('/')[2] else False
    dtag = d.split('/')[2].split('-')[0].replace('MiniAODv4', '').replace('MiniAODv2', '').replace('APVv2', 'APV').replace('MiniAOD', '')

    pf = ""
    cfg = "configs/crabConfig_"+dname+"_"+run+".py"
    if isext:
        cfg = cfg.replace('.py', '_ext.py')
        pf = "_ext"

    if 'TTtoLminusNu2Q' in dname or 'TTtoLplusNu2Q' in dname:
        dname = dname.replace('TTtoLminusNu2Q', 'TTtoLM2Q').replace('TTtoLplusNu2Q', 'TTtoLP2Q')
    
    f = open(cfg, "w")
    
    f.write("from CRABClient.UserUtilities import config\n")
    f.write("config = config()\n\n")
    f.write("config.General.requestName = '"+dname+"_"+dtag+"_"+tag+pf+"'\n")
    f.write("config.General.workArea = 'crab'\n")
    f.write("config.General.transferOutputs = True\n\n")
    f.write("config.JobType.pluginName = 'Analysis'\n")
    f.write("config.JobType.psetName = 'driver/step_3_cfg_"+run+".py'\n")
    f.write("config.JobType.pyCfgParams = []\n")
    f.write("NCORES = 4\n")
    f.write("config.JobType.maxMemoryMB = 2000 * NCORES\n")
    f.write("config.JobType.numCores = NCORES\n\n")
###    f.write("config.Data.inputDBS = 'phys03'\n")
    f.write("config.Data.inputDataset = '"+d+"'\n")
    f.write("config.Data.outLFNDirBase = '/store/user/"+user+"/LRSMSamples/'\n")
    f.write("config.Data.splitting = 'FileBased'\n")
    f.write("config.Data.unitsPerJob = 2\n")
    f.write("config.Data.outputDatasetTag = '"+dname+"_"+dtag+"_"+tag+pf+"'\n")
    f.write("config.Data.publication = False\n\n")
    f.write("config.User.voGroup = 'becms'\n")
    f.write("config.Site.storageSite = 'T2_BE_IIHE'\n")
    f.close()

    os.system("crab submit -c "+cfg)
