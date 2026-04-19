from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMuon_Run2022A_NanoAODv15_LRSM_20260418'
config.General.workArea = 'crab'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'driver/step_3_cfg_run3_2022.py'
config.JobType.pyCfgParams = []
NCORES = 4
config.JobType.maxMemoryMB = 2000 * NCORES
config.JobType.numCores = NCORES

config.Data.inputDataset = '/SingleMuon/Run2022A-22Sep2023-v1/MINIAOD'
config.Data.outLFNDirBase = '/store/user/kskovpen/LRSMSamples/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outputDatasetTag = 'SingleMuon_Run2022A_NanoAODv15_LRSM_20260418'
config.Data.publication = False

config.User.voGroup = 'becms'
config.Site.storageSite = 'T2_BE_IIHE'
