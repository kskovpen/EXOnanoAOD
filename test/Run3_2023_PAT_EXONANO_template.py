import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('NANO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:/pnfs/iihe/cms/store/user/kskovpen/LRSMProd/miniaod/2022PreEE/lrsm_wr5000n20_ee_nlo_ms/0.root"),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('test nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('Run3_2023_PAT_EXONANO_template.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2023_realistic_postBPix', '')

# Path and EndPath definitions
#process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
#process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
#process.Flag_BadPFMuonDzFilter = cms.Path(process.BadPFMuonDzFilter)
#process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
#process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
#process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
#process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
#process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
#process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
#process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
#process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
#process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
#process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
#process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
#process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
#process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
#process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
#process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
#process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
#process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
#process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
#process.Flag_hfNoisyHitsFilter = cms.Path(process.hfNoisyHitsFilter)
#process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
#process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
#process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
#process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
#process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
#process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

process.load('PhysicsTools.EXOnanoAOD.displacedInclusiveVertexing_cff')

process.nanoAOD_step += process.displacedInclusiveVertexing

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
#process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadPFMuonDzFilter,process.Flag_hfNoisyHitsFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
#process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon

#call to customisation function nanoAOD_customizeData imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# End of customisation functions

# customisation of the process.

from PhysicsTools.EXOnanoAOD.DispJetTableProducer_cff import *

process = add_customTables_template(process)

# End of customisation functions

# Customisation from command line

process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
