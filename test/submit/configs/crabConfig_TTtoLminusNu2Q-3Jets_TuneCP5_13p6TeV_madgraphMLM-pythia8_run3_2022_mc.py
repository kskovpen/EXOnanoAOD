from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTtoLM2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8_Run3Summer22_NanoAODv15_LRSM_20260418'
config.General.workArea = 'crab'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'driver/step_3_cfg_run3_2022_mc.py'
config.JobType.pyCfgParams = []
NCORES = 4
config.JobType.maxMemoryMB = 2000 * NCORES
config.JobType.numCores = NCORES

config.Data.inputDataset = '/TTtoLminusNu2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.outLFNDirBase = '/store/user/kskovpen/LRSMSamples/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outputDatasetTag = 'TTtoLM2Q-3Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8_Run3Summer22_NanoAODv15_LRSM_20260418'
config.Data.publication = False

config.User.voGroup = 'becms'
config.Site.storageSite = 'T2_BE_IIHE'
